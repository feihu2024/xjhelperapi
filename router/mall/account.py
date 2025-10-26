import datetime, time
from model import m_schema
from dao import d_db, d_account, d_package, d_order, d_balance, d_user
from router import r_query
from model.mall import m_account
from typing import List, Optional
from fastapi import APIRouter, HTTPException
from model.address import UserAddress
from common import global_define, global_function
import logging

router = APIRouter()


@router.post(f'/create')
async def create_account(item: m_account.CreateAccount):
    """创建账户"""
    t_account = m_account.TUserAccount(**item.dict())
    t_account = d_account.create_account(t_account)
    return m_account.SCreateAccount(**t_account.__dict__)


@router.delete(f'/delete')
async def delete_account(account_id: int):
    d_account.delete_account_by_id(account_id)
    # 删除不存在的条目不会报错，如何解决？
    return {'code': 200, 'message': 'success'}


@router.post(f'/update', summary="修改用户金额和积分")
async def update_account(item: m_account.GetCoinBalance):
    """根据账户id更新账户"""
    if item.user_action == 'balance':
        d_account.update_account_by_id(item.id, {"balance":item.balance})
        d_account.insert_bank(m_account.BalanceModel(
            user_id=item.user_id,
            change=item.balance,
            balance=item.balance,
            create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        ))
    elif item.user_action == 'lock_balance':
        d_account.update_lock_balance_by_id(item.id, {"lock_balance":item.lock_balance})
    else:
        d_account.update_account_by_id(item.id, {"coin":item.coin})
        d_account.insert_coin(m_account.CoinModel(
            user_id=item.user_id,
            change=item.coin,
            coin=item.coin,
            create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        ))
    return {'code': 200, 'message': 'success'}


@router.post(f'/prepare_withdraw', response_model=dict, summary='用户准备提现')
async def user_prepare_with_draw(user_id: int):
    query_str = {"table": "user_bank",
                 "joins": [{"table": "user", "on_left": "user_id", "on_right": "id", "method": "right"}],
                 "filters": [{"field": "user.id", "value": user_id}]}
    return await r_query.get(r_query.QueryData.parse_obj(query_str))


@router.post(f'/start_withdraw', response_model=dict, summary='用户申请提现')
async def user_start_with_draw(data: m_account.WithdrawModel):
    s_user: m_schema.SUser = d_db.get_user(user_id=data.user_id)
    if s_user is not None:
        if s_user.is_agree:
            fee_pro = 0
            if s_user.level_id == 0:
                if data.fee_type == 1:
                    fee_pro = global_define.setting_withdraw['fans'][0]
                elif data.fee_type == 2:
                    fee_pro = global_define.setting_withdraw['fans'][1]
            elif s_user.level_id == 1:
                if data.fee_type == 1:
                    fee_pro = global_define.setting_withdraw['member'][0]
                elif data.fee_type == 2:
                    fee_pro = global_define.setting_withdraw['member'][1]
            elif s_user.level_id == 2:
                if data.fee_type == 1:
                    fee_pro = global_define.setting_withdraw['boss'][0]
                elif data.fee_type == 2:
                    fee_pro = global_define.setting_withdraw['boss'][1]
            else:
                if data.fee_type == 1:
                    fee_pro = global_define.setting_withdraw['bigboss'][0]
                elif data.fee_type == 2:
                    fee_pro = global_define.setting_withdraw['bigboss'][1]
            if fee_pro != data.fee_pro:
                return {'code': 200, 'message': '前后端扣费比例不一致'}

            user_accounts = d_account.get_account_info( data.user_id)
            if not user_accounts or user_accounts.balance < data.amount:
                return {'code': 200, 'message': '资金账户错误'}

            if not s_user.phone:
                return {'code': 200, 'message': '联系方式错误'}

            if not data.type_id:
                return {'code': 200, 'message': '提现类型错误'}

            # 提现范围：大于10元，小于500元
            if data.amount < 1000 or data.amount > 50000:
                return {'code': 200, 'message': '提现金额错误'}

            new_draw = m_schema.CreateUserWithdraw(amount=data.amount, user_withdraw_status_id=1, user_id=data.user_id,
                                                   create_time=datetime.datetime.now(),
                                                   update_time=datetime.datetime.now(),
                                                   fee_type=data.fee_type,
                                                   fee_pro=data.fee_pro,
                                                   out_batch_no=global_function.get_randoms(30),
                                                   batch_name="用户余额提现",
                                                   batch_remark=global_define.balance_type[19],
                                                   out_detail_no=global_function.get_randoms(30),
                                                   user_name=s_user.name,
                                                   user_phone=s_user.phone,
                                                   type_id=data.type_id
                                                   )
            d_db.insert_user_withdraw(new_draw)

            total_balance = user_accounts.balance - data.amount
            d_account.update_account_by_id(user_accounts.id, {"balance": total_balance})
            d_account.add_balance(m_account.BalanceModel(
                user_id=data.user_id,
                change=-data.amount,
                balance=total_balance,
                type=global_define.balance_type[19],
                create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            ))
            return {'code': 200, 'message': 'success'}
        else:
            return {'code': 200, 'message': '未实名认证'}
    else:
        return {'code': 200, 'message': '该用户不存在'}

