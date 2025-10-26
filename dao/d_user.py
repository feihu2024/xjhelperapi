from sqlalchemy.orm import Session
from common import Dao
from model.schema import TBalance, TCoin, TUser
from model.m_schema import *
from sqlalchemy import or_, and_, func
from typing import List, Optional
from sqlalchemy import text
import time
from datetime import datetime
from dao import d_settings
from fastapi import HTTPException

def get_user_by_id(user_id: int):
    with Dao() as db:
        return db.query(TUser).where(TUser.id == user_id).first()


def get_user_by_username(username: str):
    with Dao() as db:
        return db.query(TUser).where(TUser.username == username).first()


def get_user_by_email(email: str) -> TUser:
    with Dao() as db:
        return db.query(TUser).where(TUser.email == email).first()


def get_user_by_phone(phone: str):
    with Dao() as db:
        return db.query(TUser).where(TUser.phone == phone).first()


def get_user_by_openid(openid: str) -> Optional[TUser]:
    with Dao() as db:
        return db.query(TUser).where(TUser.open_id == openid).first()


def insert_user(user: TUser) -> TUser:
    with Dao() as db:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user


def get_user_baseinfo(user_id: int = 0):
    with Dao() as db:
        sql_str = f"select torder.user_id as user_id, t_user.username, t_user.nickname, t_user.avatar,count(torder.id) as order_count, sum(torder.paid_amount) as paid_balance_total, sum(torder.paid_balance) as flash_cost_total from ((t_flash_order as torder inner join t_user on torder.user_id = t_user.id) INNER JOIN t_package on torder.package_id=t_package.id) INNER JOIN t_good on t_package.good_id=t_good.id where torder.user_id={user_id}"
        res = db.execute(text(sql_str))
        res_fetch = res.fetchall()
        return res_fetch

def update_last_active_time(user_id: int = 0):
    with Dao() as db:
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        db.query(TUser).where(TUser.id == user_id).update({"last_active_time": now_time})
        db.commit()

#推广系，设置t_user的parent_id
def update_user_parent(user_id:int=0, parent_id:int=0):
    re = False
    with Dao() as db:
        user_info = db.query(TUser).where(TUser.id == user_id).first()
        if user_info:
            #要修改的父级与原来的相同，则不需要修改
            if user_info.parent_id != parent_id:
                if user_info.parent_id_history is not None:
                    re = db.query(TUser).where(TUser.id == user_id).update({"parent_id": parent_id, "parent_id_history":user_info.parent_id_history + "," + str(user_info.parent_id), "level_top_time":datetime.now()})
                else:
                    if user_info.parent_id is not None:
                        re = db.query(TUser).where(TUser.id == user_id).update({"parent_id": parent_id,"parent_id_history": str(user_info.parent_id), "level_top_time":datetime.now()})
                    else:
                        re = db.query(TUser).where(TUser.id == user_id).update({"parent_id": parent_id, "level_top_time":datetime.now()})
                db.commit()
    return re

#推广系，满足升级条件时，升级为顶级推广人
def update_user_top(user_id: int = 0):
    parent_info = get_user_by_id(user_id)
    if parent_info:
        user_count = get_lower_user_count(user_id)
        upload_count = d_settings.get_settings().recommend_num
        # 派生用户达到设置数量，而且不是顶级推荐人，会员级别达到1以上，则进行顶级升级
        is_up = True
        if user_count >= upload_count and parent_info.parent_id is None and parent_info.level_id >= 1:
            update_user_parent(user_id, 0)
            is_up = False

        if parent_info.parent_id is None:
            parent_info.parent_id = -1
        if user_count >= upload_count and parent_info.parent_id > 0 and parent_info.level_id >= 1 and is_up:
            with Dao() as db:
                list = db.query(TUser).where(TUser.parent_id == user_id).all()
                user_limit = d_settings.get_settings().parent_user_limit
                limit_num = 1
                for li in list:
                    if limit_num > user_limit:
                        break
                    if li.level_id > 0:
                        update_user_parent(li.id, parent_info.parent_id)
                        limit_num += 1
                #将用户推荐级别设置为顶级
                update_user_parent(user_id,0)

