from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from fastapi.exceptions import HTTPException


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
    