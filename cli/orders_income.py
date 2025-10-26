import datetime,time,sys,math
from pathlib import Path
root_dir = Path(__file__).parents[1]
model_dir = root_dir / 'model'
#print(root_dir)
# print(model_dir)
sys.path.append(str(root_dir))

from common import Dao, global_define
#from common.global_define import *
from model import schema, m_schema

from dao import d_user_account, d_account, d_user, d_package, d_order, d_groupsir, d_settings, d_supplier_account, d_supplier_income
from model.mall import m_account
from typing import Optional


def get_orders(card_time: datetime, page: int, good_type:int = 0):
    re_data = {"total":0, "data":[]}
    """  以下标注状态均可分配收益
|  0 | 未付款             | pay    |
|  1 | 未发货             | send   | **
|  2 | 已发货             | send   | **
|  3 | 退货协商中         | return |
|  4 | 等待退货物流       | return |
|  5 | 商品退回中         | return |
|  6 | 退货已签收         | return |
|  7 | 已签收             | send   |**
|  8 | 已完结             | finish |**
|  9 | 未使用             | NULL   |**
| 10 | 已使用             | NULL   |**
用户订单，支付才能创建，所以一直使用t_order.create_time，而paid_time实际未使用
select * from t_order LEFT JOIN t_good ON t_order.good_id=t_good.id where t_order.status_id in (1,2,7,8,9,10) and t_order.is_assign_income=0 and t_order.create_time > "2023-6-1 12:22:11" AND t_good.type=0
good_type=0默认为卡券；1为实体
"""
    with Dao() as db:
        #实体订单，未发货，不予结算
        if good_type == 1:
            card_info = db.query(schema.TOrder, schema.TGood, schema.TGoodSpec, schema.TOrderSource)\
            .outerjoin(schema.TGood, schema.TOrder.good_id == schema.TGood.id)\
            .outerjoin(schema.TGoodSpec,schema.TOrder.spec_id == schema.TGoodSpec.id)\
            .outerjoin(schema.TOrderSource,schema.TOrder.id == schema.TOrderSource.order_id)\
            .filter(schema.TOrder.status_id.in_([2,7,8,9,10]), schema.TOrder.is_assign_income == 0, schema.TOrder.delivery_time < card_time)\
            .filter(schema.TGood.type == good_type)
        else:
            card_info = db.query(schema.TOrder, schema.TGood, schema.TGoodSpec, schema.TOrderSource)\
            .outerjoin(schema.TGood, schema.TOrder.good_id == schema.TGood.id)\
            .outerjoin(schema.TGoodSpec,schema.TOrder.spec_id == schema.TGoodSpec.id)\
            .outerjoin(schema.TOrderSource,schema.TOrder.id == schema.TOrderSource.order_id)\
            .filter(schema.TOrder.status_id.in_([1,2,7,8,9,10]), schema.TOrder.is_assign_income == 0, schema.TOrder.create_time < card_time)\
            .filter(schema.TGood.type == good_type)

        re_data['total'] = card_info.count()
        re_data['data'] = card_info.offset(page * 20 - 20).limit(20).all()
    return re_data


def assgin_income(items):
    t_order, t_good, t_good_spec, t_order_source = items
    share_mall_fee_with_other(t_order.id)

