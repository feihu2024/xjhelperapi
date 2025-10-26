from fastapi import APIRouter
#from sqlalchemy.ext.declarative import declarative_base
from model.schema import TBalance
from dao import d_balance, d_account
from fastapi.exceptions import HTTPException
from model.mall import m_account
from common import global_define
import time
import logging
from service.wx_service import wxpay

#Base = declarative_base()
#metadata = Base.metadata

router = APIRouter()

@router.post(f"/search_balance", summary="获取收益记录")
async def search_balance(item: d_balance.SearchBalance):
    # if item.user_id is None:
    #     raise HTTPException(400, "未知用户")
    # if item.user_id <= 0:
    #     raise HTTPException(400, "未找到用户")
    return d_balance.search_balance(item)

@router.post(f"/search_lockbalance", summary="获取锁定额变动记录")
async def search_lockbalance(item: d_balance.SearchBalance):
    return d_balance.search_lock_balance(item)

@router.post(f"/search_days", summary="获取剩余秒杀退货收益天数")
async def search_balance(user_id: int):
    """
    id，'主键id'；
    user_id，'用户id'；
    income_days ，'剩余秒杀退货收益天数'
    """
    if user_id is None:
        raise HTTPException(400, "未知用户")
    if user_id <= 0:
        raise HTTPException(400, "未找到用户")
    return d_balance.search_days(user_id)

@router.get(f'/detail_withdraw', summary='用户申请提现详情')
async def user_detail_withdraw(withdraw_id:int):
    """
    type_id,提现类型（1表示银行卡，2表示微信零钱）；fee_type，扣费类型（1表示扣费倒锁定余额，2表示直接扣费）；
    user_withdraw_status_id，状态（1申请中，2已审核，3	已拒绝，4，已失败）
    """
    return d_account.get_user_withdraw(withdraw_id)

@router.get(f'/deny_withdraw', summary='拒绝提现')
async def user_deny_withdraw(withdraw_id:int):
    deny_info = d_account.get_user_withdraw(withdraw_id)
    if not deny_info:
        raise HTTPException(400, "未知数据")
    if deny_info['TUserWithdraw'].user_withdraw_status_id != 1:
        raise HTTPException(400, "提现数据错误")

    d_account.update_user_withdraw_status(deny_info['TUserWithdraw'].id, 3)
    total_balance = deny_info[2].balance +  deny_info[0].amount
    d_account.update_account_by_id(deny_info[2].id, {"balance":total_balance})
    d_account.add_balance(m_account.BalanceModel(
        user_id=deny_info[0].user_id,
        change=deny_info[0].amount,
        balance=total_balance,
        type=global_define.balance_type[20],
        create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    ))
    return {'code': 200, 'message': 'success'}

@router.post(f'/pass_withdraw', summary='提现审核通过')
async def user_pass_withdraw(data: m_account.PassWithdrawModel):
    """
    :type_id,提现类型（1表示银行卡，2表示微信零钱）；fee_type，扣费类型（1表示扣费倒锁定余额，2表示直接扣费）；
    :user_withdraw_status_id，状态（1申请中，2已审核，3	已拒绝，4，已失败）
    """
    base_info = d_account.get_user_withdraw(data.withdraw_id)
    if not base_info:
        raise HTTPException(400, "未知数据")
    if base_info['TUserWithdraw'].user_withdraw_status_id != 1:
        raise HTTPException(400, "状态错误")
    if data.amount != base_info[0].amount:
        raise HTTPException(400, "提现金额不一致")
    if data.fee_type != base_info[0].fee_type:
        raise HTTPException(400, "提现方式不一致")
    if data.fee_pro != base_info[0].fee_pro:
        raise HTTPException(400, "提现比例不一致")
    deduct_balance = int(base_info[0].amount * base_info[0].fee_pro)
    fee_balance = base_info[0].amount - deduct_balance
    if data.fee_balance != fee_balance:
        raise HTTPException(400, "提现税后金额不一致")
    if data.deduct_balance != deduct_balance:
        raise HTTPException(400, "提现税金不一致")

    logging.info('start to withdraw')
    res = wxpay.transfer_batch(
        out_batch_no=base_info[0].out_batch_no,
        batch_name=base_info[0].batch_name,
        batch_remark=base_info[0].batch_remark,
        total_amount=fee_balance,
        total_num=1,
        transfer_detail_list=[{"out_detail_no": base_info[0].out_detail_no, "transfer_amount": fee_balance, "transfer_remark": base_info[0].batch_remark, "openid": base_info[1].open_id}],
        transfer_scene_id="1001"
    )
    logging.info(res)
    logging.info(f"提现申请ID: {base_info[0].id}")
    if res[0] == 200:
        d_account.update_user_withdraw_balance(base_info[0].id, fee_balance, deduct_balance)
        d_account.update_user_withdraw_status(base_info[0].id, 2)
        if base_info[0].fee_type == 1:
            total_lock_balance = base_info[2].lock_balance + deduct_balance
            d_account.update_account_by_id(base_info[2].id, {"lock_balance": total_lock_balance})
            d_account.add_lock_balance(m_account.LockBalanceModel(
                user_id=base_info[0].user_id,
                change=deduct_balance,
                lock_balance=total_lock_balance,
                type=global_define.balance_type[21],
                create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            ))
    else:
        d_account.update_user_withdraw_status(base_info[0].id, 4)
    return {'code': 200, 'message': 'success'}