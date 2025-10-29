import datetime, time
import random
import ssl
import json
import urllib.error
import io
import requests
import numpy as np
import logging

import model.mall.response
from dao import d_user, d_db
from urllib.parse import urlencode
from model.res.auth import LoginRes
from model.schema import TUser
from model import m_schema
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Body
from service.auth_service import token_encode
from service import wx_service
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from common import global_define
from model import schema

router = APIRouter()

class GoodspecPostpic(BaseModel):
    user_id: Optional[int] = Field(None, title='推广人id')
    path: Optional[str] = Field(None, title='推广地址 /page/....')
    spec_id:  Optional[int] = Field(None, title='规格id，用于获取那个规格的海报图片')
    style: Optional[str] = Field(None, title='样式，为生成各种样式推广海报预留的参数')

class Posterpic(BaseModel):
    user_id: Optional[int] = Field(None, title='推广人id')
    poster_id: Optional[int] = Field(None, title='选中海报图的id')
    poster_url: Optional[str] = Field(None, title='选中的海报地址')
    path: Optional[str] = Field(None, title='推广地址 /page/....')

class UpdateUser(BaseModel):
    id: Optional[int] = Field(None, title='用户id')
    nickname: Optional[str] = Field(None, title='用户昵称')
    avatar: Optional[str] = Field(None, title='头像url')
    phone: Optional[str] = Field(None, title='手机电话号码')
    valcode: Optional[str] = Field(None, title='post提交code')

@router.get("/wx_login", response_model=LoginRes, summary='微信登录接口')
def wx_login(code: str, user_id:int = 0) -> LoginRes:
    """
    微信登录，参数为code，例如 `/mall/wx_login?code=xxxxxx`
    Login by wx code
    """
    wx_res = wx_service.wx_login(code)
    t_user = d_user.get_user_by_openid(wx_res.openid)
    if t_user is None:
        if user_id > 0:
            t_user = TUser(open_id=wx_res.openid, union_id=wx_res.unionid,parent_id=user_id,invited_user_id=user_id)
            t_user = d_user.insert_user(t_user)
            #更新团成员
            #d_groupsir.add_groupsir(t_user.id, user_id, '新用户入团')
        else:
            #t_user = TUser(open_id=wx_res.openid, union_id=wx_res.unionid,parent_id=-1)
            t_user = TUser(open_id=wx_res.openid, union_id=wx_res.unionid)
            t_user = d_user.insert_user(t_user)

    # 更新系统用户级别
    if t_user.level_id == 0:
        d_user.update_sysuser_active(t_user.id)
    elif t_user.level_id == 1:
        d_user.update_sysuser_high(t_user.id)
    elif t_user.level_id == 2:
        d_user.update_sysuser_top(t_user.id)

    # 更新推广用户级别
    d_user.update_user_top(t_user.id)

    token = token_encode(user_id=t_user.id)
    res = LoginRes(token=token, user_id=t_user.id, nickname=t_user.nickname, avatar=t_user.avatar)
    return res


@router.get(f'/check', response_model=dict, summary="是否实名")
async def user_check(user_id: int):
    user = d_db.get_user(user_id=user_id)
    if user is not None:
        if user.is_agree == 1:
            return {'code': 1, 'detail': '该用户已实名', 'data': {'username': user.username, 'idcard': user.id_card}}
        else:
            return {'code': 0, 'detail': '该用户未实名'}
    else:
        return {'code': 2, 'detail': '该用户不存在'}


@router.post('/check_idcard', response_model=dict, summary='用户实名认证')
async def user_check_idcard(user_id: int, name: str, idcard: str):
    host = 'https://idcert.market.alicloudapi.com'
    path = '/idcard'
    appcode = 'ac375fe220064a038b864231ba5b820d'  # 开通服务后 买家中心-查看AppCode
    query = urlencode({'idCard': idcard, 'name': name})
    url = host + path + '?' + query
    #idcard唯一性验证
    get_card = d_user.get_user_forcard(idcard)
    if get_card:
        raise HTTPException(status_code=400, detail="认证信息已存在")
    request = urllib2.Request(url)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    response = urllib2.urlopen(request, context=ctx)
    content = json.loads(response.read().decode(encoding='utf-8'))
    if content['status'] == '01':
        d_db.update_user(item=m_schema.SUser(id=user_id, username=name, name=name, id_card=idcard, is_agree=1))
        return {'code': 200, 'message': 'success'}
    else:
        raise HTTPException(status_code=400, detail=content['msg'])


