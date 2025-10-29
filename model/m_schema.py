from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from fastapi.exceptions import HTTPException


class CreateBalance(BaseModel):
    user_id: Optional[int] = Field(title='外键')
    change: Optional[int] = Field(title='变动金额')
    balance: Optional[int] = Field(title='余额')
    type: Optional[str] = Field(title='类型')
    description: Optional[str] = Field(title='详细描述')
    create_time: Optional[datetime] = Field(title='创建时间')
    user_withdraw_id: Optional[int]
    operator_id: Optional[int] = Field(title='操作员ID')
    out_trade_no: Optional[str]
    good_id: Optional[str] = Field(title='收益商品id')
    good_title: Optional[str] = Field(title='收益商品标题名称')
    good_num: Optional[str] = Field(title='收益商品数量')

        
class SBalance(CreateBalance):
    id: int

    class Config:
        orm_mode = True

class Balance(CreateBalance):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResBalance(BaseModel):
    data: List[SBalance]
    total: int
    
class CreateChinesePointSubject(BaseModel):
    create_time: Optional[datetime] = Field(title='创建时间')
    cps_content: Optional[str] = Field(title='知识点或重点题内容')
    cps_create_name: Optional[str] = Field(title='创建人')
    class_id: Optional[int] = Field(title='所属年级id')
    subject_id: Optional[int] = Field(title='所属科目点id')
    knowledge_id: Optional[int] = Field(title='所属知识点id')
    answer_txt: Optional[str] = Field(title='文本回答')
    answer_pic_path: Optional[str] = Field(title='图片回答路径')
    answer_audio_path: Optional[str] = Field(title='多媒体回答路径')
    knowledge_list: Optional[str] = Field(title='所属知识点列表，逗号分割')

        
class SChinesePointSubject(CreateChinesePointSubject):
    cps_id: int = Field(title='主键id')

    class Config:
        orm_mode = True

class ChinesePointSubject(CreateChinesePointSubject):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResChinesePointSubject(BaseModel):
    data: List[SChinesePointSubject]
    total: int
    
class CreateCity(BaseModel):
    cname: Optional[str]
    parid: Optional[int] = Field(title='上级地区id，默认0为顶级地区')
    status: Optional[int] = Field(title='地区状态')

        
class SCity(CreateCity):
    id: int

    class Config:
        orm_mode = True

class City(CreateCity):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResCity(BaseModel):
    data: List[SCity]
    total: int
    
class CreateCoin(BaseModel):
    user_id: Optional[int] = Field(title='外键')
    change: Optional[int] = Field(title='变动')
    coin: Optional[int] = Field(title='积分')
    type: Optional[str] = Field(title='类型')
    description: Optional[str] = Field(title='详细')
    create_time: Optional[datetime] = Field(title='创建时间')
    out_trade_no: Optional[str]

        
class SCoin(CreateCoin):
    id: int

    class Config:
        orm_mode = True

class Coin(CreateCoin):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResCoin(BaseModel):
    data: List[SCoin]
    total: int
    
class CreateEnglishPointSubject(BaseModel):
    create_time: Optional[datetime] = Field(title='创建时间')
    eps_content: Optional[str] = Field(title='知识点或重点题内容')
    eps_create_name: Optional[str] = Field(title='创建人')
    class_id: Optional[int] = Field(title='所属年级id')
    subject_id: Optional[int] = Field(title='所属科目点id')
    knowledge_id: Optional[int] = Field(title='所属知识点id')
    answer_txt: Optional[str] = Field(title='文本回答')
    answer_pic_path: Optional[str] = Field(title='图片回答路径')
    answer_audio_path: Optional[str] = Field(title='多媒体回答路径')
    knowledge_list: Optional[str] = Field(title='所属知识点列表，逗号分割')

        
class SEnglishPointSubject(CreateEnglishPointSubject):
    eps_id: int = Field(title='主键id')

    class Config:
        orm_mode = True

class EnglishPointSubject(CreateEnglishPointSubject):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResEnglishPointSubject(BaseModel):
    data: List[SEnglishPointSubject]
    total: int
    
class CreateKnowledgePoint(BaseModel):
    create_time: Optional[datetime] = Field(title='创建时间')
    kn_name: Optional[str] = Field(title='知识点名称')
    kn_create_name: Optional[str] = Field(title='创建人')
    class_id: Optional[int] = Field(title='所属年级id')
    subject_id: Optional[int] = Field(title='所属科目点id')

        
class SKnowledgePoint(CreateKnowledgePoint):
    kn_id: int = Field(title='主键id')

    class Config:
        orm_mode = True

class KnowledgePoint(CreateKnowledgePoint):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResKnowledgePoint(BaseModel):
    data: List[SKnowledgePoint]
    total: int
    
class CreateMathPointSubject(BaseModel):
    create_time: Optional[datetime] = Field(title='创建时间')
    mps_content: Optional[str] = Field(title='知识点或重点题内容')
    mps_create_name: Optional[str] = Field(title='创建人')
    class_id: Optional[int] = Field(title='所属年级id')
    subject_id: Optional[int] = Field(title='所属科目点id')
    knowledge_id: Optional[int] = Field(title='所属知识点id')
    answer_txt: Optional[str] = Field(title='文本回答')
    answer_pic_path: Optional[str] = Field(title='图片回答路径')
    answer_audio_path: Optional[str] = Field(title='多媒体回答路径')
    knowledge_list: Optional[str] = Field(title='所属知识点列表，逗号分割')

        
