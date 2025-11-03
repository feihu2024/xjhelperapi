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
async def point_list(page: int = 1, page_size: int = 20):
    """
    返回：jinnengyuansession携带到请求体head中，作为后端接口请求的token
    """
    return d_cl_su_kn_type.get_point_list(page, page_size)

@router.get(f'/type_list', summary='题型目录表')
async def type_list(page: int = 1, page_size: int = 20):
    """
    返回：jinnengyuansession携带到请求体head中，作为后端接口请求的token
    """
    return d_cl_su_kn_type.get_type_list(page, page_size)