@router.get(f'/send_phone_code', response_model=dict, summary="发送短信验证码")
async def send_phone_code(phone: str, user_id: Optional[int] = None, employee_id: Optional[int] = None,
                          store_owner_id: Optional[int] = None,
                          worker_id: Optional[int] = None):
    """
    employee_id:代表商家负责人id
    store_owner_id:代表店铺负责人id
    worker_id:代表普通员工id
    """
    # 购买服务后移动到配置文件里
    host = 'https://dfsmsv2.market.alicloudapi.com'
    path = '/data/send_sms_v2'
    appcode = 'ac375fe220064a038b864231ba5b820d'
    # 购买服务后移动到配置文件里
    method = 'POST'
    bodys = {}
    url = host + path
    code = str(random.randint(100000, 999999))
    bodys['content'] = f"code:{code}"
    bodys['phone_number'] = phone
    bodys['template_id'] = "TPL_0000"
    post_data = urlencode(bodys)
    request = urllib2.Request(url, data=post_data.encode('utf-8'), method=method)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        response = urllib2.urlopen(request, context=ctx)
    except urllib.error.HTTPError as e:
        return {'code': 204, 'message': "bad request"}
    content = json.loads(response.read().decode(encoding='utf-8'))
    if content['status'] == 'OK':
        if user_id is not None:
            phone_code: List[m_schema.SUserPhoneCode] = d_db.filter_user_phone_code(items={'user_id': user_id},
                                                                                    search_items={}, set_items={},
                                                                                    page=1,
                                                                                    page_size=1)
            if phone_code:
                phone_code[0].code = code
                phone_code[0].send_time = datetime.datetime.now()
                d_db.update_user_phone_code(phone_code[0])
            else:
                d_db.insert_user_phone_code(
                    item=m_schema.CreateUserPhoneCode(user_id=user_id, phone=phone, code=code, expired_time=5 * 60,
                                                      send_time=datetime.datetime.now()))
        elif employee_id is not None:
            phone_code: List[m_schema.SUserPhoneCode] = d_db.filter_user_phone_code(items={'employee_id': employee_id},
                                                                                    search_items={}, set_items={},
                                                                                    page=1, page_size=1)
            if phone_code:
                phone_code[0].code = code
                phone_code[0].send_time = datetime.datetime.now()
                d_db.update_user_phone_code(phone_code[0])
            else:
                d_db.insert_user_phone_code(
                    item=m_schema.CreateUserPhoneCode(employee_id=employee_id, phone=phone, code=code,
                                                      expired_time=5 * 60,
                                                      send_time=datetime.datetime.now()))

        elif store_owner_id is not None:
            phone_code: List[m_schema.SUserPhoneCode] = d_db.filter_user_phone_code(
                items={'store_owner_id': store_owner_id},
                search_items={}, set_items={},
                page=1, page_size=1)
            if phone_code:
                phone_code[0].code = code
                phone_code[0].send_time = datetime.datetime.now()
                d_db.update_user_phone_code(phone_code[0])
            else:
                d_db.insert_user_phone_code(
                    item=m_schema.CreateUserPhoneCode(store_owner_id=store_owner_id, phone=phone, code=code,
                                                      expired_time=5 * 60,
                                                      send_time=datetime.datetime.now()))

        elif worker_id is not None:
            phone_code: List[m_schema.SUserPhoneCode] = d_db.filter_user_phone_code(items={'worker_id': worker_id},
                                                                                    search_items={}, set_items={},
                                                                                    page=1, page_size=1)
            if phone_code:
                phone_code[0].code = code
                phone_code[0].send_time = datetime.datetime.now()
                d_db.update_user_phone_code(phone_code[0])
            else:
                d_db.insert_user_phone_code(
                    item=m_schema.CreateUserPhoneCode(worker_id=worker_id, phone=phone, code=code, expired_time=5 * 60,
                                                      send_time=datetime.datetime.now()))
        else:
            d_db.insert_user_phone_code(
                item=m_schema.CreateUserPhoneCode(phone=phone, code=code, expired_time=5 * 60,
                                                  send_time=datetime.datetime.now()))

        return {'code': 200, 'message': 'success'}
    else:
        return {'code': 204, 'message': 'fail'}