def update_sysuser_level(user_id:int = 0):
    user_info = get_user_by_id(user_id)
    if user_info and user_info.level_id < 3:
        update_date = {}
        if user_info.level_id == 0:
            update_date['level_id'] = 1
            update_date["level_one_time"] = datetime.now()
        elif user_info.level_id == 1:
            update_date['level_id'] = 2
            update_date["level_two_time"] = datetime.now()
        elif user_info.level_id == 2:
            update_date['level_id'] = 3
            update_date["level_three_time"] = datetime.now()
        if update_date:
            with Dao() as db:
                re = db.query(TUser).where(TUser.id == user_id).update(update_date)
                db.commit()
                return re
    return 0

#会员系，活跃会员升级为高级会员
def update_sysuser_high(user_id:int = 0):
    sys_settings = d_settings.get_settings()
    user_info = get_user_by_id(user_id)
    re = 0
    if user_info and user_info.level_id == 1:
        lower_count = get_lower_user_count(user_id)
        if lower_count >= sys_settings.many_high_user:
            re = update_sysuser_level(user_id)
            # 更新推荐人级别
            # if user_info.invited_user_id is not None:
            #     update_sysuser_top(user_info.invited_user_id)
    return re

#会员系，高级会员升级为顶级会员
def update_sysuser_top(user_id:int = 0):
    sys_settings = d_settings.get_settings()
    user_info = get_user_by_id(user_id)
    re = 0
    if user_info and user_info.level_id == 2:
        lower_count = get_lower_user_count(user_id, 1)
        if lower_count >= sys_settings.many_top_user:
            re = update_sysuser_level(user_id)
    return re

#推广系， 下级会员统计
def get_lower_count(parent_id:int = 0, level:int = 0):
    with Dao() as db:
        return db.query(TUser).where(TUser.parent_id == parent_id).where(TUser.level_id > level).count()

#会员系， 下级会员统计
def get_lower_user_count(invited_user_id:int = 0, level:int = 0):
    with Dao() as db:
        return db.query(TUser).where(TUser.invited_user_id == invited_user_id).where(TUser.level_id > level).count()

def get_top_id(user_id:int = 0):
    with Dao() as db:
        user_info = db.query(TUser).where(TUser.id==user_id).first()
        if user_info is None:
            #raise HTTPException(f"未知用户：{user_id}")
            return 0
        re_id = user_info.id
        if user_info.parent_id is None:
            user_info.parent_id = 0
        if user_info.parent_id > 0:
            return get_top_id(user_info.parent_id)
        else:
            return re_id

def get_top_users(top_id:int = 0, data_list:list = [], id_list:list = []):
    data = {}
    id_list.append(top_id)
    with Dao() as db:
        lower_data = db.query(TUser).where(TUser.parent_id==top_id).all()
        data['total'] = len(lower_data)
        data['data'] = lower_data
        if data['total'] > 0:
            data_list.append(data)
        for ld in lower_data:
            if ld.id not in id_list:
                get_top_users(ld.id, data_list, id_list)
    return data_list

def get_recommend_users_tree(user_id:int = 0):
    top_id = get_top_id(user_id)
    user_info = get_user_by_id(top_id)
    re_data = []
    if user_info:
        re_data.append(user_info)
        tree_data = get_top_users(top_id,[],[])
        re_data.append(tree_data)
    return re_data

def get_invited_user(user_id:int):
    with Dao() as db:
        return db.query(TUser).filter(TUser.invited_user_id==user_id).all()

def get_invparent_user(user_ids:list):
    with Dao() as db:
        return db.query(TUser).filter(TUser.parent_id.in_(user_ids)).all()

def get_invparent_user_ids(user_id:int):
    ls = get_invparent_user([user_id])
    re_ids = []
    for i in ls:
        re_ids.append(i.id)
    return re_ids

