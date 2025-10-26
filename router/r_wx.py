#!/usr/bin/env python
# encoding: utf-8
import datetime
from typing import List, Optional

from fastapi import APIRouter, Request
from fastapi.exceptions import HTTPException

from common import Dao
from dao import d_db
from model import schema
from service.wx_service import wxpay

router = APIRouter()


@router.post('/notify/pay')
async def notify(request: Request):
    result = wxpay.callback(request.headers, await request.body())
    if result and result.get('event_type') == 'TRANSACTION.SUCCESS':
        resource = result.get('resource')

        # appid = resource.get('appid')
        # mchid = resource.get('mchid')
        out_trade_no = resource.get('out_trade_no')
        amount = resource.get('amount').get('total')
        #s_order.pay_success(amount=amount, out_trade_no=out_trade_no)

        # transaction_id = resource.get('transaction_id')
        # trade_type = resource.get('trade_type')
        # trade_state = resource.get('trade_state')
        # trade_state_desc = resource.get('trade_state_desc')
        # bank_type = resource.get('bank_type')
        # attach = resource.get('attach')
        # success_time = resource.get('success_time')
        # payer = resource.get('payer')
        # amount = resource.get('amount').get('total')
        # TODO: 根据返回参数进行必要的业务处理，处理完后返回200或204
        return {'code': 'SUCCESS', 'message': '成功'}
    else:
        raise HTTPException(status_code=500, detail={"code": 'FAILED', "message": "失败"})


@router.post('/notify/flash_pay')
async def notify(request: Request):
    result = wxpay.callback(request.headers, await request.body())
    if result and result.get('event_type') == 'TRANSACTION.SUCCESS':
        resource = result.get('resource')

        # appid = resource.get('appid')
        # mchid = resource.get('mchid')
        out_trade_no = resource.get('out_trade_no')
        amount = resource.get('amount').get('total')
        #s_flash_order.pay_success(amount=amount, out_trade_no=out_trade_no)

        # transaction_id = resource.get('transaction_id')
        # trade_type = resource.get('trade_type')
        # trade_state = resource.get('trade_state')
        # trade_state_desc = resource.get('trade_state_desc')
        # bank_type = resource.get('bank_type')
        # attach = resource.get('attach')
        # success_time = resource.get('success_time')
        # payer = resource.get('payer')
        # amount = resource.get('amount').get('total')
        # TODO: 根据返回参数进行必要的业务处理，处理完后返回200或204
        return {'code': 'SUCCESS', 'message': '成功'}
    else:
        raise HTTPException(status_code=500, detail={"code": 'FAILED', "message": "失败"})