@router.get(f'/verify_phone_code', response_model=dict, summary='校验短信验证码')
async def verify_phone_code(code: str, phone: Optional[str] = None, user_id: Optional[int] = None,
                            employee_id: Optional[int] = None, store_owner_id: Optional[int] = None,
                            worker_id: Optional[int] = None):
    if user_id is not None and employee_id is not None:
        return {'code': 204, 'detail': '参数过多'}

    user_phone_code: List[m_schema.SUserPhoneCode] = d_db.filter_user_phone_code(items={'code': code, 'phone': phone},
                                                                                 search_items={},
                                                                                 set_items={}, page=1, page_size=1)
    if user_id is not None:
        user_phone_code: List[m_schema.SUserPhoneCode] = d_db.filter_user_phone_code(items={'user_id': user_id},
                                                                                     search_items={},
                                                                                     set_items={}, page=1, page_size=1)
    if employee_id is not None:
        user_phone_code: List[m_schema.SUserPhoneCode] = d_db.filter_user_phone_code(items={'employee_id': employee_id},
                                                                                     search_items={},
                                                                                     set_items={}, page=1, page_size=1)
    if store_owner_id is not None:
        user_phone_code: List[m_schema.SUserPhoneCode] = d_db.filter_user_phone_code(
            items={'store_owner_id': store_owner_id},
            search_items={},
            set_items={}, page=1, page_size=1)
    if worker_id is not None:
        user_phone_code: List[m_schema.SUserPhoneCode] = d_db.filter_user_phone_code(items={'worker_id': worker_id},
                                                                                     search_items={},
                                                                                     set_items={}, page=1, page_size=1)

    if user_phone_code:
        phone_code = user_phone_code[0].code
        send_time = user_phone_code[0].send_time
        seconds = user_phone_code[0].expired_time
        time_now = datetime.datetime.now()
        over_time = send_time + datetime.timedelta(seconds=seconds)
        if time_now > over_time:
            raise HTTPException(status_code=201, detail='验证码过期')
        if phone_code != code:
            raise HTTPException(status_code=202, detail='验证码错误')
        if over_time > time_now and phone_code == code:
            return {'detail': 'success', 'data': {}}
    else:
        raise HTTPException(status_code=203, detail='用户不存在')


@router.get(f'/get_wx_phone', response_model=model.mall.response.PhoneNumber, summary='获取微信手机号')
async def get_wx_phone(code: str):
    phone_info = wx_service.mall_wx_sdk.get_phone_number(code=code)
    phone_info = phone_info.phone_info

    return model.mall.response.PhoneNumber(
        phoneNumber=phone_info.phoneNumber,
        purePhoneNumber=phone_info.purePhoneNumber,
        countryCode=phone_info.countryCode
    )

@router.get(f'/get_user_list', response_model=list, summary='获取用户列表')
async def get_user_list(get_page: int = 1):
    user = d_db.get_users_list(page=get_page)
    return user

@router.get(f'/get_user_baseinfo', summary='获取用户基础信息')
async def get_user_baseinfo(user_id: int = 0):
    res_fetch = d_user.get_user_baseinfo(user_id)
    #print('------------------------------------')
    #print(res_fetch)
    return_fetch = {
        "user_id": res_fetch[0][0],
        "user_name": res_fetch[0][1],
        "nickname": res_fetch[0][2],
        "avatar": res_fetch[0][3],
        "order_count": res_fetch[0][4],
        "paid_balance_total": res_fetch[0][5],
        "flash_cost_total": res_fetch[0][6]
    }
    return return_fetch
