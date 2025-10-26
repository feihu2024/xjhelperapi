#!/usr/bin/env python
# encoding: utf-8
import datetime
from typing import List, Optional
import logging
from model.m_schema import SOrder, SGood

from fastapi import HTTPException

from common import Dao, global_define
from model import schema
from model.schema import TOrder, TGood
from dao import d_order, d_user
from service import share_fee_service


def pay_success(amount: int, out_trade_no: str):
    with Dao() as db:
        order_infos = db.query(TOrder, TGood, schema.TGoodSpec)\
            .outerjoin(TGood, TGood.id == TOrder.good_id).filter(TOrder.status_id == 0)\
            .outerjoin(schema.TGoodSpec, schema.TGoodSpec.id == TOrder.spec_id)\
            .filter(TOrder.out_trade_no == out_trade_no).all()

        orders = []
        goods = []
        good_titles = []
        good_ids = []
        good_nums = []
        for order, good, spec in order_infos:
            order: TOrder
            good: TGood
            spec: schema.TGoodSpec

            # 状态更新 卡券商品->未使用  实体商品->未发货
            if good.type == 0: # 卡券商品
                order.status_id = 9 # 未使用
            elif good.type == 1: # 实体商品
                order.status_id = 1 # 未发货
            else:
                order.status_id = 2  # 已发货

            # db.query(TOrder).filter(TOrder.id == order.id).update({'status_id': order.status_id})
            db.flush()

            # 销量更新
            good.num_sale = order.number + good.num_sale if good.num_sale else order.number
            spec.num_sale = order.number + spec.num_sale if spec.num_sale else order.number

            ## 更新订单来源
            d_order.update_order_source(order)

            # 防止session过期而造成order或good数据丢失
            orders.append(SOrder.parse_obj(order.__dict__))
            goods.append(SGood.parse_obj(good.__dict__))
            good_titles.append(good.title)
            good_ids.append(good.id)
            good_nums.append(order.number)

        if len(orders) > 0:
            user_id = orders[0].paider_id
        elif db.query(schema.TOrder).filter(schema.TOrder.out_trade_no == out_trade_no).first() is None:
            logging.error(f"没有发现相关订单, out_trade_no: {out_trade_no}")
            return
            # raise HTTPException(status_code=500, detail={"code": 'FAILED', "detail": "失败,没有发现相关订单"})
        else:
            logging.warning(f"订单已处理, out_trade_no: {out_trade_no}")
            db.commit()
            return

        if user_id is None:
            raise HTTPException(status_code=500, detail={"code": 'FAILED', "detail": "失败,用户id为空"})

        user_account: Optional[schema.TUserAccount] = db.query(schema.TUserAccount).filter(
            schema.TUserAccount.user_id == user_id).first()
        if user_account is None:
            raise HTTPException(status_code=500, detail={"code": 'FAILED', "detail": "失败,没有发现该用户的账户"})

        coin_cost = sum([order.paid_coin for order in orders])
        lock_balance_cost = sum([order.paid_lock_balance for order in orders])
        balance_cost = sum([order.paid_balance for order in orders])
        amount_cost = sum([order.paid_amount for order in orders])

        # 更新账户与添加记录
        if coin_cost:
            user_account.coin = user_account.coin - coin_cost
            coin_record = schema.TCoin(
                change=-coin_cost,
                user_id=user_id,
                coin=user_account.coin,
                create_time=datetime.datetime.now(),
                out_trade_no=out_trade_no,
                description=global_define.balance_type[11],
                type=global_define.balance_type[11]
            )
            db.add(coin_record)
            db.flush()

        if lock_balance_cost:
            user_account.lock_balance = user_account.lock_balance - lock_balance_cost
            lock_balance_record = schema.TLockBalance(
                change=-lock_balance_cost,
                user_id=user_id,
                lock_balance=user_account.lock_balance,
                create_time=datetime.datetime.now(),
                out_trade_no=out_trade_no,
                description=global_define.balance_type[11],
                type=global_define.balance_type[11]
            )
            db.add(lock_balance_record)
            db.flush()

        if balance_cost:
            user_account.balance = user_account.balance - balance_cost
            balance_record = schema.TBalance(
                change=-balance_cost,
                user_id=user_id,
                balance=user_account.balance,
                create_time=datetime.datetime.now(),
                out_trade_no=out_trade_no,
                description=global_define.balance_type[11],
                type=global_define.balance_type[11],
                good_id=",".join([str(i) for i in good_ids]),
                good_title=",".join([str(i) for i in good_titles]),
                good_num=",".join([str(i) for i in good_nums])
            )
            db.add(balance_record)
            db.flush()

        if amount_cost:
            balance_amount = schema.TBalance(
                change=-amount_cost,
                user_id=user_id,
                balance=user_account.balance,
                create_time=datetime.datetime.now(),
                out_trade_no=out_trade_no,
                description=global_define.balance_type[18],
                type=global_define.balance_type[18],
                good_id=",".join([str(i) for i in good_ids]),
                good_title=",".join([str(i) for i in good_titles]),
                good_num=",".join([str(i) for i in good_nums])
            )
            db.add(balance_amount)
            db.flush()

        if amount != amount_cost:
            raise HTTPException(status_code=500, detail={"code": 'FAILED', "detail": "支付金额不一致"})

        payment_record = schema.TUserPaymentHistory(fee=amount, description='购买商品', create_time=datetime.datetime.now())
        db.add(payment_record)
        db.flush()

        t_user = d_user.get_user_by_id(user_id)
        if t_user:
            # 更新系统用户级别
            if t_user.level_id == 0:
                d_user.update_sysuser_active(t_user.id)
            elif t_user.level_id == 1:
                d_user.update_sysuser_high(t_user.id)
            elif t_user.level_id == 2:
                d_user.update_sysuser_top(t_user.id)
            # 更新推广用户级别
            d_user.update_user_top(user_id)

        db.commit()


    # 分润  购买支付环节不需要分润  确认收货才会分
    # for t_order, t_good in zip(orders, goods):
    #     if t_good and t_good.type == 0:
    #         share_fee_service.share_mall_fee_with_other(order_id=t_order.id)
    #