def share_mall_fee_with_other(order_id: int):
    """share mall fee with other"""
    with Dao() as db:
        # 查询数据
        t_order, t_user, t_spec, t_good = db.query(schema.TOrder, schema.TUser, schema.TGoodSpec, schema.TGood)\
            .outerjoin(schema.TUser, schema.TUser.id==schema.TOrder.paider_id)\
            .outerjoin(schema.TGoodSpec, schema.TGoodSpec.id==schema.TOrder.spec_id)\
            .outerjoin(schema.TGood, schema.TOrder.good_id==schema.TGood.id)\
            .filter(schema.TOrder.id == order_id).first()
        if t_order is None:
            print("订单不存在")
            return
        if t_user is None:
            print("用户不存在")
            return
        if t_spec is None:
            print("商品不存在")
            return
        if t_order.is_assign_income:
            print("已经分配过收益")
            return
        t_order: schema.TOrder
        t_user: schema.TUser
        t_spec: schema.TGoodSpec
        #t_source: schema.TOrderSource
        t_good: schema.TGood

        #更新秒杀包持有人订单收益记录
        # user_income_l = 0
        # groupsir_income_l = 0
        # parent_income = 0
        # top_income = 0
        # recommender_income = 0
        # supplier_income = 0
        #
        #更新秒杀包持有人订单收益记录
        user_income_l = []
        groupsir_income_l = []
        parent_income = 0
        invited_income = 0
        top_income = 0
        recommender_income = 0
        supplier_income = 0
        eqlevel_income = 0
        t_source_list = d_order.get_order_source(t_order.id)
        for t_source in t_source_list:
            if t_source.source_id is not None:
                get_res = d_package.get_order_package_forid(t_source.source_id)
                if get_res is not None:
                    t_flash_order, t_package = get_res
                    user_income = t_spec.price * t_source.amount - t_package.flash_sale_price * t_source.amount
                    # 更新收益
                    account_info = d_account.get_account_info_add(t_flash_order.user_id)
                    total_balance = account_info.balance + user_income
                    d_account.update_account_by_id(account_info.id, {"balance": total_balance})
                    # 更新持有人收益记录
                    d_account.add_balance(m_account.BalanceModel(
                        user_id=t_flash_order.user_id,
                        change=user_income,
                        balance=total_balance,
                        type=global_define.balance_type[7],
                        create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                        good_id=str(t_good.id),
                        good_title=t_good.title,
                        good_num=str(t_source.amount)
                    ))
                    user_income_l.append({"uid":t_flash_order.user_id,"ch":user_income})

                    #团长收益
                    groupsir_user_info = d_groupsir.get_member_for_user(t_flash_order.user_id)
                    if groupsir_user_info:
                        groupsir_income = t_spec.price * t_source.amount * d_settings.get_settings().tuan_order_income / 1000
                        groupsir_account_info = d_account.get_account_info_add(groupsir_user_info.user_id)
                        total_balance = groupsir_account_info.balance + groupsir_income
                        d_account.update_account_by_id(groupsir_account_info.id, {"balance": total_balance})
                        d_account.add_balance(m_account.BalanceModel(
                            user_id=groupsir_user_info.user_id,
                            change=groupsir_income,
                            balance=total_balance,
                            type=global_define.balance_type[4],
                            create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                            good_id=str(t_good.id),
                            good_title=t_good.title,
                            good_num=str(t_source.amount)
                        ))
                        groupsir_income_l.append({"uid":groupsir_user_info.user_id,"ch":groupsir_income})



        # 层级奖
        if t_order.parent_uid is not None and t_order.parent_uid > 0:
            parent_info = d_account.get_account_info_add(t_order.parent_uid)
            if parent_info and t_spec.parent_fee > 0:
                parent_income = t_spec.parent_fee * t_order.number
                total_balance = parent_info.balance + parent_income
                d_account.update_account_by_id(parent_info.id, {"balance": total_balance})
                d_account.add_balance(m_account.BalanceModel(
                    user_id=parent_info.user_id,
                    change=parent_income,
                    balance=total_balance,
                    type=global_define.balance_type[1],
                    create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    good_id=str(t_good.id),
                    good_title=t_good.title,
                    good_num=str(t_order.number)
                ))

        # 直推级奖
        if t_order.invited_uid is not None and t_order.invited_uid > 0:
            parent_info = d_account.get_account_info_add(t_order.invited_uid)
            if parent_info and t_spec.recommender_fee > 0:
                invited_income = t_spec.recommender_fee * t_order.number
                total_balance = parent_info.balance + invited_income
                d_account.update_account_by_id(parent_info.id, {"balance": total_balance})
                d_account.add_balance(m_account.BalanceModel(
                    user_id=parent_info.user_id,
                    change=invited_income,
                    balance=total_balance,
                    type=global_define.balance_type[14],
                    create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    good_id=str(t_good.id),
                    good_title=t_good.title,
                    good_num=str(t_order.number)
                ))

        # 见点奖
        if t_order.top_uid is not None and t_order.top_uid > 0 and t_spec.top_fee > 0:
            top_user_info_data = d_user.get_user_by_id(t_order.top_uid)
            top_user_info = d_account.get_account_info_add(t_order.top_uid)
            if top_user_info_data:
                top_income = t_spec.top_fee * t_order.number
                total_balance = top_user_info.balance + top_income
                d_account.update_account_by_id(top_user_info.id, {"balance": total_balance})
                d_account.add_balance(m_account.BalanceModel(
                    user_id=t_order.top_uid,
                    change=top_income,
                    balance=total_balance,
                    type=global_define.balance_type[2],
                    create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    good_id=str(t_good.id),
                    good_title=t_good.title,
                    good_num=str(t_order.number)
                ))

        # 平级奖
        if t_order.eqlevel_uid is not None and t_order.eqlevel_uid > 0 and t_spec.eqlevel_fee > 0:
            eqlevel_user_info_data = d_user.get_user_by_id(t_order.eqlevel_uid)
            eqlevel_user_info_account = d_account.get_account_info_add(t_order.eqlevel_uid)
            if eqlevel_user_info_data:
                eqlevel_income = t_spec.eqlevel_fee * t_order.number
                total_balance = eqlevel_user_info_account.balance + eqlevel_income
                d_account.update_account_by_id(eqlevel_user_info_account.id, {"balance": total_balance})
                d_account.add_balance(m_account.BalanceModel(
                    user_id=t_order.eqlevel_uid,
                    change=eqlevel_income,
                    balance=total_balance,
                    type=global_define.balance_type[22],
                    create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    good_id=str(t_good.id),
                    good_title=t_good.title,
                    good_num=str(t_order.number)
                ))

        # 商品分享奖励
        if t_order.recommender_id is not None:
            if t_order.recommender_id and t_order.recommender_id > 0:
                recommender_info = d_account.get_account_info_add(t_order.recommender_id)
            else:
                recommender_info = None
            if recommender_info and t_spec.share_fee and t_spec.share_fee > 0:
                recommender_income = t_spec.share_fee * t_order.number
                total_balance = recommender_info.balance + recommender_income
                d_account.update_account_by_id(recommender_info.id, {"balance": total_balance})
                d_account.add_balance(m_account.BalanceModel(
                    user_id=recommender_info.user_id,
                    change=recommender_income,
                    balance=total_balance,
                    type=global_define.balance_type[3],
                    create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    good_id=str(t_good.id),
                    good_title=t_good.title,
                    good_num=str(t_order.number)
                ))

        #供货收益
        if t_order.supplier_uid is not None and t_order.supplier_uid > 0 and t_spec.supplier_fee > 0:
            supplier_info = d_account.get_account_info_add(t_order.supplier_uid)
            if supplier_info:
                supplier_income = t_spec.supplier_fee * t_order.number
                if supplier_info.balance is None:
                    supplier_info.balance = 0
                total_balance = supplier_info.balance + supplier_income
                d_account.update_account_by_id(supplier_info.id, {"balance": total_balance})
                d_account.add_balance(m_account.BalanceModel(
                    user_id=t_order.supplier_uid,
                    change=supplier_income,
                    balance=total_balance,
                    type=global_define.balance_type[15],
                    create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    good_id=str(t_good.id),
                    good_title=t_good.title,
                    good_num=str(t_order.number)
                ))

        #更新订单收益分配状态
        now_time = datetime.datetime.now()
        d_order.assign_income_order(schema.TOrder(
            id=t_order.id,
            complete_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            is_assign_income=1,
            status_id=8,
            detail=f"[{now_time}#持有：{user_income_l}#层：{parent_income}#点：{top_income}#推：{invited_income}#享：{recommender_income}#供：{supplier_income}#团：{groupsir_income_l}#平：{eqlevel_income}#cli超时处理]"
        ))

        db.commit()