#
# @router.post(f'/get_user_post_pic', summary='获取用户推广产品二维码,带参?user_id=n')
# async def get_user_baseinfo(data:GoodspecPostpic):
#     """
#     返回png格式的图像二进制码
#     """
#     if data.spec_id is None:
#         raise HTTPException(status_code=304, detail='规格参数错误')
#     data_spec = d_good.get_good_spec_by_id(data.spec_id)
#     if not data_spec:
#         raise HTTPException(status_code=304, detail='未找到规格数据')
#     data_good = d_good.get_good_data(data_spec.good_id)
#     if not data_good:
#         raise HTTPException(status_code=304, detail='未找到商品数据')
#
#     haibao = './pic_package/haibao_online.jpg'
#     chanpin = './pic_package/chanpin.jpg'
#     #erweima = './pic_package/erweima.jpg'
#     logo = './pic_package/logo_online.png'
#     path = "?".join((data.path, f"superiors_user_id={data.user_id}&id={data.spec_id}"))
#     code_pic = wx_service.mall_wx_sdk.get_getwxacode(300, path)
#     # logging.info(f"图片URL：{path}")
#     is_spec_post = False
#     if data_spec.post is not None:
#         haibao = './' + data_spec.post.split('com/')[1]
#         try:
#             haibao_pil = Image.open(haibao).convert('RGBA')
#             is_spec_post = True
#         except:
#             haibao = './pic_package/haibao_online.jpg'
#             haibao_pil = Image.open(haibao).convert('RGBA')
#     elif data_good.image_url is not None:
#         haibao_pil = Image.open(haibao).convert('RGBA')
#
#
#     stream = io.BytesIO(code_pic)
#     erweima_pil = Image.open(stream).convert("RGBA")
#     haibao_pil.paste(erweima_pil, (794, 1388, erweima_pil.width + 794, erweima_pil.height + 1388))
#
#     if not is_spec_post:
#         chanpin = './' + data_good.image_url.split('com/')[1]
#         try:
#             chanpin_pil = Image.open(chanpin).convert('RGBA')
#         except:
#             logging.info(f"get_user_post_pic，bad path: {chanpin}")
#             chanpin = './pic_package/chanpin.jpg'
#             chanpin_pil = Image.open(chanpin).convert('RGBA')
#             if is_spec_post:
#                 is_spec_post = False
#         #erweima_pil = Image.open(erweima).convert('RGBA')
#         #logo_pil = Image.open(logo).convert('RGBA').resize((208,201))
#
#         chanpin_pil = chanpin_pil.resize((1195, 1195))
#         haibao_pil.paste(chanpin_pil, (0, 0, chanpin_pil.width, chanpin_pil.height))
#         #haibao_pil.paste(logo_pil, (10, 10, logo_pil.width + 10, logo_pil.height + 10))
#
#         draw = ImageDraw.Draw(haibao_pil)
#         font_path = './pic_package/msyhbd.ttc'
#         font = ImageFont.truetype(font=font_path, size=50, encoding='utf-8')
#         if data_good.title is None:
#             data_good.title = ""
#         draw.text(xy=(70, 1265), text=f"{data_good.title[0:20]}", fill=(0, 0, 0), font=font)
#         font = ImageFont.truetype(font=font_path, size=70, encoding='utf-8')
#         if data_spec.price is None:
#             data_spec.price = 0
#         if data_spec.price_line is None:
#             data_spec.price_line = 0
#         draw.text(xy=(60, 1450), text='￥ ' + str('%.2f' % (data_spec.price/100)), fill=(0, 0, 0), font=font)
#         draw.text(xy=(390, 1450), text='￥' + str('%.2f' % (data_spec.price_line/100)), fill=(160, 160, 160), font=font)
#         draw.line([(370, 1495), (640, 1495)], fill="gray", width=4)
#
#     img_byte = io.BytesIO()
#     haibao_pil.convert('RGB').save(img_byte, format='jpeg', quality=60)
#     haibao_pil.close()
#     erweima_pil.close()
#     if not is_spec_post:
#         chanpin_pil.close()
#     #logo_pil.close()
#     return StreamingResponse(content=io.BytesIO(img_byte.getvalue()), media_type="image/jpeg")

    # bg = './code_default2.jpg'
    # path = "?".join((data.path, f"superiors_user_id={data.user_id}&id={data.spec_id}"))
    # #image_bg = Image.new("RGBA", (800, 1000), "#00ff00")
    # image_bg = Image.open(bg).convert('RGBA')
    # image_array = []
    # if data.spec_id is not None:
    #     data_spec = d_good.get_good_spec_by_id(data.spec_id)
    #     if data_spec is not None:
    #         if data_spec.post is not None:
    #             file_path = './assets' + data_spec.post.split('/assets')[1]
    #             image_bg = Image.open(file_path)
    # code_pic = wx_service.mall_wx_sdk.get_getwxacode(280, path)
    # stream = io.BytesIO(code_pic)
    # image_stream = Image.open(stream).convert("RGBA")
    #
    # #重置背景图片大小
    # # image_bg.resize((600,800))
    # image_bg_size = image_bg.size
    # image_bg.paste(image_stream, (image_bg_size[0] - 322, image_bg_size[1] - 360), image_stream)
    # img_byte = io.BytesIO()
    # image_bg.save(img_byte, format='png')
    # return StreamingResponse(content=io.BytesIO(img_byte.getvalue()), media_type="image/png")

