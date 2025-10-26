from datetime import datetime
from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import List, Optional
from sqlalchemy import Column, Float, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

router = APIRouter()


class TAdmin(Base):
    __tablename__ = 't_admin'

    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String(45))
    gender = Column(String(20))
    email = Column(String(45))
    password = Column(String(45))
    phone = Column(String(45))
    id_card = Column(String(45))
    level_id = Column(Integer)
    status = Column(String(20))
    register_time = Column(TIMESTAMP, comment='in seconds')
    last_active_time = Column(TIMESTAMP, comment='最后登录时间')


class UserData(BaseModel):
    num: Optional[int] = Field(title='会员总数')
    daily_add: Optional[int] = Field(title='当日新增')
    active: Optional[int] = Field(title='活跃用户')
    male_ratio: Optional[float] = Field(title='男性占比')
    female_ratio: Optional[float] = Field(title='女性占比')


class InactiveUser(BaseModel):
    username: Optional[str]
    email: Optional[str]
    nickname: Optional[str] = Field(title='昵称')
    phone: Optional[str]
    id_card: Optional[str] = Field(title='身份证')
    level_id: Optional[int] = Field(title='等级')
    status: Optional[str]
    register_time: Optional[datetime] = Field(title='in seconds')
    avatar: Optional[str]


class SaleData(BaseModel):
    total_sale: Optional[int] = Field(title='商品销售总额')
    income: Optional[int] = Field(title='销售收益')
    current_sale: Optional[int] = Field(title='当日销售总额')
    flash_sale: Optional[int] = Field(title='总秒杀价值', default=6000)
    cost: Optional[int] = Field(title='兑付成本', default=1500)


class AdminRequest(BaseModel):
    username: str = Field(title='管理员账号', default='admin')
    password: str
