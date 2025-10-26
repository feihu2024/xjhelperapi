import time
import datetime
from common import Dao
from model import m_admin
from config import SECRET
from jose import JWTError, jwt
from sqlalchemy import func, and_
from model.schema import TUser
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


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


def query_users() -> m_admin.UserData:
    time_now = datetime.datetime.now()
    with Dao() as db:
        # 统计会员总量
        total_num = db.query(TUser).count()

        # 根据时间条件统计日增长活跃用户数量
        daily_add = db.query(TUser).filter(TUser.register_time >= time_now - datetime.timedelta(days=1)).count()

        # 根据最后登录时间统计活跃数量
        active_num = db.query(TUser).where(TUser.last_active_time >= time_now - datetime.timedelta(days=5)).count()

        # 根据性别条件统计男性用户的数量
        male = db.query(TUser).where(TUser.gender == 'male').count()
        # 根据性别条件统计女性用户的数量
        female = db.query(TUser).where(TUser.gender == 'female').count()

        # 计算男女用户的占比
        male_ratio: float = male / (male + female)
        female_ratio: float = female / (male + female)

        return m_admin.UserData(num=total_num, daily_add=daily_add,
                                active=active_num, male_ratio=male_ratio, female_ratio=female_ratio)


def silent_users(page: int = 1, page_size: int = 10):
    """根据最后登录时间统计非活跃用户"""
    time_now = datetime.datetime.now()
    with Dao() as db:
        silents = db.query(TUser). \
            where(TUser.last_active_time < time_now - datetime.timedelta(days=10)). \
            offset((page - 1) * page_size).limit(page_size).all()

        return silents




def query_daily_add(day: datetime.datetime.date) -> int:
    zero_time = datetime.time()
    zero_day = datetime.datetime.combine(day, zero_time)
    time_condition = and_(TUser.register_time >= zero_day,
                          TUser.register_time <= zero_day + datetime.timedelta(days=1))
    with Dao() as db:
        num = db.query(TUser).where(time_condition).count()
        db.commit()
        return num