@router.post(f'/get_code_pic', summary='获取用户推广小程序二维码,带参?user_id=n')
async def get_user_baseinfo(data:GoodspecPostpic):
    """
    返回png格式的图像二进制码
    """
    path = "?".join((data.path, f"superiors_user_id={data.user_id}"))
    code_pic = wx_service.mall_wx_sdk.get_getwxacode(300, path)
    # stream = io.BytesIO(code_pic)
    # erweima_pil = Image.open(stream).convert("RGBA")
    # img_byte = io.BytesIO()
    # haibao_pil.convert('RGB').save(img_byte, format='jpeg', quality=60)
    return StreamingResponse(content=io.BytesIO(code_pic), media_type="image/jpeg")

# @router.get(f'/get_posters', summary='获取海报图列表')
# async def get_posters():
#     return d_address.list_tposter_front()
#
# @router.post(f'/get_posters_share', summary='获取合成海报图')
# async def get_posters_share(data:Posterpic):
#     """
#     返回jpg格式的图像二进制码, poster_id 与 poster_url需要一致
#     """
#     if not data.poster_id or not data.user_id or not data.path or not data.poster_url:
#         raise HTTPException(status_code=304, detail='data error!!')
#     poster_info = d_address.get_poster_by_id(data.poster_id)
#     if not poster_info:
#         raise HTTPException(status_code=304, detail='poster_id error!!')
#     if poster_info.poster_url != data.poster_url:
#         raise HTTPException(status_code=304, detail='前后端path不一致!!')
#
#     haibao = './pic_package/xhaibao_default.jpg'
#     path = "?".join((data.path, f"superiors_user_id={data.user_id}"))
#     #haibao_pil = Image.open(haibao).convert('RGBA')
#     if data.poster_url is not None:
#         haibao = './' + data.poster_url.split('com/')[1]
#     try:
#         haibao_pil = Image.open(haibao).convert('RGBA')
#     except:
#         logging.info(f"get_posters_share，bad path: {haibao}")
#         haibao = './pic_package/xhaibao_default.jpg'
#         haibao_pil = Image.open(haibao).convert('RGBA')
#     #erweima_pil = Image.open(erweima).convert('RGBA')
#     #logo_pil = Image.open(logo).convert('RGBA').resize((208,201))
#     code_pic = wx_service.mall_wx_sdk.get_getwxacode(300, path)
#     stream = io.BytesIO(code_pic)
#     erweima_pil = Image.open(stream).convert("RGBA")
#     haibao_pil = haibao_pil.resize((1275, 2270))
#     haibao_pil.paste(erweima_pil, (828, 1857, erweima_pil.width + 828, erweima_pil.height + 1857))
#
#     img_byte = io.BytesIO()
#     haibao_pil.convert('RGB').save(img_byte, format='jpeg', quality=60)
#     haibao_pil.close()
#     erweima_pil.close()
#     #logo_pil.close()
#     return StreamingResponse(content=io.BytesIO(img_byte.getvalue()), media_type="image/jpeg")