def get_invited_user_ids(user_id:int):
    ls = get_invited_user(user_id)
    re_ids = []
    for i in ls:
        re_ids.append(i.id)
    return re_ids

def get_member_ids_one(user_ids:list):
    re_ids = []
    with Dao() as db:
        res = db.query(TUser.id).filter(TUser.parent_id.in_(user_ids)).all()
        if res is not None:
            for r in res:
                re_ids.append(r.id)
    return re_ids

def get_member_ids(user_id:int):
    ids = []
    get_ids = get_member_ids_one([user_id])
    if len(get_ids) > 0:
        for i in get_ids:
            ids.append(i)
        get_ids = get_member_ids_one(get_ids)
        if len(get_ids) > 0:
            for i in get_ids:
                ids.append(i)
    return ids

def get_comein_users(user_id:int):
    re_val = {"parent_uid":None, "top_uid":None, "invited_uid":None, "supplier_uid":None, "eqlevel_uid":None}
    user_info = get_user_by_id(user_id)
    top_user_id = get_top_id(user_id)
    #if top_user_id != user_id and top_user_id > 0:
    if top_user_id > 0:
        top_info = get_user_by_id(top_user_id)
        if top_info:
            if top_info.parent_id is not None and top_info.level_id > 0:
                re_val['top_uid'] = top_user_id
                if top_info.invited_user_id is not None:
                    top_invited_info = get_user_by_id(top_info.invited_user_id)
                    if top_invited_info:
                        re_val['eqlevel_uid'] = top_info.invited_user_id

    #层级收益与推荐收益不能同时获取
    # if user_info.parent_id is not None:
    #     re_val['parent_uid'] = user_info.parent_id
    # elif user_info.invited_user_id is not None:
    #     re_val['invited_uid'] = user_info.invited_user_id
    #
    # if user_info.invited_user_id is not None and re_val['invited_uid'] is None and user_info.parent_id != user_info.invited_user_id:
    #     re_val['invited_uid'] = user_info.invited_user_id

    # 层级收益与推荐收益可以同时获取
    if user_info.parent_id is not None:
        re_val['parent_uid'] = user_info.parent_id
    if user_info.invited_user_id is not None:
        re_val['invited_uid'] = user_info.invited_user_id

    return re_val

def get_user_forcard(card: str):
    with Dao() as db:
        return db.query(TUser).filter(TUser.id_card == card).first()

def del_user(user_id: int):
    with Dao() as db:
        db.query(TUser).filter(TUser.id == user_id).delete()
        db.commit()

def update_user_base_info(user_data: SUser):
    with Dao() as db:
        re = db.query(TUser).where(TUser.id == user_data.id).update({"nickname": user_data.nickname, "phone":user_data.phone, "avatar": user_data.avatar})
        db.commit()