@router.post(f'/user_bank/create', response_model=m_schema.SUserBank, summary="用户添加银行卡（默认)")
async def create_user_default_bank(item: m_schema.CreateUserBank) -> m_schema.SUserBank:
    if item.is_default == 1:
        banks: List[m_schema.SUserBank] = d_db.filter_user_bank(items={'user_id': item.user_id}, search_items={},
                                                                set_items={}, page=1, page_size=100)
        for bank in banks:
            if bank.is_default:
                bank.is_default = 0
                d_db.update_user_bank(bank)

        return d_db.insert_user_bank(item)
    else:
        return d_db.insert_user_bank(item)


@router.post(f'/user_bank/set_default', response_model=dict, summary="设置默认银行卡")
def set_default_address(user_id: int, bank_id: int):
    """将用户地址列表下的某个地址设置为默认地址"""
    banks: List[m_schema.SUserBank] = d_db.filter_user_bank(items={'user_id': user_id}, search_items={},
                                                            set_items={})
    for bank in banks:
        if bank.id == bank_id:
            bank.is_default = 1
            d_db.update_user_bank(item=bank)
        else:
            bank.is_default = 0
            d_db.update_user_bank(item=bank)
    return {'code': 200, 'message': 'success'}

@router.get(f'/get', response_model=list, summary="获取银行卡信息")
def get_user_account(user_id:int = 0):
    account_info = d_account.get_acount_list(user_id)
    re = []
    for i in account_info:
        i = i.__dict__
        #re.append({"id":i.get('id'), "user_id":i.get('user_id'), "balance":i.get('balance'), "lock_balance":i.get('lock_balance'), "coin":i.get('coin'), "description":i.get('description'), "create_time":i.get('create_time'), "bank_name":i.get('bank_name'), "id_card":i.get('id_card')})
        re.append({"id":i.get('id'), "bank_name":i.get('bank_name'), "username":i.get('username'), "id_card":i.get('id_card'), "user_id":i.get('user_id'), "phone":i.get('phone'), "bank_address":i.get('bank_address'), "is_default":i.get('is_default')})
    return re

@router.get(f'/get_coin_balance', response_model=m_account.SCreateAccount, summary="获取积分和余额")
def get_user_coin_balance(user_id:int = 0):
    account_info = d_account.get_coin_balance_list(user_id)
    re = None
    for i in account_info:
        re = i.__dict__
        #re.append({"id":i.get('id'), "user_id":i.get('user_id'), "balance":i.get('balance'), "lock_balance":i.get('lock_balance'), "coin":i.get('coin'), "description":i.get('description'), "create_time":i.get('create_time'), "bank_name":i.get('bank_name'), "id_card":i.get('id_card')})
    return re

@router.post(f'/update_bank', response_model=dict, summary="修改银行卡信息t_user_bank")
def update_bank(items: m_account.GetUserBank):
    d_account.update_bank(items.bank_id, {"id_card": items.id_card, "bank_name": items.bank_name})
    return {'code': 200, 'message': 'success'}