def main():
    now_time = datetime.datetime.now()
    card_time = now_time - datetime.timedelta(days=global_define.setting_orders['card_income_times'])
    body_time = now_time - datetime.timedelta(days=global_define.setting_orders['body_income_times'])

    #测试时间
    #card_time = now_time + datetime.timedelta(days=1)
    #body_time = now_time + datetime.timedelta(days=1)

    print(f"{now_time} - 超时订单收益任务启动")
    card_orders = get_orders(card_time, 1)
    if card_orders['total'] > 0:
        print(f"共{card_orders['total']} - 卡券收益订单")
        for item in card_orders['data']:
            assgin_income(item)
        pages = math.ceil(card_orders['total'] / 20)
        i = 2
        while i <= pages:
            card_orders = get_orders(card_time, i)
            for item in card_orders['data']:
                assgin_income(item)

    print(f"卡券收益计算完毕")
    body_orders = get_orders(body_time, 1, 1)
    if body_orders['total'] > 0:
        print(f"共{body_orders['total']} - 实体收益订单")
        for item in body_orders['data']:
            assgin_income(item)
        pages = math.ceil(body_orders['total'] / 20)
        i = 2
        while i <= pages:
            body_orders = get_orders(card_time, i, 1)
            for item in body_orders['data']:
                assgin_income(item)
    print(f"实体收益计算完毕")

def main2():
    share_mall_fee_with_other(1)
    pass

if __name__ == '__main__':
    main()