class SMathPointSubject(CreateMathPointSubject):
    mps_id: int = Field(title='主键id')

    class Config:
        orm_mode = True

class MathPointSubject(CreateMathPointSubject):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResMathPointSubject(BaseModel):
    data: List[SMathPointSubject]
    total: int
    
class CreateQuestionType(BaseModel):
    create_time: Optional[datetime] = Field(title='创建时间')
    qu_name: Optional[str] = Field(title='题型目录名称')
    qu_create_name: Optional[str] = Field(title='创建人')
    class_id: Optional[int] = Field(title='所属年级id')
    subject_id: Optional[int] = Field(title='所属科目点id')
    knowledge_id: Optional[int] = Field(title='所属知识点id')
    knowledge_list: Optional[str] = Field(title='所属知识点列表，逗号分割')

        
class SQuestionType(CreateQuestionType):
    qu_id: int = Field(title='主键id')

    class Config:
        orm_mode = True

class QuestionType(CreateQuestionType):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResQuestionType(BaseModel):
    data: List[SQuestionType]
    total: int
    
class CreateRemainPointSubject(BaseModel):
    create_time: Optional[datetime] = Field(title='创建时间')
    rps_content: Optional[str] = Field(title='知识点或重点题内容')
    rps_create_name: Optional[str] = Field(title='创建人')
    class_id: Optional[int] = Field(title='所属年级id')
    subject_id: Optional[int] = Field(title='所属科目点id')
    knowledge_id: Optional[int] = Field(title='所属知识点id')
    answer_txt: Optional[str] = Field(title='文本回答')
    answer_pic_path: Optional[str] = Field(title='图片回答路径')
    answer_audio_path: Optional[str] = Field(title='多媒体回答路径')
    knowledge_list: Optional[str] = Field(title='所属知识点列表，逗号分割')

        
class SRemainPointSubject(CreateRemainPointSubject):
    rps_id: int = Field(title='主键id')

    class Config:
        orm_mode = True

class RemainPointSubject(CreateRemainPointSubject):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResRemainPointSubject(BaseModel):
    data: List[SRemainPointSubject]
    total: int
    
class CreateShClas(BaseModel):
    create_time: Optional[datetime] = Field(title='创建时间')
    cl_name: Optional[str] = Field(title='年级名称')
    cl_create_name: Optional[str] = Field(title='创建人')

        
class SShClas(CreateShClas):
    cl_id: int = Field(title='主键id')

    class Config:
        orm_mode = True

class ShClas(CreateShClas):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResShClas(BaseModel):
    data: List[SShClas]
    total: int
    
class CreateShSubject(BaseModel):
    create_time: Optional[datetime] = Field(title='创建时间')
    su_name: Optional[str] = Field(title='学科名称')
    su_create_name: Optional[str] = Field(title='创建人')
    class_id: Optional[int] = Field(title='所属年级id')
    knowledge_list: Optional[str] = Field(title='所属知识点列表，逗号分割')

        
class SShSubject(CreateShSubject):
    su_id: int = Field(title='主键id')

    class Config:
        orm_mode = True

class ShSubject(CreateShSubject):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResShSubject(BaseModel):
    data: List[SShSubject]
    total: int
    
class CreateUser(BaseModel):
    username: Optional[str] = Field(title='用户名')
    email: Optional[str] = Field(title='邮箱')
    open_id: Optional[str] = Field(title='openID from wechat channel')
    union_id: Optional[str] = Field(title='unionID from tecent')
    password: Optional[str] = Field(title='密码（哈希值）')
    nickname: Optional[str] = Field(title='昵称')
    phone: Optional[str] = Field(title='联系方式')
    id_card: Optional[str] = Field(title='身份证')
    level_id: Optional[int] = Field(title='用户等等级 默认是0')
    status: Optional[int] = Field(title='0: 已实名   1: 未实名,被is_agree替代')
    register_time: Optional[datetime] = Field(title='注册时间')
    avatar: Optional[str] = Field(title='头像url')
    invited_user_id: Optional[int] = Field(title='邀请人id')
    coin: Optional[int] = Field(title='积分')
    gender: Optional[int] = Field(title='0:  男  1:  女')
    last_active_time: Optional[datetime] = Field(title='最近登录时间')
    name: Optional[str] = Field(title='用户名')
    is_agree: Optional[int] = Field(title='是否已经校验')
    parent_id: Optional[int] = Field(title='父级用户')
    parent_id_history: Optional[str] = Field(title='曾经的上级(ID之间逗号分隔)')
    level_one_time: Optional[datetime] = Field(title='升级活跃会员时间')
    level_two_time: Optional[datetime] = Field(title='升级老板会员时间')
    level_three_time: Optional[datetime] = Field(title='升级大老板会员时间')
    level_top_time: Optional[datetime] = Field(title='升级推广顶级时间')
    manage_id: Optional[int] = Field(title='管理等级 默认是0')

        
class SUser(CreateUser):
    id: int = Field(title='标识id')

    class Config:
        orm_mode = True

class User(CreateUser):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResUser(BaseModel):
    data: List[SUser]
    total: int
    