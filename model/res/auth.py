from pydantic import BaseModel, Field
from typing import Optional


class LoginRes(BaseModel):
    user_id: int
    token: str
    nickname: Optional[str]
    avatar: Optional[str]


class SupplierLoginRes(BaseModel):
    employee_id: int = Field(title='商家人员id')
    level_id: Optional[int] = Field(title='人员角色id')
    token: str