@router.post(f'/get_coin_balance_income', summary="获取用户余额、积分、预收益")
def get_user_coin_balance_income(user_id:int = 0):
    """
    计算条件：订单未计算收益，且在已支付或发货中。
    返回值：balance，余额；lock_balance，锁定余额；coin，积分；freeze_balance，冻结额；flash_order_balance，近杀包出2个月秒售预收益额;order_id_income，预收益订单1,2,3；latest_preincome，最近一次正收益
    """
    re_val = [{"balance":0, "lock_balance":0, "coin":0, "freeze_balance":0, "flash_order_balance":0, "order_id_income":[], "latest_preincome":0}]
    account_info = d_account.get_coin_balance(user_id)
    if account_info:
        re_val[0]['balance'] = account_info.balance
        re_val[0]['lock_balance'] = account_info.lock_balance
        re_val[0]['coin'] = account_info.coin
        re_val[0]['freeze_balance'] = account_info.freeze_balance

    #最近一笔预收益
    preincome = d_order.get_user_willcomein_order(user_id)
    if preincome:
        l, g, s = preincome[0]
        if l and g and s:
            #分享
            if l.recommender_id is not None and l.recommender_id > 0 and s.share_fee is not None:
                if s.supplier_fee > 0 and l.recommender_id == user_id:
                    re_val[0]['latest_preincome'] += l.number * s.share_fee

            #层级
            if l.parent_uid is not None and l.parent_uid > 0 and s.parent_fee is not None:
                if s.parent_fee > 0 and l.parent_uid == user_id:
                    re_val[0]['latest_preincome'] += l.number * s.parent_fee

            # 直推
            if l.invited_uid is not None and l.invited_uid > 0 and s.recommender_fee is not None:
                if s.recommender_fee > 0 and l.invited_uid == user_id:
                    re_val[0]['latest_preincome'] += l.number * s.recommender_fee

            # 供货介绍人的收益
            if l.supplier_uid is not None and l.supplier_uid > 0 and s.supplier_fee is not None:
                if s.supplier_fee > 0 and l.supplier_uid == user_id:
                    re_val[0]['latest_preincome'] += l.number * s.supplier_fee
            # 见点
            if l.top_uid is not None and l.top_uid > 0 and s.top_fee is not None:
                if s.top_fee > 0 and l.top_uid == user_id:
                    re_val[0]['latest_preincome'] += l.number * s.top_fee
        else:
            logging.info(f"预收益信息")
            if l:
                logging.info(f"order:{l.id}")
            if g:
                logging.info(f"good:{g.id}")
            if s:
                logging.info(f"good_spec:{s.id}")

    flash_order_ids = d_package.get_flash_order_ids(user_id)
    if len(flash_order_ids) > 0:
        flash_orders = d_order.get_user_falsh_orders(flash_order_ids)
        if flash_orders is not None:
            for t_order_source, t_order, t_good_spec in flash_orders:
                get_res = d_package.get_order_package_forid(t_order_source.source_id)
                if get_res is not None and t_good_spec is not None:
                    t_order, t_package = get_res
                    if t_good_spec.price is None:
                        t_good_spec.price = 0
                    if t_package.flash_sale_price is None:
                        t_package.flash_sale_price = 0
                    this_balance = t_good_spec.price * t_order_source.amount - t_package.flash_sale_price * t_order_source.amount
                    re_val[0]["order_id_income"].append(t_order.id)
                    re_val[0]["flash_order_balance"] += this_balance

    #flash_order_balance 暂时不用，代最近一次预收益字段
    re_val[0]["flash_order_balance"] = re_val[0]['latest_preincome']
    return re_val

