import time
import datetime
from common import Dao
from model import m_admin
from config import SECRET
from jose import JWTError, jwt
from sqlalchemy import func, and_
from model.schema import TUser, TAdmin
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


class this_CreateAdmin(BaseModel):
    username: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    level_id: Optional[int]
    id_card: Optional[str]
    gender: Optional[str]
    register_time: Optional[datetime.datetime] = Field(title='创建时间')
    last_active_time: Optional[datetime.datetime]
    status: Optional[str]
    business_id: Optional[int] = Field(title='商家ID_busiess_content')
    admin_id: Optional[int] = Field(title='所属商家管理id')
    user_pic: Optional[str] = Field(title='头像url')
    user_info: Optional[str] = Field(title='用户备注')


class this_SAdmin(this_CreateAdmin):
    id: int

    class Config:
        orm_mode = True


def login_for_token(username: str, password: str):
    user = get_admin_by_username(username=username)
    if not user:
        return ''
    if user.password == password:
        data = {
            'user_id': user.id,
            'time': time.time() + SECRET.VALID_TIME
        }
        token = get_login_token_encode(data)
        #raise HTTPException(status_code=200, detail={'token': token, 'massage': 'Success'}, headers={"data": '123'})
        return token
    else:
        return ''

def get_login_token_encode(data:dict):
    return jwt.encode(data, SECRET.SECRET_KEY, algorithm=SECRET.ALGORITHM)

def get_login_token_decode(token:str):
    re_json = {}
    try:
        re_json = jwt.decode(token, SECRET.SECRET_KEY, algorithms=[SECRET.ALGORITHM])
    except Exception as e:
        print(e)
    return re_json

def is_login(token:str):
    data = get_login_token_decode(token)
    this_time = time.time()
    re_code = ''
    if data:
        if data.get('time') > this_time:
            data['time'] = this_time + SECRET.VALID_TIME
            re_code = get_login_token_encode(data)
    return re_code

def get_admin_by_username(username: str):
    with Dao() as db:
        return db.query(m_admin.TAdmin).where(m_admin.TAdmin.username == username).first()


def login_shop_token(username: str, password: str, user_id:int):
    data = {
        'user_id': user_id,
        'time': time.time() + SECRET.VALID_TIME
    }
    token = {'token_val': get_login_token_encode(data), 'user_id': user_id}
    return token

def get_login_id(token:str):
    data = get_login_token_decode(token)
    this_time = time.time()
    re_code = 0
    if data:
        if data.get('time') > this_time:
            data['time'] = this_time + SECRET.VALID_TIME
            re_code = int(data['user_id'])
    return re_code

def get_admin_by_id(admin_id: int) -> Optional[this_SAdmin]:
    # with Dao() as db:
    #     return db.query(TAdmin).where(TAdmin.id == admin_id).first()
    with Dao() as db:
        t = db.query(TAdmin).where(TAdmin.id == admin_id).first()
        if t:
            return this_SAdmin.parse_obj(t.__dict__)
        else:
            return None
