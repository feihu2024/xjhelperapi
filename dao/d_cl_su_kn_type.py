from sqlalchemy.orm import Session
from common import Dao
from model.schema import TShClas, TShSubject, TQuestionType, TKnowledgePoint
from model.m_schema import *
from sqlalchemy import or_, and_, func
from typing import List, Optional
from sqlalchemy import text
import time
from datetime import datetime
from fastapi import HTTPException


def get_class_list(page:int = 1, page_size:int = 20):
    with Dao() as db:
        q = db.query(TShClas).offset(page * page_size - page_size).limit(page_size).all()
        return q


# def insert_user(user: TUser) -> TUser:
#     with Dao() as db:
#         db.add(user)
#         db.commit()
#         db.refresh(user)
#         return user

# def update_last_active_time(user_id: int = 0):
#     with Dao() as db:
#         now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#         db.query(TUser).where(TUser.id == user_id).update({"last_active_time": now_time})
#         db.commit()
#
# def update_sysuser_level(user_id:int = 0):
#     user_info = get_user_by_id(user_id)
#     if user_info and user_info.level_id < 3:
#         update_date = {}
#         if user_info.level_id == 0:
#             update_date['level_id'] = 1
#             update_date["level_one_time"] = datetime.now()
#         elif user_info.level_id == 1:
#             update_date['level_id'] = 2
#             update_date["level_two_time"] = datetime.now()
#         elif user_info.level_id == 2:
#             update_date['level_id'] = 3
#             update_date["level_three_time"] = datetime.now()
#         if update_date:
#             with Dao() as db:
#                 re = db.query(TUser).where(TUser.id == user_id).update(update_date)
#                 db.commit()
#                 return re
#     return 0

#推广系， 下级会员统计
# def get_lower_count(parent_id:int = 0, level:int = 0):
#     with Dao() as db:
#         return db.query(TUser).where(TUser.parent_id == parent_id).where(TUser.level_id > level).count()
#
# def get_invited_user(user_id:int):
#     with Dao() as db:
#         return db.query(TUser).filter(TUser.invited_user_id==user_id).all()
#
# def del_user(user_id: int):
#     with Dao() as db:
#         db.query(TUser).filter(TUser.id == user_id).delete()
#         db.commit()