@router.post(f'/get_balance_income_list', summary="获取预收益列表")
def get_balance_income_list(user_id:int = 0):
    """
    计算条件：订单未计算收益，且在已支付1或发货中2。|
        "type": "秒杀单商品售出",  |
        "detail": "客户订单未完结",|
        "good_name": null, 商品标题名称|
        "good_id": 1, 商品id|
        "good_spec_id": 1, 使用规格id|
        "t_order_create_time": null, 客户订单创建时间|
        "t_order_num": 10, 客户订单包含秒杀包商品数量|
        "t_order_income": 200， 本次秒杀包出售收益额|
    """
    re_val = []
    flash_order_ids = d_package.get_flash_order_ids(user_id)
    if len(flash_order_ids) > 0:
        flash_orders = d_order.get_user_falsh_orders2(flash_order_ids)
        if flash_orders is not None:
            for t_order_source, t_order, t_good_spec, t_good in flash_orders:
                get_res = d_package.get_order_package_forid(t_order_source.source_id)
                if get_res is not None and t_good_spec is not None:
                    t_order, t_package = get_res
                    if t_good_spec.price is None:
                        t_good_spec.price = 0
                    if t_package.flash_sale_price is None:
                        t_package.flash_sale_price = 0
                    this_balance = t_good_spec.price * t_order_source.amount - t_package.flash_sale_price * t_order_source.amount
                    re_val.append({"type": global_define.balance_type[7],"detail": "客户订单未完结","good_name": t_good.title, "good_id":t_good.id, \
                                   "good_spec_id": t_good_spec.id, "t_order_create_time": t_order.create_time, "t_order_num": t_order_source.amount, \
                                   "t_order_income": this_balance})
    #分享收益 1 | 未发货    2 | 已发货   9 | 未使用
    orders_list = d_order.get_user_willcomein_order(user_id)
    for l,g,s in orders_list:
        if g is None or s is None:
            continue
        #分享
        if l.recommender_id is not None and l.recommender_id > 0 and s.share_fee is not None:
            if s.share_fee > 0 and l.recommender_id == user_id:
                re_val.append({"type": global_define.balance_type[13], "detail": "客户订单未完结","good_name": g.title, "good_id": g.id,\
                               "good_spec_id": s.id, "t_order_create_time": l.create_time, "t_order_num": l.number, "t_order_income": s.share_fee, "order_id": l.id})
        #层级
        if l.parent_uid is not None and l.parent_uid > 0 and s.parent_fee is not None:
            if s.parent_fee > 0 and l.parent_uid == user_id:
                re_val.append({"type": global_define.balance_type[1], "detail": "客户订单未完结", "good_name": g.title, "good_id": g.id, \
                               "good_spec_id": s.id, "t_order_create_time": l.create_time, "t_order_num": l.number,
                               "t_order_income": s.parent_fee, "order_id": l.id})
        # 直推
        if l.invited_uid is not None and l.invited_uid > 0 and s.recommender_fee is not None:
            if s.recommender_fee > 0 and l.invited_uid == user_id:
                re_val.append({"type": global_define.balance_type[14], "detail": "客户订单未完结", "good_name": g.title, "good_id": g.id, \
                               "good_spec_id": s.id, "t_order_create_time": l.create_time, "t_order_num": l.number,
                               "t_order_income": s.recommender_fee, "order_id": l.id})

        # 供货介绍人的收益
        if l.supplier_uid is not None and l.supplier_uid > 0 and s.supplier_fee is not None:
            if s.supplier_fee > 0 and l.supplier_uid == user_id:
                re_val.append({"type": global_define.balance_type[15], "detail": "客户订单未完结", "good_name": g.title, "good_id": g.id, \
                               "good_spec_id": s.id, "t_order_create_time": l.create_time, "t_order_num": l.number,
                               "t_order_income": s.supplier_fee, "order_id": l.id})
        # 见点
        if l.top_uid is not None and l.top_uid > 0 and s.top_fee is not None:
            if s.top_fee > 0 and l.top_uid == user_id:
                re_val.append({"type": global_define.balance_type[2], "detail": "客户订单未完结", "good_name": g.title, "good_id": g.id, \
                               "good_spec_id": s.id, "t_order_create_time": l.create_time, "t_order_num": l.number,
                               "t_order_income": s.top_fee, "order_id": l.id})
        # 平级奖
        if l.eqlevel_uid is not None and l.eqlevel_uid > 0 and s.eqlevel_fee is not None:
            if s.eqlevel_fee > 0 and l.eqlevel_uid == user_id:
                re_val.append({"type": global_define.balance_type[22], "detail": "客户订单未完结", "good_name": g.title, "good_id": g.id, \
                               "good_spec_id": s.id, "t_order_create_time": l.create_time, "t_order_num": l.number,
                               "t_order_income": s.eqlevel_fee, "order_id": l.id})
    return re_val
    #
    # uinfo = d_user.get_user_by_id(user_id)
    # uids = []
    # comein_name = global_define.balance_type[1]
    # is_inv = True
    # if uinfo.parent_id is not None and uinfo.parent_id == 0:
    #     uids = d_user.get_invited_user_ids(user_id)
    #     comein_name = global_define.balance_type[14]
    # else:
    #     uids = d_user.get_invparent_user_ids(user_id)
    #     is_inv = False
    # inv_list = d_order.get_user_invparent_order(uids)
    # for l,g,s in inv_list:
    #     if g is None or s is None:
    #         continue
    #     comein_balance = s.parent_fee
    #     if is_inv:
    #         comein_balance = s.recommender_fee
    #     re_val.append({"type": comein_name, "detail": "客户订单未完结","good_name": g.title, "good_id": g.id,\
    #                    "good_spec_id": s.id, "t_order_create_time": l.create_time, "t_order_num": l.number, "t_order_income": comein_balance})
    #
    # #供货介绍人的收益
    # introducer_list = d_order.get_user_introducer_order(user_id)
    # for l,g,s in introducer_list:
    #     if g is None or s is None:
    #         continue
    #     re_val.append({"type": global_define.balance_type[15], "detail": "客户订单未完结","good_name": g.title, "good_id": g.id,\
    #                    "good_spec_id": s.id, "t_order_create_time": l.create_time, "t_order_num": l.number, "t_order_income": s.supplier_fee})
    # #见点
    # if uinfo.parent_id is not None and uinfo.parent_id == 0:
    #     member_ids = d_user.get_member_ids([user_id])
    #     top_list = d_order.get_user_invparent_order(member_ids)
    #     for l, g, s in top_list:
    #         if g is None or s is None or l.create_time < uinfo.level_top_time:
    #             continue
    #         re_val.append({"type": global_define.balance_type[2], "detail": "客户订单未完结", "good_name": g.title, "good_id": g.id, \
    #                        "good_spec_id": s.id, "t_order_create_time": l.create_time, "t_order_num": l.number,
    #                        "t_order_income": s.top_fee})
    #


@router.post(f"/search_balance", summary="获取收益记录")
async def search_balance(item: d_balance.SearchBalance):
    if item.user_id is None:
        return {'status': 200, 'message': '请设置查询用户'}
    return d_balance.search_balance(item)