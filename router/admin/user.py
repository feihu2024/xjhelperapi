from model.m_schema import *
from fastapi import APIRouter
from dao import d_admin, d_user, d_groupsir, d_order, d_db
from model import m_admin
from typing import List
import datetime
from model import schema, m_schema
from service import express_service, share_fee_service
from common import Dao
from fastapi.responses import JSONResponse
from fastapi import HTTPException

router = APIRouter()


@router.get(f'/users_data', response_model=m_admin.UserData, summary='查询会员总数 活跃会员 当日新增 男女比例')
async def platform_userdata():
    """
    查询平台用户数据:  会员总数  活跃会员  当日新增  男女比例
    """
    user_data = d_admin.query_users()
    return user_data


@router.get(f'/silents_data', summary='查询不活跃用户名单')
async def get_inactive_users(page: int = 1, page_size: int = 10) -> List[m_schema.CreateUser]:
    """
     获取非活跃用户名单
    """
    silents = d_admin.silent_users(page, page_size)
    return [m_schema.CreateUser.parse_obj(t.__dict__) for t in silents]


@router.get(f'/sales_data', response_model=m_admin.SaleData, summary='查询销售业绩')
async def get_platform_data():
    sale_data = d_admin.query_sales()
    return sale_data


@router.post(f'/login', summary='管理登录')
async def admin_login(admin: m_admin.AdminRequest):
    """
    username:tom password:abcd
    """
    username = admin.username
    password = admin.password
    res = d_admin.login_for_token(username, password)
    if res:
        content = {"message": "add cookie"}
        response = JSONResponse(content=content)
        response.set_cookie(key="kemaikemaisession", value=f"{res}")
        return {"key":"kemaikemaisession", "value":f"{res}"}
    else:
        raise HTTPException(status_code=404, detail={'status': 404, 'massage': 'error'})

    #return d_admin.login_for_token(username, password)

@router.post(f'/login_out', summary='管理退出登录')
async def login_out():
    content = {"message": "del cookie"}
    response = JSONResponse(content=content)
    response.set_cookie(key="kemaikemaisession", value="****************")
    return response

@router.post(f'/daily_add', response_model=int, summary='根据日期查询每日新增')
async def user_daily_add(day: datetime.date = datetime.date.today()) -> int:
    """
    根据日期查询当日新增
    """
    return d_admin.query_daily_add(day)


@router.get(f'/mall_tips', response_model=None, summary='查询商城提示 比如发货提现提醒')
async def get_mall_tips():
    return None


@router.get(f'/get_relationships', summary='返回某个用户的推荐关系（上下层级都包括）')
async def get_user_relationship(user_id:int = 0):
    if user_id>0:
        return d_user.get_recommend_users_tree(user_id)
    else:
        return {"status":400, "detail": "非法用户id"}

@router.post(f'/get_user_info', summary='返回某个用户的基本信息')
async def get_user_info(user_id:int = 0):
    if user_id>0:
        return d_user.get_user_by_id(user_id)
    else:
        return {"status":400, "detail": "非法用户id"}


@router.get(f'/get_user_test', summary='test')
async def get_user_test(user_id:int=1, parent_id:int=1):
    #re_id = d_user.update_sysuser_high(user_id)
    #d_groupsir.add_groupsir(user_id,parent_id,'')
    orders = [schema.TOrder(good_id=1, number=4),schema.TOrder(good_id=124, number=4)]
    with Dao() as db:
        db.add_all(orders)
        db.flush()
        d_order.update_order_source(orders)
        db.commit()
    #share_fee_service.share_mall_fee_with_other(user_id)
    return 'yes'

@router.get(f'/duser', summary='删除用户')
async def del_user(user_id:int, valcode:str):
    if valcode == 'omgc@kXw%tyyfBI4$q':
        user_info = d_user.get_user_by_id(user_id)
        if user_info:
            d_user.del_user(user_id)
            return {"status": 200, "detail": "success"}

    return {"status": 404, "detail": "error"}

