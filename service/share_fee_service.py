from typing import Optional
from fastapi.exceptions import HTTPException

from common import Dao, global_define
from model.schema import TUser, TOrder, TGoodSpec, TFlashOrder, TPackage, TOrderSource, TGood, TSupplierIncome
from dao import d_user_account, d_account, d_user, d_package, d_order, d_groupsir, d_settings, d_supplier_account, d_supplier_income, d_good
from model.mall import m_account
import time, datetime

def share_mall_fee_with_other(order_id: int):
    """share mall fee with other"""
    with Dao() as db:
        # 查询数据
        t_order, t_user, t_spec, t_good = db.query(TOrder, TUser, TGoodSpec, TGood)\
            .outerjoin(TUser, TUser.id==TOrder.paider_id)\
            .outerjoin(TGoodSpec, TGoodSpec.id==TOrder.spec_id)\
            .outerjoin(TGood, TOrder.good_id==TGood.id)\
            .filter(TOrder.id == order_id).first()
        if t_order is None:
            raise HTTPException(400, "订单不存在")
        if t_user is None:
            raise HTTPException(400, "用户不存在")
        if t_spec is None:
            raise HTTPException(400, "商品不存在")
        if t_order.is_assign_income:
            raise HTTPException(400, "已经分配过收益")
        t_order: TOrder
        t_user: TUser
        t_spec: TGoodSpec
        #t_source: TOrderSource
        t_good: TGood

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
                    #tgood = d_good(t_package.good_id)
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
        # parent_id: Optional[int] = None
        # balance_type = global_define.balance_type[1]
        # is_invited = False
        # if t_user.parent_id is not None:
        #     parent_id = t_user.parent_id
        # elif t_user.invited_user_id is not None:
        #     parent_id = t_user.invited_user_id
        #     balance_type = global_define.balance_type[14]
        #     is_invited = True

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
        # top_user_id = d_user.get_top_id(t_user.id)
        # if top_user_id == t_user.id or top_user_id == 0:
        #     top_user_info = None
        # else:
        #     top_user_info = d_account.get_account_info_add(top_user_id)

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

        #供货收益 介绍人的收益
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

        #供货商收回成本
        # if t_spec.supplier_fee is not None and t_good.supplier_id is not None:
        #     supplier_info = d_supplier_account.get_account_info(t_good.supplier_id)
        #     if supplier_info:
        #         supplier_income = t_spec.supplier_fee * t_order.number
        #         if supplier_info.amount is None:
        #             supplier_info.amount = 0
        #         total_balance = supplier_info.amount + supplier_income
        #         d_supplier_account.update_account_by_id(supplier_info.id, {"change": supplier_income,"amount": total_balance})
        #         d_supplier_income.add_income(TSupplierIncome(
        #             supplier_id=t_good.supplier_id,
        #             change=supplier_income,
        #             balance=total_balance,
        #             type=global_define.balance_type[8],
        #             create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        #             operator_id=10000
        #             # good_id=str(t_good.id),
        #             # good_title=t_good.title,
        #             # good_num=str(t_order.number)
        #         ))

        #更新订单收益分配状态
        now_time = datetime.datetime.now()
        d_order.assign_income_order(TOrder(
            id=t_order.id,
            complete_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            is_assign_income=1,
            detail=f"[{now_time}#持有：{user_income_l}#层：{parent_income}#点：{top_income}#推：{invited_income}#享：{recommender_income}#供：{supplier_income}#团：{groupsir_income_l}#平：{eqlevel_income}]"
        ))
        # 更新系统用户级别
        if t_user.level_id == 0:
            d_user.update_sysuser_active(t_user.id)
        elif t_user.level_id == 1:
            d_user.update_sysuser_high(t_user.id)
        elif t_user.level_id == 2:
            d_user.update_sysuser_top(t_user.id)
        db.commit()


def share_package_fee_with_other(flash_order_id: int):
    """share mall fee with other"""
    with Dao() as db:
        t_flash_order, t_package, t_user = db.query(TFlashOrder, TPackage, TUser).outerjoin(TPackage, TPackage.id==TFlashOrder.package_id).outerjoin(TUser, TUser.id == TFlashOrder.user_id).filter(TFlashOrder.id == flash_order_id).first()
        if t_flash_order is None:
            raise HTTPException(400, "订单不存在")
        if t_package is None:
            raise HTTPException(400, "秒杀包不存在")
        if t_user is None:
            raise HTTPException(400, "用户不存在")
        
        t_package: TPackage
        t_user: TUser

        # 层级奖
        share_fee: int  = t_package.share_fee
        while share_fee is not None and share_fee > 0:
            parent_id = t_user.parent_id
            share_fee = share_fee // 2

            if parent_id is None:
                break

            d_user_account.balance_change(
                user_id=parent_id,
                fee=share_fee,
                category='层级奖',
                description='秒杀包奖励',
                db=db
            )
            t_user = db.query(TUser).filter(TUser.id == parent_id).first()

        db.commit()