@router.get(f'/get_user_info',summary='获取用户基本信息')
async def get_user_info(user_id: int):
    if user_id is None:
        raise HTTPException(status_code=203, detail='用户不存在')
    if user_id <= 0:
        raise HTTPException(status_code=203, detail='未找到用户')

    user_info = d_user.get_user_by_id(user_id)

    if user_info:
        # 更新系统用户级别
        if user_info.level_id == 0:
            d_user.update_sysuser_active(user_id)
        elif user_info.level_id == 1:
            d_user.update_sysuser_high(user_id)
        elif user_info.level_id == 2:
            d_user.update_sysuser_top(user_id)

        # 更新推广用户级别
        d_user.update_user_top(user_id)
    else:
        raise HTTPException(status_code=203, detail='未找到用户')

    user_info = d_user.get_user_by_id(user_id)
    if user_info.level_id == 0:
        user_info.withdraw = global_define.setting_withdraw['fans']
    elif user_info.level_id == 1:
        user_info.withdraw = global_define.setting_withdraw['member']
    elif user_info.level_id == 2:
        user_info.withdraw = global_define.setting_withdraw['boss']
    else:
        user_info.withdraw = global_define.setting_withdraw['bigboss']

    return user_info

@router.get(f'/get_user_info_by_phone',summary='通过手机号获取用户基本信息')
async def get_user_info_by_phone(phone: str):
    if str is None or str == '':
        raise HTTPException(status_code=203, detail='用户不存在')
    return d_user.get_user_by_phone(phone)

@router.post(f'/get_wx_token', summary='获取微信token')
async def get_wx_token():
    return wx_service.mall_wx_sdk.get_access_token()

@router.post(f'/get_wx_link', summary='获取微信短连接')
async def get_wx_link(page_url:str , page_title:str = None, is_permanent=False):
    return wx_service.mall_wx_sdk.get_getwxshorturl(page_url, page_title, is_permanent)

@router.post(f'/get_invited_user', summary='获取直推用户列表')
async def get_invited_user(user_id:int):
    return d_user.get_invited_user(user_id)

@router.post(f'/get_invparent_user', summary='获取直推下级团队成员列表')
async def get_parent_user(user_id:int):
    inv_list =  d_user.get_invited_user(user_id)
    invusers = []
    for i in inv_list:
        invusers.append(i.id)
    return d_user.get_invparent_user(invusers)

@router.post(f'/updateu', summary='更新用户基本信息')
async def update_user(user_data: UpdateUser):
    """
    更新用户，昵称、头像url、手机号码; valcode：tNP1Lp4wubp07Lx
    """
    update_data: m_schema.SUser = m_schema.SUser
    if user_data.valcode is None or user_data.valcode != 'tNP1Lp4wubp07Lx':
        raise HTTPException(status_code=403, detail='code error!')
    user_info = d_user.get_user_by_id(user_data.id)
    if not user_info:
        raise HTTPException(status_code=403, detail='user error!')
    update_data.id = user_data.id
    if user_data.phone is not None:
        if d_user.get_user_by_phone(user_data.phone) is not None:
            raise HTTPException(status_code=403, detail='手机已存在!')
        if user_info.phone is not None:
            if len(user_data.phone) > 10:
                raise HTTPException(status_code=403, detail='手机已绑定!')

    update_data.phone = user_data.phone
    if user_data.nickname:
        update_data.nickname = user_data.nickname
    else:
        update_data.nickname = user_info.nickname
    if user_data.avatar:
        update_data.avatar = user_data.avatar
    else:
        update_data.avatar = user_info.avatar
    d_user.update_user_base_info(update_data)
    return {'code': 200, 'detail': 'success'}


#@router.post(f'/get_user_test', response_model=m_order.UserGoodsInfo, summary='test')
@router.post(f'/get_user_test', summary='test')
async def get_user_test(user:m_schema.CreateUser):
    re_val={'status':200}
    re_val['data'] = d_user.update_sysuser_active(1)
    test = ''
    return re_val
