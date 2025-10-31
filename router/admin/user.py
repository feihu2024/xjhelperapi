from model.m_schema import *
from fastapi import APIRouter, Depends, Header, HTTPException, Request
from dao import d_admin, d_user, d_db
from model import m_admin
import datetime, re
# from service import express_service, share_fee_service
from common import Dao
from fastapi.responses import JSONResponse
from fastapi import HTTPException

async def verify_token(jinnengyuansession: str = Header(...)):
    #if jinnengyuansession != "fake-super-secret-token":
    if not d_admin.is_login(jinnengyuansession):
        raise HTTPException(status_code=400, detail="login invalid")

router = APIRouter()

ontent = {"message": "add cookie"}


@router.post(f'/login', summary='管理登录')
async def admin_login(admin: m_admin.AdminRequest):
    """
    返回：jinnengyuansession携带到请求体head中，作为后端接口请求的token
    """
    username = admin.username
    password = admin.password
    res = d_admin.login_for_token(username, password)
    if res:
        content = {"message": "add cookie"}
        response = JSONResponse(content=content)
        token_val = res.get('token_val')
        response.set_cookie(key="jinnengyuansession", value=f"{token_val}")
        return {"key": "jinnengyuansession", "value": f"{token_val}", "user_id": res.get('user_id')}
    else:
        raise HTTPException(status_code=404, detail={'status': 404, 'massage': 'error'})


@router.get(f'/logintest', summary='获取测试token')
async def logintest():
    """
    返回：jinnengyuansession携带到请求体head中，作为后端接口请求的token
    """
    return d_admin.login_shop_token('admintest', 'kc1n6MVB', 10)


#
# @router.post(f'/shop_login', summary='资金运营商家登录')
# async def shop_login(admin: m_admin.AdminRequest):
#     """
#     username:tom password:abcd
#     """
#     username = admin.username
#     password = admin.password
#     shop_info: List[m_schema.SShShop] = d_db.filter_sh_shop(items={'user_name': username, 'user_pass':password}, search_items={},
#                                                             set_items={})
#     if shop_info:
#         res = d_admin.login_shop_token(username, password, shop_info[0].id)
#         if shop_info[0].parent_id != 0:
#             pinpai_info: List[m_schema.SShShop] = d_db.filter_sh_shop(items={'id':shop_info[0].parent_id}, search_items={},
#                                                             set_items={})
#         else:
#             pinpai_info = shop_info
#         token_val = res.get('token_val')
#         return {"key":"kemaikemaisession", "value":f"{token_val}", "user_id": res.get('user_id'), "data":shop_info[0], "pinpai_data":pinpai_info[0] }
#     else:
#         raise HTTPException(status_code=404, detail={'status': 404, 'massage': 'error'})

@router.post(f'/login_out', summary='管理退出登录')
async def login_out():
    content = {"message": "del cookie"}
    response = JSONResponse(content=content)
    response.set_cookie(key="kemaikemaisession", value="****************")
    return response


#
# @router.post(f'/daily_add', response_model=int, summary='根据日期查询每日新增')
# async def user_daily_add(day: datetime.date = datetime.date.today()) -> int:
#     """
#     根据日期查询当日新增
#     """
#     return d_admin.query_daily_add(day)
#
#
# @router.get(f'/mall_tips', response_model=None, summary='查询商城提示 比如发货提现提醒')
# async def get_mall_tips():
#     return None
#
#
# @router.get(f'/get_relationships', summary='返回某个用户的推荐关系（上下层级都包括）')
# async def get_user_relationship(user_id:int = 0):
#     if user_id>0:
#         return d_user.get_recommend_users_tree(user_id)
#     else:
#         return {"status":400, "detail": "非法用户id"}

@router.post(f'/get_user_info', dependencies=[Depends(verify_token)], summary='返回某个用户的基本信息')
async def get_user_info(request: Request):
    jinnengyuansession = request.headers.get('jinnengyuansession')
    user_id = d_admin.get_login_id(jinnengyuansession)
    if user_id > 0:
        return d_admin.get_admin_by_id(user_id)
    else:
        return {"status": 400, "detail": "login error!"}


@router.post(f'/admin_update', dependencies=[Depends(verify_token)], response_model=str, summary='管理信息修改')
async def update_admin(item: SAdmin) -> str:
    d_db.update_admin(item)
    return "success"


@router.post(f'/admin_create', dependencies=[Depends(verify_token)], response_model=SAdmin, summary='创建管理员')
async def create_admin(item: CreateAdmin) -> SAdmin:
    dict_item = dict(item)
    for k, v in dict_item.items():
        if v is not None:
            v = str(v)
            v = v.replace(" ", "")
            get_search = re.search(r"'", v, flags=0)
            get_search2 = re.search(r'%27', v, flags=0)
            get_search3 = re.search(r'unionselect', v, flags=0)
            if get_search or get_search2 or get_search3:
                raise HTTPException(status_code=404, detail='bad way~~~~~~')

    return d_db.insert_admin(item)