def filter_user(items: dict, search_items: dict = {}, set_items: dict = {}, page: int = 1, page_size: int = 20) -> List[
    SUser]:
    with Dao() as db:
        q = db.query(TUser)

        if 'id' in items:
            q = q.where(TUser.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUser.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUser.id <= items['id_end'])

        if 'username' in items:
            q = q.where(TUser.username == items['username'])
        if 'username_start' in items:
            q = q.where(TUser.username >= items['username_start'])
        if 'username_end' in items:
            q = q.where(TUser.username <= items['username_end'])

        if 'email' in items:
            q = q.where(TUser.email == items['email'])
        if 'email_start' in items:
            q = q.where(TUser.email >= items['email_start'])
        if 'email_end' in items:
            q = q.where(TUser.email <= items['email_end'])

        if 'open_id' in items:
            q = q.where(TUser.open_id == items['open_id'])
        if 'open_id_start' in items:
            q = q.where(TUser.open_id >= items['open_id_start'])
        if 'open_id_end' in items:
            q = q.where(TUser.open_id <= items['open_id_end'])

        if 'union_id' in items:
            q = q.where(TUser.union_id == items['union_id'])
        if 'union_id_start' in items:
            q = q.where(TUser.union_id >= items['union_id_start'])
        if 'union_id_end' in items:
            q = q.where(TUser.union_id <= items['union_id_end'])

        if 'password' in items:
            q = q.where(TUser.password == items['password'])
        if 'password_start' in items:
            q = q.where(TUser.password >= items['password_start'])
        if 'password_end' in items:
            q = q.where(TUser.password <= items['password_end'])

        if 'nickname' in items:
            q = q.where(TUser.nickname == items['nickname'])
        if 'nickname_start' in items:
            q = q.where(TUser.nickname >= items['nickname_start'])
        if 'nickname_end' in items:
            q = q.where(TUser.nickname <= items['nickname_end'])

        if 'phone' in items:
            q = q.where(TUser.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TUser.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TUser.phone <= items['phone_end'])

        if 'id_card' in items:
            q = q.where(TUser.id_card == items['id_card'])
        if 'id_card_start' in items:
            q = q.where(TUser.id_card >= items['id_card_start'])
        if 'id_card_end' in items:
            q = q.where(TUser.id_card <= items['id_card_end'])

        if 'level_id' in items:
            q = q.where(TUser.level_id == items['level_id'])
        if 'level_id_start' in items:
            q = q.where(TUser.level_id >= items['level_id_start'])
        if 'level_id_end' in items:
            q = q.where(TUser.level_id <= items['level_id_end'])

        if 'status' in items:
            q = q.where(TUser.status == items['status'])
        if 'status_start' in items:
            q = q.where(TUser.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TUser.status <= items['status_end'])

        if 'register_time' in items:
            q = q.where(TUser.register_time == items['register_time'])
        if 'register_time_start' in items:
            q = q.where(TUser.register_time >= items['register_time_start'])
        if 'register_time_end' in items:
            q = q.where(TUser.register_time <= items['register_time_end'])

        if 'avatar' in items:
            q = q.where(TUser.avatar == items['avatar'])
        if 'avatar_start' in items:
            q = q.where(TUser.avatar >= items['avatar_start'])
        if 'avatar_end' in items:
            q = q.where(TUser.avatar <= items['avatar_end'])

        if 'invited_user_id' in items:
            q = q.where(TUser.invited_user_id == items['invited_user_id'])
        if 'invited_user_id_start' in items:
            q = q.where(TUser.invited_user_id >= items['invited_user_id_start'])
        if 'invited_user_id_end' in items:
            q = q.where(TUser.invited_user_id <= items['invited_user_id_end'])

        if 'coin' in items:
            q = q.where(TUser.coin == items['coin'])
        if 'coin_start' in items:
            q = q.where(TUser.coin >= items['coin_start'])
        if 'coin_end' in items:
            q = q.where(TUser.coin <= items['coin_end'])

        if 'gender' in items:
            q = q.where(TUser.gender == items['gender'])
        if 'gender_start' in items:
            q = q.where(TUser.gender >= items['gender_start'])
        if 'gender_end' in items:
            q = q.where(TUser.gender <= items['gender_end'])

        if 'last_active_time' in items:
            q = q.where(TUser.last_active_time == items['last_active_time'])
        if 'last_active_time_start' in items:
            q = q.where(TUser.last_active_time >= items['last_active_time_start'])
        if 'last_active_time_end' in items:
            q = q.where(TUser.last_active_time <= items['last_active_time_end'])

        if 'name' in items:
            q = q.where(TUser.name == items['name'])
        if 'name_start' in items:
            q = q.where(TUser.name >= items['name_start'])
        if 'name_end' in items:
            q = q.where(TUser.name <= items['name_end'])

        if 'is_agree' in items:
            q = q.where(TUser.is_agree == items['is_agree'])
        if 'is_agree_start' in items:
            q = q.where(TUser.is_agree >= items['is_agree_start'])
        if 'is_agree_end' in items:
            q = q.where(TUser.is_agree <= items['is_agree_end'])

        if 'parent_id' in items:
            q = q.where(TUser.parent_id == items['parent_id'])
        if 'parent_id_start' in items:
            q = q.where(TUser.parent_id >= items['parent_id_start'])
        if 'parent_id_end' in items:
            q = q.where(TUser.parent_id <= items['parent_id_end'])

        if 'parent_id_history' in items:
            q = q.where(TUser.parent_id_history == items['parent_id_history'])
        if 'parent_id_history_start' in items:
            q = q.where(TUser.parent_id_history >= items['parent_id_history_start'])
        if 'parent_id_history_end' in items:
            q = q.where(TUser.parent_id_history <= items['parent_id_history_end'])

        if 'id' in set_items:
            q = q.where(TUser.id.in_(set_items['id']))

        if 'username' in set_items:
            q = q.where(TUser.username.in_(set_items['username']))

        if 'email' in set_items:
            q = q.where(TUser.email.in_(set_items['email']))

        if 'open_id' in set_items:
            q = q.where(TUser.open_id.in_(set_items['open_id']))

        if 'union_id' in set_items:
            q = q.where(TUser.union_id.in_(set_items['union_id']))

        if 'password' in set_items:
            q = q.where(TUser.password.in_(set_items['password']))

        if 'nickname' in set_items:
            q = q.where(TUser.nickname.in_(set_items['nickname']))

        if 'phone' in set_items:
            q = q.where(TUser.phone.in_(set_items['phone']))

        if 'id_card' in set_items:
            q = q.where(TUser.id_card.in_(set_items['id_card']))

        if 'level_id' in set_items:
            q = q.where(TUser.level_id.in_(set_items['level_id']))

        if 'status' in set_items:
            q = q.where(TUser.status.in_(set_items['status']))

        if 'register_time' in set_items:
            q = q.where(TUser.register_time.in_(set_items['register_time']))

        if 'avatar' in set_items:
            q = q.where(TUser.avatar.in_(set_items['avatar']))

        if 'invited_user_id' in set_items:
            q = q.where(TUser.invited_user_id.in_(set_items['invited_user_id']))

        if 'coin' in set_items:
            q = q.where(TUser.coin.in_(set_items['coin']))

        if 'gender' in set_items:
            q = q.where(TUser.gender.in_(set_items['gender']))

        if 'last_active_time' in set_items:
            q = q.where(TUser.last_active_time.in_(set_items['last_active_time']))

        if 'name' in set_items:
            q = q.where(TUser.name.in_(set_items['name']))

        if 'is_agree' in set_items:
            q = q.where(TUser.is_agree.in_(set_items['is_agree']))

        if 'parent_id' in set_items:
            q = q.where(TUser.parent_id.in_(set_items['parent_id']))

        if 'parent_id_history' in set_items:
            q = q.where(TUser.parent_id_history.in_(set_items['parent_id_history']))

        if 'username' in search_items:
            q = q.where(TUser.username.like(search_items['username']))

        if 'email' in search_items:
            q = q.where(TUser.email.like(search_items['email']))

        if 'open_id' in search_items:
            q = q.where(TUser.open_id.like(search_items['open_id']))

        if 'union_id' in search_items:
            q = q.where(TUser.union_id.like(search_items['union_id']))

        if 'password' in search_items:
            q = q.where(TUser.password.like(search_items['password']))

        if 'nickname' in search_items:
            q = q.where(TUser.nickname.like(search_items['nickname']))

        if 'phone' in search_items:
            q = q.where(TUser.phone.like(search_items['phone']))

        if 'id_card' in search_items:
            q = q.where(TUser.id_card.like(search_items['id_card']))

        if 'avatar' in search_items:
            q = q.where(TUser.avatar.like(search_items['avatar']))

        if 'name' in search_items:
            q = q.where(TUser.name.like(search_items['name']))

        if 'parent_id_history' in search_items:
            q = q.where(TUser.parent_id_history.like(search_items['parent_id_history']))
        q = q.order_by(TUser.id.desc())

        t_user_list = q.offset(page * page_size - page_size).limit(page_size).all()
        return [SUser.parse_obj(t.__dict__) for t in t_user_list]