from model.m_schema import *
from fastapi import APIRouter, Depends, Header, HTTPException, Request
from dao import d_db, d_cl_su_kn_type, d_admin
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

@router.get(f'/class_list', summary='年级列表')
async def class_list(page: int = 1, page_size: int = 20):
    """
    返回：jinnengyuansession携带到请求体head中，作为后端接口请求的token
    """
    return d_cl_su_kn_type.get_class_list(page, page_size)

@router.get(f'/subject_list', summary='学科列表')
async def subject_list(page: int = 1, page_size: int = 20):
    """
    返回：jinnengyuansession携带到请求体head中，作为后端接口请求的token
    """
    return d_cl_su_kn_type.get_subject_list(page, page_size)

@router.get(f'/point_list', summary='知识点目录')
async def point_list(page: int = 1, page_size: int = 20, class_id: int = 0, subject_id:int = 0):
    """
    返回：jinnengyuansession携带到请求体head中，作为后端接口请求的token
    """
    return d_cl_su_kn_type.get_point_list(page, page_size, class_id, subject_id)

@router.get(f'/type_list', summary='题型目录表')
async def type_list(page: int = 1, page_size: int = 20):
    """
    返回：jinnengyuansession携带到请求体head中，作为后端接口请求的token
    """
    return d_cl_su_kn_type.get_type_list(page, page_size)

@router.post(f'/subject_create', response_model=SShSubject, summary='添加学科')
async def subject_create(item: CreateShSubject) -> SShSubject:
    dict_item = dict(item)
    for k,v in dict_item.items():
        if v is not None:
            v = str(v)
            v = v.replace(" ", "")
            get_search = re.search(r"'", v, flags=0)
            get_search2 = re.search(r'%27', v, flags=0)
            get_search3 = re.search(r'unionselect', v, flags=0)
            if get_search or get_search2 or get_search3:
               raise HTTPException(status_code=404, detail='bad way~~~~~~')

    return d_db.insert_sh_subject(item)

@router.post(f'/subject_update', response_model=str)
async def subject_update(item: SShSubject) -> str:
    # d_db.update_sh_subject(item)
    d_cl_su_kn_type.update_sh_subject(item)
    return "success"

@router.get(f'/subject_del', response_model=str)
async def subject_del(del_id: int, valcode:str ='IAqGo4QhEGET') -> str:
    d_cl_su_kn_type.del_subject(del_id)
    return "success"

@router.post(f'/chinese_point_subject/create', response_model=SChinesePointSubject)
async def create_chinese_point_subject(item: CreateChinesePointSubject) -> SChinesePointSubject:
    dict_item = dict(item)
    for k,v in dict_item.items():
        if v is not None:
            v = str(v)
            v = v.replace(" ", "")
            get_search = re.search(r"'", v, flags=0)
            get_search2 = re.search(r'%27', v, flags=0)
            get_search3 = re.search(r'unionselect', v, flags=0)
            if get_search or get_search2 or get_search3:
               raise HTTPException(status_code=404, detail='bad way~~~~~~')

    return d_db.insert_chinese_point_subject(item)

@router.post(f'/chinese_point_subject/update', response_model=str)
async def update_chinese_point_subject(item: SChinesePointSubject) -> str:
    d_cl_su_kn_type.update_chinese_point_subject(item)
    return "success"

@router.post(f'/knowledge_point/create', response_model=SKnowledgePoint)
async def create_knowledge_point(item: CreateKnowledgePoint) -> SKnowledgePoint:
    dict_item = dict(item)
    for k,v in dict_item.items():
        if v is not None:
            v = str(v)
            v = v.replace(" ", "")
            get_search = re.search(r"'", v, flags=0)
            get_search2 = re.search(r'%27', v, flags=0)
            get_search3 = re.search(r'unionselect', v, flags=0)
            if get_search or get_search2 or get_search3:
               raise HTTPException(status_code=404, detail='bad way~~~~~~')

    return d_db.insert_knowledge_point(item)

@router.post(f'/knowledge_point/update', response_model=str)
async def update_knowledge_point(item: SKnowledgePoint) -> str:
    d_cl_su_kn_type.update_knowledge_point(item)
    return "success"