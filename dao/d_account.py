from common import Dao
from model.mall import m_account
from model.schema import TUserAccount, TUserBank, TCoin, TBalance, TUser, TUserWithdraw, TLockBalance
import time, datetime

def create_account(item: m_account.TUserAccount):
    with Dao() as db:
        db.add(item)
        db.commit()
        db.refresh(item)
    return item


def delete_account_by_id(account_id: int):
    with Dao() as db:
        db.query(TUserAccount).where(TUserAccount.id == account_id).delete()
        db.commit()


def update_account_by_id(account_id: int, item: dict):
    with Dao() as db:
        if item.get("id"):
            item.pop("id")
        db.query(TUserAccount).where(TUserAccount.id == account_id).update(item)
        db.commit()

def get_account_info(user_id:int = 0):
    with Dao() as db:
        return db.query(TUserAccount).filter(TUserAccount.user_id == user_id).first()

def get_account_info_add(user_id:int = 0):
    if user_id is None:
        user_id = 0
    with Dao() as db:
        account_info = db.query(TUserAccount).filter(TUserAccount.user_id == user_id).first()
        if not account_info and user_id > 0:
            account_info = create_account(TUserAccount(
                user_id = user_id,
                balance = 0,
                lock_balance = 0,
                coin = 0,
                create_time = datetime.datetime.now()
            ))
        return account_info

def get_acount_list(user_id:int):
    with Dao() as db:
        #q = db.query(TUserAccount)
        #t_acount_list = q.where(TUserAccount.user_id == user_id).all()
        q = db.query(TUserBank)
        t_acount_list = q.where(TUserBank.user_id == user_id).all()
        return t_acount_list

def get_coin_balance_list(user_id:int):
    with Dao() as db:
        q = db.query(TUserAccount)
        t_acount_list = q.where(TUserAccount.user_id == user_id).all()
        return t_acount_list

def get_coin_balance(user_id:int):
    with Dao() as db:
        return db.query(TUserAccount).where(TUserAccount.user_id == user_id).first()

def update_bank(account_id: int, item: dict):
    with Dao() as db:
        if item.get("id"):
            item.pop("id")
        db.query(TUserBank).where(TUserBank.id == account_id).update(item)
        db.commit()

def insert_coin(items: m_account.CoinModel):
    add_instance = TCoin(
        user_id=items.user_id,
        change=items.change,
        coin=items.coin,
        type="manager",
        create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    )
    with Dao() as db:
        db.add(add_instance)
        db.commit()

def insert_bank(items: m_account.BalanceModel):
    add_instance = TBalance(
        user_id=items.user_id,
        change=items.change,
        balance=items.balance,
        type="manager",
        create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    )
    with Dao() as db:
        db.add(add_instance)
        db.commit()

def add_balance(items: m_account.BalanceModel):
    add_instance = TBalance(
        user_id=items.user_id,
        change=items.change,
        balance=items.balance,
        type=items.type,
        create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        good_id=items.good_id,
        good_title=items.good_title,
        good_num=items.good_num,
        out_trade_no=items.out_trade_no

    )
    with Dao() as db:
        db.add(add_instance)
        db.commit()

def add_lock_balance(items: m_account.LockBalanceModel):
    add_instance = TLockBalance(
        user_id=items.user_id,
        change=items.change,
        lock_balance=items.lock_balance,
        type=items.type,
        create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        out_trade_no=items.out_trade_no
    )
    with Dao() as db:
        db.add(add_instance)
        db.commit()

def get_user_withdraw(withdraw_id:int):
    with Dao() as db:
        res = db.query(TUserWithdraw, TUser, TUserAccount) \
            .outerjoin(TUser, TUserWithdraw.user_id == TUser.id) \
            .outerjoin(TUserAccount, TUserWithdraw.user_id == TUserAccount.user_id) \
            .filter(TUserWithdraw.id == withdraw_id).first()
        return res

def update_user_withdraw_status(withdraw_id:int, user_withdraw_status_id:int):
    with Dao() as db:
        db.query(TUserWithdraw).where(TUserWithdraw.id == withdraw_id).update({"user_withdraw_status_id": user_withdraw_status_id})
        db.commit()

def update_user_withdraw_balance(withdraw_id:int, fee_balance:int, deduct_balance:int):
    with Dao() as db:
        db.query(TUserWithdraw).where(TUserWithdraw.id == withdraw_id).update({"fee_balance": fee_balance, "deduct_balance": deduct_balance})
        db.commit()