@router.get(f'/user/filter', response_model=FilterResUser)
async def filter_user(
        id: Optional[str] = None,
        username: Optional[str] = None,
        email: Optional[str] = None,
        open_id: Optional[str] = None,
        union_id: Optional[str] = None,
        password: Optional[str] = None,
        nickname: Optional[str] = None,
        phone: Optional[str] = None,
        id_card: Optional[str] = None,
        level_id: Optional[str] = None,
        status: Optional[str] = None,
        register_time: Optional[str] = None,
        avatar: Optional[str] = None,
        invited_user_id: Optional[str] = None,
        coin: Optional[str] = None,
        gender: Optional[str] = None,
        last_active_time: Optional[str] = None,
        name: Optional[str] = None,
        is_agree: Optional[str] = None,
        parent_id: Optional[str] = None,
        parent_id_history: Optional[str] = None,
        l_id: Optional[str] = None,
        l_username: Optional[str] = None,
        l_email: Optional[str] = None,
        l_open_id: Optional[str] = None,
        l_union_id: Optional[str] = None,
        l_password: Optional[str] = None,
        l_nickname: Optional[str] = None,
        l_phone: Optional[str] = None,
        l_id_card: Optional[str] = None,
        l_level_id: Optional[str] = None,
        l_status: Optional[str] = None,
        l_register_time: Optional[str] = None,
        l_avatar: Optional[str] = None,
        l_invited_user_id: Optional[str] = None,
        l_coin: Optional[str] = None,
        l_gender: Optional[str] = None,
        l_last_active_time: Optional[str] = None,
        l_name: Optional[str] = None,
        l_is_agree: Optional[str] = None,
        l_parent_id: Optional[str] = None,
        l_parent_id_history: Optional[str] = None,
        s_username: Optional[str] = None,
        s_email: Optional[str] = None,
        s_open_id: Optional[str] = None,
        s_union_id: Optional[str] = None,
        s_password: Optional[str] = None,
        s_nickname: Optional[str] = None,
        s_phone: Optional[str] = None,
        s_id_card: Optional[str] = None,
        s_avatar: Optional[str] = None,
        s_name: Optional[str] = None,
        s_parent_id_history: Optional[str] = None,
        page: int = 1,
        page_size: int = 20) -> FilterResUser:
    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """

    items = dict()
    search_items = dict()
    set_items = dict()

    if id is not None:
        values = id.split(',')
        if len(values) == 1:
            val = values[0]
            items['id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['id_start'] = int(val)

            val = values[1]
            if val != '':
                items['id_end'] = int(val)

    if username is not None:
        values = username.split(',')
        if len(values) == 1:
            val = values[0]
            items['username'] = val
        else:
            val = values[0]
            if val != '':
                items['username_start'] = val

            val = values[1]
            if val != '':
                items['username_end'] = val

    if email is not None:
        values = email.split(',')
        if len(values) == 1:
            val = values[0]
            items['email'] = val
        else:
            val = values[0]
            if val != '':
                items['email_start'] = val

            val = values[1]
            if val != '':
                items['email_end'] = val

    if open_id is not None:
        values = open_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['open_id'] = val
        else:
            val = values[0]
            if val != '':
                items['open_id_start'] = val

            val = values[1]
            if val != '':
                items['open_id_end'] = val

    if union_id is not None:
        values = union_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['union_id'] = val
        else:
            val = values[0]
            if val != '':
                items['union_id_start'] = val

            val = values[1]
            if val != '':
                items['union_id_end'] = val

    if password is not None:
        values = password.split(',')
        if len(values) == 1:
            val = values[0]
            items['password'] = val
        else:
            val = values[0]
            if val != '':
                items['password_start'] = val

            val = values[1]
            if val != '':
                items['password_end'] = val

    if nickname is not None:
        values = nickname.split(',')
        if len(values) == 1:
            val = values[0]
            items['nickname'] = val
        else:
            val = values[0]
            if val != '':
                items['nickname_start'] = val

            val = values[1]
            if val != '':
                items['nickname_end'] = val

    if phone is not None:
        values = phone.split(',')
        if len(values) == 1:
            val = values[0]
            items['phone'] = val
        else:
            val = values[0]
            if val != '':
                items['phone_start'] = val

            val = values[1]
            if val != '':
                items['phone_end'] = val

    if id_card is not None:
        values = id_card.split(',')
        if len(values) == 1:
            val = values[0]
            items['id_card'] = val
        else:
            val = values[0]
            if val != '':
                items['id_card_start'] = val

            val = values[1]
            if val != '':
                items['id_card_end'] = val

    if level_id is not None:
        values = level_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['level_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['level_id_start'] = int(val)

            val = values[1]
            if val != '':
                items['level_id_end'] = int(val)

    if status is not None:
        values = status.split(',')
        if len(values) == 1:
            val = values[0]
            items['status'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['status_start'] = int(val)

            val = values[1]
            if val != '':
                items['status_end'] = int(val)

    if register_time is not None:
        values = register_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['register_time'] = datetime.datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['register_time_start'] = datetime.datetime.fromtimestamp(int(val))

            val = values[1]
            if val != '':
                items['register_time_end'] = datetime.datetime.fromtimestamp(int(val))

    if avatar is not None:
        values = avatar.split(',')
        if len(values) == 1:
            val = values[0]
            items['avatar'] = val
        else:
            val = values[0]
            if val != '':
                items['avatar_start'] = val

            val = values[1]
            if val != '':
                items['avatar_end'] = val

    if invited_user_id is not None:
        values = invited_user_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['invited_user_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['invited_user_id_start'] = int(val)

            val = values[1]
            if val != '':
                items['invited_user_id_end'] = int(val)

    if coin is not None:
        values = coin.split(',')
        if len(values) == 1:
            val = values[0]
            items['coin'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['coin_start'] = int(val)

            val = values[1]
            if val != '':
                items['coin_end'] = int(val)

    if gender is not None:
        values = gender.split(',')
        if len(values) == 1:
            val = values[0]
            items['gender'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['gender_start'] = int(val)

            val = values[1]
            if val != '':
                items['gender_end'] = int(val)

    if last_active_time is not None:
        values = last_active_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['last_active_time'] = datetime.datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['last_active_time_start'] = datetime.datetime.fromtimestamp(int(val))

            val = values[1]
            if val != '':
                items['last_active_time_end'] = datetime.datetime.fromtimestamp(int(val))

    if name is not None:
        values = name.split(',')
        if len(values) == 1:
            val = values[0]
            items['name'] = val
        else:
            val = values[0]
            if val != '':
                items['name_start'] = val

            val = values[1]
            if val != '':
                items['name_end'] = val

    if is_agree is not None:
        values = is_agree.split(',')
        if len(values) == 1:
            val = values[0]
            items['is_agree'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['is_agree_start'] = int(val)

            val = values[1]
            if val != '':
                items['is_agree_end'] = int(val)

    if parent_id is not None:
        values = parent_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['parent_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['parent_id_start'] = int(val)

            val = values[1]
            if val != '':
                items['parent_id_end'] = int(val)

    if parent_id_history is not None:
        values = parent_id_history.split(',')
        if len(values) == 1:
            val = values[0]
            items['parent_id_history'] = val
        else:
            val = values[0]
            if val != '':
                items['parent_id_history_start'] = val

            val = values[1]
            if val != '':
                items['parent_id_history_end'] = val

    if s_username is not None:
        search_items['username'] = '%' + s_username + '%'

    if s_email is not None:
        search_items['email'] = '%' + s_email + '%'

    if s_open_id is not None:
        search_items['open_id'] = '%' + s_open_id + '%'

    if s_union_id is not None:
        search_items['union_id'] = '%' + s_union_id + '%'

    if s_password is not None:
        search_items['password'] = '%' + s_password + '%'

    if s_nickname is not None:
        search_items['nickname'] = '%' + s_nickname + '%'

    if s_phone is not None:
        search_items['phone'] = '%' + s_phone + '%'

    if s_id_card is not None:
        search_items['id_card'] = '%' + s_id_card + '%'

    if s_avatar is not None:
        search_items['avatar'] = '%' + s_avatar + '%'

    if s_name is not None:
        search_items['name'] = '%' + s_name + '%'

    if s_parent_id_history is not None:
        search_items['parent_id_history'] = '%' + s_parent_id_history + '%'

    if l_id is not None:
        values = l_id.split(',')
        values = [int(val) for val in values]
        set_items['id'] = values

    if l_username is not None:
        values = l_username.split(',')
        values = [val for val in values]
        set_items['username'] = values

    if l_email is not None:
        values = l_email.split(',')
        values = [val for val in values]
        set_items['email'] = values

    if l_open_id is not None:
        values = l_open_id.split(',')
        values = [val for val in values]
        set_items['open_id'] = values

    if l_union_id is not None:
        values = l_union_id.split(',')
        values = [val for val in values]
        set_items['union_id'] = values

    if l_password is not None:
        values = l_password.split(',')
        values = [val for val in values]
        set_items['password'] = values

    if l_nickname is not None:
        values = l_nickname.split(',')
        values = [val for val in values]
        set_items['nickname'] = values

    if l_phone is not None:
        values = l_phone.split(',')
        values = [val for val in values]
        set_items['phone'] = values

    if l_id_card is not None:
        values = l_id_card.split(',')
        values = [val for val in values]
        set_items['id_card'] = values

    if l_level_id is not None:
        values = l_level_id.split(',')
        values = [int(val) for val in values]
        set_items['level_id'] = values

    if l_status is not None:
        values = l_status.split(',')
        values = [int(val) for val in values]
        set_items['status'] = values

    if l_register_time is not None:
        values = l_register_time.split(',')
        values = [datetime.datetime.fromtimestamp(int(val)) for val in values]
        set_items['register_time'] = values

    if l_avatar is not None:
        values = l_avatar.split(',')
        values = [val for val in values]
        set_items['avatar'] = values

    if l_invited_user_id is not None:
        values = l_invited_user_id.split(',')
        values = [int(val) for val in values]
        set_items['invited_user_id'] = values

    if l_coin is not None:
        values = l_coin.split(',')
        values = [int(val) for val in values]
        set_items['coin'] = values

    if l_gender is not None:
        values = l_gender.split(',')
        values = [int(val) for val in values]
        set_items['gender'] = values

    if l_last_active_time is not None:
        values = l_last_active_time.split(',')
        values = [datetime.datetime.fromtimestamp(int(val)) for val in values]
        set_items['last_active_time'] = values

    if l_name is not None:
        values = l_name.split(',')
        values = [val for val in values]
        set_items['name'] = values

    if l_is_agree is not None:
        values = l_is_agree.split(',')
        values = [int(val) for val in values]
        set_items['is_agree'] = values

    if l_parent_id is not None:
        values = l_parent_id.split(',')
        values = [int(val) for val in values]
        set_items['parent_id'] = values

    if l_parent_id_history is not None:
        values = l_parent_id_history.split(',')
        values = [val for val in values]
        set_items['parent_id_history'] = values

    data = d_user.filter_user(items, search_items, set_items, page, page_size)
    c = d_db.filter_count_user(items, search_items, set_items)
    return FilterResUser(data=data, total=c)

