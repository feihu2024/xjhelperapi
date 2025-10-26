from common import Dao
from common.db import SessionLocal
from typing import List
from model.m_schema import *
from model.schema import *
from fastapi.exceptions import HTTPException

def model2dict(item) -> dict:
    return {key: val for key, val in item.dict().items() if val is not None}

    
def insert_address(item: CreateAddress, db: Optional[SessionLocal] = None) -> SAddress:
    data = model2dict(item)
    t = TAddress(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SAddress.parse_obj(t.__dict__)

    
def delete_address(address_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TAddress).where(TAddress.id == address_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TAddress).where(TAddress.id == address_id).delete()
        db.commit()

    
def update_address(item: SAddress, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TAddress).where(TAddress.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TAddress).where(TAddress.id == item.id).update(data)
        db.commit()

    
def get_address(address_id: int) -> Optional[SAddress]:
    with Dao() as db:
        t = db.query(TAddress).where(TAddress.id == address_id).first()
        if t:
            return SAddress.parse_obj(t.__dict__)
        else:
            return None


def filter_address(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SAddress]:
    with Dao() as db:
        q = db.query(TAddress)


        if 'id' in items:
            q = q.where(TAddress.id == items['id'])
        if 'id_start' in items:
            q = q.where(TAddress.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TAddress.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TAddress.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TAddress.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TAddress.user_id <= items['user_id_end'])
        
        if 'province' in items:
            q = q.where(TAddress.province == items['province'])
        if 'province_start' in items:
            q = q.where(TAddress.province >= items['province_start'])
        if 'province_end' in items:
            q = q.where(TAddress.province <= items['province_end'])
        
        if 'city' in items:
            q = q.where(TAddress.city == items['city'])
        if 'city_start' in items:
            q = q.where(TAddress.city >= items['city_start'])
        if 'city_end' in items:
            q = q.where(TAddress.city <= items['city_end'])
        
        if 'area' in items:
            q = q.where(TAddress.area == items['area'])
        if 'area_start' in items:
            q = q.where(TAddress.area >= items['area_start'])
        if 'area_end' in items:
            q = q.where(TAddress.area <= items['area_end'])
        
        if 'street' in items:
            q = q.where(TAddress.street == items['street'])
        if 'street_start' in items:
            q = q.where(TAddress.street >= items['street_start'])
        if 'street_end' in items:
            q = q.where(TAddress.street <= items['street_end'])
        
        if 'description' in items:
            q = q.where(TAddress.description == items['description'])
        if 'description_start' in items:
            q = q.where(TAddress.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TAddress.description <= items['description_end'])
        
        if 'default_' in items:
            q = q.where(TAddress.default_ == items['default_'])
        if 'default__start' in items:
            q = q.where(TAddress.default_ >= items['default__start'])
        if 'default__end' in items:
            q = q.where(TAddress.default_ <= items['default__end'])
        
        if 'consignee' in items:
            q = q.where(TAddress.consignee == items['consignee'])
        if 'consignee_start' in items:
            q = q.where(TAddress.consignee >= items['consignee_start'])
        if 'consignee_end' in items:
            q = q.where(TAddress.consignee <= items['consignee_end'])
        
        if 'phone' in items:
            q = q.where(TAddress.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TAddress.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TAddress.phone <= items['phone_end'])
        

        if 'id' in set_items:
            q = q.where(TAddress.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TAddress.user_id.in_(set_items['user_id']))
        
        if 'province' in set_items:
            q = q.where(TAddress.province.in_(set_items['province']))
        
        if 'city' in set_items:
            q = q.where(TAddress.city.in_(set_items['city']))
        
        if 'area' in set_items:
            q = q.where(TAddress.area.in_(set_items['area']))
        
        if 'street' in set_items:
            q = q.where(TAddress.street.in_(set_items['street']))
        
        if 'description' in set_items:
            q = q.where(TAddress.description.in_(set_items['description']))
        
        if 'default_' in set_items:
            q = q.where(TAddress.default_.in_(set_items['default_']))
        
        if 'consignee' in set_items:
            q = q.where(TAddress.consignee.in_(set_items['consignee']))
        
        if 'phone' in set_items:
            q = q.where(TAddress.phone.in_(set_items['phone']))
        

        if 'province' in search_items:
            q = q.where(TAddress.province.like(search_items['province']))
        
        if 'city' in search_items:
            q = q.where(TAddress.city.like(search_items['city']))
        
        if 'area' in search_items:
            q = q.where(TAddress.area.like(search_items['area']))
        
        if 'street' in search_items:
            q = q.where(TAddress.street.like(search_items['street']))
        
        if 'description' in search_items:
            q = q.where(TAddress.description.like(search_items['description']))
        
        if 'consignee' in search_items:
            q = q.where(TAddress.consignee.like(search_items['consignee']))
        
        if 'phone' in search_items:
            q = q.where(TAddress.phone.like(search_items['phone']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TAddress.phone.asc())
                orders.append(TAddress.id.asc())
            elif val == 'desc':
                #orders.append(TAddress.phone.desc())
                orders.append(TAddress.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_address_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SAddress.parse_obj(t.__dict__) for t in t_address_list]


def filter_count_address(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TAddress)


        if 'id' in items:
            q = q.where(TAddress.id == items['id'])
        if 'id_start' in items:
            q = q.where(TAddress.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TAddress.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TAddress.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TAddress.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TAddress.user_id <= items['user_id_end'])
        
        if 'province' in items:
            q = q.where(TAddress.province == items['province'])
        if 'province_start' in items:
            q = q.where(TAddress.province >= items['province_start'])
        if 'province_end' in items:
            q = q.where(TAddress.province <= items['province_end'])
        
        if 'city' in items:
            q = q.where(TAddress.city == items['city'])
        if 'city_start' in items:
            q = q.where(TAddress.city >= items['city_start'])
        if 'city_end' in items:
            q = q.where(TAddress.city <= items['city_end'])
        
        if 'area' in items:
            q = q.where(TAddress.area == items['area'])
        if 'area_start' in items:
            q = q.where(TAddress.area >= items['area_start'])
        if 'area_end' in items:
            q = q.where(TAddress.area <= items['area_end'])
        
        if 'street' in items:
            q = q.where(TAddress.street == items['street'])
        if 'street_start' in items:
            q = q.where(TAddress.street >= items['street_start'])
        if 'street_end' in items:
            q = q.where(TAddress.street <= items['street_end'])
        
        if 'description' in items:
            q = q.where(TAddress.description == items['description'])
        if 'description_start' in items:
            q = q.where(TAddress.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TAddress.description <= items['description_end'])
        
        if 'default_' in items:
            q = q.where(TAddress.default_ == items['default_'])
        if 'default__start' in items:
            q = q.where(TAddress.default_ >= items['default__start'])
        if 'default__end' in items:
            q = q.where(TAddress.default_ <= items['default__end'])
        
        if 'consignee' in items:
            q = q.where(TAddress.consignee == items['consignee'])
        if 'consignee_start' in items:
            q = q.where(TAddress.consignee >= items['consignee_start'])
        if 'consignee_end' in items:
            q = q.where(TAddress.consignee <= items['consignee_end'])
        
        if 'phone' in items:
            q = q.where(TAddress.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TAddress.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TAddress.phone <= items['phone_end'])
        

        if 'id' in set_items:
            q = q.where(TAddress.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TAddress.user_id.in_(set_items['user_id']))
        
        if 'province' in set_items:
            q = q.where(TAddress.province.in_(set_items['province']))
        
        if 'city' in set_items:
            q = q.where(TAddress.city.in_(set_items['city']))
        
        if 'area' in set_items:
            q = q.where(TAddress.area.in_(set_items['area']))
        
        if 'street' in set_items:
            q = q.where(TAddress.street.in_(set_items['street']))
        
        if 'description' in set_items:
            q = q.where(TAddress.description.in_(set_items['description']))
        
        if 'default_' in set_items:
            q = q.where(TAddress.default_.in_(set_items['default_']))
        
        if 'consignee' in set_items:
            q = q.where(TAddress.consignee.in_(set_items['consignee']))
        
        if 'phone' in set_items:
            q = q.where(TAddress.phone.in_(set_items['phone']))
        

        if 'province' in search_items:
            q = q.where(TAddress.province.like(search_items['province']))
        
        if 'city' in search_items:
            q = q.where(TAddress.city.like(search_items['city']))
        
        if 'area' in search_items:
            q = q.where(TAddress.area.like(search_items['area']))
        
        if 'street' in search_items:
            q = q.where(TAddress.street.like(search_items['street']))
        
        if 'description' in search_items:
            q = q.where(TAddress.description.like(search_items['description']))
        
        if 'consignee' in search_items:
            q = q.where(TAddress.consignee.like(search_items['consignee']))
        
        if 'phone' in search_items:
            q = q.where(TAddress.phone.like(search_items['phone']))
        
    
        c = q.count()
        return c

    
def insert_admin(item: CreateAdmin, db: Optional[SessionLocal] = None) -> SAdmin:
    data = model2dict(item)
    t = TAdmin(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SAdmin.parse_obj(t.__dict__)

    
def delete_admin(admin_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TAdmin).where(TAdmin.id == admin_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TAdmin).where(TAdmin.id == admin_id).delete()
        db.commit()

    
def update_admin(item: SAdmin, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TAdmin).where(TAdmin.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TAdmin).where(TAdmin.id == item.id).update(data)
        db.commit()

    
def get_admin(admin_id: int) -> Optional[SAdmin]:
    with Dao() as db:
        t = db.query(TAdmin).where(TAdmin.id == admin_id).first()
        if t:
            return SAdmin.parse_obj(t.__dict__)
        else:
            return None


def filter_admin(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SAdmin]:
    with Dao() as db:
        q = db.query(TAdmin)


        if 'id' in items:
            q = q.where(TAdmin.id == items['id'])
        if 'id_start' in items:
            q = q.where(TAdmin.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TAdmin.id <= items['id_end'])
        
        if 'username' in items:
            q = q.where(TAdmin.username == items['username'])
        if 'username_start' in items:
            q = q.where(TAdmin.username >= items['username_start'])
        if 'username_end' in items:
            q = q.where(TAdmin.username <= items['username_end'])
        
        if 'phone' in items:
            q = q.where(TAdmin.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TAdmin.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TAdmin.phone <= items['phone_end'])
        
        if 'email' in items:
            q = q.where(TAdmin.email == items['email'])
        if 'email_start' in items:
            q = q.where(TAdmin.email >= items['email_start'])
        if 'email_end' in items:
            q = q.where(TAdmin.email <= items['email_end'])
        
        if 'level_id' in items:
            q = q.where(TAdmin.level_id == items['level_id'])
        if 'level_id_start' in items:
            q = q.where(TAdmin.level_id >= items['level_id_start'])
        if 'level_id_end' in items:
            q = q.where(TAdmin.level_id <= items['level_id_end'])
        
        if 'password' in items:
            q = q.where(TAdmin.password == items['password'])
        if 'password_start' in items:
            q = q.where(TAdmin.password >= items['password_start'])
        if 'password_end' in items:
            q = q.where(TAdmin.password <= items['password_end'])
        
        if 'id_card' in items:
            q = q.where(TAdmin.id_card == items['id_card'])
        if 'id_card_start' in items:
            q = q.where(TAdmin.id_card >= items['id_card_start'])
        if 'id_card_end' in items:
            q = q.where(TAdmin.id_card <= items['id_card_end'])
        
        if 'gender' in items:
            q = q.where(TAdmin.gender == items['gender'])
        if 'gender_start' in items:
            q = q.where(TAdmin.gender >= items['gender_start'])
        if 'gender_end' in items:
            q = q.where(TAdmin.gender <= items['gender_end'])
        
        if 'register_time' in items:
            q = q.where(TAdmin.register_time == items['register_time'])
        if 'register_time_start' in items:
            q = q.where(TAdmin.register_time >= items['register_time_start'])
        if 'register_time_end' in items:
            q = q.where(TAdmin.register_time <= items['register_time_end'])
        
        if 'last_active_time' in items:
            q = q.where(TAdmin.last_active_time == items['last_active_time'])
        if 'last_active_time_start' in items:
            q = q.where(TAdmin.last_active_time >= items['last_active_time_start'])
        if 'last_active_time_end' in items:
            q = q.where(TAdmin.last_active_time <= items['last_active_time_end'])
        
        if 'status' in items:
            q = q.where(TAdmin.status == items['status'])
        if 'status_start' in items:
            q = q.where(TAdmin.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TAdmin.status <= items['status_end'])
        

        if 'id' in set_items:
            q = q.where(TAdmin.id.in_(set_items['id']))
        
        if 'username' in set_items:
            q = q.where(TAdmin.username.in_(set_items['username']))
        
        if 'phone' in set_items:
            q = q.where(TAdmin.phone.in_(set_items['phone']))
        
        if 'email' in set_items:
            q = q.where(TAdmin.email.in_(set_items['email']))
        
        if 'level_id' in set_items:
            q = q.where(TAdmin.level_id.in_(set_items['level_id']))
        
        if 'password' in set_items:
            q = q.where(TAdmin.password.in_(set_items['password']))
        
        if 'id_card' in set_items:
            q = q.where(TAdmin.id_card.in_(set_items['id_card']))
        
        if 'gender' in set_items:
            q = q.where(TAdmin.gender.in_(set_items['gender']))
        
        if 'register_time' in set_items:
            q = q.where(TAdmin.register_time.in_(set_items['register_time']))
        
        if 'last_active_time' in set_items:
            q = q.where(TAdmin.last_active_time.in_(set_items['last_active_time']))
        
        if 'status' in set_items:
            q = q.where(TAdmin.status.in_(set_items['status']))
        

        if 'username' in search_items:
            q = q.where(TAdmin.username.like(search_items['username']))
        
        if 'phone' in search_items:
            q = q.where(TAdmin.phone.like(search_items['phone']))
        
        if 'email' in search_items:
            q = q.where(TAdmin.email.like(search_items['email']))
        
        if 'password' in search_items:
            q = q.where(TAdmin.password.like(search_items['password']))
        
        if 'id_card' in search_items:
            q = q.where(TAdmin.id_card.like(search_items['id_card']))
        
        if 'gender' in search_items:
            q = q.where(TAdmin.gender.like(search_items['gender']))
        
        if 'status' in search_items:
            q = q.where(TAdmin.status.like(search_items['status']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TAdmin.status.asc())
                orders.append(TAdmin.id.asc())
            elif val == 'desc':
                #orders.append(TAdmin.status.desc())
                orders.append(TAdmin.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_admin_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SAdmin.parse_obj(t.__dict__) for t in t_admin_list]


def filter_count_admin(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TAdmin)


        if 'id' in items:
            q = q.where(TAdmin.id == items['id'])
        if 'id_start' in items:
            q = q.where(TAdmin.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TAdmin.id <= items['id_end'])
        
        if 'username' in items:
            q = q.where(TAdmin.username == items['username'])
        if 'username_start' in items:
            q = q.where(TAdmin.username >= items['username_start'])
        if 'username_end' in items:
            q = q.where(TAdmin.username <= items['username_end'])
        
        if 'phone' in items:
            q = q.where(TAdmin.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TAdmin.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TAdmin.phone <= items['phone_end'])
        
        if 'email' in items:
            q = q.where(TAdmin.email == items['email'])
        if 'email_start' in items:
            q = q.where(TAdmin.email >= items['email_start'])
        if 'email_end' in items:
            q = q.where(TAdmin.email <= items['email_end'])
        
        if 'level_id' in items:
            q = q.where(TAdmin.level_id == items['level_id'])
        if 'level_id_start' in items:
            q = q.where(TAdmin.level_id >= items['level_id_start'])
        if 'level_id_end' in items:
            q = q.where(TAdmin.level_id <= items['level_id_end'])
        
        if 'password' in items:
            q = q.where(TAdmin.password == items['password'])
        if 'password_start' in items:
            q = q.where(TAdmin.password >= items['password_start'])
        if 'password_end' in items:
            q = q.where(TAdmin.password <= items['password_end'])
        
        if 'id_card' in items:
            q = q.where(TAdmin.id_card == items['id_card'])
        if 'id_card_start' in items:
            q = q.where(TAdmin.id_card >= items['id_card_start'])
        if 'id_card_end' in items:
            q = q.where(TAdmin.id_card <= items['id_card_end'])
        
        if 'gender' in items:
            q = q.where(TAdmin.gender == items['gender'])
        if 'gender_start' in items:
            q = q.where(TAdmin.gender >= items['gender_start'])
        if 'gender_end' in items:
            q = q.where(TAdmin.gender <= items['gender_end'])
        
        if 'register_time' in items:
            q = q.where(TAdmin.register_time == items['register_time'])
        if 'register_time_start' in items:
            q = q.where(TAdmin.register_time >= items['register_time_start'])
        if 'register_time_end' in items:
            q = q.where(TAdmin.register_time <= items['register_time_end'])
        
        if 'last_active_time' in items:
            q = q.where(TAdmin.last_active_time == items['last_active_time'])
        if 'last_active_time_start' in items:
            q = q.where(TAdmin.last_active_time >= items['last_active_time_start'])
        if 'last_active_time_end' in items:
            q = q.where(TAdmin.last_active_time <= items['last_active_time_end'])
        
        if 'status' in items:
            q = q.where(TAdmin.status == items['status'])
        if 'status_start' in items:
            q = q.where(TAdmin.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TAdmin.status <= items['status_end'])
        

        if 'id' in set_items:
            q = q.where(TAdmin.id.in_(set_items['id']))
        
        if 'username' in set_items:
            q = q.where(TAdmin.username.in_(set_items['username']))
        
        if 'phone' in set_items:
            q = q.where(TAdmin.phone.in_(set_items['phone']))
        
        if 'email' in set_items:
            q = q.where(TAdmin.email.in_(set_items['email']))
        
        if 'level_id' in set_items:
            q = q.where(TAdmin.level_id.in_(set_items['level_id']))
        
        if 'password' in set_items:
            q = q.where(TAdmin.password.in_(set_items['password']))
        
        if 'id_card' in set_items:
            q = q.where(TAdmin.id_card.in_(set_items['id_card']))
        
        if 'gender' in set_items:
            q = q.where(TAdmin.gender.in_(set_items['gender']))
        
        if 'register_time' in set_items:
            q = q.where(TAdmin.register_time.in_(set_items['register_time']))
        
        if 'last_active_time' in set_items:
            q = q.where(TAdmin.last_active_time.in_(set_items['last_active_time']))
        
        if 'status' in set_items:
            q = q.where(TAdmin.status.in_(set_items['status']))
        

        if 'username' in search_items:
            q = q.where(TAdmin.username.like(search_items['username']))
        
        if 'phone' in search_items:
            q = q.where(TAdmin.phone.like(search_items['phone']))
        
        if 'email' in search_items:
            q = q.where(TAdmin.email.like(search_items['email']))
        
        if 'password' in search_items:
            q = q.where(TAdmin.password.like(search_items['password']))
        
        if 'id_card' in search_items:
            q = q.where(TAdmin.id_card.like(search_items['id_card']))
        
        if 'gender' in search_items:
            q = q.where(TAdmin.gender.like(search_items['gender']))
        
        if 'status' in search_items:
            q = q.where(TAdmin.status.like(search_items['status']))
        
    
        c = q.count()
        return c

    
def insert_balance(item: CreateBalance, db: Optional[SessionLocal] = None) -> SBalance:
    data = model2dict(item)
    t = TBalance(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SBalance.parse_obj(t.__dict__)

    
def delete_balance(balance_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TBalance).where(TBalance.id == balance_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TBalance).where(TBalance.id == balance_id).delete()
        db.commit()

    
def update_balance(item: SBalance, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TBalance).where(TBalance.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TBalance).where(TBalance.id == item.id).update(data)
        db.commit()

    
def get_balance(balance_id: int) -> Optional[SBalance]:
    with Dao() as db:
        t = db.query(TBalance).where(TBalance.id == balance_id).first()
        if t:
            return SBalance.parse_obj(t.__dict__)
        else:
            return None


def filter_balance(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SBalance]:
    with Dao() as db:
        q = db.query(TBalance)


        if 'id' in items:
            q = q.where(TBalance.id == items['id'])
        if 'id_start' in items:
            q = q.where(TBalance.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TBalance.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TBalance.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TBalance.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TBalance.user_id <= items['user_id_end'])
        
        if 'change' in items:
            q = q.where(TBalance.change == items['change'])
        if 'change_start' in items:
            q = q.where(TBalance.change >= items['change_start'])
        if 'change_end' in items:
            q = q.where(TBalance.change <= items['change_end'])
        
        if 'balance' in items:
            q = q.where(TBalance.balance == items['balance'])
        if 'balance_start' in items:
            q = q.where(TBalance.balance >= items['balance_start'])
        if 'balance_end' in items:
            q = q.where(TBalance.balance <= items['balance_end'])
        
        if 'type' in items:
            q = q.where(TBalance.type == items['type'])
        if 'type_start' in items:
            q = q.where(TBalance.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TBalance.type <= items['type_end'])
        
        if 'description' in items:
            q = q.where(TBalance.description == items['description'])
        if 'description_start' in items:
            q = q.where(TBalance.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TBalance.description <= items['description_end'])
        
        if 'create_time' in items:
            q = q.where(TBalance.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TBalance.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TBalance.create_time <= items['create_time_end'])
        
        if 'user_withdraw_id' in items:
            q = q.where(TBalance.user_withdraw_id == items['user_withdraw_id'])
        if 'user_withdraw_id_start' in items:
            q = q.where(TBalance.user_withdraw_id >= items['user_withdraw_id_start'])
        if 'user_withdraw_id_end' in items:
            q = q.where(TBalance.user_withdraw_id <= items['user_withdraw_id_end'])
        
        if 'operator_id' in items:
            q = q.where(TBalance.operator_id == items['operator_id'])
        if 'operator_id_start' in items:
            q = q.where(TBalance.operator_id >= items['operator_id_start'])
        if 'operator_id_end' in items:
            q = q.where(TBalance.operator_id <= items['operator_id_end'])
        
        if 'out_trade_no' in items:
            q = q.where(TBalance.out_trade_no == items['out_trade_no'])
        if 'out_trade_no_start' in items:
            q = q.where(TBalance.out_trade_no >= items['out_trade_no_start'])
        if 'out_trade_no_end' in items:
            q = q.where(TBalance.out_trade_no <= items['out_trade_no_end'])
        
        if 'good_id' in items:
            q = q.where(TBalance.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TBalance.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TBalance.good_id <= items['good_id_end'])
        
        if 'good_title' in items:
            q = q.where(TBalance.good_title == items['good_title'])
        if 'good_title_start' in items:
            q = q.where(TBalance.good_title >= items['good_title_start'])
        if 'good_title_end' in items:
            q = q.where(TBalance.good_title <= items['good_title_end'])
        
        if 'good_num' in items:
            q = q.where(TBalance.good_num == items['good_num'])
        if 'good_num_start' in items:
            q = q.where(TBalance.good_num >= items['good_num_start'])
        if 'good_num_end' in items:
            q = q.where(TBalance.good_num <= items['good_num_end'])
        

        if 'id' in set_items:
            q = q.where(TBalance.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TBalance.user_id.in_(set_items['user_id']))
        
        if 'change' in set_items:
            q = q.where(TBalance.change.in_(set_items['change']))
        
        if 'balance' in set_items:
            q = q.where(TBalance.balance.in_(set_items['balance']))
        
        if 'type' in set_items:
            q = q.where(TBalance.type.in_(set_items['type']))
        
        if 'description' in set_items:
            q = q.where(TBalance.description.in_(set_items['description']))
        
        if 'create_time' in set_items:
            q = q.where(TBalance.create_time.in_(set_items['create_time']))
        
        if 'user_withdraw_id' in set_items:
            q = q.where(TBalance.user_withdraw_id.in_(set_items['user_withdraw_id']))
        
        if 'operator_id' in set_items:
            q = q.where(TBalance.operator_id.in_(set_items['operator_id']))
        
        if 'out_trade_no' in set_items:
            q = q.where(TBalance.out_trade_no.in_(set_items['out_trade_no']))
        
        if 'good_id' in set_items:
            q = q.where(TBalance.good_id.in_(set_items['good_id']))
        
        if 'good_title' in set_items:
            q = q.where(TBalance.good_title.in_(set_items['good_title']))
        
        if 'good_num' in set_items:
            q = q.where(TBalance.good_num.in_(set_items['good_num']))
        

        if 'type' in search_items:
            q = q.where(TBalance.type.like(search_items['type']))
        
        if 'description' in search_items:
            q = q.where(TBalance.description.like(search_items['description']))
        
        if 'out_trade_no' in search_items:
            q = q.where(TBalance.out_trade_no.like(search_items['out_trade_no']))
        
        if 'good_id' in search_items:
            q = q.where(TBalance.good_id.like(search_items['good_id']))
        
        if 'good_title' in search_items:
            q = q.where(TBalance.good_title.like(search_items['good_title']))
        
        if 'good_num' in search_items:
            q = q.where(TBalance.good_num.like(search_items['good_num']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TBalance.good_num.asc())
                orders.append(TBalance.id.asc())
            elif val == 'desc':
                #orders.append(TBalance.good_num.desc())
                orders.append(TBalance.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_balance_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SBalance.parse_obj(t.__dict__) for t in t_balance_list]


def filter_count_balance(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TBalance)


        if 'id' in items:
            q = q.where(TBalance.id == items['id'])
        if 'id_start' in items:
            q = q.where(TBalance.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TBalance.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TBalance.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TBalance.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TBalance.user_id <= items['user_id_end'])
        
        if 'change' in items:
            q = q.where(TBalance.change == items['change'])
        if 'change_start' in items:
            q = q.where(TBalance.change >= items['change_start'])
        if 'change_end' in items:
            q = q.where(TBalance.change <= items['change_end'])
        
        if 'balance' in items:
            q = q.where(TBalance.balance == items['balance'])
        if 'balance_start' in items:
            q = q.where(TBalance.balance >= items['balance_start'])
        if 'balance_end' in items:
            q = q.where(TBalance.balance <= items['balance_end'])
        
        if 'type' in items:
            q = q.where(TBalance.type == items['type'])
        if 'type_start' in items:
            q = q.where(TBalance.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TBalance.type <= items['type_end'])
        
        if 'description' in items:
            q = q.where(TBalance.description == items['description'])
        if 'description_start' in items:
            q = q.where(TBalance.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TBalance.description <= items['description_end'])
        
        if 'create_time' in items:
            q = q.where(TBalance.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TBalance.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TBalance.create_time <= items['create_time_end'])
        
        if 'user_withdraw_id' in items:
            q = q.where(TBalance.user_withdraw_id == items['user_withdraw_id'])
        if 'user_withdraw_id_start' in items:
            q = q.where(TBalance.user_withdraw_id >= items['user_withdraw_id_start'])
        if 'user_withdraw_id_end' in items:
            q = q.where(TBalance.user_withdraw_id <= items['user_withdraw_id_end'])
        
        if 'operator_id' in items:
            q = q.where(TBalance.operator_id == items['operator_id'])
        if 'operator_id_start' in items:
            q = q.where(TBalance.operator_id >= items['operator_id_start'])
        if 'operator_id_end' in items:
            q = q.where(TBalance.operator_id <= items['operator_id_end'])
        
        if 'out_trade_no' in items:
            q = q.where(TBalance.out_trade_no == items['out_trade_no'])
        if 'out_trade_no_start' in items:
            q = q.where(TBalance.out_trade_no >= items['out_trade_no_start'])
        if 'out_trade_no_end' in items:
            q = q.where(TBalance.out_trade_no <= items['out_trade_no_end'])
        
        if 'good_id' in items:
            q = q.where(TBalance.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TBalance.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TBalance.good_id <= items['good_id_end'])
        
        if 'good_title' in items:
            q = q.where(TBalance.good_title == items['good_title'])
        if 'good_title_start' in items:
            q = q.where(TBalance.good_title >= items['good_title_start'])
        if 'good_title_end' in items:
            q = q.where(TBalance.good_title <= items['good_title_end'])
        
        if 'good_num' in items:
            q = q.where(TBalance.good_num == items['good_num'])
        if 'good_num_start' in items:
            q = q.where(TBalance.good_num >= items['good_num_start'])
        if 'good_num_end' in items:
            q = q.where(TBalance.good_num <= items['good_num_end'])
        

        if 'id' in set_items:
            q = q.where(TBalance.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TBalance.user_id.in_(set_items['user_id']))
        
        if 'change' in set_items:
            q = q.where(TBalance.change.in_(set_items['change']))
        
        if 'balance' in set_items:
            q = q.where(TBalance.balance.in_(set_items['balance']))
        
        if 'type' in set_items:
            q = q.where(TBalance.type.in_(set_items['type']))
        
        if 'description' in set_items:
            q = q.where(TBalance.description.in_(set_items['description']))
        
        if 'create_time' in set_items:
            q = q.where(TBalance.create_time.in_(set_items['create_time']))
        
        if 'user_withdraw_id' in set_items:
            q = q.where(TBalance.user_withdraw_id.in_(set_items['user_withdraw_id']))
        
        if 'operator_id' in set_items:
            q = q.where(TBalance.operator_id.in_(set_items['operator_id']))
        
        if 'out_trade_no' in set_items:
            q = q.where(TBalance.out_trade_no.in_(set_items['out_trade_no']))
        
        if 'good_id' in set_items:
            q = q.where(TBalance.good_id.in_(set_items['good_id']))
        
        if 'good_title' in set_items:
            q = q.where(TBalance.good_title.in_(set_items['good_title']))
        
        if 'good_num' in set_items:
            q = q.where(TBalance.good_num.in_(set_items['good_num']))
        

        if 'type' in search_items:
            q = q.where(TBalance.type.like(search_items['type']))
        
        if 'description' in search_items:
            q = q.where(TBalance.description.like(search_items['description']))
        
        if 'out_trade_no' in search_items:
            q = q.where(TBalance.out_trade_no.like(search_items['out_trade_no']))
        
        if 'good_id' in search_items:
            q = q.where(TBalance.good_id.like(search_items['good_id']))
        
        if 'good_title' in search_items:
            q = q.where(TBalance.good_title.like(search_items['good_title']))
        
        if 'good_num' in search_items:
            q = q.where(TBalance.good_num.like(search_items['good_num']))
        
    
        c = q.count()
        return c

    
def insert_banner(item: CreateBanner, db: Optional[SessionLocal] = None) -> SBanner:
    data = model2dict(item)
    t = TBanner(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SBanner.parse_obj(t.__dict__)

    
def delete_banner(banner_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TBanner).where(TBanner.id == banner_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TBanner).where(TBanner.id == banner_id).delete()
        db.commit()

    
def update_banner(item: SBanner, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TBanner).where(TBanner.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TBanner).where(TBanner.id == item.id).update(data)
        db.commit()

    
def get_banner(banner_id: int) -> Optional[SBanner]:
    with Dao() as db:
        t = db.query(TBanner).where(TBanner.id == banner_id).first()
        if t:
            return SBanner.parse_obj(t.__dict__)
        else:
            return None


def filter_banner(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SBanner]:
    with Dao() as db:
        q = db.query(TBanner)


        if 'id' in items:
            q = q.where(TBanner.id == items['id'])
        if 'id_start' in items:
            q = q.where(TBanner.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TBanner.id <= items['id_end'])
        
        if 'image' in items:
            q = q.where(TBanner.image == items['image'])
        if 'image_start' in items:
            q = q.where(TBanner.image >= items['image_start'])
        if 'image_end' in items:
            q = q.where(TBanner.image <= items['image_end'])
        
        if 'title' in items:
            q = q.where(TBanner.title == items['title'])
        if 'title_start' in items:
            q = q.where(TBanner.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TBanner.title <= items['title_end'])
        
        if 'subtitle' in items:
            q = q.where(TBanner.subtitle == items['subtitle'])
        if 'subtitle_start' in items:
            q = q.where(TBanner.subtitle >= items['subtitle_start'])
        if 'subtitle_end' in items:
            q = q.where(TBanner.subtitle <= items['subtitle_end'])
        
        if 'width' in items:
            q = q.where(TBanner.width == items['width'])
        if 'width_start' in items:
            q = q.where(TBanner.width >= items['width_start'])
        if 'width_end' in items:
            q = q.where(TBanner.width <= items['width_end'])
        
        if 'height' in items:
            q = q.where(TBanner.height == items['height'])
        if 'height_start' in items:
            q = q.where(TBanner.height >= items['height_start'])
        if 'height_end' in items:
            q = q.where(TBanner.height <= items['height_end'])
        
        if 'create_time' in items:
            q = q.where(TBanner.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TBanner.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TBanner.create_time <= items['create_time_end'])
        
        if 'description' in items:
            q = q.where(TBanner.description == items['description'])
        if 'description_start' in items:
            q = q.where(TBanner.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TBanner.description <= items['description_end'])
        
        if 'good_id' in items:
            q = q.where(TBanner.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TBanner.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TBanner.good_id <= items['good_id_end'])
        
        if 'ban_label' in items:
            q = q.where(TBanner.ban_label == items['ban_label'])
        if 'ban_label_start' in items:
            q = q.where(TBanner.ban_label >= items['ban_label_start'])
        if 'ban_label_end' in items:
            q = q.where(TBanner.ban_label <= items['ban_label_end'])
        
        if 'type_id' in items:
            q = q.where(TBanner.type_id == items['type_id'])
        if 'type_id_start' in items:
            q = q.where(TBanner.type_id >= items['type_id_start'])
        if 'type_id_end' in items:
            q = q.where(TBanner.type_id <= items['type_id_end'])
        
        if 'good_spec_id' in items:
            q = q.where(TBanner.good_spec_id == items['good_spec_id'])
        if 'good_spec_id_start' in items:
            q = q.where(TBanner.good_spec_id >= items['good_spec_id_start'])
        if 'good_spec_id_end' in items:
            q = q.where(TBanner.good_spec_id <= items['good_spec_id_end'])
        

        if 'id' in set_items:
            q = q.where(TBanner.id.in_(set_items['id']))
        
        if 'image' in set_items:
            q = q.where(TBanner.image.in_(set_items['image']))
        
        if 'title' in set_items:
            q = q.where(TBanner.title.in_(set_items['title']))
        
        if 'subtitle' in set_items:
            q = q.where(TBanner.subtitle.in_(set_items['subtitle']))
        
        if 'width' in set_items:
            q = q.where(TBanner.width.in_(set_items['width']))
        
        if 'height' in set_items:
            q = q.where(TBanner.height.in_(set_items['height']))
        
        if 'create_time' in set_items:
            q = q.where(TBanner.create_time.in_(set_items['create_time']))
        
        if 'description' in set_items:
            q = q.where(TBanner.description.in_(set_items['description']))
        
        if 'good_id' in set_items:
            q = q.where(TBanner.good_id.in_(set_items['good_id']))
        
        if 'ban_label' in set_items:
            q = q.where(TBanner.ban_label.in_(set_items['ban_label']))
        
        if 'type_id' in set_items:
            q = q.where(TBanner.type_id.in_(set_items['type_id']))
        
        if 'good_spec_id' in set_items:
            q = q.where(TBanner.good_spec_id.in_(set_items['good_spec_id']))
        

        if 'image' in search_items:
            q = q.where(TBanner.image.like(search_items['image']))
        
        if 'title' in search_items:
            q = q.where(TBanner.title.like(search_items['title']))
        
        if 'subtitle' in search_items:
            q = q.where(TBanner.subtitle.like(search_items['subtitle']))
        
        if 'description' in search_items:
            q = q.where(TBanner.description.like(search_items['description']))
        
        if 'ban_label' in search_items:
            q = q.where(TBanner.ban_label.like(search_items['ban_label']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TBanner.good_spec_id.asc())
                orders.append(TBanner.id.asc())
            elif val == 'desc':
                #orders.append(TBanner.good_spec_id.desc())
                orders.append(TBanner.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_banner_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SBanner.parse_obj(t.__dict__) for t in t_banner_list]


def filter_count_banner(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TBanner)


        if 'id' in items:
            q = q.where(TBanner.id == items['id'])
        if 'id_start' in items:
            q = q.where(TBanner.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TBanner.id <= items['id_end'])
        
        if 'image' in items:
            q = q.where(TBanner.image == items['image'])
        if 'image_start' in items:
            q = q.where(TBanner.image >= items['image_start'])
        if 'image_end' in items:
            q = q.where(TBanner.image <= items['image_end'])
        
        if 'title' in items:
            q = q.where(TBanner.title == items['title'])
        if 'title_start' in items:
            q = q.where(TBanner.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TBanner.title <= items['title_end'])
        
        if 'subtitle' in items:
            q = q.where(TBanner.subtitle == items['subtitle'])
        if 'subtitle_start' in items:
            q = q.where(TBanner.subtitle >= items['subtitle_start'])
        if 'subtitle_end' in items:
            q = q.where(TBanner.subtitle <= items['subtitle_end'])
        
        if 'width' in items:
            q = q.where(TBanner.width == items['width'])
        if 'width_start' in items:
            q = q.where(TBanner.width >= items['width_start'])
        if 'width_end' in items:
            q = q.where(TBanner.width <= items['width_end'])
        
        if 'height' in items:
            q = q.where(TBanner.height == items['height'])
        if 'height_start' in items:
            q = q.where(TBanner.height >= items['height_start'])
        if 'height_end' in items:
            q = q.where(TBanner.height <= items['height_end'])
        
        if 'create_time' in items:
            q = q.where(TBanner.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TBanner.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TBanner.create_time <= items['create_time_end'])
        
        if 'description' in items:
            q = q.where(TBanner.description == items['description'])
        if 'description_start' in items:
            q = q.where(TBanner.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TBanner.description <= items['description_end'])
        
        if 'good_id' in items:
            q = q.where(TBanner.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TBanner.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TBanner.good_id <= items['good_id_end'])
        
        if 'ban_label' in items:
            q = q.where(TBanner.ban_label == items['ban_label'])
        if 'ban_label_start' in items:
            q = q.where(TBanner.ban_label >= items['ban_label_start'])
        if 'ban_label_end' in items:
            q = q.where(TBanner.ban_label <= items['ban_label_end'])
        
        if 'type_id' in items:
            q = q.where(TBanner.type_id == items['type_id'])
        if 'type_id_start' in items:
            q = q.where(TBanner.type_id >= items['type_id_start'])
        if 'type_id_end' in items:
            q = q.where(TBanner.type_id <= items['type_id_end'])
        
        if 'good_spec_id' in items:
            q = q.where(TBanner.good_spec_id == items['good_spec_id'])
        if 'good_spec_id_start' in items:
            q = q.where(TBanner.good_spec_id >= items['good_spec_id_start'])
        if 'good_spec_id_end' in items:
            q = q.where(TBanner.good_spec_id <= items['good_spec_id_end'])
        

        if 'id' in set_items:
            q = q.where(TBanner.id.in_(set_items['id']))
        
        if 'image' in set_items:
            q = q.where(TBanner.image.in_(set_items['image']))
        
        if 'title' in set_items:
            q = q.where(TBanner.title.in_(set_items['title']))
        
        if 'subtitle' in set_items:
            q = q.where(TBanner.subtitle.in_(set_items['subtitle']))
        
        if 'width' in set_items:
            q = q.where(TBanner.width.in_(set_items['width']))
        
        if 'height' in set_items:
            q = q.where(TBanner.height.in_(set_items['height']))
        
        if 'create_time' in set_items:
            q = q.where(TBanner.create_time.in_(set_items['create_time']))
        
        if 'description' in set_items:
            q = q.where(TBanner.description.in_(set_items['description']))
        
        if 'good_id' in set_items:
            q = q.where(TBanner.good_id.in_(set_items['good_id']))
        
        if 'ban_label' in set_items:
            q = q.where(TBanner.ban_label.in_(set_items['ban_label']))
        
        if 'type_id' in set_items:
            q = q.where(TBanner.type_id.in_(set_items['type_id']))
        
        if 'good_spec_id' in set_items:
            q = q.where(TBanner.good_spec_id.in_(set_items['good_spec_id']))
        

        if 'image' in search_items:
            q = q.where(TBanner.image.like(search_items['image']))
        
        if 'title' in search_items:
            q = q.where(TBanner.title.like(search_items['title']))
        
        if 'subtitle' in search_items:
            q = q.where(TBanner.subtitle.like(search_items['subtitle']))
        
        if 'description' in search_items:
            q = q.where(TBanner.description.like(search_items['description']))
        
        if 'ban_label' in search_items:
            q = q.where(TBanner.ban_label.like(search_items['ban_label']))
        
    
        c = q.count()
        return c

    
def insert_cart(item: CreateCart, db: Optional[SessionLocal] = None) -> SCart:
    data = model2dict(item)
    t = TCart(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SCart.parse_obj(t.__dict__)

    
def delete_cart(cart_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TCart).where(TCart.id == cart_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TCart).where(TCart.id == cart_id).delete()
        db.commit()

    
def update_cart(item: SCart, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TCart).where(TCart.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TCart).where(TCart.id == item.id).update(data)
        db.commit()

    
def get_cart(cart_id: int) -> Optional[SCart]:
    with Dao() as db:
        t = db.query(TCart).where(TCart.id == cart_id).first()
        if t:
            return SCart.parse_obj(t.__dict__)
        else:
            return None


def filter_cart(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SCart]:
    with Dao() as db:
        q = db.query(TCart)


        if 'id' in items:
            q = q.where(TCart.id == items['id'])
        if 'id_start' in items:
            q = q.where(TCart.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TCart.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TCart.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TCart.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TCart.user_id <= items['user_id_end'])
        
        if 'good_id' in items:
            q = q.where(TCart.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TCart.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TCart.good_id <= items['good_id_end'])
        
        if 'amount' in items:
            q = q.where(TCart.amount == items['amount'])
        if 'amount_start' in items:
            q = q.where(TCart.amount >= items['amount_start'])
        if 'amount_end' in items:
            q = q.where(TCart.amount <= items['amount_end'])
        
        if 'creat_time' in items:
            q = q.where(TCart.creat_time == items['creat_time'])
        if 'creat_time_start' in items:
            q = q.where(TCart.creat_time >= items['creat_time_start'])
        if 'creat_time_end' in items:
            q = q.where(TCart.creat_time <= items['creat_time_end'])
        
        if 'good_spec_id' in items:
            q = q.where(TCart.good_spec_id == items['good_spec_id'])
        if 'good_spec_id_start' in items:
            q = q.where(TCart.good_spec_id >= items['good_spec_id_start'])
        if 'good_spec_id_end' in items:
            q = q.where(TCart.good_spec_id <= items['good_spec_id_end'])
        

        if 'id' in set_items:
            q = q.where(TCart.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TCart.user_id.in_(set_items['user_id']))
        
        if 'good_id' in set_items:
            q = q.where(TCart.good_id.in_(set_items['good_id']))
        
        if 'amount' in set_items:
            q = q.where(TCart.amount.in_(set_items['amount']))
        
        if 'creat_time' in set_items:
            q = q.where(TCart.creat_time.in_(set_items['creat_time']))
        
        if 'good_spec_id' in set_items:
            q = q.where(TCart.good_spec_id.in_(set_items['good_spec_id']))
        

    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TCart.good_spec_id.asc())
                orders.append(TCart.id.asc())
            elif val == 'desc':
                #orders.append(TCart.good_spec_id.desc())
                orders.append(TCart.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_cart_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SCart.parse_obj(t.__dict__) for t in t_cart_list]


def filter_count_cart(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TCart)


        if 'id' in items:
            q = q.where(TCart.id == items['id'])
        if 'id_start' in items:
            q = q.where(TCart.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TCart.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TCart.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TCart.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TCart.user_id <= items['user_id_end'])
        
        if 'good_id' in items:
            q = q.where(TCart.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TCart.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TCart.good_id <= items['good_id_end'])
        
        if 'amount' in items:
            q = q.where(TCart.amount == items['amount'])
        if 'amount_start' in items:
            q = q.where(TCart.amount >= items['amount_start'])
        if 'amount_end' in items:
            q = q.where(TCart.amount <= items['amount_end'])
        
        if 'creat_time' in items:
            q = q.where(TCart.creat_time == items['creat_time'])
        if 'creat_time_start' in items:
            q = q.where(TCart.creat_time >= items['creat_time_start'])
        if 'creat_time_end' in items:
            q = q.where(TCart.creat_time <= items['creat_time_end'])
        
        if 'good_spec_id' in items:
            q = q.where(TCart.good_spec_id == items['good_spec_id'])
        if 'good_spec_id_start' in items:
            q = q.where(TCart.good_spec_id >= items['good_spec_id_start'])
        if 'good_spec_id_end' in items:
            q = q.where(TCart.good_spec_id <= items['good_spec_id_end'])
        

        if 'id' in set_items:
            q = q.where(TCart.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TCart.user_id.in_(set_items['user_id']))
        
        if 'good_id' in set_items:
            q = q.where(TCart.good_id.in_(set_items['good_id']))
        
        if 'amount' in set_items:
            q = q.where(TCart.amount.in_(set_items['amount']))
        
        if 'creat_time' in set_items:
            q = q.where(TCart.creat_time.in_(set_items['creat_time']))
        
        if 'good_spec_id' in set_items:
            q = q.where(TCart.good_spec_id.in_(set_items['good_spec_id']))
        

    
        c = q.count()
        return c

    
def insert_category(item: CreateCategory, db: Optional[SessionLocal] = None) -> SCategory:
    data = model2dict(item)
    t = TCategory(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SCategory.parse_obj(t.__dict__)

    
def delete_category(category_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TCategory).where(TCategory.id == category_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TCategory).where(TCategory.id == category_id).delete()
        db.commit()

    
def update_category(item: SCategory, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TCategory).where(TCategory.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TCategory).where(TCategory.id == item.id).update(data)
        db.commit()

    
def get_category(category_id: int) -> Optional[SCategory]:
    with Dao() as db:
        t = db.query(TCategory).where(TCategory.id == category_id).first()
        if t:
            return SCategory.parse_obj(t.__dict__)
        else:
            return None


def filter_category(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SCategory]:
    with Dao() as db:
        q = db.query(TCategory)


        if 'id' in items:
            q = q.where(TCategory.id == items['id'])
        if 'id_start' in items:
            q = q.where(TCategory.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TCategory.id <= items['id_end'])
        
        if 'cname' in items:
            q = q.where(TCategory.cname == items['cname'])
        if 'cname_start' in items:
            q = q.where(TCategory.cname >= items['cname_start'])
        if 'cname_end' in items:
            q = q.where(TCategory.cname <= items['cname_end'])
        
        if 'parent_category_id' in items:
            q = q.where(TCategory.parent_category_id == items['parent_category_id'])
        if 'parent_category_id_start' in items:
            q = q.where(TCategory.parent_category_id >= items['parent_category_id_start'])
        if 'parent_category_id_end' in items:
            q = q.where(TCategory.parent_category_id <= items['parent_category_id_end'])
        

        if 'id' in set_items:
            q = q.where(TCategory.id.in_(set_items['id']))
        
        if 'cname' in set_items:
            q = q.where(TCategory.cname.in_(set_items['cname']))
        
        if 'parent_category_id' in set_items:
            q = q.where(TCategory.parent_category_id.in_(set_items['parent_category_id']))
        

        if 'cname' in search_items:
            q = q.where(TCategory.cname.like(search_items['cname']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TCategory.parent_category_id.asc())
                orders.append(TCategory.id.asc())
            elif val == 'desc':
                #orders.append(TCategory.parent_category_id.desc())
                orders.append(TCategory.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_category_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SCategory.parse_obj(t.__dict__) for t in t_category_list]


def filter_count_category(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TCategory)


        if 'id' in items:
            q = q.where(TCategory.id == items['id'])
        if 'id_start' in items:
            q = q.where(TCategory.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TCategory.id <= items['id_end'])
        
        if 'cname' in items:
            q = q.where(TCategory.cname == items['cname'])
        if 'cname_start' in items:
            q = q.where(TCategory.cname >= items['cname_start'])
        if 'cname_end' in items:
            q = q.where(TCategory.cname <= items['cname_end'])
        
        if 'parent_category_id' in items:
            q = q.where(TCategory.parent_category_id == items['parent_category_id'])
        if 'parent_category_id_start' in items:
            q = q.where(TCategory.parent_category_id >= items['parent_category_id_start'])
        if 'parent_category_id_end' in items:
            q = q.where(TCategory.parent_category_id <= items['parent_category_id_end'])
        

        if 'id' in set_items:
            q = q.where(TCategory.id.in_(set_items['id']))
        
        if 'cname' in set_items:
            q = q.where(TCategory.cname.in_(set_items['cname']))
        
        if 'parent_category_id' in set_items:
            q = q.where(TCategory.parent_category_id.in_(set_items['parent_category_id']))
        

        if 'cname' in search_items:
            q = q.where(TCategory.cname.like(search_items['cname']))
        
    
        c = q.count()
        return c

    
def insert_city(item: CreateCity, db: Optional[SessionLocal] = None) -> SCity:
    data = model2dict(item)
    t = TCity(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SCity.parse_obj(t.__dict__)

    
def delete_city(city_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TCity).where(TCity.id == city_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TCity).where(TCity.id == city_id).delete()
        db.commit()

    
def update_city(item: SCity, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TCity).where(TCity.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TCity).where(TCity.id == item.id).update(data)
        db.commit()

    
def get_city(city_id: int) -> Optional[SCity]:
    with Dao() as db:
        t = db.query(TCity).where(TCity.id == city_id).first()
        if t:
            return SCity.parse_obj(t.__dict__)
        else:
            return None


def filter_city(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SCity]:
    with Dao() as db:
        q = db.query(TCity)


        if 'id' in items:
            q = q.where(TCity.id == items['id'])
        if 'id_start' in items:
            q = q.where(TCity.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TCity.id <= items['id_end'])
        
        if 'cname' in items:
            q = q.where(TCity.cname == items['cname'])
        if 'cname_start' in items:
            q = q.where(TCity.cname >= items['cname_start'])
        if 'cname_end' in items:
            q = q.where(TCity.cname <= items['cname_end'])
        
        if 'parid' in items:
            q = q.where(TCity.parid == items['parid'])
        if 'parid_start' in items:
            q = q.where(TCity.parid >= items['parid_start'])
        if 'parid_end' in items:
            q = q.where(TCity.parid <= items['parid_end'])
        
        if 'status' in items:
            q = q.where(TCity.status == items['status'])
        if 'status_start' in items:
            q = q.where(TCity.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TCity.status <= items['status_end'])
        

        if 'id' in set_items:
            q = q.where(TCity.id.in_(set_items['id']))
        
        if 'cname' in set_items:
            q = q.where(TCity.cname.in_(set_items['cname']))
        
        if 'parid' in set_items:
            q = q.where(TCity.parid.in_(set_items['parid']))
        
        if 'status' in set_items:
            q = q.where(TCity.status.in_(set_items['status']))
        

        if 'cname' in search_items:
            q = q.where(TCity.cname.like(search_items['cname']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TCity.status.asc())
                orders.append(TCity.id.asc())
            elif val == 'desc':
                #orders.append(TCity.status.desc())
                orders.append(TCity.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_city_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SCity.parse_obj(t.__dict__) for t in t_city_list]


def filter_count_city(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TCity)


        if 'id' in items:
            q = q.where(TCity.id == items['id'])
        if 'id_start' in items:
            q = q.where(TCity.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TCity.id <= items['id_end'])
        
        if 'cname' in items:
            q = q.where(TCity.cname == items['cname'])
        if 'cname_start' in items:
            q = q.where(TCity.cname >= items['cname_start'])
        if 'cname_end' in items:
            q = q.where(TCity.cname <= items['cname_end'])
        
        if 'parid' in items:
            q = q.where(TCity.parid == items['parid'])
        if 'parid_start' in items:
            q = q.where(TCity.parid >= items['parid_start'])
        if 'parid_end' in items:
            q = q.where(TCity.parid <= items['parid_end'])
        
        if 'status' in items:
            q = q.where(TCity.status == items['status'])
        if 'status_start' in items:
            q = q.where(TCity.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TCity.status <= items['status_end'])
        

        if 'id' in set_items:
            q = q.where(TCity.id.in_(set_items['id']))
        
        if 'cname' in set_items:
            q = q.where(TCity.cname.in_(set_items['cname']))
        
        if 'parid' in set_items:
            q = q.where(TCity.parid.in_(set_items['parid']))
        
        if 'status' in set_items:
            q = q.where(TCity.status.in_(set_items['status']))
        

        if 'cname' in search_items:
            q = q.where(TCity.cname.like(search_items['cname']))
        
    
        c = q.count()
        return c

    
def insert_coin(item: CreateCoin, db: Optional[SessionLocal] = None) -> SCoin:
    data = model2dict(item)
    t = TCoin(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SCoin.parse_obj(t.__dict__)

    
def delete_coin(coin_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TCoin).where(TCoin.id == coin_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TCoin).where(TCoin.id == coin_id).delete()
        db.commit()

    
def update_coin(item: SCoin, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TCoin).where(TCoin.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TCoin).where(TCoin.id == item.id).update(data)
        db.commit()

    
def get_coin(coin_id: int) -> Optional[SCoin]:
    with Dao() as db:
        t = db.query(TCoin).where(TCoin.id == coin_id).first()
        if t:
            return SCoin.parse_obj(t.__dict__)
        else:
            return None


def filter_coin(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SCoin]:
    with Dao() as db:
        q = db.query(TCoin)


        if 'id' in items:
            q = q.where(TCoin.id == items['id'])
        if 'id_start' in items:
            q = q.where(TCoin.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TCoin.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TCoin.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TCoin.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TCoin.user_id <= items['user_id_end'])
        
        if 'change' in items:
            q = q.where(TCoin.change == items['change'])
        if 'change_start' in items:
            q = q.where(TCoin.change >= items['change_start'])
        if 'change_end' in items:
            q = q.where(TCoin.change <= items['change_end'])
        
        if 'coin' in items:
            q = q.where(TCoin.coin == items['coin'])
        if 'coin_start' in items:
            q = q.where(TCoin.coin >= items['coin_start'])
        if 'coin_end' in items:
            q = q.where(TCoin.coin <= items['coin_end'])
        
        if 'type' in items:
            q = q.where(TCoin.type == items['type'])
        if 'type_start' in items:
            q = q.where(TCoin.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TCoin.type <= items['type_end'])
        
        if 'description' in items:
            q = q.where(TCoin.description == items['description'])
        if 'description_start' in items:
            q = q.where(TCoin.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TCoin.description <= items['description_end'])
        
        if 'create_time' in items:
            q = q.where(TCoin.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TCoin.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TCoin.create_time <= items['create_time_end'])
        
        if 'out_trade_no' in items:
            q = q.where(TCoin.out_trade_no == items['out_trade_no'])
        if 'out_trade_no_start' in items:
            q = q.where(TCoin.out_trade_no >= items['out_trade_no_start'])
        if 'out_trade_no_end' in items:
            q = q.where(TCoin.out_trade_no <= items['out_trade_no_end'])
        

        if 'id' in set_items:
            q = q.where(TCoin.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TCoin.user_id.in_(set_items['user_id']))
        
        if 'change' in set_items:
            q = q.where(TCoin.change.in_(set_items['change']))
        
        if 'coin' in set_items:
            q = q.where(TCoin.coin.in_(set_items['coin']))
        
        if 'type' in set_items:
            q = q.where(TCoin.type.in_(set_items['type']))
        
        if 'description' in set_items:
            q = q.where(TCoin.description.in_(set_items['description']))
        
        if 'create_time' in set_items:
            q = q.where(TCoin.create_time.in_(set_items['create_time']))
        
        if 'out_trade_no' in set_items:
            q = q.where(TCoin.out_trade_no.in_(set_items['out_trade_no']))
        

        if 'type' in search_items:
            q = q.where(TCoin.type.like(search_items['type']))
        
        if 'description' in search_items:
            q = q.where(TCoin.description.like(search_items['description']))
        
        if 'out_trade_no' in search_items:
            q = q.where(TCoin.out_trade_no.like(search_items['out_trade_no']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TCoin.out_trade_no.asc())
                orders.append(TCoin.id.asc())
            elif val == 'desc':
                #orders.append(TCoin.out_trade_no.desc())
                orders.append(TCoin.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_coin_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SCoin.parse_obj(t.__dict__) for t in t_coin_list]


def filter_count_coin(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TCoin)


        if 'id' in items:
            q = q.where(TCoin.id == items['id'])
        if 'id_start' in items:
            q = q.where(TCoin.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TCoin.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TCoin.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TCoin.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TCoin.user_id <= items['user_id_end'])
        
        if 'change' in items:
            q = q.where(TCoin.change == items['change'])
        if 'change_start' in items:
            q = q.where(TCoin.change >= items['change_start'])
        if 'change_end' in items:
            q = q.where(TCoin.change <= items['change_end'])
        
        if 'coin' in items:
            q = q.where(TCoin.coin == items['coin'])
        if 'coin_start' in items:
            q = q.where(TCoin.coin >= items['coin_start'])
        if 'coin_end' in items:
            q = q.where(TCoin.coin <= items['coin_end'])
        
        if 'type' in items:
            q = q.where(TCoin.type == items['type'])
        if 'type_start' in items:
            q = q.where(TCoin.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TCoin.type <= items['type_end'])
        
        if 'description' in items:
            q = q.where(TCoin.description == items['description'])
        if 'description_start' in items:
            q = q.where(TCoin.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TCoin.description <= items['description_end'])
        
        if 'create_time' in items:
            q = q.where(TCoin.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TCoin.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TCoin.create_time <= items['create_time_end'])
        
        if 'out_trade_no' in items:
            q = q.where(TCoin.out_trade_no == items['out_trade_no'])
        if 'out_trade_no_start' in items:
            q = q.where(TCoin.out_trade_no >= items['out_trade_no_start'])
        if 'out_trade_no_end' in items:
            q = q.where(TCoin.out_trade_no <= items['out_trade_no_end'])
        

        if 'id' in set_items:
            q = q.where(TCoin.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TCoin.user_id.in_(set_items['user_id']))
        
        if 'change' in set_items:
            q = q.where(TCoin.change.in_(set_items['change']))
        
        if 'coin' in set_items:
            q = q.where(TCoin.coin.in_(set_items['coin']))
        
        if 'type' in set_items:
            q = q.where(TCoin.type.in_(set_items['type']))
        
        if 'description' in set_items:
            q = q.where(TCoin.description.in_(set_items['description']))
        
        if 'create_time' in set_items:
            q = q.where(TCoin.create_time.in_(set_items['create_time']))
        
        if 'out_trade_no' in set_items:
            q = q.where(TCoin.out_trade_no.in_(set_items['out_trade_no']))
        

        if 'type' in search_items:
            q = q.where(TCoin.type.like(search_items['type']))
        
        if 'description' in search_items:
            q = q.where(TCoin.description.like(search_items['description']))
        
        if 'out_trade_no' in search_items:
            q = q.where(TCoin.out_trade_no.like(search_items['out_trade_no']))
        
    
        c = q.count()
        return c

    
def insert_combo(item: CreateCombo, db: Optional[SessionLocal] = None) -> SCombo:
    data = model2dict(item)
    t = TCombo(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SCombo.parse_obj(t.__dict__)

    
def delete_combo(combo_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TCombo).where(TCombo.id == combo_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TCombo).where(TCombo.id == combo_id).delete()
        db.commit()

    
def update_combo(item: SCombo, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TCombo).where(TCombo.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TCombo).where(TCombo.id == item.id).update(data)
        db.commit()

    
def get_combo(combo_id: int) -> Optional[SCombo]:
    with Dao() as db:
        t = db.query(TCombo).where(TCombo.id == combo_id).first()
        if t:
            return SCombo.parse_obj(t.__dict__)
        else:
            return None


def filter_combo(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SCombo]:
    with Dao() as db:
        q = db.query(TCombo)


        if 'id' in items:
            q = q.where(TCombo.id == items['id'])
        if 'id_start' in items:
            q = q.where(TCombo.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TCombo.id <= items['id_end'])
        
        if 'good_id' in items:
            q = q.where(TCombo.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TCombo.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TCombo.good_id <= items['good_id_end'])
        
        if 'title' in items:
            q = q.where(TCombo.title == items['title'])
        if 'title_start' in items:
            q = q.where(TCombo.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TCombo.title <= items['title_end'])
        
        if 'amount' in items:
            q = q.where(TCombo.amount == items['amount'])
        if 'amount_start' in items:
            q = q.where(TCombo.amount >= items['amount_start'])
        if 'amount_end' in items:
            q = q.where(TCombo.amount <= items['amount_end'])
        
        if 'price' in items:
            q = q.where(TCombo.price == items['price'])
        if 'price_start' in items:
            q = q.where(TCombo.price >= items['price_start'])
        if 'price_end' in items:
            q = q.where(TCombo.price <= items['price_end'])
        

        if 'id' in set_items:
            q = q.where(TCombo.id.in_(set_items['id']))
        
        if 'good_id' in set_items:
            q = q.where(TCombo.good_id.in_(set_items['good_id']))
        
        if 'title' in set_items:
            q = q.where(TCombo.title.in_(set_items['title']))
        
        if 'amount' in set_items:
            q = q.where(TCombo.amount.in_(set_items['amount']))
        
        if 'price' in set_items:
            q = q.where(TCombo.price.in_(set_items['price']))
        

        if 'title' in search_items:
            q = q.where(TCombo.title.like(search_items['title']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TCombo.price.asc())
                orders.append(TCombo.id.asc())
            elif val == 'desc':
                #orders.append(TCombo.price.desc())
                orders.append(TCombo.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_combo_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SCombo.parse_obj(t.__dict__) for t in t_combo_list]


def filter_count_combo(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TCombo)


        if 'id' in items:
            q = q.where(TCombo.id == items['id'])
        if 'id_start' in items:
            q = q.where(TCombo.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TCombo.id <= items['id_end'])
        
        if 'good_id' in items:
            q = q.where(TCombo.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TCombo.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TCombo.good_id <= items['good_id_end'])
        
        if 'title' in items:
            q = q.where(TCombo.title == items['title'])
        if 'title_start' in items:
            q = q.where(TCombo.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TCombo.title <= items['title_end'])
        
        if 'amount' in items:
            q = q.where(TCombo.amount == items['amount'])
        if 'amount_start' in items:
            q = q.where(TCombo.amount >= items['amount_start'])
        if 'amount_end' in items:
            q = q.where(TCombo.amount <= items['amount_end'])
        
        if 'price' in items:
            q = q.where(TCombo.price == items['price'])
        if 'price_start' in items:
            q = q.where(TCombo.price >= items['price_start'])
        if 'price_end' in items:
            q = q.where(TCombo.price <= items['price_end'])
        

        if 'id' in set_items:
            q = q.where(TCombo.id.in_(set_items['id']))
        
        if 'good_id' in set_items:
            q = q.where(TCombo.good_id.in_(set_items['good_id']))
        
        if 'title' in set_items:
            q = q.where(TCombo.title.in_(set_items['title']))
        
        if 'amount' in set_items:
            q = q.where(TCombo.amount.in_(set_items['amount']))
        
        if 'price' in set_items:
            q = q.where(TCombo.price.in_(set_items['price']))
        

        if 'title' in search_items:
            q = q.where(TCombo.title.like(search_items['title']))
        
    
        c = q.count()
        return c

    
def insert_delivery_rule(item: CreateDeliveryRule, db: Optional[SessionLocal] = None) -> SDeliveryRule:
    data = model2dict(item)
    t = TDeliveryRule(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SDeliveryRule.parse_obj(t.__dict__)

    
def delete_delivery_rule(delivery_rule_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TDeliveryRule).where(TDeliveryRule.id == delivery_rule_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TDeliveryRule).where(TDeliveryRule.id == delivery_rule_id).delete()
        db.commit()

    
def update_delivery_rule(item: SDeliveryRule, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TDeliveryRule).where(TDeliveryRule.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TDeliveryRule).where(TDeliveryRule.id == item.id).update(data)
        db.commit()

    
def get_delivery_rule(delivery_rule_id: int) -> Optional[SDeliveryRule]:
    with Dao() as db:
        t = db.query(TDeliveryRule).where(TDeliveryRule.id == delivery_rule_id).first()
        if t:
            return SDeliveryRule.parse_obj(t.__dict__)
        else:
            return None


def filter_delivery_rule(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SDeliveryRule]:
    with Dao() as db:
        q = db.query(TDeliveryRule)


        if 'id' in items:
            q = q.where(TDeliveryRule.id == items['id'])
        if 'id_start' in items:
            q = q.where(TDeliveryRule.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TDeliveryRule.id <= items['id_end'])
        
        if 'good_id' in items:
            q = q.where(TDeliveryRule.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TDeliveryRule.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TDeliveryRule.good_id <= items['good_id_end'])
        
        if 'spec_id' in items:
            q = q.where(TDeliveryRule.spec_id == items['spec_id'])
        if 'spec_id_start' in items:
            q = q.where(TDeliveryRule.spec_id >= items['spec_id_start'])
        if 'spec_id_end' in items:
            q = q.where(TDeliveryRule.spec_id <= items['spec_id_end'])
        
        if 'province' in items:
            q = q.where(TDeliveryRule.province == items['province'])
        if 'province_start' in items:
            q = q.where(TDeliveryRule.province >= items['province_start'])
        if 'province_end' in items:
            q = q.where(TDeliveryRule.province <= items['province_end'])
        
        if 'city' in items:
            q = q.where(TDeliveryRule.city == items['city'])
        if 'city_start' in items:
            q = q.where(TDeliveryRule.city >= items['city_start'])
        if 'city_end' in items:
            q = q.where(TDeliveryRule.city <= items['city_end'])
        
        if 'area' in items:
            q = q.where(TDeliveryRule.area == items['area'])
        if 'area_start' in items:
            q = q.where(TDeliveryRule.area >= items['area_start'])
        if 'area_end' in items:
            q = q.where(TDeliveryRule.area <= items['area_end'])
        
        if 'is_reachable' in items:
            q = q.where(TDeliveryRule.is_reachable == items['is_reachable'])
        if 'is_reachable_start' in items:
            q = q.where(TDeliveryRule.is_reachable >= items['is_reachable_start'])
        if 'is_reachable_end' in items:
            q = q.where(TDeliveryRule.is_reachable <= items['is_reachable_end'])
        
        if 'delivery_fee' in items:
            q = q.where(TDeliveryRule.delivery_fee == items['delivery_fee'])
        if 'delivery_fee_start' in items:
            q = q.where(TDeliveryRule.delivery_fee >= items['delivery_fee_start'])
        if 'delivery_fee_end' in items:
            q = q.where(TDeliveryRule.delivery_fee <= items['delivery_fee_end'])
        

        if 'id' in set_items:
            q = q.where(TDeliveryRule.id.in_(set_items['id']))
        
        if 'good_id' in set_items:
            q = q.where(TDeliveryRule.good_id.in_(set_items['good_id']))
        
        if 'spec_id' in set_items:
            q = q.where(TDeliveryRule.spec_id.in_(set_items['spec_id']))
        
        if 'province' in set_items:
            q = q.where(TDeliveryRule.province.in_(set_items['province']))
        
        if 'city' in set_items:
            q = q.where(TDeliveryRule.city.in_(set_items['city']))
        
        if 'area' in set_items:
            q = q.where(TDeliveryRule.area.in_(set_items['area']))
        
        if 'is_reachable' in set_items:
            q = q.where(TDeliveryRule.is_reachable.in_(set_items['is_reachable']))
        
        if 'delivery_fee' in set_items:
            q = q.where(TDeliveryRule.delivery_fee.in_(set_items['delivery_fee']))
        

        if 'province' in search_items:
            q = q.where(TDeliveryRule.province.like(search_items['province']))
        
        if 'city' in search_items:
            q = q.where(TDeliveryRule.city.like(search_items['city']))
        
        if 'area' in search_items:
            q = q.where(TDeliveryRule.area.like(search_items['area']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TDeliveryRule.delivery_fee.asc())
                orders.append(TDeliveryRule.id.asc())
            elif val == 'desc':
                #orders.append(TDeliveryRule.delivery_fee.desc())
                orders.append(TDeliveryRule.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_delivery_rule_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SDeliveryRule.parse_obj(t.__dict__) for t in t_delivery_rule_list]


def filter_count_delivery_rule(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TDeliveryRule)


        if 'id' in items:
            q = q.where(TDeliveryRule.id == items['id'])
        if 'id_start' in items:
            q = q.where(TDeliveryRule.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TDeliveryRule.id <= items['id_end'])
        
        if 'good_id' in items:
            q = q.where(TDeliveryRule.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TDeliveryRule.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TDeliveryRule.good_id <= items['good_id_end'])
        
        if 'spec_id' in items:
            q = q.where(TDeliveryRule.spec_id == items['spec_id'])
        if 'spec_id_start' in items:
            q = q.where(TDeliveryRule.spec_id >= items['spec_id_start'])
        if 'spec_id_end' in items:
            q = q.where(TDeliveryRule.spec_id <= items['spec_id_end'])
        
        if 'province' in items:
            q = q.where(TDeliveryRule.province == items['province'])
        if 'province_start' in items:
            q = q.where(TDeliveryRule.province >= items['province_start'])
        if 'province_end' in items:
            q = q.where(TDeliveryRule.province <= items['province_end'])
        
        if 'city' in items:
            q = q.where(TDeliveryRule.city == items['city'])
        if 'city_start' in items:
            q = q.where(TDeliveryRule.city >= items['city_start'])
        if 'city_end' in items:
            q = q.where(TDeliveryRule.city <= items['city_end'])
        
        if 'area' in items:
            q = q.where(TDeliveryRule.area == items['area'])
        if 'area_start' in items:
            q = q.where(TDeliveryRule.area >= items['area_start'])
        if 'area_end' in items:
            q = q.where(TDeliveryRule.area <= items['area_end'])
        
        if 'is_reachable' in items:
            q = q.where(TDeliveryRule.is_reachable == items['is_reachable'])
        if 'is_reachable_start' in items:
            q = q.where(TDeliveryRule.is_reachable >= items['is_reachable_start'])
        if 'is_reachable_end' in items:
            q = q.where(TDeliveryRule.is_reachable <= items['is_reachable_end'])
        
        if 'delivery_fee' in items:
            q = q.where(TDeliveryRule.delivery_fee == items['delivery_fee'])
        if 'delivery_fee_start' in items:
            q = q.where(TDeliveryRule.delivery_fee >= items['delivery_fee_start'])
        if 'delivery_fee_end' in items:
            q = q.where(TDeliveryRule.delivery_fee <= items['delivery_fee_end'])
        

        if 'id' in set_items:
            q = q.where(TDeliveryRule.id.in_(set_items['id']))
        
        if 'good_id' in set_items:
            q = q.where(TDeliveryRule.good_id.in_(set_items['good_id']))
        
        if 'spec_id' in set_items:
            q = q.where(TDeliveryRule.spec_id.in_(set_items['spec_id']))
        
        if 'province' in set_items:
            q = q.where(TDeliveryRule.province.in_(set_items['province']))
        
        if 'city' in set_items:
            q = q.where(TDeliveryRule.city.in_(set_items['city']))
        
        if 'area' in set_items:
            q = q.where(TDeliveryRule.area.in_(set_items['area']))
        
        if 'is_reachable' in set_items:
            q = q.where(TDeliveryRule.is_reachable.in_(set_items['is_reachable']))
        
        if 'delivery_fee' in set_items:
            q = q.where(TDeliveryRule.delivery_fee.in_(set_items['delivery_fee']))
        

        if 'province' in search_items:
            q = q.where(TDeliveryRule.province.like(search_items['province']))
        
        if 'city' in search_items:
            q = q.where(TDeliveryRule.city.like(search_items['city']))
        
        if 'area' in search_items:
            q = q.where(TDeliveryRule.area.like(search_items['area']))
        
    
        c = q.count()
        return c

    
def insert_export_file(item: CreateExportFile, db: Optional[SessionLocal] = None) -> SExportFile:
    data = model2dict(item)
    t = TExportFile(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SExportFile.parse_obj(t.__dict__)

    
def delete_export_file(export_file_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TExportFile).where(TExportFile.id == export_file_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TExportFile).where(TExportFile.id == export_file_id).delete()
        db.commit()

    
def update_export_file(item: SExportFile, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TExportFile).where(TExportFile.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TExportFile).where(TExportFile.id == item.id).update(data)
        db.commit()

    
def get_export_file(export_file_id: int) -> Optional[SExportFile]:
    with Dao() as db:
        t = db.query(TExportFile).where(TExportFile.id == export_file_id).first()
        if t:
            return SExportFile.parse_obj(t.__dict__)
        else:
            return None


def filter_export_file(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SExportFile]:
    with Dao() as db:
        q = db.query(TExportFile)


        if 'id' in items:
            q = q.where(TExportFile.id == items['id'])
        if 'id_start' in items:
            q = q.where(TExportFile.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TExportFile.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TExportFile.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TExportFile.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TExportFile.user_id <= items['user_id_end'])
        
        if 'export_url' in items:
            q = q.where(TExportFile.export_url == items['export_url'])
        if 'export_url_start' in items:
            q = q.where(TExportFile.export_url >= items['export_url_start'])
        if 'export_url_end' in items:
            q = q.where(TExportFile.export_url <= items['export_url_end'])
        
        if 'type' in items:
            q = q.where(TExportFile.type == items['type'])
        if 'type_start' in items:
            q = q.where(TExportFile.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TExportFile.type <= items['type_end'])
        
        if 'description' in items:
            q = q.where(TExportFile.description == items['description'])
        if 'description_start' in items:
            q = q.where(TExportFile.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TExportFile.description <= items['description_end'])
        
        if 'create_time' in items:
            q = q.where(TExportFile.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TExportFile.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TExportFile.create_time <= items['create_time_end'])
        

        if 'id' in set_items:
            q = q.where(TExportFile.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TExportFile.user_id.in_(set_items['user_id']))
        
        if 'export_url' in set_items:
            q = q.where(TExportFile.export_url.in_(set_items['export_url']))
        
        if 'type' in set_items:
            q = q.where(TExportFile.type.in_(set_items['type']))
        
        if 'description' in set_items:
            q = q.where(TExportFile.description.in_(set_items['description']))
        
        if 'create_time' in set_items:
            q = q.where(TExportFile.create_time.in_(set_items['create_time']))
        

        if 'export_url' in search_items:
            q = q.where(TExportFile.export_url.like(search_items['export_url']))
        
        if 'type' in search_items:
            q = q.where(TExportFile.type.like(search_items['type']))
        
        if 'description' in search_items:
            q = q.where(TExportFile.description.like(search_items['description']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TExportFile.create_time.asc())
                orders.append(TExportFile.id.asc())
            elif val == 'desc':
                #orders.append(TExportFile.create_time.desc())
                orders.append(TExportFile.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_export_file_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SExportFile.parse_obj(t.__dict__) for t in t_export_file_list]


def filter_count_export_file(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TExportFile)


        if 'id' in items:
            q = q.where(TExportFile.id == items['id'])
        if 'id_start' in items:
            q = q.where(TExportFile.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TExportFile.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TExportFile.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TExportFile.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TExportFile.user_id <= items['user_id_end'])
        
        if 'export_url' in items:
            q = q.where(TExportFile.export_url == items['export_url'])
        if 'export_url_start' in items:
            q = q.where(TExportFile.export_url >= items['export_url_start'])
        if 'export_url_end' in items:
            q = q.where(TExportFile.export_url <= items['export_url_end'])
        
        if 'type' in items:
            q = q.where(TExportFile.type == items['type'])
        if 'type_start' in items:
            q = q.where(TExportFile.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TExportFile.type <= items['type_end'])
        
        if 'description' in items:
            q = q.where(TExportFile.description == items['description'])
        if 'description_start' in items:
            q = q.where(TExportFile.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TExportFile.description <= items['description_end'])
        
        if 'create_time' in items:
            q = q.where(TExportFile.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TExportFile.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TExportFile.create_time <= items['create_time_end'])
        

        if 'id' in set_items:
            q = q.where(TExportFile.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TExportFile.user_id.in_(set_items['user_id']))
        
        if 'export_url' in set_items:
            q = q.where(TExportFile.export_url.in_(set_items['export_url']))
        
        if 'type' in set_items:
            q = q.where(TExportFile.type.in_(set_items['type']))
        
        if 'description' in set_items:
            q = q.where(TExportFile.description.in_(set_items['description']))
        
        if 'create_time' in set_items:
            q = q.where(TExportFile.create_time.in_(set_items['create_time']))
        

        if 'export_url' in search_items:
            q = q.where(TExportFile.export_url.like(search_items['export_url']))
        
        if 'type' in search_items:
            q = q.where(TExportFile.type.like(search_items['type']))
        
        if 'description' in search_items:
            q = q.where(TExportFile.description.like(search_items['description']))
        
    
        c = q.count()
        return c

    
def insert_flash_order(item: CreateFlashOrder, db: Optional[SessionLocal] = None) -> SFlashOrder:
    data = model2dict(item)
    t = TFlashOrder(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SFlashOrder.parse_obj(t.__dict__)

    
def delete_flash_order(flash_order_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TFlashOrder).where(TFlashOrder.id == flash_order_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TFlashOrder).where(TFlashOrder.id == flash_order_id).delete()
        db.commit()

    
def update_flash_order(item: SFlashOrder, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TFlashOrder).where(TFlashOrder.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TFlashOrder).where(TFlashOrder.id == item.id).update(data)
        db.commit()

    
def get_flash_order(flash_order_id: int) -> Optional[SFlashOrder]:
    with Dao() as db:
        t = db.query(TFlashOrder).where(TFlashOrder.id == flash_order_id).first()
        if t:
            return SFlashOrder.parse_obj(t.__dict__)
        else:
            return None


def filter_flash_order(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SFlashOrder]:
    with Dao() as db:
        q = db.query(TFlashOrder)


        if 'id' in items:
            q = q.where(TFlashOrder.id == items['id'])
        if 'id_start' in items:
            q = q.where(TFlashOrder.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TFlashOrder.id <= items['id_end'])
        
        if 'package_id' in items:
            q = q.where(TFlashOrder.package_id == items['package_id'])
        if 'package_id_start' in items:
            q = q.where(TFlashOrder.package_id >= items['package_id_start'])
        if 'package_id_end' in items:
            q = q.where(TFlashOrder.package_id <= items['package_id_end'])
        
        if 'status' in items:
            q = q.where(TFlashOrder.status == items['status'])
        if 'status_start' in items:
            q = q.where(TFlashOrder.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TFlashOrder.status <= items['status_end'])
        
        if 'create_time' in items:
            q = q.where(TFlashOrder.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TFlashOrder.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TFlashOrder.create_time <= items['create_time_end'])
        
        if 'paid_time' in items:
            q = q.where(TFlashOrder.paid_time == items['paid_time'])
        if 'paid_time_start' in items:
            q = q.where(TFlashOrder.paid_time >= items['paid_time_start'])
        if 'paid_time_end' in items:
            q = q.where(TFlashOrder.paid_time <= items['paid_time_end'])
        
        if 'user_id' in items:
            q = q.where(TFlashOrder.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TFlashOrder.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TFlashOrder.user_id <= items['user_id_end'])
        
        if 'number' in items:
            q = q.where(TFlashOrder.number == items['number'])
        if 'number_start' in items:
            q = q.where(TFlashOrder.number >= items['number_start'])
        if 'number_end' in items:
            q = q.where(TFlashOrder.number <= items['number_end'])
        
        if 'flash_price' in items:
            q = q.where(TFlashOrder.flash_price == items['flash_price'])
        if 'flash_price_start' in items:
            q = q.where(TFlashOrder.flash_price >= items['flash_price_start'])
        if 'flash_price_end' in items:
            q = q.where(TFlashOrder.flash_price <= items['flash_price_end'])
        
        if 'flash_cost' in items:
            q = q.where(TFlashOrder.flash_cost == items['flash_cost'])
        if 'flash_cost_start' in items:
            q = q.where(TFlashOrder.flash_cost >= items['flash_cost_start'])
        if 'flash_cost_end' in items:
            q = q.where(TFlashOrder.flash_cost <= items['flash_cost_end'])
        
        if 'out_trade_no' in items:
            q = q.where(TFlashOrder.out_trade_no == items['out_trade_no'])
        if 'out_trade_no_start' in items:
            q = q.where(TFlashOrder.out_trade_no >= items['out_trade_no_start'])
        if 'out_trade_no_end' in items:
            q = q.where(TFlashOrder.out_trade_no <= items['out_trade_no_end'])
        
        if 'paid_amount' in items:
            q = q.where(TFlashOrder.paid_amount == items['paid_amount'])
        if 'paid_amount_start' in items:
            q = q.where(TFlashOrder.paid_amount >= items['paid_amount_start'])
        if 'paid_amount_end' in items:
            q = q.where(TFlashOrder.paid_amount <= items['paid_amount_end'])
        
        if 'paid_balance' in items:
            q = q.where(TFlashOrder.paid_balance == items['paid_balance'])
        if 'paid_balance_start' in items:
            q = q.where(TFlashOrder.paid_balance >= items['paid_balance_start'])
        if 'paid_balance_end' in items:
            q = q.where(TFlashOrder.paid_balance <= items['paid_balance_end'])
        
        if 'single_status' in items:
            q = q.where(TFlashOrder.single_status == items['single_status'])
        if 'single_status_start' in items:
            q = q.where(TFlashOrder.single_status >= items['single_status_start'])
        if 'single_status_end' in items:
            q = q.where(TFlashOrder.single_status <= items['single_status_end'])
        
        if 'sold' in items:
            q = q.where(TFlashOrder.sold == items['sold'])
        if 'sold_start' in items:
            q = q.where(TFlashOrder.sold >= items['sold_start'])
        if 'sold_end' in items:
            q = q.where(TFlashOrder.sold <= items['sold_end'])
        
        if 'whole_status' in items:
            q = q.where(TFlashOrder.whole_status == items['whole_status'])
        if 'whole_status_start' in items:
            q = q.where(TFlashOrder.whole_status >= items['whole_status_start'])
        if 'whole_status_end' in items:
            q = q.where(TFlashOrder.whole_status <= items['whole_status_end'])
        
        if 'spec_id' in items:
            q = q.where(TFlashOrder.spec_id == items['spec_id'])
        if 'spec_id_start' in items:
            q = q.where(TFlashOrder.spec_id >= items['spec_id_start'])
        if 'spec_id_end' in items:
            q = q.where(TFlashOrder.spec_id <= items['spec_id_end'])
        
        if 'put_on_time' in items:
            q = q.where(TFlashOrder.put_on_time == items['put_on_time'])
        if 'put_on_time_start' in items:
            q = q.where(TFlashOrder.put_on_time >= items['put_on_time_start'])
        if 'put_on_time_end' in items:
            q = q.where(TFlashOrder.put_on_time <= items['put_on_time_end'])
        
        if 'detail' in items:
            q = q.where(TFlashOrder.detail == items['detail'])
        if 'detail_start' in items:
            q = q.where(TFlashOrder.detail >= items['detail_start'])
        if 'detail_end' in items:
            q = q.where(TFlashOrder.detail <= items['detail_end'])
        
        if 'is_assign_income' in items:
            q = q.where(TFlashOrder.is_assign_income == items['is_assign_income'])
        if 'is_assign_income_start' in items:
            q = q.where(TFlashOrder.is_assign_income >= items['is_assign_income_start'])
        if 'is_assign_income_end' in items:
            q = q.where(TFlashOrder.is_assign_income <= items['is_assign_income_end'])
        
        if 'complete_time' in items:
            q = q.where(TFlashOrder.complete_time == items['complete_time'])
        if 'complete_time_start' in items:
            q = q.where(TFlashOrder.complete_time >= items['complete_time_start'])
        if 'complete_time_end' in items:
            q = q.where(TFlashOrder.complete_time <= items['complete_time_end'])
        
        if 'return_sold' in items:
            q = q.where(TFlashOrder.return_sold == items['return_sold'])
        if 'return_sold_start' in items:
            q = q.where(TFlashOrder.return_sold >= items['return_sold_start'])
        if 'return_sold_end' in items:
            q = q.where(TFlashOrder.return_sold <= items['return_sold_end'])
        

        if 'id' in set_items:
            q = q.where(TFlashOrder.id.in_(set_items['id']))
        
        if 'package_id' in set_items:
            q = q.where(TFlashOrder.package_id.in_(set_items['package_id']))
        
        if 'status' in set_items:
            q = q.where(TFlashOrder.status.in_(set_items['status']))
        
        if 'create_time' in set_items:
            q = q.where(TFlashOrder.create_time.in_(set_items['create_time']))
        
        if 'paid_time' in set_items:
            q = q.where(TFlashOrder.paid_time.in_(set_items['paid_time']))
        
        if 'user_id' in set_items:
            q = q.where(TFlashOrder.user_id.in_(set_items['user_id']))
        
        if 'number' in set_items:
            q = q.where(TFlashOrder.number.in_(set_items['number']))
        
        if 'flash_price' in set_items:
            q = q.where(TFlashOrder.flash_price.in_(set_items['flash_price']))
        
        if 'flash_cost' in set_items:
            q = q.where(TFlashOrder.flash_cost.in_(set_items['flash_cost']))
        
        if 'out_trade_no' in set_items:
            q = q.where(TFlashOrder.out_trade_no.in_(set_items['out_trade_no']))
        
        if 'paid_amount' in set_items:
            q = q.where(TFlashOrder.paid_amount.in_(set_items['paid_amount']))
        
        if 'paid_balance' in set_items:
            q = q.where(TFlashOrder.paid_balance.in_(set_items['paid_balance']))
        
        if 'single_status' in set_items:
            q = q.where(TFlashOrder.single_status.in_(set_items['single_status']))
        
        if 'sold' in set_items:
            q = q.where(TFlashOrder.sold.in_(set_items['sold']))
        
        if 'whole_status' in set_items:
            q = q.where(TFlashOrder.whole_status.in_(set_items['whole_status']))
        
        if 'spec_id' in set_items:
            q = q.where(TFlashOrder.spec_id.in_(set_items['spec_id']))
        
        if 'put_on_time' in set_items:
            q = q.where(TFlashOrder.put_on_time.in_(set_items['put_on_time']))
        
        if 'detail' in set_items:
            q = q.where(TFlashOrder.detail.in_(set_items['detail']))
        
        if 'is_assign_income' in set_items:
            q = q.where(TFlashOrder.is_assign_income.in_(set_items['is_assign_income']))
        
        if 'complete_time' in set_items:
            q = q.where(TFlashOrder.complete_time.in_(set_items['complete_time']))
        
        if 'return_sold' in set_items:
            q = q.where(TFlashOrder.return_sold.in_(set_items['return_sold']))
        

        if 'out_trade_no' in search_items:
            q = q.where(TFlashOrder.out_trade_no.like(search_items['out_trade_no']))
        
        if 'detail' in search_items:
            q = q.where(TFlashOrder.detail.like(search_items['detail']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TFlashOrder.return_sold.asc())
                orders.append(TFlashOrder.id.asc())
            elif val == 'desc':
                #orders.append(TFlashOrder.return_sold.desc())
                orders.append(TFlashOrder.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_flash_order_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SFlashOrder.parse_obj(t.__dict__) for t in t_flash_order_list]


def filter_count_flash_order(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TFlashOrder)


        if 'id' in items:
            q = q.where(TFlashOrder.id == items['id'])
        if 'id_start' in items:
            q = q.where(TFlashOrder.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TFlashOrder.id <= items['id_end'])
        
        if 'package_id' in items:
            q = q.where(TFlashOrder.package_id == items['package_id'])
        if 'package_id_start' in items:
            q = q.where(TFlashOrder.package_id >= items['package_id_start'])
        if 'package_id_end' in items:
            q = q.where(TFlashOrder.package_id <= items['package_id_end'])
        
        if 'status' in items:
            q = q.where(TFlashOrder.status == items['status'])
        if 'status_start' in items:
            q = q.where(TFlashOrder.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TFlashOrder.status <= items['status_end'])
        
        if 'create_time' in items:
            q = q.where(TFlashOrder.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TFlashOrder.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TFlashOrder.create_time <= items['create_time_end'])
        
        if 'paid_time' in items:
            q = q.where(TFlashOrder.paid_time == items['paid_time'])
        if 'paid_time_start' in items:
            q = q.where(TFlashOrder.paid_time >= items['paid_time_start'])
        if 'paid_time_end' in items:
            q = q.where(TFlashOrder.paid_time <= items['paid_time_end'])
        
        if 'user_id' in items:
            q = q.where(TFlashOrder.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TFlashOrder.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TFlashOrder.user_id <= items['user_id_end'])
        
        if 'number' in items:
            q = q.where(TFlashOrder.number == items['number'])
        if 'number_start' in items:
            q = q.where(TFlashOrder.number >= items['number_start'])
        if 'number_end' in items:
            q = q.where(TFlashOrder.number <= items['number_end'])
        
        if 'flash_price' in items:
            q = q.where(TFlashOrder.flash_price == items['flash_price'])
        if 'flash_price_start' in items:
            q = q.where(TFlashOrder.flash_price >= items['flash_price_start'])
        if 'flash_price_end' in items:
            q = q.where(TFlashOrder.flash_price <= items['flash_price_end'])
        
        if 'flash_cost' in items:
            q = q.where(TFlashOrder.flash_cost == items['flash_cost'])
        if 'flash_cost_start' in items:
            q = q.where(TFlashOrder.flash_cost >= items['flash_cost_start'])
        if 'flash_cost_end' in items:
            q = q.where(TFlashOrder.flash_cost <= items['flash_cost_end'])
        
        if 'out_trade_no' in items:
            q = q.where(TFlashOrder.out_trade_no == items['out_trade_no'])
        if 'out_trade_no_start' in items:
            q = q.where(TFlashOrder.out_trade_no >= items['out_trade_no_start'])
        if 'out_trade_no_end' in items:
            q = q.where(TFlashOrder.out_trade_no <= items['out_trade_no_end'])
        
        if 'paid_amount' in items:
            q = q.where(TFlashOrder.paid_amount == items['paid_amount'])
        if 'paid_amount_start' in items:
            q = q.where(TFlashOrder.paid_amount >= items['paid_amount_start'])
        if 'paid_amount_end' in items:
            q = q.where(TFlashOrder.paid_amount <= items['paid_amount_end'])
        
        if 'paid_balance' in items:
            q = q.where(TFlashOrder.paid_balance == items['paid_balance'])
        if 'paid_balance_start' in items:
            q = q.where(TFlashOrder.paid_balance >= items['paid_balance_start'])
        if 'paid_balance_end' in items:
            q = q.where(TFlashOrder.paid_balance <= items['paid_balance_end'])
        
        if 'single_status' in items:
            q = q.where(TFlashOrder.single_status == items['single_status'])
        if 'single_status_start' in items:
            q = q.where(TFlashOrder.single_status >= items['single_status_start'])
        if 'single_status_end' in items:
            q = q.where(TFlashOrder.single_status <= items['single_status_end'])
        
        if 'sold' in items:
            q = q.where(TFlashOrder.sold == items['sold'])
        if 'sold_start' in items:
            q = q.where(TFlashOrder.sold >= items['sold_start'])
        if 'sold_end' in items:
            q = q.where(TFlashOrder.sold <= items['sold_end'])
        
        if 'whole_status' in items:
            q = q.where(TFlashOrder.whole_status == items['whole_status'])
        if 'whole_status_start' in items:
            q = q.where(TFlashOrder.whole_status >= items['whole_status_start'])
        if 'whole_status_end' in items:
            q = q.where(TFlashOrder.whole_status <= items['whole_status_end'])
        
        if 'spec_id' in items:
            q = q.where(TFlashOrder.spec_id == items['spec_id'])
        if 'spec_id_start' in items:
            q = q.where(TFlashOrder.spec_id >= items['spec_id_start'])
        if 'spec_id_end' in items:
            q = q.where(TFlashOrder.spec_id <= items['spec_id_end'])
        
        if 'put_on_time' in items:
            q = q.where(TFlashOrder.put_on_time == items['put_on_time'])
        if 'put_on_time_start' in items:
            q = q.where(TFlashOrder.put_on_time >= items['put_on_time_start'])
        if 'put_on_time_end' in items:
            q = q.where(TFlashOrder.put_on_time <= items['put_on_time_end'])
        
        if 'detail' in items:
            q = q.where(TFlashOrder.detail == items['detail'])
        if 'detail_start' in items:
            q = q.where(TFlashOrder.detail >= items['detail_start'])
        if 'detail_end' in items:
            q = q.where(TFlashOrder.detail <= items['detail_end'])
        
        if 'is_assign_income' in items:
            q = q.where(TFlashOrder.is_assign_income == items['is_assign_income'])
        if 'is_assign_income_start' in items:
            q = q.where(TFlashOrder.is_assign_income >= items['is_assign_income_start'])
        if 'is_assign_income_end' in items:
            q = q.where(TFlashOrder.is_assign_income <= items['is_assign_income_end'])
        
        if 'complete_time' in items:
            q = q.where(TFlashOrder.complete_time == items['complete_time'])
        if 'complete_time_start' in items:
            q = q.where(TFlashOrder.complete_time >= items['complete_time_start'])
        if 'complete_time_end' in items:
            q = q.where(TFlashOrder.complete_time <= items['complete_time_end'])
        
        if 'return_sold' in items:
            q = q.where(TFlashOrder.return_sold == items['return_sold'])
        if 'return_sold_start' in items:
            q = q.where(TFlashOrder.return_sold >= items['return_sold_start'])
        if 'return_sold_end' in items:
            q = q.where(TFlashOrder.return_sold <= items['return_sold_end'])
        

        if 'id' in set_items:
            q = q.where(TFlashOrder.id.in_(set_items['id']))
        
        if 'package_id' in set_items:
            q = q.where(TFlashOrder.package_id.in_(set_items['package_id']))
        
        if 'status' in set_items:
            q = q.where(TFlashOrder.status.in_(set_items['status']))
        
        if 'create_time' in set_items:
            q = q.where(TFlashOrder.create_time.in_(set_items['create_time']))
        
        if 'paid_time' in set_items:
            q = q.where(TFlashOrder.paid_time.in_(set_items['paid_time']))
        
        if 'user_id' in set_items:
            q = q.where(TFlashOrder.user_id.in_(set_items['user_id']))
        
        if 'number' in set_items:
            q = q.where(TFlashOrder.number.in_(set_items['number']))
        
        if 'flash_price' in set_items:
            q = q.where(TFlashOrder.flash_price.in_(set_items['flash_price']))
        
        if 'flash_cost' in set_items:
            q = q.where(TFlashOrder.flash_cost.in_(set_items['flash_cost']))
        
        if 'out_trade_no' in set_items:
            q = q.where(TFlashOrder.out_trade_no.in_(set_items['out_trade_no']))
        
        if 'paid_amount' in set_items:
            q = q.where(TFlashOrder.paid_amount.in_(set_items['paid_amount']))
        
        if 'paid_balance' in set_items:
            q = q.where(TFlashOrder.paid_balance.in_(set_items['paid_balance']))
        
        if 'single_status' in set_items:
            q = q.where(TFlashOrder.single_status.in_(set_items['single_status']))
        
        if 'sold' in set_items:
            q = q.where(TFlashOrder.sold.in_(set_items['sold']))
        
        if 'whole_status' in set_items:
            q = q.where(TFlashOrder.whole_status.in_(set_items['whole_status']))
        
        if 'spec_id' in set_items:
            q = q.where(TFlashOrder.spec_id.in_(set_items['spec_id']))
        
        if 'put_on_time' in set_items:
            q = q.where(TFlashOrder.put_on_time.in_(set_items['put_on_time']))
        
        if 'detail' in set_items:
            q = q.where(TFlashOrder.detail.in_(set_items['detail']))
        
        if 'is_assign_income' in set_items:
            q = q.where(TFlashOrder.is_assign_income.in_(set_items['is_assign_income']))
        
        if 'complete_time' in set_items:
            q = q.where(TFlashOrder.complete_time.in_(set_items['complete_time']))
        
        if 'return_sold' in set_items:
            q = q.where(TFlashOrder.return_sold.in_(set_items['return_sold']))
        

        if 'out_trade_no' in search_items:
            q = q.where(TFlashOrder.out_trade_no.like(search_items['out_trade_no']))
        
        if 'detail' in search_items:
            q = q.where(TFlashOrder.detail.like(search_items['detail']))
        
    
        c = q.count()
        return c

    
def insert_flash_order_return(item: CreateFlashOrderReturn, db: Optional[SessionLocal] = None) -> SFlashOrderReturn:
    data = model2dict(item)
    t = TFlashOrderReturn(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SFlashOrderReturn.parse_obj(t.__dict__)

    
def delete_flash_order_return(flash_order_return_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TFlashOrderReturn).where(TFlashOrderReturn.id == flash_order_return_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TFlashOrderReturn).where(TFlashOrderReturn.id == flash_order_return_id).delete()
        db.commit()

    
def update_flash_order_return(item: SFlashOrderReturn, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TFlashOrderReturn).where(TFlashOrderReturn.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TFlashOrderReturn).where(TFlashOrderReturn.id == item.id).update(data)
        db.commit()

    
def get_flash_order_return(flash_order_return_id: int) -> Optional[SFlashOrderReturn]:
    with Dao() as db:
        t = db.query(TFlashOrderReturn).where(TFlashOrderReturn.id == flash_order_return_id).first()
        if t:
            return SFlashOrderReturn.parse_obj(t.__dict__)
        else:
            return None


def filter_flash_order_return(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SFlashOrderReturn]:
    with Dao() as db:
        q = db.query(TFlashOrderReturn)


        if 'id' in items:
            q = q.where(TFlashOrderReturn.id == items['id'])
        if 'id_start' in items:
            q = q.where(TFlashOrderReturn.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TFlashOrderReturn.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TFlashOrderReturn.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TFlashOrderReturn.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TFlashOrderReturn.user_id <= items['user_id_end'])
        
        if 'income_days' in items:
            q = q.where(TFlashOrderReturn.income_days == items['income_days'])
        if 'income_days_start' in items:
            q = q.where(TFlashOrderReturn.income_days >= items['income_days_start'])
        if 'income_days_end' in items:
            q = q.where(TFlashOrderReturn.income_days <= items['income_days_end'])
        
        if 'latest_time' in items:
            q = q.where(TFlashOrderReturn.latest_time == items['latest_time'])
        if 'latest_time_start' in items:
            q = q.where(TFlashOrderReturn.latest_time >= items['latest_time_start'])
        if 'latest_time_end' in items:
            q = q.where(TFlashOrderReturn.latest_time <= items['latest_time_end'])
        
        if 'latest_income_user' in items:
            q = q.where(TFlashOrderReturn.latest_income_user == items['latest_income_user'])
        if 'latest_income_user_start' in items:
            q = q.where(TFlashOrderReturn.latest_income_user >= items['latest_income_user_start'])
        if 'latest_income_user_end' in items:
            q = q.where(TFlashOrderReturn.latest_income_user <= items['latest_income_user_end'])
        
        if 'latest_income_layer' in items:
            q = q.where(TFlashOrderReturn.latest_income_layer == items['latest_income_layer'])
        if 'latest_income_layer_start' in items:
            q = q.where(TFlashOrderReturn.latest_income_layer >= items['latest_income_layer_start'])
        if 'latest_income_layer_end' in items:
            q = q.where(TFlashOrderReturn.latest_income_layer <= items['latest_income_layer_end'])
        
        if 'latest_income_toper' in items:
            q = q.where(TFlashOrderReturn.latest_income_toper == items['latest_income_toper'])
        if 'latest_income_toper_start' in items:
            q = q.where(TFlashOrderReturn.latest_income_toper >= items['latest_income_toper_start'])
        if 'latest_income_toper_end' in items:
            q = q.where(TFlashOrderReturn.latest_income_toper <= items['latest_income_toper_end'])
        
        if 'latest_income_groupsir' in items:
            q = q.where(TFlashOrderReturn.latest_income_groupsir == items['latest_income_groupsir'])
        if 'latest_income_groupsir_start' in items:
            q = q.where(TFlashOrderReturn.latest_income_groupsir >= items['latest_income_groupsir_start'])
        if 'latest_income_groupsir_end' in items:
            q = q.where(TFlashOrderReturn.latest_income_groupsir <= items['latest_income_groupsir_end'])
        

        if 'id' in set_items:
            q = q.where(TFlashOrderReturn.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TFlashOrderReturn.user_id.in_(set_items['user_id']))
        
        if 'income_days' in set_items:
            q = q.where(TFlashOrderReturn.income_days.in_(set_items['income_days']))
        
        if 'latest_time' in set_items:
            q = q.where(TFlashOrderReturn.latest_time.in_(set_items['latest_time']))
        
        if 'latest_income_user' in set_items:
            q = q.where(TFlashOrderReturn.latest_income_user.in_(set_items['latest_income_user']))
        
        if 'latest_income_layer' in set_items:
            q = q.where(TFlashOrderReturn.latest_income_layer.in_(set_items['latest_income_layer']))
        
        if 'latest_income_toper' in set_items:
            q = q.where(TFlashOrderReturn.latest_income_toper.in_(set_items['latest_income_toper']))
        
        if 'latest_income_groupsir' in set_items:
            q = q.where(TFlashOrderReturn.latest_income_groupsir.in_(set_items['latest_income_groupsir']))
        

    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TFlashOrderReturn.latest_income_groupsir.asc())
                orders.append(TFlashOrderReturn.id.asc())
            elif val == 'desc':
                #orders.append(TFlashOrderReturn.latest_income_groupsir.desc())
                orders.append(TFlashOrderReturn.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_flash_order_return_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SFlashOrderReturn.parse_obj(t.__dict__) for t in t_flash_order_return_list]


def filter_count_flash_order_return(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TFlashOrderReturn)


        if 'id' in items:
            q = q.where(TFlashOrderReturn.id == items['id'])
        if 'id_start' in items:
            q = q.where(TFlashOrderReturn.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TFlashOrderReturn.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TFlashOrderReturn.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TFlashOrderReturn.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TFlashOrderReturn.user_id <= items['user_id_end'])
        
        if 'income_days' in items:
            q = q.where(TFlashOrderReturn.income_days == items['income_days'])
        if 'income_days_start' in items:
            q = q.where(TFlashOrderReturn.income_days >= items['income_days_start'])
        if 'income_days_end' in items:
            q = q.where(TFlashOrderReturn.income_days <= items['income_days_end'])
        
        if 'latest_time' in items:
            q = q.where(TFlashOrderReturn.latest_time == items['latest_time'])
        if 'latest_time_start' in items:
            q = q.where(TFlashOrderReturn.latest_time >= items['latest_time_start'])
        if 'latest_time_end' in items:
            q = q.where(TFlashOrderReturn.latest_time <= items['latest_time_end'])
        
        if 'latest_income_user' in items:
            q = q.where(TFlashOrderReturn.latest_income_user == items['latest_income_user'])
        if 'latest_income_user_start' in items:
            q = q.where(TFlashOrderReturn.latest_income_user >= items['latest_income_user_start'])
        if 'latest_income_user_end' in items:
            q = q.where(TFlashOrderReturn.latest_income_user <= items['latest_income_user_end'])
        
        if 'latest_income_layer' in items:
            q = q.where(TFlashOrderReturn.latest_income_layer == items['latest_income_layer'])
        if 'latest_income_layer_start' in items:
            q = q.where(TFlashOrderReturn.latest_income_layer >= items['latest_income_layer_start'])
        if 'latest_income_layer_end' in items:
            q = q.where(TFlashOrderReturn.latest_income_layer <= items['latest_income_layer_end'])
        
        if 'latest_income_toper' in items:
            q = q.where(TFlashOrderReturn.latest_income_toper == items['latest_income_toper'])
        if 'latest_income_toper_start' in items:
            q = q.where(TFlashOrderReturn.latest_income_toper >= items['latest_income_toper_start'])
        if 'latest_income_toper_end' in items:
            q = q.where(TFlashOrderReturn.latest_income_toper <= items['latest_income_toper_end'])
        
        if 'latest_income_groupsir' in items:
            q = q.where(TFlashOrderReturn.latest_income_groupsir == items['latest_income_groupsir'])
        if 'latest_income_groupsir_start' in items:
            q = q.where(TFlashOrderReturn.latest_income_groupsir >= items['latest_income_groupsir_start'])
        if 'latest_income_groupsir_end' in items:
            q = q.where(TFlashOrderReturn.latest_income_groupsir <= items['latest_income_groupsir_end'])
        

        if 'id' in set_items:
            q = q.where(TFlashOrderReturn.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TFlashOrderReturn.user_id.in_(set_items['user_id']))
        
        if 'income_days' in set_items:
            q = q.where(TFlashOrderReturn.income_days.in_(set_items['income_days']))
        
        if 'latest_time' in set_items:
            q = q.where(TFlashOrderReturn.latest_time.in_(set_items['latest_time']))
        
        if 'latest_income_user' in set_items:
            q = q.where(TFlashOrderReturn.latest_income_user.in_(set_items['latest_income_user']))
        
        if 'latest_income_layer' in set_items:
            q = q.where(TFlashOrderReturn.latest_income_layer.in_(set_items['latest_income_layer']))
        
        if 'latest_income_toper' in set_items:
            q = q.where(TFlashOrderReturn.latest_income_toper.in_(set_items['latest_income_toper']))
        
        if 'latest_income_groupsir' in set_items:
            q = q.where(TFlashOrderReturn.latest_income_groupsir.in_(set_items['latest_income_groupsir']))
        

    
        c = q.count()
        return c

    
def insert_package_order_status(item: CreatePackageOrderStatus, db: Optional[SessionLocal] = None) -> SPackageOrderStatus:
    data = model2dict(item)
    t = TPackageOrderStatus(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SPackageOrderStatus.parse_obj(t.__dict__)

    
def delete_package_order_status(package_order_status_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TPackageOrderStatus).where(TPackageOrderStatus.id == package_order_status_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPackageOrderStatus).where(TPackageOrderStatus.id == package_order_status_id).delete()
        db.commit()

    
def update_package_order_status(item: SPackageOrderStatus, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TPackageOrderStatus).where(TPackageOrderStatus.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPackageOrderStatus).where(TPackageOrderStatus.id == item.id).update(data)
        db.commit()

    
def get_package_order_status(package_order_status_id: int) -> Optional[SPackageOrderStatus]:
    with Dao() as db:
        t = db.query(TPackageOrderStatus).where(TPackageOrderStatus.id == package_order_status_id).first()
        if t:
            return SPackageOrderStatus.parse_obj(t.__dict__)
        else:
            return None


def filter_package_order_status(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SPackageOrderStatus]:
    with Dao() as db:
        q = db.query(TPackageOrderStatus)


        if 'id' in items:
            q = q.where(TPackageOrderStatus.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPackageOrderStatus.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPackageOrderStatus.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TPackageOrderStatus.title == items['title'])
        if 'title_start' in items:
            q = q.where(TPackageOrderStatus.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TPackageOrderStatus.title <= items['title_end'])
        

        if 'id' in set_items:
            q = q.where(TPackageOrderStatus.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TPackageOrderStatus.title.in_(set_items['title']))
        

        if 'title' in search_items:
            q = q.where(TPackageOrderStatus.title.like(search_items['title']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TPackageOrderStatus.title.asc())
                orders.append(TPackageOrderStatus.id.asc())
            elif val == 'desc':
                #orders.append(TPackageOrderStatus.title.desc())
                orders.append(TPackageOrderStatus.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_package_order_status_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SPackageOrderStatus.parse_obj(t.__dict__) for t in t_package_order_status_list]


def filter_count_package_order_status(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TPackageOrderStatus)


        if 'id' in items:
            q = q.where(TPackageOrderStatus.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPackageOrderStatus.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPackageOrderStatus.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TPackageOrderStatus.title == items['title'])
        if 'title_start' in items:
            q = q.where(TPackageOrderStatus.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TPackageOrderStatus.title <= items['title_end'])
        

        if 'id' in set_items:
            q = q.where(TPackageOrderStatus.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TPackageOrderStatus.title.in_(set_items['title']))
        

        if 'title' in search_items:
            q = q.where(TPackageOrderStatus.title.like(search_items['title']))
        
    
        c = q.count()
        return c

    
def insert_good(item: CreateGood, db: Optional[SessionLocal] = None) -> SGood:
    data = model2dict(item)
    t = TGood(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SGood.parse_obj(t.__dict__)

    
def delete_good(good_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TGood).where(TGood.id == good_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGood).where(TGood.id == good_id).delete()
        db.commit()

    
def update_good(item: SGood, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TGood).where(TGood.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGood).where(TGood.id == item.id).update(data)
        db.commit()

    
def get_good(good_id: int) -> Optional[SGood]:
    with Dao() as db:
        t = db.query(TGood).where(TGood.id == good_id).first()
        if t:
            return SGood.parse_obj(t.__dict__)
        else:
            return None


def filter_good(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SGood]:
    with Dao() as db:
        q = db.query(TGood)


        if 'id' in items:
            q = q.where(TGood.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGood.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGood.id <= items['id_end'])
        
        if 'name' in items:
            q = q.where(TGood.name == items['name'])
        if 'name_start' in items:
            q = q.where(TGood.name >= items['name_start'])
        if 'name_end' in items:
            q = q.where(TGood.name <= items['name_end'])
        
        if 'is_flash_sale' in items:
            q = q.where(TGood.is_flash_sale == items['is_flash_sale'])
        if 'is_flash_sale_start' in items:
            q = q.where(TGood.is_flash_sale >= items['is_flash_sale_start'])
        if 'is_flash_sale_end' in items:
            q = q.where(TGood.is_flash_sale <= items['is_flash_sale_end'])
        
        if 'category_id' in items:
            q = q.where(TGood.category_id == items['category_id'])
        if 'category_id_start' in items:
            q = q.where(TGood.category_id >= items['category_id_start'])
        if 'category_id_end' in items:
            q = q.where(TGood.category_id <= items['category_id_end'])
        
        if 'type' in items:
            q = q.where(TGood.type == items['type'])
        if 'type_start' in items:
            q = q.where(TGood.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TGood.type <= items['type_end'])
        
        if 'num_sale' in items:
            q = q.where(TGood.num_sale == items['num_sale'])
        if 'num_sale_start' in items:
            q = q.where(TGood.num_sale >= items['num_sale_start'])
        if 'num_sale_end' in items:
            q = q.where(TGood.num_sale <= items['num_sale_end'])
        
        if 'image_url' in items:
            q = q.where(TGood.image_url == items['image_url'])
        if 'image_url_start' in items:
            q = q.where(TGood.image_url >= items['image_url_start'])
        if 'image_url_end' in items:
            q = q.where(TGood.image_url <= items['image_url_end'])
        
        if 'priority' in items:
            q = q.where(TGood.priority == items['priority'])
        if 'priority_start' in items:
            q = q.where(TGood.priority >= items['priority_start'])
        if 'priority_end' in items:
            q = q.where(TGood.priority <= items['priority_end'])
        
        if 'add_coin' in items:
            q = q.where(TGood.add_coin == items['add_coin'])
        if 'add_coin_start' in items:
            q = q.where(TGood.add_coin >= items['add_coin_start'])
        if 'add_coin_end' in items:
            q = q.where(TGood.add_coin <= items['add_coin_end'])
        
        if 'model_id' in items:
            q = q.where(TGood.model_id == items['model_id'])
        if 'model_id_start' in items:
            q = q.where(TGood.model_id >= items['model_id_start'])
        if 'model_id_end' in items:
            q = q.where(TGood.model_id <= items['model_id_end'])
        
        if 'expired_time' in items:
            q = q.where(TGood.expired_time == items['expired_time'])
        if 'expired_time_start' in items:
            q = q.where(TGood.expired_time >= items['expired_time_start'])
        if 'expired_time_end' in items:
            q = q.where(TGood.expired_time <= items['expired_time_end'])
        
        if 'parent_good_id' in items:
            q = q.where(TGood.parent_good_id == items['parent_good_id'])
        if 'parent_good_id_start' in items:
            q = q.where(TGood.parent_good_id >= items['parent_good_id_start'])
        if 'parent_good_id_end' in items:
            q = q.where(TGood.parent_good_id <= items['parent_good_id_end'])
        
        if 'title' in items:
            q = q.where(TGood.title == items['title'])
        if 'title_start' in items:
            q = q.where(TGood.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TGood.title <= items['title_end'])
        
        if 'subtitle' in items:
            q = q.where(TGood.subtitle == items['subtitle'])
        if 'subtitle_start' in items:
            q = q.where(TGood.subtitle >= items['subtitle_start'])
        if 'subtitle_end' in items:
            q = q.where(TGood.subtitle <= items['subtitle_end'])
        
        if 'stock_cordon' in items:
            q = q.where(TGood.stock_cordon == items['stock_cordon'])
        if 'stock_cordon_start' in items:
            q = q.where(TGood.stock_cordon >= items['stock_cordon_start'])
        if 'stock_cordon_end' in items:
            q = q.where(TGood.stock_cordon <= items['stock_cordon_end'])
        
        if 'status' in items:
            q = q.where(TGood.status == items['status'])
        if 'status_start' in items:
            q = q.where(TGood.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TGood.status <= items['status_end'])
        
        if 'details' in items:
            q = q.where(TGood.details == items['details'])
        if 'details_start' in items:
            q = q.where(TGood.details >= items['details_start'])
        if 'details_end' in items:
            q = q.where(TGood.details <= items['details_end'])
        
        if 'supplier_id' in items:
            q = q.where(TGood.supplier_id == items['supplier_id'])
        if 'supplier_id_start' in items:
            q = q.where(TGood.supplier_id >= items['supplier_id_start'])
        if 'supplier_id_end' in items:
            q = q.where(TGood.supplier_id <= items['supplier_id_end'])
        
        if 'share_ratio' in items:
            q = q.where(TGood.share_ratio == items['share_ratio'])
        if 'share_ratio_start' in items:
            q = q.where(TGood.share_ratio >= items['share_ratio_start'])
        if 'share_ratio_end' in items:
            q = q.where(TGood.share_ratio <= items['share_ratio_end'])
        
        if 'create_time' in items:
            q = q.where(TGood.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TGood.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TGood.create_time <= items['create_time_end'])
        
        if 'last_update_time' in items:
            q = q.where(TGood.last_update_time == items['last_update_time'])
        if 'last_update_time_start' in items:
            q = q.where(TGood.last_update_time >= items['last_update_time_start'])
        if 'last_update_time_end' in items:
            q = q.where(TGood.last_update_time <= items['last_update_time_end'])
        
        if 'saleable' in items:
            q = q.where(TGood.saleable == items['saleable'])
        if 'saleable_start' in items:
            q = q.where(TGood.saleable >= items['saleable_start'])
        if 'saleable_end' in items:
            q = q.where(TGood.saleable <= items['saleable_end'])
        
        if 'click_count' in items:
            q = q.where(TGood.click_count == items['click_count'])
        if 'click_count_start' in items:
            q = q.where(TGood.click_count >= items['click_count_start'])
        if 'click_count_end' in items:
            q = q.where(TGood.click_count <= items['click_count_end'])
        
        if 'transmit_count' in items:
            q = q.where(TGood.transmit_count == items['transmit_count'])
        if 'transmit_count_start' in items:
            q = q.where(TGood.transmit_count >= items['transmit_count_start'])
        if 'transmit_count_end' in items:
            q = q.where(TGood.transmit_count <= items['transmit_count_end'])
        
        if 'coinable' in items:
            q = q.where(TGood.coinable == items['coinable'])
        if 'coinable_start' in items:
            q = q.where(TGood.coinable >= items['coinable_start'])
        if 'coinable_end' in items:
            q = q.where(TGood.coinable <= items['coinable_end'])
        
        if 'price_line' in items:
            q = q.where(TGood.price_line == items['price_line'])
        if 'price_line_start' in items:
            q = q.where(TGood.price_line >= items['price_line_start'])
        if 'price_line_end' in items:
            q = q.where(TGood.price_line <= items['price_line_end'])
        
        if 'introducer_id' in items:
            q = q.where(TGood.introducer_id == items['introducer_id'])
        if 'introducer_id_start' in items:
            q = q.where(TGood.introducer_id >= items['introducer_id_start'])
        if 'introducer_id_end' in items:
            q = q.where(TGood.introducer_id <= items['introducer_id_end'])
        
        if 'sell_high' in items:
            q = q.where(TGood.sell_high == items['sell_high'])
        if 'sell_high_start' in items:
            q = q.where(TGood.sell_high >= items['sell_high_start'])
        if 'sell_high_end' in items:
            q = q.where(TGood.sell_high <= items['sell_high_end'])
        
        if 'sell_low' in items:
            q = q.where(TGood.sell_low == items['sell_low'])
        if 'sell_low_start' in items:
            q = q.where(TGood.sell_low >= items['sell_low_start'])
        if 'sell_low_end' in items:
            q = q.where(TGood.sell_low <= items['sell_low_end'])
        
        if 'cost_high' in items:
            q = q.where(TGood.cost_high == items['cost_high'])
        if 'cost_high_start' in items:
            q = q.where(TGood.cost_high >= items['cost_high_start'])
        if 'cost_high_end' in items:
            q = q.where(TGood.cost_high <= items['cost_high_end'])
        
        if 'cost_low' in items:
            q = q.where(TGood.cost_low == items['cost_low'])
        if 'cost_low_start' in items:
            q = q.where(TGood.cost_low >= items['cost_low_start'])
        if 'cost_low_end' in items:
            q = q.where(TGood.cost_low <= items['cost_low_end'])
        
        if 'display' in items:
            q = q.where(TGood.display == items['display'])
        if 'display_start' in items:
            q = q.where(TGood.display >= items['display_start'])
        if 'display_end' in items:
            q = q.where(TGood.display <= items['display_end'])
        
        if 'coinable_number' in items:
            q = q.where(TGood.coinable_number == items['coinable_number'])
        if 'coinable_number_start' in items:
            q = q.where(TGood.coinable_number >= items['coinable_number_start'])
        if 'coinable_number_end' in items:
            q = q.where(TGood.coinable_number <= items['coinable_number_end'])
        
        if 'is_package' in items:
            q = q.where(TGood.is_package == items['is_package'])
        if 'is_package_start' in items:
            q = q.where(TGood.is_package >= items['is_package_start'])
        if 'is_package_end' in items:
            q = q.where(TGood.is_package <= items['is_package_end'])
        
        if 'fake_owner_name' in items:
            q = q.where(TGood.fake_owner_name == items['fake_owner_name'])
        if 'fake_owner_name_start' in items:
            q = q.where(TGood.fake_owner_name >= items['fake_owner_name_start'])
        if 'fake_owner_name_end' in items:
            q = q.where(TGood.fake_owner_name <= items['fake_owner_name_end'])
        
        if 'fake_owner_phone' in items:
            q = q.where(TGood.fake_owner_phone == items['fake_owner_phone'])
        if 'fake_owner_phone_start' in items:
            q = q.where(TGood.fake_owner_phone >= items['fake_owner_phone_start'])
        if 'fake_owner_phone_end' in items:
            q = q.where(TGood.fake_owner_phone <= items['fake_owner_phone_end'])
        
        if 'unavailable_date' in items:
            q = q.where(TGood.unavailable_date == items['unavailable_date'])
        if 'unavailable_date_start' in items:
            q = q.where(TGood.unavailable_date >= items['unavailable_date_start'])
        if 'unavailable_date_end' in items:
            q = q.where(TGood.unavailable_date <= items['unavailable_date_end'])
        
        if 'available_time' in items:
            q = q.where(TGood.available_time == items['available_time'])
        if 'available_time_start' in items:
            q = q.where(TGood.available_time >= items['available_time_start'])
        if 'available_time_end' in items:
            q = q.where(TGood.available_time <= items['available_time_end'])
        
        if 'usage_rule' in items:
            q = q.where(TGood.usage_rule == items['usage_rule'])
        if 'usage_rule_start' in items:
            q = q.where(TGood.usage_rule >= items['usage_rule_start'])
        if 'usage_rule_end' in items:
            q = q.where(TGood.usage_rule <= items['usage_rule_end'])
        
        if 'refund_rule' in items:
            q = q.where(TGood.refund_rule == items['refund_rule'])
        if 'refund_rule_start' in items:
            q = q.where(TGood.refund_rule >= items['refund_rule_start'])
        if 'refund_rule_end' in items:
            q = q.where(TGood.refund_rule <= items['refund_rule_end'])
        
        if 'order_expired_time' in items:
            q = q.where(TGood.order_expired_time == items['order_expired_time'])
        if 'order_expired_time_start' in items:
            q = q.where(TGood.order_expired_time >= items['order_expired_time_start'])
        if 'order_expired_time_end' in items:
            q = q.where(TGood.order_expired_time <= items['order_expired_time_end'])
        
        if 'cover_url' in items:
            q = q.where(TGood.cover_url == items['cover_url'])
        if 'cover_url_start' in items:
            q = q.where(TGood.cover_url >= items['cover_url_start'])
        if 'cover_url_end' in items:
            q = q.where(TGood.cover_url <= items['cover_url_end'])
        
        if 'video_url' in items:
            q = q.where(TGood.video_url == items['video_url'])
        if 'video_url_start' in items:
            q = q.where(TGood.video_url >= items['video_url_start'])
        if 'video_url_end' in items:
            q = q.where(TGood.video_url <= items['video_url_end'])
        

        if 'id' in set_items:
            q = q.where(TGood.id.in_(set_items['id']))
        
        if 'name' in set_items:
            q = q.where(TGood.name.in_(set_items['name']))
        
        if 'is_flash_sale' in set_items:
            q = q.where(TGood.is_flash_sale.in_(set_items['is_flash_sale']))
        
        if 'category_id' in set_items:
            q = q.where(TGood.category_id.in_(set_items['category_id']))
        
        if 'type' in set_items:
            q = q.where(TGood.type.in_(set_items['type']))
        
        if 'num_sale' in set_items:
            q = q.where(TGood.num_sale.in_(set_items['num_sale']))
        
        if 'image_url' in set_items:
            q = q.where(TGood.image_url.in_(set_items['image_url']))
        
        if 'priority' in set_items:
            q = q.where(TGood.priority.in_(set_items['priority']))
        
        if 'add_coin' in set_items:
            q = q.where(TGood.add_coin.in_(set_items['add_coin']))
        
        if 'model_id' in set_items:
            q = q.where(TGood.model_id.in_(set_items['model_id']))
        
        if 'expired_time' in set_items:
            q = q.where(TGood.expired_time.in_(set_items['expired_time']))
        
        if 'parent_good_id' in set_items:
            q = q.where(TGood.parent_good_id.in_(set_items['parent_good_id']))
        
        if 'title' in set_items:
            q = q.where(TGood.title.in_(set_items['title']))
        
        if 'subtitle' in set_items:
            q = q.where(TGood.subtitle.in_(set_items['subtitle']))
        
        if 'stock_cordon' in set_items:
            q = q.where(TGood.stock_cordon.in_(set_items['stock_cordon']))
        
        if 'status' in set_items:
            q = q.where(TGood.status.in_(set_items['status']))
        
        if 'details' in set_items:
            q = q.where(TGood.details.in_(set_items['details']))
        
        if 'supplier_id' in set_items:
            q = q.where(TGood.supplier_id.in_(set_items['supplier_id']))
        
        if 'share_ratio' in set_items:
            q = q.where(TGood.share_ratio.in_(set_items['share_ratio']))
        
        if 'create_time' in set_items:
            q = q.where(TGood.create_time.in_(set_items['create_time']))
        
        if 'last_update_time' in set_items:
            q = q.where(TGood.last_update_time.in_(set_items['last_update_time']))
        
        if 'saleable' in set_items:
            q = q.where(TGood.saleable.in_(set_items['saleable']))
        
        if 'click_count' in set_items:
            q = q.where(TGood.click_count.in_(set_items['click_count']))
        
        if 'transmit_count' in set_items:
            q = q.where(TGood.transmit_count.in_(set_items['transmit_count']))
        
        if 'coinable' in set_items:
            q = q.where(TGood.coinable.in_(set_items['coinable']))
        
        if 'price_line' in set_items:
            q = q.where(TGood.price_line.in_(set_items['price_line']))
        
        if 'introducer_id' in set_items:
            q = q.where(TGood.introducer_id.in_(set_items['introducer_id']))
        
        if 'sell_high' in set_items:
            q = q.where(TGood.sell_high.in_(set_items['sell_high']))
        
        if 'sell_low' in set_items:
            q = q.where(TGood.sell_low.in_(set_items['sell_low']))
        
        if 'cost_high' in set_items:
            q = q.where(TGood.cost_high.in_(set_items['cost_high']))
        
        if 'cost_low' in set_items:
            q = q.where(TGood.cost_low.in_(set_items['cost_low']))
        
        if 'display' in set_items:
            q = q.where(TGood.display.in_(set_items['display']))
        
        if 'coinable_number' in set_items:
            q = q.where(TGood.coinable_number.in_(set_items['coinable_number']))
        
        if 'is_package' in set_items:
            q = q.where(TGood.is_package.in_(set_items['is_package']))
        
        if 'fake_owner_name' in set_items:
            q = q.where(TGood.fake_owner_name.in_(set_items['fake_owner_name']))
        
        if 'fake_owner_phone' in set_items:
            q = q.where(TGood.fake_owner_phone.in_(set_items['fake_owner_phone']))
        
        if 'unavailable_date' in set_items:
            q = q.where(TGood.unavailable_date.in_(set_items['unavailable_date']))
        
        if 'available_time' in set_items:
            q = q.where(TGood.available_time.in_(set_items['available_time']))
        
        if 'usage_rule' in set_items:
            q = q.where(TGood.usage_rule.in_(set_items['usage_rule']))
        
        if 'refund_rule' in set_items:
            q = q.where(TGood.refund_rule.in_(set_items['refund_rule']))
        
        if 'order_expired_time' in set_items:
            q = q.where(TGood.order_expired_time.in_(set_items['order_expired_time']))
        
        if 'cover_url' in set_items:
            q = q.where(TGood.cover_url.in_(set_items['cover_url']))
        
        if 'video_url' in set_items:
            q = q.where(TGood.video_url.in_(set_items['video_url']))
        

        if 'name' in search_items:
            q = q.where(TGood.name.like(search_items['name']))
        
        if 'image_url' in search_items:
            q = q.where(TGood.image_url.like(search_items['image_url']))
        
        if 'title' in search_items:
            q = q.where(TGood.title.like(search_items['title']))
        
        if 'subtitle' in search_items:
            q = q.where(TGood.subtitle.like(search_items['subtitle']))
        
        if 'details' in search_items:
            q = q.where(TGood.details.like(search_items['details']))
        
        if 'fake_owner_name' in search_items:
            q = q.where(TGood.fake_owner_name.like(search_items['fake_owner_name']))
        
        if 'fake_owner_phone' in search_items:
            q = q.where(TGood.fake_owner_phone.like(search_items['fake_owner_phone']))
        
        if 'unavailable_date' in search_items:
            q = q.where(TGood.unavailable_date.like(search_items['unavailable_date']))
        
        if 'available_time' in search_items:
            q = q.where(TGood.available_time.like(search_items['available_time']))
        
        if 'usage_rule' in search_items:
            q = q.where(TGood.usage_rule.like(search_items['usage_rule']))
        
        if 'refund_rule' in search_items:
            q = q.where(TGood.refund_rule.like(search_items['refund_rule']))
        
        if 'cover_url' in search_items:
            q = q.where(TGood.cover_url.like(search_items['cover_url']))
        
        if 'video_url' in search_items:
            q = q.where(TGood.video_url.like(search_items['video_url']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TGood.video_url.asc())
                orders.append(TGood.id.asc())
            elif val == 'desc':
                #orders.append(TGood.video_url.desc())
                orders.append(TGood.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_good_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SGood.parse_obj(t.__dict__) for t in t_good_list]


def filter_count_good(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TGood)


        if 'id' in items:
            q = q.where(TGood.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGood.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGood.id <= items['id_end'])
        
        if 'name' in items:
            q = q.where(TGood.name == items['name'])
        if 'name_start' in items:
            q = q.where(TGood.name >= items['name_start'])
        if 'name_end' in items:
            q = q.where(TGood.name <= items['name_end'])
        
        if 'is_flash_sale' in items:
            q = q.where(TGood.is_flash_sale == items['is_flash_sale'])
        if 'is_flash_sale_start' in items:
            q = q.where(TGood.is_flash_sale >= items['is_flash_sale_start'])
        if 'is_flash_sale_end' in items:
            q = q.where(TGood.is_flash_sale <= items['is_flash_sale_end'])
        
        if 'category_id' in items:
            q = q.where(TGood.category_id == items['category_id'])
        if 'category_id_start' in items:
            q = q.where(TGood.category_id >= items['category_id_start'])
        if 'category_id_end' in items:
            q = q.where(TGood.category_id <= items['category_id_end'])
        
        if 'type' in items:
            q = q.where(TGood.type == items['type'])
        if 'type_start' in items:
            q = q.where(TGood.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TGood.type <= items['type_end'])
        
        if 'num_sale' in items:
            q = q.where(TGood.num_sale == items['num_sale'])
        if 'num_sale_start' in items:
            q = q.where(TGood.num_sale >= items['num_sale_start'])
        if 'num_sale_end' in items:
            q = q.where(TGood.num_sale <= items['num_sale_end'])
        
        if 'image_url' in items:
            q = q.where(TGood.image_url == items['image_url'])
        if 'image_url_start' in items:
            q = q.where(TGood.image_url >= items['image_url_start'])
        if 'image_url_end' in items:
            q = q.where(TGood.image_url <= items['image_url_end'])
        
        if 'priority' in items:
            q = q.where(TGood.priority == items['priority'])
        if 'priority_start' in items:
            q = q.where(TGood.priority >= items['priority_start'])
        if 'priority_end' in items:
            q = q.where(TGood.priority <= items['priority_end'])
        
        if 'add_coin' in items:
            q = q.where(TGood.add_coin == items['add_coin'])
        if 'add_coin_start' in items:
            q = q.where(TGood.add_coin >= items['add_coin_start'])
        if 'add_coin_end' in items:
            q = q.where(TGood.add_coin <= items['add_coin_end'])
        
        if 'model_id' in items:
            q = q.where(TGood.model_id == items['model_id'])
        if 'model_id_start' in items:
            q = q.where(TGood.model_id >= items['model_id_start'])
        if 'model_id_end' in items:
            q = q.where(TGood.model_id <= items['model_id_end'])
        
        if 'expired_time' in items:
            q = q.where(TGood.expired_time == items['expired_time'])
        if 'expired_time_start' in items:
            q = q.where(TGood.expired_time >= items['expired_time_start'])
        if 'expired_time_end' in items:
            q = q.where(TGood.expired_time <= items['expired_time_end'])
        
        if 'parent_good_id' in items:
            q = q.where(TGood.parent_good_id == items['parent_good_id'])
        if 'parent_good_id_start' in items:
            q = q.where(TGood.parent_good_id >= items['parent_good_id_start'])
        if 'parent_good_id_end' in items:
            q = q.where(TGood.parent_good_id <= items['parent_good_id_end'])
        
        if 'title' in items:
            q = q.where(TGood.title == items['title'])
        if 'title_start' in items:
            q = q.where(TGood.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TGood.title <= items['title_end'])
        
        if 'subtitle' in items:
            q = q.where(TGood.subtitle == items['subtitle'])
        if 'subtitle_start' in items:
            q = q.where(TGood.subtitle >= items['subtitle_start'])
        if 'subtitle_end' in items:
            q = q.where(TGood.subtitle <= items['subtitle_end'])
        
        if 'stock_cordon' in items:
            q = q.where(TGood.stock_cordon == items['stock_cordon'])
        if 'stock_cordon_start' in items:
            q = q.where(TGood.stock_cordon >= items['stock_cordon_start'])
        if 'stock_cordon_end' in items:
            q = q.where(TGood.stock_cordon <= items['stock_cordon_end'])
        
        if 'status' in items:
            q = q.where(TGood.status == items['status'])
        if 'status_start' in items:
            q = q.where(TGood.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TGood.status <= items['status_end'])
        
        if 'details' in items:
            q = q.where(TGood.details == items['details'])
        if 'details_start' in items:
            q = q.where(TGood.details >= items['details_start'])
        if 'details_end' in items:
            q = q.where(TGood.details <= items['details_end'])
        
        if 'supplier_id' in items:
            q = q.where(TGood.supplier_id == items['supplier_id'])
        if 'supplier_id_start' in items:
            q = q.where(TGood.supplier_id >= items['supplier_id_start'])
        if 'supplier_id_end' in items:
            q = q.where(TGood.supplier_id <= items['supplier_id_end'])
        
        if 'share_ratio' in items:
            q = q.where(TGood.share_ratio == items['share_ratio'])
        if 'share_ratio_start' in items:
            q = q.where(TGood.share_ratio >= items['share_ratio_start'])
        if 'share_ratio_end' in items:
            q = q.where(TGood.share_ratio <= items['share_ratio_end'])
        
        if 'create_time' in items:
            q = q.where(TGood.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TGood.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TGood.create_time <= items['create_time_end'])
        
        if 'last_update_time' in items:
            q = q.where(TGood.last_update_time == items['last_update_time'])
        if 'last_update_time_start' in items:
            q = q.where(TGood.last_update_time >= items['last_update_time_start'])
        if 'last_update_time_end' in items:
            q = q.where(TGood.last_update_time <= items['last_update_time_end'])
        
        if 'saleable' in items:
            q = q.where(TGood.saleable == items['saleable'])
        if 'saleable_start' in items:
            q = q.where(TGood.saleable >= items['saleable_start'])
        if 'saleable_end' in items:
            q = q.where(TGood.saleable <= items['saleable_end'])
        
        if 'click_count' in items:
            q = q.where(TGood.click_count == items['click_count'])
        if 'click_count_start' in items:
            q = q.where(TGood.click_count >= items['click_count_start'])
        if 'click_count_end' in items:
            q = q.where(TGood.click_count <= items['click_count_end'])
        
        if 'transmit_count' in items:
            q = q.where(TGood.transmit_count == items['transmit_count'])
        if 'transmit_count_start' in items:
            q = q.where(TGood.transmit_count >= items['transmit_count_start'])
        if 'transmit_count_end' in items:
            q = q.where(TGood.transmit_count <= items['transmit_count_end'])
        
        if 'coinable' in items:
            q = q.where(TGood.coinable == items['coinable'])
        if 'coinable_start' in items:
            q = q.where(TGood.coinable >= items['coinable_start'])
        if 'coinable_end' in items:
            q = q.where(TGood.coinable <= items['coinable_end'])
        
        if 'price_line' in items:
            q = q.where(TGood.price_line == items['price_line'])
        if 'price_line_start' in items:
            q = q.where(TGood.price_line >= items['price_line_start'])
        if 'price_line_end' in items:
            q = q.where(TGood.price_line <= items['price_line_end'])
        
        if 'introducer_id' in items:
            q = q.where(TGood.introducer_id == items['introducer_id'])
        if 'introducer_id_start' in items:
            q = q.where(TGood.introducer_id >= items['introducer_id_start'])
        if 'introducer_id_end' in items:
            q = q.where(TGood.introducer_id <= items['introducer_id_end'])
        
        if 'sell_high' in items:
            q = q.where(TGood.sell_high == items['sell_high'])
        if 'sell_high_start' in items:
            q = q.where(TGood.sell_high >= items['sell_high_start'])
        if 'sell_high_end' in items:
            q = q.where(TGood.sell_high <= items['sell_high_end'])
        
        if 'sell_low' in items:
            q = q.where(TGood.sell_low == items['sell_low'])
        if 'sell_low_start' in items:
            q = q.where(TGood.sell_low >= items['sell_low_start'])
        if 'sell_low_end' in items:
            q = q.where(TGood.sell_low <= items['sell_low_end'])
        
        if 'cost_high' in items:
            q = q.where(TGood.cost_high == items['cost_high'])
        if 'cost_high_start' in items:
            q = q.where(TGood.cost_high >= items['cost_high_start'])
        if 'cost_high_end' in items:
            q = q.where(TGood.cost_high <= items['cost_high_end'])
        
        if 'cost_low' in items:
            q = q.where(TGood.cost_low == items['cost_low'])
        if 'cost_low_start' in items:
            q = q.where(TGood.cost_low >= items['cost_low_start'])
        if 'cost_low_end' in items:
            q = q.where(TGood.cost_low <= items['cost_low_end'])
        
        if 'display' in items:
            q = q.where(TGood.display == items['display'])
        if 'display_start' in items:
            q = q.where(TGood.display >= items['display_start'])
        if 'display_end' in items:
            q = q.where(TGood.display <= items['display_end'])
        
        if 'coinable_number' in items:
            q = q.where(TGood.coinable_number == items['coinable_number'])
        if 'coinable_number_start' in items:
            q = q.where(TGood.coinable_number >= items['coinable_number_start'])
        if 'coinable_number_end' in items:
            q = q.where(TGood.coinable_number <= items['coinable_number_end'])
        
        if 'is_package' in items:
            q = q.where(TGood.is_package == items['is_package'])
        if 'is_package_start' in items:
            q = q.where(TGood.is_package >= items['is_package_start'])
        if 'is_package_end' in items:
            q = q.where(TGood.is_package <= items['is_package_end'])
        
        if 'fake_owner_name' in items:
            q = q.where(TGood.fake_owner_name == items['fake_owner_name'])
        if 'fake_owner_name_start' in items:
            q = q.where(TGood.fake_owner_name >= items['fake_owner_name_start'])
        if 'fake_owner_name_end' in items:
            q = q.where(TGood.fake_owner_name <= items['fake_owner_name_end'])
        
        if 'fake_owner_phone' in items:
            q = q.where(TGood.fake_owner_phone == items['fake_owner_phone'])
        if 'fake_owner_phone_start' in items:
            q = q.where(TGood.fake_owner_phone >= items['fake_owner_phone_start'])
        if 'fake_owner_phone_end' in items:
            q = q.where(TGood.fake_owner_phone <= items['fake_owner_phone_end'])
        
        if 'unavailable_date' in items:
            q = q.where(TGood.unavailable_date == items['unavailable_date'])
        if 'unavailable_date_start' in items:
            q = q.where(TGood.unavailable_date >= items['unavailable_date_start'])
        if 'unavailable_date_end' in items:
            q = q.where(TGood.unavailable_date <= items['unavailable_date_end'])
        
        if 'available_time' in items:
            q = q.where(TGood.available_time == items['available_time'])
        if 'available_time_start' in items:
            q = q.where(TGood.available_time >= items['available_time_start'])
        if 'available_time_end' in items:
            q = q.where(TGood.available_time <= items['available_time_end'])
        
        if 'usage_rule' in items:
            q = q.where(TGood.usage_rule == items['usage_rule'])
        if 'usage_rule_start' in items:
            q = q.where(TGood.usage_rule >= items['usage_rule_start'])
        if 'usage_rule_end' in items:
            q = q.where(TGood.usage_rule <= items['usage_rule_end'])
        
        if 'refund_rule' in items:
            q = q.where(TGood.refund_rule == items['refund_rule'])
        if 'refund_rule_start' in items:
            q = q.where(TGood.refund_rule >= items['refund_rule_start'])
        if 'refund_rule_end' in items:
            q = q.where(TGood.refund_rule <= items['refund_rule_end'])
        
        if 'order_expired_time' in items:
            q = q.where(TGood.order_expired_time == items['order_expired_time'])
        if 'order_expired_time_start' in items:
            q = q.where(TGood.order_expired_time >= items['order_expired_time_start'])
        if 'order_expired_time_end' in items:
            q = q.where(TGood.order_expired_time <= items['order_expired_time_end'])
        
        if 'cover_url' in items:
            q = q.where(TGood.cover_url == items['cover_url'])
        if 'cover_url_start' in items:
            q = q.where(TGood.cover_url >= items['cover_url_start'])
        if 'cover_url_end' in items:
            q = q.where(TGood.cover_url <= items['cover_url_end'])
        
        if 'video_url' in items:
            q = q.where(TGood.video_url == items['video_url'])
        if 'video_url_start' in items:
            q = q.where(TGood.video_url >= items['video_url_start'])
        if 'video_url_end' in items:
            q = q.where(TGood.video_url <= items['video_url_end'])
        

        if 'id' in set_items:
            q = q.where(TGood.id.in_(set_items['id']))
        
        if 'name' in set_items:
            q = q.where(TGood.name.in_(set_items['name']))
        
        if 'is_flash_sale' in set_items:
            q = q.where(TGood.is_flash_sale.in_(set_items['is_flash_sale']))
        
        if 'category_id' in set_items:
            q = q.where(TGood.category_id.in_(set_items['category_id']))
        
        if 'type' in set_items:
            q = q.where(TGood.type.in_(set_items['type']))
        
        if 'num_sale' in set_items:
            q = q.where(TGood.num_sale.in_(set_items['num_sale']))
        
        if 'image_url' in set_items:
            q = q.where(TGood.image_url.in_(set_items['image_url']))
        
        if 'priority' in set_items:
            q = q.where(TGood.priority.in_(set_items['priority']))
        
        if 'add_coin' in set_items:
            q = q.where(TGood.add_coin.in_(set_items['add_coin']))
        
        if 'model_id' in set_items:
            q = q.where(TGood.model_id.in_(set_items['model_id']))
        
        if 'expired_time' in set_items:
            q = q.where(TGood.expired_time.in_(set_items['expired_time']))
        
        if 'parent_good_id' in set_items:
            q = q.where(TGood.parent_good_id.in_(set_items['parent_good_id']))
        
        if 'title' in set_items:
            q = q.where(TGood.title.in_(set_items['title']))
        
        if 'subtitle' in set_items:
            q = q.where(TGood.subtitle.in_(set_items['subtitle']))
        
        if 'stock_cordon' in set_items:
            q = q.where(TGood.stock_cordon.in_(set_items['stock_cordon']))
        
        if 'status' in set_items:
            q = q.where(TGood.status.in_(set_items['status']))
        
        if 'details' in set_items:
            q = q.where(TGood.details.in_(set_items['details']))
        
        if 'supplier_id' in set_items:
            q = q.where(TGood.supplier_id.in_(set_items['supplier_id']))
        
        if 'share_ratio' in set_items:
            q = q.where(TGood.share_ratio.in_(set_items['share_ratio']))
        
        if 'create_time' in set_items:
            q = q.where(TGood.create_time.in_(set_items['create_time']))
        
        if 'last_update_time' in set_items:
            q = q.where(TGood.last_update_time.in_(set_items['last_update_time']))
        
        if 'saleable' in set_items:
            q = q.where(TGood.saleable.in_(set_items['saleable']))
        
        if 'click_count' in set_items:
            q = q.where(TGood.click_count.in_(set_items['click_count']))
        
        if 'transmit_count' in set_items:
            q = q.where(TGood.transmit_count.in_(set_items['transmit_count']))
        
        if 'coinable' in set_items:
            q = q.where(TGood.coinable.in_(set_items['coinable']))
        
        if 'price_line' in set_items:
            q = q.where(TGood.price_line.in_(set_items['price_line']))
        
        if 'introducer_id' in set_items:
            q = q.where(TGood.introducer_id.in_(set_items['introducer_id']))
        
        if 'sell_high' in set_items:
            q = q.where(TGood.sell_high.in_(set_items['sell_high']))
        
        if 'sell_low' in set_items:
            q = q.where(TGood.sell_low.in_(set_items['sell_low']))
        
        if 'cost_high' in set_items:
            q = q.where(TGood.cost_high.in_(set_items['cost_high']))
        
        if 'cost_low' in set_items:
            q = q.where(TGood.cost_low.in_(set_items['cost_low']))
        
        if 'display' in set_items:
            q = q.where(TGood.display.in_(set_items['display']))
        
        if 'coinable_number' in set_items:
            q = q.where(TGood.coinable_number.in_(set_items['coinable_number']))
        
        if 'is_package' in set_items:
            q = q.where(TGood.is_package.in_(set_items['is_package']))
        
        if 'fake_owner_name' in set_items:
            q = q.where(TGood.fake_owner_name.in_(set_items['fake_owner_name']))
        
        if 'fake_owner_phone' in set_items:
            q = q.where(TGood.fake_owner_phone.in_(set_items['fake_owner_phone']))
        
        if 'unavailable_date' in set_items:
            q = q.where(TGood.unavailable_date.in_(set_items['unavailable_date']))
        
        if 'available_time' in set_items:
            q = q.where(TGood.available_time.in_(set_items['available_time']))
        
        if 'usage_rule' in set_items:
            q = q.where(TGood.usage_rule.in_(set_items['usage_rule']))
        
        if 'refund_rule' in set_items:
            q = q.where(TGood.refund_rule.in_(set_items['refund_rule']))
        
        if 'order_expired_time' in set_items:
            q = q.where(TGood.order_expired_time.in_(set_items['order_expired_time']))
        
        if 'cover_url' in set_items:
            q = q.where(TGood.cover_url.in_(set_items['cover_url']))
        
        if 'video_url' in set_items:
            q = q.where(TGood.video_url.in_(set_items['video_url']))
        

        if 'name' in search_items:
            q = q.where(TGood.name.like(search_items['name']))
        
        if 'image_url' in search_items:
            q = q.where(TGood.image_url.like(search_items['image_url']))
        
        if 'title' in search_items:
            q = q.where(TGood.title.like(search_items['title']))
        
        if 'subtitle' in search_items:
            q = q.where(TGood.subtitle.like(search_items['subtitle']))
        
        if 'details' in search_items:
            q = q.where(TGood.details.like(search_items['details']))
        
        if 'fake_owner_name' in search_items:
            q = q.where(TGood.fake_owner_name.like(search_items['fake_owner_name']))
        
        if 'fake_owner_phone' in search_items:
            q = q.where(TGood.fake_owner_phone.like(search_items['fake_owner_phone']))
        
        if 'unavailable_date' in search_items:
            q = q.where(TGood.unavailable_date.like(search_items['unavailable_date']))
        
        if 'available_time' in search_items:
            q = q.where(TGood.available_time.like(search_items['available_time']))
        
        if 'usage_rule' in search_items:
            q = q.where(TGood.usage_rule.like(search_items['usage_rule']))
        
        if 'refund_rule' in search_items:
            q = q.where(TGood.refund_rule.like(search_items['refund_rule']))
        
        if 'cover_url' in search_items:
            q = q.where(TGood.cover_url.like(search_items['cover_url']))
        
        if 'video_url' in search_items:
            q = q.where(TGood.video_url.like(search_items['video_url']))
        
    
        c = q.count()
        return c

    
def insert_good_category(item: CreateGoodCategory, db: Optional[SessionLocal] = None) -> SGoodCategory:
    data = model2dict(item)
    t = TGoodCategory(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SGoodCategory.parse_obj(t.__dict__)

    
def delete_good_category(good_category_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TGoodCategory).where(TGoodCategory.id == good_category_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodCategory).where(TGoodCategory.id == good_category_id).delete()
        db.commit()

    
def update_good_category(item: SGoodCategory, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TGoodCategory).where(TGoodCategory.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodCategory).where(TGoodCategory.id == item.id).update(data)
        db.commit()

    
def get_good_category(good_category_id: int) -> Optional[SGoodCategory]:
    with Dao() as db:
        t = db.query(TGoodCategory).where(TGoodCategory.id == good_category_id).first()
        if t:
            return SGoodCategory.parse_obj(t.__dict__)
        else:
            return None


def filter_good_category(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SGoodCategory]:
    with Dao() as db:
        q = db.query(TGoodCategory)


        if 'id' in items:
            q = q.where(TGoodCategory.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodCategory.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodCategory.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TGoodCategory.title == items['title'])
        if 'title_start' in items:
            q = q.where(TGoodCategory.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TGoodCategory.title <= items['title_end'])
        
        if 'general_id' in items:
            q = q.where(TGoodCategory.general_id == items['general_id'])
        if 'general_id_start' in items:
            q = q.where(TGoodCategory.general_id >= items['general_id_start'])
        if 'general_id_end' in items:
            q = q.where(TGoodCategory.general_id <= items['general_id_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodCategory.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TGoodCategory.title.in_(set_items['title']))
        
        if 'general_id' in set_items:
            q = q.where(TGoodCategory.general_id.in_(set_items['general_id']))
        

        if 'title' in search_items:
            q = q.where(TGoodCategory.title.like(search_items['title']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TGoodCategory.general_id.asc())
                orders.append(TGoodCategory.id.asc())
            elif val == 'desc':
                #orders.append(TGoodCategory.general_id.desc())
                orders.append(TGoodCategory.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_good_category_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SGoodCategory.parse_obj(t.__dict__) for t in t_good_category_list]


def filter_count_good_category(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TGoodCategory)


        if 'id' in items:
            q = q.where(TGoodCategory.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodCategory.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodCategory.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TGoodCategory.title == items['title'])
        if 'title_start' in items:
            q = q.where(TGoodCategory.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TGoodCategory.title <= items['title_end'])
        
        if 'general_id' in items:
            q = q.where(TGoodCategory.general_id == items['general_id'])
        if 'general_id_start' in items:
            q = q.where(TGoodCategory.general_id >= items['general_id_start'])
        if 'general_id_end' in items:
            q = q.where(TGoodCategory.general_id <= items['general_id_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodCategory.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TGoodCategory.title.in_(set_items['title']))
        
        if 'general_id' in set_items:
            q = q.where(TGoodCategory.general_id.in_(set_items['general_id']))
        

        if 'title' in search_items:
            q = q.where(TGoodCategory.title.like(search_items['title']))
        
    
        c = q.count()
        return c

    
def insert_good_image(item: CreateGoodImage, db: Optional[SessionLocal] = None) -> SGoodImage:
    data = model2dict(item)
    t = TGoodImage(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SGoodImage.parse_obj(t.__dict__)

    
def delete_good_image(good_image_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TGoodImage).where(TGoodImage.id == good_image_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodImage).where(TGoodImage.id == good_image_id).delete()
        db.commit()

    
def update_good_image(item: SGoodImage, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TGoodImage).where(TGoodImage.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodImage).where(TGoodImage.id == item.id).update(data)
        db.commit()

    
def get_good_image(good_image_id: int) -> Optional[SGoodImage]:
    with Dao() as db:
        t = db.query(TGoodImage).where(TGoodImage.id == good_image_id).first()
        if t:
            return SGoodImage.parse_obj(t.__dict__)
        else:
            return None


def filter_good_image(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SGoodImage]:
    with Dao() as db:
        q = db.query(TGoodImage)


        if 'id' in items:
            q = q.where(TGoodImage.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodImage.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodImage.id <= items['id_end'])
        
        if 'image' in items:
            q = q.where(TGoodImage.image == items['image'])
        if 'image_start' in items:
            q = q.where(TGoodImage.image >= items['image_start'])
        if 'image_end' in items:
            q = q.where(TGoodImage.image <= items['image_end'])
        
        if 'good_id' in items:
            q = q.where(TGoodImage.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TGoodImage.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TGoodImage.good_id <= items['good_id_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodImage.id.in_(set_items['id']))
        
        if 'image' in set_items:
            q = q.where(TGoodImage.image.in_(set_items['image']))
        
        if 'good_id' in set_items:
            q = q.where(TGoodImage.good_id.in_(set_items['good_id']))
        

        if 'image' in search_items:
            q = q.where(TGoodImage.image.like(search_items['image']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TGoodImage.good_id.asc())
                orders.append(TGoodImage.id.asc())
            elif val == 'desc':
                #orders.append(TGoodImage.good_id.desc())
                orders.append(TGoodImage.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_good_image_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SGoodImage.parse_obj(t.__dict__) for t in t_good_image_list]


def filter_count_good_image(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TGoodImage)


        if 'id' in items:
            q = q.where(TGoodImage.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodImage.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodImage.id <= items['id_end'])
        
        if 'image' in items:
            q = q.where(TGoodImage.image == items['image'])
        if 'image_start' in items:
            q = q.where(TGoodImage.image >= items['image_start'])
        if 'image_end' in items:
            q = q.where(TGoodImage.image <= items['image_end'])
        
        if 'good_id' in items:
            q = q.where(TGoodImage.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TGoodImage.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TGoodImage.good_id <= items['good_id_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodImage.id.in_(set_items['id']))
        
        if 'image' in set_items:
            q = q.where(TGoodImage.image.in_(set_items['image']))
        
        if 'good_id' in set_items:
            q = q.where(TGoodImage.good_id.in_(set_items['good_id']))
        

        if 'image' in search_items:
            q = q.where(TGoodImage.image.like(search_items['image']))
        
    
        c = q.count()
        return c

    
def insert_good_introducer(item: CreateGoodIntroducer, db: Optional[SessionLocal] = None) -> SGoodIntroducer:
    data = model2dict(item)
    t = TGoodIntroducer(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SGoodIntroducer.parse_obj(t.__dict__)

    
def delete_good_introducer(good_introducer_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TGoodIntroducer).where(TGoodIntroducer.id == good_introducer_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodIntroducer).where(TGoodIntroducer.id == good_introducer_id).delete()
        db.commit()

    
def update_good_introducer(item: SGoodIntroducer, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TGoodIntroducer).where(TGoodIntroducer.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodIntroducer).where(TGoodIntroducer.id == item.id).update(data)
        db.commit()

    
def get_good_introducer(good_introducer_id: int) -> Optional[SGoodIntroducer]:
    with Dao() as db:
        t = db.query(TGoodIntroducer).where(TGoodIntroducer.id == good_introducer_id).first()
        if t:
            return SGoodIntroducer.parse_obj(t.__dict__)
        else:
            return None


def filter_good_introducer(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SGoodIntroducer]:
    with Dao() as db:
        q = db.query(TGoodIntroducer)


        if 'id' in items:
            q = q.where(TGoodIntroducer.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodIntroducer.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodIntroducer.id <= items['id_end'])
        
        if 'name' in items:
            q = q.where(TGoodIntroducer.name == items['name'])
        if 'name_start' in items:
            q = q.where(TGoodIntroducer.name >= items['name_start'])
        if 'name_end' in items:
            q = q.where(TGoodIntroducer.name <= items['name_end'])
        
        if 'phone' in items:
            q = q.where(TGoodIntroducer.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TGoodIntroducer.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TGoodIntroducer.phone <= items['phone_end'])
        
        if 'address' in items:
            q = q.where(TGoodIntroducer.address == items['address'])
        if 'address_start' in items:
            q = q.where(TGoodIntroducer.address >= items['address_start'])
        if 'address_end' in items:
            q = q.where(TGoodIntroducer.address <= items['address_end'])
        
        if 'id_card' in items:
            q = q.where(TGoodIntroducer.id_card == items['id_card'])
        if 'id_card_start' in items:
            q = q.where(TGoodIntroducer.id_card >= items['id_card_start'])
        if 'id_card_end' in items:
            q = q.where(TGoodIntroducer.id_card <= items['id_card_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodIntroducer.id.in_(set_items['id']))
        
        if 'name' in set_items:
            q = q.where(TGoodIntroducer.name.in_(set_items['name']))
        
        if 'phone' in set_items:
            q = q.where(TGoodIntroducer.phone.in_(set_items['phone']))
        
        if 'address' in set_items:
            q = q.where(TGoodIntroducer.address.in_(set_items['address']))
        
        if 'id_card' in set_items:
            q = q.where(TGoodIntroducer.id_card.in_(set_items['id_card']))
        

        if 'name' in search_items:
            q = q.where(TGoodIntroducer.name.like(search_items['name']))
        
        if 'phone' in search_items:
            q = q.where(TGoodIntroducer.phone.like(search_items['phone']))
        
        if 'address' in search_items:
            q = q.where(TGoodIntroducer.address.like(search_items['address']))
        
        if 'id_card' in search_items:
            q = q.where(TGoodIntroducer.id_card.like(search_items['id_card']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TGoodIntroducer.id_card.asc())
                orders.append(TGoodIntroducer.id.asc())
            elif val == 'desc':
                #orders.append(TGoodIntroducer.id_card.desc())
                orders.append(TGoodIntroducer.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_good_introducer_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SGoodIntroducer.parse_obj(t.__dict__) for t in t_good_introducer_list]


def filter_count_good_introducer(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TGoodIntroducer)


        if 'id' in items:
            q = q.where(TGoodIntroducer.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodIntroducer.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodIntroducer.id <= items['id_end'])
        
        if 'name' in items:
            q = q.where(TGoodIntroducer.name == items['name'])
        if 'name_start' in items:
            q = q.where(TGoodIntroducer.name >= items['name_start'])
        if 'name_end' in items:
            q = q.where(TGoodIntroducer.name <= items['name_end'])
        
        if 'phone' in items:
            q = q.where(TGoodIntroducer.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TGoodIntroducer.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TGoodIntroducer.phone <= items['phone_end'])
        
        if 'address' in items:
            q = q.where(TGoodIntroducer.address == items['address'])
        if 'address_start' in items:
            q = q.where(TGoodIntroducer.address >= items['address_start'])
        if 'address_end' in items:
            q = q.where(TGoodIntroducer.address <= items['address_end'])
        
        if 'id_card' in items:
            q = q.where(TGoodIntroducer.id_card == items['id_card'])
        if 'id_card_start' in items:
            q = q.where(TGoodIntroducer.id_card >= items['id_card_start'])
        if 'id_card_end' in items:
            q = q.where(TGoodIntroducer.id_card <= items['id_card_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodIntroducer.id.in_(set_items['id']))
        
        if 'name' in set_items:
            q = q.where(TGoodIntroducer.name.in_(set_items['name']))
        
        if 'phone' in set_items:
            q = q.where(TGoodIntroducer.phone.in_(set_items['phone']))
        
        if 'address' in set_items:
            q = q.where(TGoodIntroducer.address.in_(set_items['address']))
        
        if 'id_card' in set_items:
            q = q.where(TGoodIntroducer.id_card.in_(set_items['id_card']))
        

        if 'name' in search_items:
            q = q.where(TGoodIntroducer.name.like(search_items['name']))
        
        if 'phone' in search_items:
            q = q.where(TGoodIntroducer.phone.like(search_items['phone']))
        
        if 'address' in search_items:
            q = q.where(TGoodIntroducer.address.like(search_items['address']))
        
        if 'id_card' in search_items:
            q = q.where(TGoodIntroducer.id_card.like(search_items['id_card']))
        
    
        c = q.count()
        return c

    
def insert_good_model(item: CreateGoodModel, db: Optional[SessionLocal] = None) -> SGoodModel:
    data = model2dict(item)
    t = TGoodModel(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SGoodModel.parse_obj(t.__dict__)

    
def delete_good_model(good_model_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TGoodModel).where(TGoodModel.id == good_model_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodModel).where(TGoodModel.id == good_model_id).delete()
        db.commit()

    
def update_good_model(item: SGoodModel, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TGoodModel).where(TGoodModel.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodModel).where(TGoodModel.id == item.id).update(data)
        db.commit()

    
def get_good_model(good_model_id: int) -> Optional[SGoodModel]:
    with Dao() as db:
        t = db.query(TGoodModel).where(TGoodModel.id == good_model_id).first()
        if t:
            return SGoodModel.parse_obj(t.__dict__)
        else:
            return None


def filter_good_model(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SGoodModel]:
    with Dao() as db:
        q = db.query(TGoodModel)


        if 'id' in items:
            q = q.where(TGoodModel.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodModel.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodModel.id <= items['id_end'])
        
        if 'model' in items:
            q = q.where(TGoodModel.model == items['model'])
        if 'model_start' in items:
            q = q.where(TGoodModel.model >= items['model_start'])
        if 'model_end' in items:
            q = q.where(TGoodModel.model <= items['model_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodModel.id.in_(set_items['id']))
        
        if 'model' in set_items:
            q = q.where(TGoodModel.model.in_(set_items['model']))
        

        if 'model' in search_items:
            q = q.where(TGoodModel.model.like(search_items['model']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TGoodModel.model.asc())
                orders.append(TGoodModel.id.asc())
            elif val == 'desc':
                #orders.append(TGoodModel.model.desc())
                orders.append(TGoodModel.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_good_model_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SGoodModel.parse_obj(t.__dict__) for t in t_good_model_list]


def filter_count_good_model(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TGoodModel)


        if 'id' in items:
            q = q.where(TGoodModel.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodModel.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodModel.id <= items['id_end'])
        
        if 'model' in items:
            q = q.where(TGoodModel.model == items['model'])
        if 'model_start' in items:
            q = q.where(TGoodModel.model >= items['model_start'])
        if 'model_end' in items:
            q = q.where(TGoodModel.model <= items['model_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodModel.id.in_(set_items['id']))
        
        if 'model' in set_items:
            q = q.where(TGoodModel.model.in_(set_items['model']))
        

        if 'model' in search_items:
            q = q.where(TGoodModel.model.like(search_items['model']))
        
    
        c = q.count()
        return c

    
def insert_good_package(item: CreateGoodPackage, db: Optional[SessionLocal] = None) -> SGoodPackage:
    data = model2dict(item)
    t = TGoodPackage(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SGoodPackage.parse_obj(t.__dict__)

    
def delete_good_package(good_package_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TGoodPackage).where(TGoodPackage.id == good_package_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodPackage).where(TGoodPackage.id == good_package_id).delete()
        db.commit()

    
def update_good_package(item: SGoodPackage, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TGoodPackage).where(TGoodPackage.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodPackage).where(TGoodPackage.id == item.id).update(data)
        db.commit()

    
def get_good_package(good_package_id: int) -> Optional[SGoodPackage]:
    with Dao() as db:
        t = db.query(TGoodPackage).where(TGoodPackage.id == good_package_id).first()
        if t:
            return SGoodPackage.parse_obj(t.__dict__)
        else:
            return None


def filter_good_package(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SGoodPackage]:
    with Dao() as db:
        q = db.query(TGoodPackage)


        if 'id' in items:
            q = q.where(TGoodPackage.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodPackage.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodPackage.id <= items['id_end'])
        
        if 'number' in items:
            q = q.where(TGoodPackage.number == items['number'])
        if 'number_start' in items:
            q = q.where(TGoodPackage.number >= items['number_start'])
        if 'number_end' in items:
            q = q.where(TGoodPackage.number <= items['number_end'])
        
        if 'price' in items:
            q = q.where(TGoodPackage.price == items['price'])
        if 'price_start' in items:
            q = q.where(TGoodPackage.price >= items['price_start'])
        if 'price_end' in items:
            q = q.where(TGoodPackage.price <= items['price_end'])
        
        if 'title' in items:
            q = q.where(TGoodPackage.title == items['title'])
        if 'title_start' in items:
            q = q.where(TGoodPackage.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TGoodPackage.title <= items['title_end'])
        
        if 'create_time' in items:
            q = q.where(TGoodPackage.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TGoodPackage.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TGoodPackage.create_time <= items['create_time_end'])
        
        if 'good_id' in items:
            q = q.where(TGoodPackage.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TGoodPackage.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TGoodPackage.good_id <= items['good_id_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodPackage.id.in_(set_items['id']))
        
        if 'number' in set_items:
            q = q.where(TGoodPackage.number.in_(set_items['number']))
        
        if 'price' in set_items:
            q = q.where(TGoodPackage.price.in_(set_items['price']))
        
        if 'title' in set_items:
            q = q.where(TGoodPackage.title.in_(set_items['title']))
        
        if 'create_time' in set_items:
            q = q.where(TGoodPackage.create_time.in_(set_items['create_time']))
        
        if 'good_id' in set_items:
            q = q.where(TGoodPackage.good_id.in_(set_items['good_id']))
        

        if 'number' in search_items:
            q = q.where(TGoodPackage.number.like(search_items['number']))
        
        if 'price' in search_items:
            q = q.where(TGoodPackage.price.like(search_items['price']))
        
        if 'title' in search_items:
            q = q.where(TGoodPackage.title.like(search_items['title']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TGoodPackage.good_id.asc())
                orders.append(TGoodPackage.id.asc())
            elif val == 'desc':
                #orders.append(TGoodPackage.good_id.desc())
                orders.append(TGoodPackage.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_good_package_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SGoodPackage.parse_obj(t.__dict__) for t in t_good_package_list]


def filter_count_good_package(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TGoodPackage)


        if 'id' in items:
            q = q.where(TGoodPackage.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodPackage.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodPackage.id <= items['id_end'])
        
        if 'number' in items:
            q = q.where(TGoodPackage.number == items['number'])
        if 'number_start' in items:
            q = q.where(TGoodPackage.number >= items['number_start'])
        if 'number_end' in items:
            q = q.where(TGoodPackage.number <= items['number_end'])
        
        if 'price' in items:
            q = q.where(TGoodPackage.price == items['price'])
        if 'price_start' in items:
            q = q.where(TGoodPackage.price >= items['price_start'])
        if 'price_end' in items:
            q = q.where(TGoodPackage.price <= items['price_end'])
        
        if 'title' in items:
            q = q.where(TGoodPackage.title == items['title'])
        if 'title_start' in items:
            q = q.where(TGoodPackage.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TGoodPackage.title <= items['title_end'])
        
        if 'create_time' in items:
            q = q.where(TGoodPackage.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TGoodPackage.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TGoodPackage.create_time <= items['create_time_end'])
        
        if 'good_id' in items:
            q = q.where(TGoodPackage.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TGoodPackage.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TGoodPackage.good_id <= items['good_id_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodPackage.id.in_(set_items['id']))
        
        if 'number' in set_items:
            q = q.where(TGoodPackage.number.in_(set_items['number']))
        
        if 'price' in set_items:
            q = q.where(TGoodPackage.price.in_(set_items['price']))
        
        if 'title' in set_items:
            q = q.where(TGoodPackage.title.in_(set_items['title']))
        
        if 'create_time' in set_items:
            q = q.where(TGoodPackage.create_time.in_(set_items['create_time']))
        
        if 'good_id' in set_items:
            q = q.where(TGoodPackage.good_id.in_(set_items['good_id']))
        

        if 'number' in search_items:
            q = q.where(TGoodPackage.number.like(search_items['number']))
        
        if 'price' in search_items:
            q = q.where(TGoodPackage.price.like(search_items['price']))
        
        if 'title' in search_items:
            q = q.where(TGoodPackage.title.like(search_items['title']))
        
    
        c = q.count()
        return c

    
def insert_good_person(item: CreateGoodPerson, db: Optional[SessionLocal] = None) -> SGoodPerson:
    data = model2dict(item)
    t = TGoodPerson(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SGoodPerson.parse_obj(t.__dict__)

    
def delete_good_person(good_person_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TGoodPerson).where(TGoodPerson.id == good_person_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodPerson).where(TGoodPerson.id == good_person_id).delete()
        db.commit()

    
def update_good_person(item: SGoodPerson, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TGoodPerson).where(TGoodPerson.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodPerson).where(TGoodPerson.id == item.id).update(data)
        db.commit()

    
def get_good_person(good_person_id: int) -> Optional[SGoodPerson]:
    with Dao() as db:
        t = db.query(TGoodPerson).where(TGoodPerson.id == good_person_id).first()
        if t:
            return SGoodPerson.parse_obj(t.__dict__)
        else:
            return None


def filter_good_person(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SGoodPerson]:
    with Dao() as db:
        q = db.query(TGoodPerson)


        if 'id' in items:
            q = q.where(TGoodPerson.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodPerson.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodPerson.id <= items['id_end'])
        
        if 'good_id' in items:
            q = q.where(TGoodPerson.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TGoodPerson.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TGoodPerson.good_id <= items['good_id_end'])
        
        if 'person_id' in items:
            q = q.where(TGoodPerson.person_id == items['person_id'])
        if 'person_id_start' in items:
            q = q.where(TGoodPerson.person_id >= items['person_id_start'])
        if 'person_id_end' in items:
            q = q.where(TGoodPerson.person_id <= items['person_id_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodPerson.id.in_(set_items['id']))
        
        if 'good_id' in set_items:
            q = q.where(TGoodPerson.good_id.in_(set_items['good_id']))
        
        if 'person_id' in set_items:
            q = q.where(TGoodPerson.person_id.in_(set_items['person_id']))
        

    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TGoodPerson.person_id.asc())
                orders.append(TGoodPerson.id.asc())
            elif val == 'desc':
                #orders.append(TGoodPerson.person_id.desc())
                orders.append(TGoodPerson.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_good_person_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SGoodPerson.parse_obj(t.__dict__) for t in t_good_person_list]


def filter_count_good_person(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TGoodPerson)


        if 'id' in items:
            q = q.where(TGoodPerson.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodPerson.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodPerson.id <= items['id_end'])
        
        if 'good_id' in items:
            q = q.where(TGoodPerson.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TGoodPerson.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TGoodPerson.good_id <= items['good_id_end'])
        
        if 'person_id' in items:
            q = q.where(TGoodPerson.person_id == items['person_id'])
        if 'person_id_start' in items:
            q = q.where(TGoodPerson.person_id >= items['person_id_start'])
        if 'person_id_end' in items:
            q = q.where(TGoodPerson.person_id <= items['person_id_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodPerson.id.in_(set_items['id']))
        
        if 'good_id' in set_items:
            q = q.where(TGoodPerson.good_id.in_(set_items['good_id']))
        
        if 'person_id' in set_items:
            q = q.where(TGoodPerson.person_id.in_(set_items['person_id']))
        

    
        c = q.count()
        return c

    
def insert_good_person_state(item: CreateGoodPersonState, db: Optional[SessionLocal] = None) -> SGoodPersonState:
    data = model2dict(item)
    t = TGoodPersonState(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SGoodPersonState.parse_obj(t.__dict__)

    
def delete_good_person_state(good_person_state_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TGoodPersonState).where(TGoodPersonState.id == good_person_state_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodPersonState).where(TGoodPersonState.id == good_person_state_id).delete()
        db.commit()

    
def update_good_person_state(item: SGoodPersonState, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TGoodPersonState).where(TGoodPersonState.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodPersonState).where(TGoodPersonState.id == item.id).update(data)
        db.commit()

    
def get_good_person_state(good_person_state_id: int) -> Optional[SGoodPersonState]:
    with Dao() as db:
        t = db.query(TGoodPersonState).where(TGoodPersonState.id == good_person_state_id).first()
        if t:
            return SGoodPersonState.parse_obj(t.__dict__)
        else:
            return None


def filter_good_person_state(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SGoodPersonState]:
    with Dao() as db:
        q = db.query(TGoodPersonState)


        if 'id' in items:
            q = q.where(TGoodPersonState.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodPersonState.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodPersonState.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TGoodPersonState.title == items['title'])
        if 'title_start' in items:
            q = q.where(TGoodPersonState.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TGoodPersonState.title <= items['title_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodPersonState.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TGoodPersonState.title.in_(set_items['title']))
        

        if 'title' in search_items:
            q = q.where(TGoodPersonState.title.like(search_items['title']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TGoodPersonState.title.asc())
                orders.append(TGoodPersonState.id.asc())
            elif val == 'desc':
                #orders.append(TGoodPersonState.title.desc())
                orders.append(TGoodPersonState.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_good_person_state_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SGoodPersonState.parse_obj(t.__dict__) for t in t_good_person_state_list]


def filter_count_good_person_state(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TGoodPersonState)


        if 'id' in items:
            q = q.where(TGoodPersonState.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodPersonState.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodPersonState.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TGoodPersonState.title == items['title'])
        if 'title_start' in items:
            q = q.where(TGoodPersonState.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TGoodPersonState.title <= items['title_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodPersonState.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TGoodPersonState.title.in_(set_items['title']))
        

        if 'title' in search_items:
            q = q.where(TGoodPersonState.title.like(search_items['title']))
        
    
        c = q.count()
        return c

    
def insert_good_priority(item: CreateGoodPriority, db: Optional[SessionLocal] = None) -> SGoodPriority:
    data = model2dict(item)
    t = TGoodPriority(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SGoodPriority.parse_obj(t.__dict__)

    
def delete_good_priority(good_priority_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TGoodPriority).where(TGoodPriority.id == good_priority_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodPriority).where(TGoodPriority.id == good_priority_id).delete()
        db.commit()

    
def update_good_priority(item: SGoodPriority, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TGoodPriority).where(TGoodPriority.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodPriority).where(TGoodPriority.id == item.id).update(data)
        db.commit()

    
def get_good_priority(good_priority_id: int) -> Optional[SGoodPriority]:
    with Dao() as db:
        t = db.query(TGoodPriority).where(TGoodPriority.id == good_priority_id).first()
        if t:
            return SGoodPriority.parse_obj(t.__dict__)
        else:
            return None


def filter_good_priority(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SGoodPriority]:
    with Dao() as db:
        q = db.query(TGoodPriority)


        if 'id' in items:
            q = q.where(TGoodPriority.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodPriority.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodPriority.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TGoodPriority.title == items['title'])
        if 'title_start' in items:
            q = q.where(TGoodPriority.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TGoodPriority.title <= items['title_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodPriority.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TGoodPriority.title.in_(set_items['title']))
        

        if 'title' in search_items:
            q = q.where(TGoodPriority.title.like(search_items['title']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TGoodPriority.title.asc())
                orders.append(TGoodPriority.id.asc())
            elif val == 'desc':
                #orders.append(TGoodPriority.title.desc())
                orders.append(TGoodPriority.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_good_priority_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SGoodPriority.parse_obj(t.__dict__) for t in t_good_priority_list]


def filter_count_good_priority(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TGoodPriority)


        if 'id' in items:
            q = q.where(TGoodPriority.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodPriority.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodPriority.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TGoodPriority.title == items['title'])
        if 'title_start' in items:
            q = q.where(TGoodPriority.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TGoodPriority.title <= items['title_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodPriority.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TGoodPriority.title.in_(set_items['title']))
        

        if 'title' in search_items:
            q = q.where(TGoodPriority.title.like(search_items['title']))
        
    
        c = q.count()
        return c

    
def insert_good_rule(item: CreateGoodRule, db: Optional[SessionLocal] = None) -> SGoodRule:
    data = model2dict(item)
    t = TGoodRule(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SGoodRule.parse_obj(t.__dict__)

    
def delete_good_rule(good_rule_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TGoodRule).where(TGoodRule.id == good_rule_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodRule).where(TGoodRule.id == good_rule_id).delete()
        db.commit()

    
def update_good_rule(item: SGoodRule, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TGoodRule).where(TGoodRule.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodRule).where(TGoodRule.id == item.id).update(data)
        db.commit()

    
def get_good_rule(good_rule_id: int) -> Optional[SGoodRule]:
    with Dao() as db:
        t = db.query(TGoodRule).where(TGoodRule.id == good_rule_id).first()
        if t:
            return SGoodRule.parse_obj(t.__dict__)
        else:
            return None


def filter_good_rule(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SGoodRule]:
    with Dao() as db:
        q = db.query(TGoodRule)


        if 'id' in items:
            q = q.where(TGoodRule.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodRule.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodRule.id <= items['id_end'])
        
        if 'good_id' in items:
            q = q.where(TGoodRule.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TGoodRule.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TGoodRule.good_id <= items['good_id_end'])
        
        if 'create_time' in items:
            q = q.where(TGoodRule.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TGoodRule.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TGoodRule.create_time <= items['create_time_end'])
        
        if 'validate_day' in items:
            q = q.where(TGoodRule.validate_day == items['validate_day'])
        if 'validate_day_start' in items:
            q = q.where(TGoodRule.validate_day >= items['validate_day_start'])
        if 'validate_day_end' in items:
            q = q.where(TGoodRule.validate_day <= items['validate_day_end'])
        
        if 'unuseful_day' in items:
            q = q.where(TGoodRule.unuseful_day == items['unuseful_day'])
        if 'unuseful_day_start' in items:
            q = q.where(TGoodRule.unuseful_day >= items['unuseful_day_start'])
        if 'unuseful_day_end' in items:
            q = q.where(TGoodRule.unuseful_day <= items['unuseful_day_end'])
        
        if 'useful_time' in items:
            q = q.where(TGoodRule.useful_time == items['useful_time'])
        if 'useful_time_start' in items:
            q = q.where(TGoodRule.useful_time >= items['useful_time_start'])
        if 'useful_time_end' in items:
            q = q.where(TGoodRule.useful_time <= items['useful_time_end'])
        
        if 'use_rule' in items:
            q = q.where(TGoodRule.use_rule == items['use_rule'])
        if 'use_rule_start' in items:
            q = q.where(TGoodRule.use_rule >= items['use_rule_start'])
        if 'use_rule_end' in items:
            q = q.where(TGoodRule.use_rule <= items['use_rule_end'])
        
        if 'return_rule' in items:
            q = q.where(TGoodRule.return_rule == items['return_rule'])
        if 'return_rule_start' in items:
            q = q.where(TGoodRule.return_rule >= items['return_rule_start'])
        if 'return_rule_end' in items:
            q = q.where(TGoodRule.return_rule <= items['return_rule_end'])
        
        if 'room' in items:
            q = q.where(TGoodRule.room == items['room'])
        if 'room_start' in items:
            q = q.where(TGoodRule.room >= items['room_start'])
        if 'room_end' in items:
            q = q.where(TGoodRule.room <= items['room_end'])
        
        if 'title' in items:
            q = q.where(TGoodRule.title == items['title'])
        if 'title_start' in items:
            q = q.where(TGoodRule.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TGoodRule.title <= items['title_end'])
        
        if 'value' in items:
            q = q.where(TGoodRule.value == items['value'])
        if 'value_start' in items:
            q = q.where(TGoodRule.value >= items['value_start'])
        if 'value_end' in items:
            q = q.where(TGoodRule.value <= items['value_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodRule.id.in_(set_items['id']))
        
        if 'good_id' in set_items:
            q = q.where(TGoodRule.good_id.in_(set_items['good_id']))
        
        if 'create_time' in set_items:
            q = q.where(TGoodRule.create_time.in_(set_items['create_time']))
        
        if 'validate_day' in set_items:
            q = q.where(TGoodRule.validate_day.in_(set_items['validate_day']))
        
        if 'unuseful_day' in set_items:
            q = q.where(TGoodRule.unuseful_day.in_(set_items['unuseful_day']))
        
        if 'useful_time' in set_items:
            q = q.where(TGoodRule.useful_time.in_(set_items['useful_time']))
        
        if 'use_rule' in set_items:
            q = q.where(TGoodRule.use_rule.in_(set_items['use_rule']))
        
        if 'return_rule' in set_items:
            q = q.where(TGoodRule.return_rule.in_(set_items['return_rule']))
        
        if 'room' in set_items:
            q = q.where(TGoodRule.room.in_(set_items['room']))
        
        if 'title' in set_items:
            q = q.where(TGoodRule.title.in_(set_items['title']))
        
        if 'value' in set_items:
            q = q.where(TGoodRule.value.in_(set_items['value']))
        

        if 'validate_day' in search_items:
            q = q.where(TGoodRule.validate_day.like(search_items['validate_day']))
        
        if 'unuseful_day' in search_items:
            q = q.where(TGoodRule.unuseful_day.like(search_items['unuseful_day']))
        
        if 'useful_time' in search_items:
            q = q.where(TGoodRule.useful_time.like(search_items['useful_time']))
        
        if 'use_rule' in search_items:
            q = q.where(TGoodRule.use_rule.like(search_items['use_rule']))
        
        if 'return_rule' in search_items:
            q = q.where(TGoodRule.return_rule.like(search_items['return_rule']))
        
        if 'title' in search_items:
            q = q.where(TGoodRule.title.like(search_items['title']))
        
        if 'value' in search_items:
            q = q.where(TGoodRule.value.like(search_items['value']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TGoodRule.value.asc())
                orders.append(TGoodRule.id.asc())
            elif val == 'desc':
                #orders.append(TGoodRule.value.desc())
                orders.append(TGoodRule.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_good_rule_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SGoodRule.parse_obj(t.__dict__) for t in t_good_rule_list]


def filter_count_good_rule(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TGoodRule)


        if 'id' in items:
            q = q.where(TGoodRule.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodRule.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodRule.id <= items['id_end'])
        
        if 'good_id' in items:
            q = q.where(TGoodRule.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TGoodRule.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TGoodRule.good_id <= items['good_id_end'])
        
        if 'create_time' in items:
            q = q.where(TGoodRule.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TGoodRule.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TGoodRule.create_time <= items['create_time_end'])
        
        if 'validate_day' in items:
            q = q.where(TGoodRule.validate_day == items['validate_day'])
        if 'validate_day_start' in items:
            q = q.where(TGoodRule.validate_day >= items['validate_day_start'])
        if 'validate_day_end' in items:
            q = q.where(TGoodRule.validate_day <= items['validate_day_end'])
        
        if 'unuseful_day' in items:
            q = q.where(TGoodRule.unuseful_day == items['unuseful_day'])
        if 'unuseful_day_start' in items:
            q = q.where(TGoodRule.unuseful_day >= items['unuseful_day_start'])
        if 'unuseful_day_end' in items:
            q = q.where(TGoodRule.unuseful_day <= items['unuseful_day_end'])
        
        if 'useful_time' in items:
            q = q.where(TGoodRule.useful_time == items['useful_time'])
        if 'useful_time_start' in items:
            q = q.where(TGoodRule.useful_time >= items['useful_time_start'])
        if 'useful_time_end' in items:
            q = q.where(TGoodRule.useful_time <= items['useful_time_end'])
        
        if 'use_rule' in items:
            q = q.where(TGoodRule.use_rule == items['use_rule'])
        if 'use_rule_start' in items:
            q = q.where(TGoodRule.use_rule >= items['use_rule_start'])
        if 'use_rule_end' in items:
            q = q.where(TGoodRule.use_rule <= items['use_rule_end'])
        
        if 'return_rule' in items:
            q = q.where(TGoodRule.return_rule == items['return_rule'])
        if 'return_rule_start' in items:
            q = q.where(TGoodRule.return_rule >= items['return_rule_start'])
        if 'return_rule_end' in items:
            q = q.where(TGoodRule.return_rule <= items['return_rule_end'])
        
        if 'room' in items:
            q = q.where(TGoodRule.room == items['room'])
        if 'room_start' in items:
            q = q.where(TGoodRule.room >= items['room_start'])
        if 'room_end' in items:
            q = q.where(TGoodRule.room <= items['room_end'])
        
        if 'title' in items:
            q = q.where(TGoodRule.title == items['title'])
        if 'title_start' in items:
            q = q.where(TGoodRule.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TGoodRule.title <= items['title_end'])
        
        if 'value' in items:
            q = q.where(TGoodRule.value == items['value'])
        if 'value_start' in items:
            q = q.where(TGoodRule.value >= items['value_start'])
        if 'value_end' in items:
            q = q.where(TGoodRule.value <= items['value_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodRule.id.in_(set_items['id']))
        
        if 'good_id' in set_items:
            q = q.where(TGoodRule.good_id.in_(set_items['good_id']))
        
        if 'create_time' in set_items:
            q = q.where(TGoodRule.create_time.in_(set_items['create_time']))
        
        if 'validate_day' in set_items:
            q = q.where(TGoodRule.validate_day.in_(set_items['validate_day']))
        
        if 'unuseful_day' in set_items:
            q = q.where(TGoodRule.unuseful_day.in_(set_items['unuseful_day']))
        
        if 'useful_time' in set_items:
            q = q.where(TGoodRule.useful_time.in_(set_items['useful_time']))
        
        if 'use_rule' in set_items:
            q = q.where(TGoodRule.use_rule.in_(set_items['use_rule']))
        
        if 'return_rule' in set_items:
            q = q.where(TGoodRule.return_rule.in_(set_items['return_rule']))
        
        if 'room' in set_items:
            q = q.where(TGoodRule.room.in_(set_items['room']))
        
        if 'title' in set_items:
            q = q.where(TGoodRule.title.in_(set_items['title']))
        
        if 'value' in set_items:
            q = q.where(TGoodRule.value.in_(set_items['value']))
        

        if 'validate_day' in search_items:
            q = q.where(TGoodRule.validate_day.like(search_items['validate_day']))
        
        if 'unuseful_day' in search_items:
            q = q.where(TGoodRule.unuseful_day.like(search_items['unuseful_day']))
        
        if 'useful_time' in search_items:
            q = q.where(TGoodRule.useful_time.like(search_items['useful_time']))
        
        if 'use_rule' in search_items:
            q = q.where(TGoodRule.use_rule.like(search_items['use_rule']))
        
        if 'return_rule' in search_items:
            q = q.where(TGoodRule.return_rule.like(search_items['return_rule']))
        
        if 'title' in search_items:
            q = q.where(TGoodRule.title.like(search_items['title']))
        
        if 'value' in search_items:
            q = q.where(TGoodRule.value.like(search_items['value']))
        
    
        c = q.count()
        return c

    
def insert_good_spec(item: CreateGoodSpec, db: Optional[SessionLocal] = None) -> SGoodSpec:
    data = model2dict(item)
    t = TGoodSpec(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SGoodSpec.parse_obj(t.__dict__)

    
def delete_good_spec(good_spec_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TGoodSpec).where(TGoodSpec.id == good_spec_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodSpec).where(TGoodSpec.id == good_spec_id).delete()
        db.commit()

    
def update_good_spec(item: SGoodSpec, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TGoodSpec).where(TGoodSpec.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodSpec).where(TGoodSpec.id == item.id).update(data)
        db.commit()

    
def get_good_spec(good_spec_id: int) -> Optional[SGoodSpec]:
    with Dao() as db:
        t = db.query(TGoodSpec).where(TGoodSpec.id == good_spec_id).first()
        if t:
            return SGoodSpec.parse_obj(t.__dict__)
        else:
            return None


def filter_good_spec(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SGoodSpec]:
    with Dao() as db:
        q = db.query(TGoodSpec)


        if 'good_id' in items:
            q = q.where(TGoodSpec.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TGoodSpec.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TGoodSpec.good_id <= items['good_id_end'])
        
        if 'price' in items:
            q = q.where(TGoodSpec.price == items['price'])
        if 'price_start' in items:
            q = q.where(TGoodSpec.price >= items['price_start'])
        if 'price_end' in items:
            q = q.where(TGoodSpec.price <= items['price_end'])
        
        if 'cost' in items:
            q = q.where(TGoodSpec.cost == items['cost'])
        if 'cost_start' in items:
            q = q.where(TGoodSpec.cost >= items['cost_start'])
        if 'cost_end' in items:
            q = q.where(TGoodSpec.cost <= items['cost_end'])
        
        if 'value' in items:
            q = q.where(TGoodSpec.value == items['value'])
        if 'value_start' in items:
            q = q.where(TGoodSpec.value >= items['value_start'])
        if 'value_end' in items:
            q = q.where(TGoodSpec.value <= items['value_end'])
        
        if 'id' in items:
            q = q.where(TGoodSpec.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodSpec.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodSpec.id <= items['id_end'])
        
        if 'stock' in items:
            q = q.where(TGoodSpec.stock == items['stock'])
        if 'stock_start' in items:
            q = q.where(TGoodSpec.stock >= items['stock_start'])
        if 'stock_end' in items:
            q = q.where(TGoodSpec.stock <= items['stock_end'])
        
        if 'price_line' in items:
            q = q.where(TGoodSpec.price_line == items['price_line'])
        if 'price_line_start' in items:
            q = q.where(TGoodSpec.price_line >= items['price_line_start'])
        if 'price_line_end' in items:
            q = q.where(TGoodSpec.price_line <= items['price_line_end'])
        
        if 'image' in items:
            q = q.where(TGoodSpec.image == items['image'])
        if 'image_start' in items:
            q = q.where(TGoodSpec.image >= items['image_start'])
        if 'image_end' in items:
            q = q.where(TGoodSpec.image <= items['image_end'])
        
        if 'is_sub_good' in items:
            q = q.where(TGoodSpec.is_sub_good == items['is_sub_good'])
        if 'is_sub_good_start' in items:
            q = q.where(TGoodSpec.is_sub_good >= items['is_sub_good_start'])
        if 'is_sub_good_end' in items:
            q = q.where(TGoodSpec.is_sub_good <= items['is_sub_good_end'])
        
        if 'num_sale' in items:
            q = q.where(TGoodSpec.num_sale == items['num_sale'])
        if 'num_sale_start' in items:
            q = q.where(TGoodSpec.num_sale >= items['num_sale_start'])
        if 'num_sale_end' in items:
            q = q.where(TGoodSpec.num_sale <= items['num_sale_end'])
        
        if 'parent_fee' in items:
            q = q.where(TGoodSpec.parent_fee == items['parent_fee'])
        if 'parent_fee_start' in items:
            q = q.where(TGoodSpec.parent_fee >= items['parent_fee_start'])
        if 'parent_fee_end' in items:
            q = q.where(TGoodSpec.parent_fee <= items['parent_fee_end'])
        
        if 'top_fee' in items:
            q = q.where(TGoodSpec.top_fee == items['top_fee'])
        if 'top_fee_start' in items:
            q = q.where(TGoodSpec.top_fee >= items['top_fee_start'])
        if 'top_fee_end' in items:
            q = q.where(TGoodSpec.top_fee <= items['top_fee_end'])
        
        if 'recommender_fee' in items:
            q = q.where(TGoodSpec.recommender_fee == items['recommender_fee'])
        if 'recommender_fee_start' in items:
            q = q.where(TGoodSpec.recommender_fee >= items['recommender_fee_start'])
        if 'recommender_fee_end' in items:
            q = q.where(TGoodSpec.recommender_fee <= items['recommender_fee_end'])
        
        if 'supplier_fee' in items:
            q = q.where(TGoodSpec.supplier_fee == items['supplier_fee'])
        if 'supplier_fee_start' in items:
            q = q.where(TGoodSpec.supplier_fee >= items['supplier_fee_start'])
        if 'supplier_fee_end' in items:
            q = q.where(TGoodSpec.supplier_fee <= items['supplier_fee_end'])
        
        if 'lower_num_people' in items:
            q = q.where(TGoodSpec.lower_num_people == items['lower_num_people'])
        if 'lower_num_people_start' in items:
            q = q.where(TGoodSpec.lower_num_people >= items['lower_num_people_start'])
        if 'lower_num_people_end' in items:
            q = q.where(TGoodSpec.lower_num_people <= items['lower_num_people_end'])
        
        if 'upper_num_people' in items:
            q = q.where(TGoodSpec.upper_num_people == items['upper_num_people'])
        if 'upper_num_people_start' in items:
            q = q.where(TGoodSpec.upper_num_people >= items['upper_num_people_start'])
        if 'upper_num_people_end' in items:
            q = q.where(TGoodSpec.upper_num_people <= items['upper_num_people_end'])
        
        if 'room' in items:
            q = q.where(TGoodSpec.room == items['room'])
        if 'room_start' in items:
            q = q.where(TGoodSpec.room >= items['room_start'])
        if 'room_end' in items:
            q = q.where(TGoodSpec.room <= items['room_end'])
        
        if 'post' in items:
            q = q.where(TGoodSpec.post == items['post'])
        if 'post_start' in items:
            q = q.where(TGoodSpec.post >= items['post_start'])
        if 'post_end' in items:
            q = q.where(TGoodSpec.post <= items['post_end'])
        
        if 'status' in items:
            q = q.where(TGoodSpec.status == items['status'])
        if 'status_start' in items:
            q = q.where(TGoodSpec.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TGoodSpec.status <= items['status_end'])
        
        if 'share_fee' in items:
            q = q.where(TGoodSpec.share_fee == items['share_fee'])
        if 'share_fee_start' in items:
            q = q.where(TGoodSpec.share_fee >= items['share_fee_start'])
        if 'share_fee_end' in items:
            q = q.where(TGoodSpec.share_fee <= items['share_fee_end'])
        
        if 'is_default' in items:
            q = q.where(TGoodSpec.is_default == items['is_default'])
        if 'is_default_start' in items:
            q = q.where(TGoodSpec.is_default >= items['is_default_start'])
        if 'is_default_end' in items:
            q = q.where(TGoodSpec.is_default <= items['is_default_end'])
        
        if 'spec_num' in items:
            q = q.where(TGoodSpec.spec_num == items['spec_num'])
        if 'spec_num_start' in items:
            q = q.where(TGoodSpec.spec_num >= items['spec_num_start'])
        if 'spec_num_end' in items:
            q = q.where(TGoodSpec.spec_num <= items['spec_num_end'])
        
        if 'profit' in items:
            q = q.where(TGoodSpec.profit == items['profit'])
        if 'profit_start' in items:
            q = q.where(TGoodSpec.profit >= items['profit_start'])
        if 'profit_end' in items:
            q = q.where(TGoodSpec.profit <= items['profit_end'])
        
        if 'eqlevel_fee' in items:
            q = q.where(TGoodSpec.eqlevel_fee == items['eqlevel_fee'])
        if 'eqlevel_fee_start' in items:
            q = q.where(TGoodSpec.eqlevel_fee >= items['eqlevel_fee_start'])
        if 'eqlevel_fee_end' in items:
            q = q.where(TGoodSpec.eqlevel_fee <= items['eqlevel_fee_end'])
        

        if 'good_id' in set_items:
            q = q.where(TGoodSpec.good_id.in_(set_items['good_id']))
        
        if 'price' in set_items:
            q = q.where(TGoodSpec.price.in_(set_items['price']))
        
        if 'cost' in set_items:
            q = q.where(TGoodSpec.cost.in_(set_items['cost']))
        
        if 'value' in set_items:
            q = q.where(TGoodSpec.value.in_(set_items['value']))
        
        if 'id' in set_items:
            q = q.where(TGoodSpec.id.in_(set_items['id']))
        
        if 'stock' in set_items:
            q = q.where(TGoodSpec.stock.in_(set_items['stock']))
        
        if 'price_line' in set_items:
            q = q.where(TGoodSpec.price_line.in_(set_items['price_line']))
        
        if 'image' in set_items:
            q = q.where(TGoodSpec.image.in_(set_items['image']))
        
        if 'is_sub_good' in set_items:
            q = q.where(TGoodSpec.is_sub_good.in_(set_items['is_sub_good']))
        
        if 'num_sale' in set_items:
            q = q.where(TGoodSpec.num_sale.in_(set_items['num_sale']))
        
        if 'parent_fee' in set_items:
            q = q.where(TGoodSpec.parent_fee.in_(set_items['parent_fee']))
        
        if 'top_fee' in set_items:
            q = q.where(TGoodSpec.top_fee.in_(set_items['top_fee']))
        
        if 'recommender_fee' in set_items:
            q = q.where(TGoodSpec.recommender_fee.in_(set_items['recommender_fee']))
        
        if 'supplier_fee' in set_items:
            q = q.where(TGoodSpec.supplier_fee.in_(set_items['supplier_fee']))
        
        if 'lower_num_people' in set_items:
            q = q.where(TGoodSpec.lower_num_people.in_(set_items['lower_num_people']))
        
        if 'upper_num_people' in set_items:
            q = q.where(TGoodSpec.upper_num_people.in_(set_items['upper_num_people']))
        
        if 'room' in set_items:
            q = q.where(TGoodSpec.room.in_(set_items['room']))
        
        if 'post' in set_items:
            q = q.where(TGoodSpec.post.in_(set_items['post']))
        
        if 'status' in set_items:
            q = q.where(TGoodSpec.status.in_(set_items['status']))
        
        if 'share_fee' in set_items:
            q = q.where(TGoodSpec.share_fee.in_(set_items['share_fee']))
        
        if 'is_default' in set_items:
            q = q.where(TGoodSpec.is_default.in_(set_items['is_default']))
        
        if 'spec_num' in set_items:
            q = q.where(TGoodSpec.spec_num.in_(set_items['spec_num']))
        
        if 'profit' in set_items:
            q = q.where(TGoodSpec.profit.in_(set_items['profit']))
        
        if 'eqlevel_fee' in set_items:
            q = q.where(TGoodSpec.eqlevel_fee.in_(set_items['eqlevel_fee']))
        

        if 'value' in search_items:
            q = q.where(TGoodSpec.value.like(search_items['value']))
        
        if 'image' in search_items:
            q = q.where(TGoodSpec.image.like(search_items['image']))
        
        if 'room' in search_items:
            q = q.where(TGoodSpec.room.like(search_items['room']))
        
        if 'post' in search_items:
            q = q.where(TGoodSpec.post.like(search_items['post']))
        
        if 'spec_num' in search_items:
            q = q.where(TGoodSpec.spec_num.like(search_items['spec_num']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TGoodSpec.eqlevel_fee.asc())
                orders.append(TGoodSpec.id.asc())
            elif val == 'desc':
                #orders.append(TGoodSpec.eqlevel_fee.desc())
                orders.append(TGoodSpec.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_good_spec_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SGoodSpec.parse_obj(t.__dict__) for t in t_good_spec_list]


def filter_count_good_spec(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TGoodSpec)


        if 'good_id' in items:
            q = q.where(TGoodSpec.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TGoodSpec.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TGoodSpec.good_id <= items['good_id_end'])
        
        if 'price' in items:
            q = q.where(TGoodSpec.price == items['price'])
        if 'price_start' in items:
            q = q.where(TGoodSpec.price >= items['price_start'])
        if 'price_end' in items:
            q = q.where(TGoodSpec.price <= items['price_end'])
        
        if 'cost' in items:
            q = q.where(TGoodSpec.cost == items['cost'])
        if 'cost_start' in items:
            q = q.where(TGoodSpec.cost >= items['cost_start'])
        if 'cost_end' in items:
            q = q.where(TGoodSpec.cost <= items['cost_end'])
        
        if 'value' in items:
            q = q.where(TGoodSpec.value == items['value'])
        if 'value_start' in items:
            q = q.where(TGoodSpec.value >= items['value_start'])
        if 'value_end' in items:
            q = q.where(TGoodSpec.value <= items['value_end'])
        
        if 'id' in items:
            q = q.where(TGoodSpec.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodSpec.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodSpec.id <= items['id_end'])
        
        if 'stock' in items:
            q = q.where(TGoodSpec.stock == items['stock'])
        if 'stock_start' in items:
            q = q.where(TGoodSpec.stock >= items['stock_start'])
        if 'stock_end' in items:
            q = q.where(TGoodSpec.stock <= items['stock_end'])
        
        if 'price_line' in items:
            q = q.where(TGoodSpec.price_line == items['price_line'])
        if 'price_line_start' in items:
            q = q.where(TGoodSpec.price_line >= items['price_line_start'])
        if 'price_line_end' in items:
            q = q.where(TGoodSpec.price_line <= items['price_line_end'])
        
        if 'image' in items:
            q = q.where(TGoodSpec.image == items['image'])
        if 'image_start' in items:
            q = q.where(TGoodSpec.image >= items['image_start'])
        if 'image_end' in items:
            q = q.where(TGoodSpec.image <= items['image_end'])
        
        if 'is_sub_good' in items:
            q = q.where(TGoodSpec.is_sub_good == items['is_sub_good'])
        if 'is_sub_good_start' in items:
            q = q.where(TGoodSpec.is_sub_good >= items['is_sub_good_start'])
        if 'is_sub_good_end' in items:
            q = q.where(TGoodSpec.is_sub_good <= items['is_sub_good_end'])
        
        if 'num_sale' in items:
            q = q.where(TGoodSpec.num_sale == items['num_sale'])
        if 'num_sale_start' in items:
            q = q.where(TGoodSpec.num_sale >= items['num_sale_start'])
        if 'num_sale_end' in items:
            q = q.where(TGoodSpec.num_sale <= items['num_sale_end'])
        
        if 'parent_fee' in items:
            q = q.where(TGoodSpec.parent_fee == items['parent_fee'])
        if 'parent_fee_start' in items:
            q = q.where(TGoodSpec.parent_fee >= items['parent_fee_start'])
        if 'parent_fee_end' in items:
            q = q.where(TGoodSpec.parent_fee <= items['parent_fee_end'])
        
        if 'top_fee' in items:
            q = q.where(TGoodSpec.top_fee == items['top_fee'])
        if 'top_fee_start' in items:
            q = q.where(TGoodSpec.top_fee >= items['top_fee_start'])
        if 'top_fee_end' in items:
            q = q.where(TGoodSpec.top_fee <= items['top_fee_end'])
        
        if 'recommender_fee' in items:
            q = q.where(TGoodSpec.recommender_fee == items['recommender_fee'])
        if 'recommender_fee_start' in items:
            q = q.where(TGoodSpec.recommender_fee >= items['recommender_fee_start'])
        if 'recommender_fee_end' in items:
            q = q.where(TGoodSpec.recommender_fee <= items['recommender_fee_end'])
        
        if 'supplier_fee' in items:
            q = q.where(TGoodSpec.supplier_fee == items['supplier_fee'])
        if 'supplier_fee_start' in items:
            q = q.where(TGoodSpec.supplier_fee >= items['supplier_fee_start'])
        if 'supplier_fee_end' in items:
            q = q.where(TGoodSpec.supplier_fee <= items['supplier_fee_end'])
        
        if 'lower_num_people' in items:
            q = q.where(TGoodSpec.lower_num_people == items['lower_num_people'])
        if 'lower_num_people_start' in items:
            q = q.where(TGoodSpec.lower_num_people >= items['lower_num_people_start'])
        if 'lower_num_people_end' in items:
            q = q.where(TGoodSpec.lower_num_people <= items['lower_num_people_end'])
        
        if 'upper_num_people' in items:
            q = q.where(TGoodSpec.upper_num_people == items['upper_num_people'])
        if 'upper_num_people_start' in items:
            q = q.where(TGoodSpec.upper_num_people >= items['upper_num_people_start'])
        if 'upper_num_people_end' in items:
            q = q.where(TGoodSpec.upper_num_people <= items['upper_num_people_end'])
        
        if 'room' in items:
            q = q.where(TGoodSpec.room == items['room'])
        if 'room_start' in items:
            q = q.where(TGoodSpec.room >= items['room_start'])
        if 'room_end' in items:
            q = q.where(TGoodSpec.room <= items['room_end'])
        
        if 'post' in items:
            q = q.where(TGoodSpec.post == items['post'])
        if 'post_start' in items:
            q = q.where(TGoodSpec.post >= items['post_start'])
        if 'post_end' in items:
            q = q.where(TGoodSpec.post <= items['post_end'])
        
        if 'status' in items:
            q = q.where(TGoodSpec.status == items['status'])
        if 'status_start' in items:
            q = q.where(TGoodSpec.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TGoodSpec.status <= items['status_end'])
        
        if 'share_fee' in items:
            q = q.where(TGoodSpec.share_fee == items['share_fee'])
        if 'share_fee_start' in items:
            q = q.where(TGoodSpec.share_fee >= items['share_fee_start'])
        if 'share_fee_end' in items:
            q = q.where(TGoodSpec.share_fee <= items['share_fee_end'])
        
        if 'is_default' in items:
            q = q.where(TGoodSpec.is_default == items['is_default'])
        if 'is_default_start' in items:
            q = q.where(TGoodSpec.is_default >= items['is_default_start'])
        if 'is_default_end' in items:
            q = q.where(TGoodSpec.is_default <= items['is_default_end'])
        
        if 'spec_num' in items:
            q = q.where(TGoodSpec.spec_num == items['spec_num'])
        if 'spec_num_start' in items:
            q = q.where(TGoodSpec.spec_num >= items['spec_num_start'])
        if 'spec_num_end' in items:
            q = q.where(TGoodSpec.spec_num <= items['spec_num_end'])
        
        if 'profit' in items:
            q = q.where(TGoodSpec.profit == items['profit'])
        if 'profit_start' in items:
            q = q.where(TGoodSpec.profit >= items['profit_start'])
        if 'profit_end' in items:
            q = q.where(TGoodSpec.profit <= items['profit_end'])
        
        if 'eqlevel_fee' in items:
            q = q.where(TGoodSpec.eqlevel_fee == items['eqlevel_fee'])
        if 'eqlevel_fee_start' in items:
            q = q.where(TGoodSpec.eqlevel_fee >= items['eqlevel_fee_start'])
        if 'eqlevel_fee_end' in items:
            q = q.where(TGoodSpec.eqlevel_fee <= items['eqlevel_fee_end'])
        

        if 'good_id' in set_items:
            q = q.where(TGoodSpec.good_id.in_(set_items['good_id']))
        
        if 'price' in set_items:
            q = q.where(TGoodSpec.price.in_(set_items['price']))
        
        if 'cost' in set_items:
            q = q.where(TGoodSpec.cost.in_(set_items['cost']))
        
        if 'value' in set_items:
            q = q.where(TGoodSpec.value.in_(set_items['value']))
        
        if 'id' in set_items:
            q = q.where(TGoodSpec.id.in_(set_items['id']))
        
        if 'stock' in set_items:
            q = q.where(TGoodSpec.stock.in_(set_items['stock']))
        
        if 'price_line' in set_items:
            q = q.where(TGoodSpec.price_line.in_(set_items['price_line']))
        
        if 'image' in set_items:
            q = q.where(TGoodSpec.image.in_(set_items['image']))
        
        if 'is_sub_good' in set_items:
            q = q.where(TGoodSpec.is_sub_good.in_(set_items['is_sub_good']))
        
        if 'num_sale' in set_items:
            q = q.where(TGoodSpec.num_sale.in_(set_items['num_sale']))
        
        if 'parent_fee' in set_items:
            q = q.where(TGoodSpec.parent_fee.in_(set_items['parent_fee']))
        
        if 'top_fee' in set_items:
            q = q.where(TGoodSpec.top_fee.in_(set_items['top_fee']))
        
        if 'recommender_fee' in set_items:
            q = q.where(TGoodSpec.recommender_fee.in_(set_items['recommender_fee']))
        
        if 'supplier_fee' in set_items:
            q = q.where(TGoodSpec.supplier_fee.in_(set_items['supplier_fee']))
        
        if 'lower_num_people' in set_items:
            q = q.where(TGoodSpec.lower_num_people.in_(set_items['lower_num_people']))
        
        if 'upper_num_people' in set_items:
            q = q.where(TGoodSpec.upper_num_people.in_(set_items['upper_num_people']))
        
        if 'room' in set_items:
            q = q.where(TGoodSpec.room.in_(set_items['room']))
        
        if 'post' in set_items:
            q = q.where(TGoodSpec.post.in_(set_items['post']))
        
        if 'status' in set_items:
            q = q.where(TGoodSpec.status.in_(set_items['status']))
        
        if 'share_fee' in set_items:
            q = q.where(TGoodSpec.share_fee.in_(set_items['share_fee']))
        
        if 'is_default' in set_items:
            q = q.where(TGoodSpec.is_default.in_(set_items['is_default']))
        
        if 'spec_num' in set_items:
            q = q.where(TGoodSpec.spec_num.in_(set_items['spec_num']))
        
        if 'profit' in set_items:
            q = q.where(TGoodSpec.profit.in_(set_items['profit']))
        
        if 'eqlevel_fee' in set_items:
            q = q.where(TGoodSpec.eqlevel_fee.in_(set_items['eqlevel_fee']))
        

        if 'value' in search_items:
            q = q.where(TGoodSpec.value.like(search_items['value']))
        
        if 'image' in search_items:
            q = q.where(TGoodSpec.image.like(search_items['image']))
        
        if 'room' in search_items:
            q = q.where(TGoodSpec.room.like(search_items['room']))
        
        if 'post' in search_items:
            q = q.where(TGoodSpec.post.like(search_items['post']))
        
        if 'spec_num' in search_items:
            q = q.where(TGoodSpec.spec_num.like(search_items['spec_num']))
        
    
        c = q.count()
        return c

    
def insert_good_spec_combo(item: CreateGoodSpecCombo, db: Optional[SessionLocal] = None) -> SGoodSpecCombo:
    data = model2dict(item)
    t = TGoodSpecCombo(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SGoodSpecCombo.parse_obj(t.__dict__)

    
def delete_good_spec_combo(good_spec_combo_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TGoodSpecCombo).where(TGoodSpecCombo.id == good_spec_combo_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodSpecCombo).where(TGoodSpecCombo.id == good_spec_combo_id).delete()
        db.commit()

    
def update_good_spec_combo(item: SGoodSpecCombo, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TGoodSpecCombo).where(TGoodSpecCombo.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodSpecCombo).where(TGoodSpecCombo.id == item.id).update(data)
        db.commit()

    
def get_good_spec_combo(good_spec_combo_id: int) -> Optional[SGoodSpecCombo]:
    with Dao() as db:
        t = db.query(TGoodSpecCombo).where(TGoodSpecCombo.id == good_spec_combo_id).first()
        if t:
            return SGoodSpecCombo.parse_obj(t.__dict__)
        else:
            return None


def filter_good_spec_combo(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SGoodSpecCombo]:
    with Dao() as db:
        q = db.query(TGoodSpecCombo)


        if 'id' in items:
            q = q.where(TGoodSpecCombo.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodSpecCombo.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodSpecCombo.id <= items['id_end'])
        
        if 'good_spec_id' in items:
            q = q.where(TGoodSpecCombo.good_spec_id == items['good_spec_id'])
        if 'good_spec_id_start' in items:
            q = q.where(TGoodSpecCombo.good_spec_id >= items['good_spec_id_start'])
        if 'good_spec_id_end' in items:
            q = q.where(TGoodSpecCombo.good_spec_id <= items['good_spec_id_end'])
        
        if 'value' in items:
            q = q.where(TGoodSpecCombo.value == items['value'])
        if 'value_start' in items:
            q = q.where(TGoodSpecCombo.value >= items['value_start'])
        if 'value_end' in items:
            q = q.where(TGoodSpecCombo.value <= items['value_end'])
        
        if 'price' in items:
            q = q.where(TGoodSpecCombo.price == items['price'])
        if 'price_start' in items:
            q = q.where(TGoodSpecCombo.price >= items['price_start'])
        if 'price_end' in items:
            q = q.where(TGoodSpecCombo.price <= items['price_end'])
        
        if 'amount' in items:
            q = q.where(TGoodSpecCombo.amount == items['amount'])
        if 'amount_start' in items:
            q = q.where(TGoodSpecCombo.amount >= items['amount_start'])
        if 'amount_end' in items:
            q = q.where(TGoodSpecCombo.amount <= items['amount_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodSpecCombo.id.in_(set_items['id']))
        
        if 'good_spec_id' in set_items:
            q = q.where(TGoodSpecCombo.good_spec_id.in_(set_items['good_spec_id']))
        
        if 'value' in set_items:
            q = q.where(TGoodSpecCombo.value.in_(set_items['value']))
        
        if 'price' in set_items:
            q = q.where(TGoodSpecCombo.price.in_(set_items['price']))
        
        if 'amount' in set_items:
            q = q.where(TGoodSpecCombo.amount.in_(set_items['amount']))
        

        if 'value' in search_items:
            q = q.where(TGoodSpecCombo.value.like(search_items['value']))
        
        if 'amount' in search_items:
            q = q.where(TGoodSpecCombo.amount.like(search_items['amount']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TGoodSpecCombo.amount.asc())
                orders.append(TGoodSpecCombo.id.asc())
            elif val == 'desc':
                #orders.append(TGoodSpecCombo.amount.desc())
                orders.append(TGoodSpecCombo.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_good_spec_combo_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SGoodSpecCombo.parse_obj(t.__dict__) for t in t_good_spec_combo_list]


def filter_count_good_spec_combo(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TGoodSpecCombo)


        if 'id' in items:
            q = q.where(TGoodSpecCombo.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodSpecCombo.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodSpecCombo.id <= items['id_end'])
        
        if 'good_spec_id' in items:
            q = q.where(TGoodSpecCombo.good_spec_id == items['good_spec_id'])
        if 'good_spec_id_start' in items:
            q = q.where(TGoodSpecCombo.good_spec_id >= items['good_spec_id_start'])
        if 'good_spec_id_end' in items:
            q = q.where(TGoodSpecCombo.good_spec_id <= items['good_spec_id_end'])
        
        if 'value' in items:
            q = q.where(TGoodSpecCombo.value == items['value'])
        if 'value_start' in items:
            q = q.where(TGoodSpecCombo.value >= items['value_start'])
        if 'value_end' in items:
            q = q.where(TGoodSpecCombo.value <= items['value_end'])
        
        if 'price' in items:
            q = q.where(TGoodSpecCombo.price == items['price'])
        if 'price_start' in items:
            q = q.where(TGoodSpecCombo.price >= items['price_start'])
        if 'price_end' in items:
            q = q.where(TGoodSpecCombo.price <= items['price_end'])
        
        if 'amount' in items:
            q = q.where(TGoodSpecCombo.amount == items['amount'])
        if 'amount_start' in items:
            q = q.where(TGoodSpecCombo.amount >= items['amount_start'])
        if 'amount_end' in items:
            q = q.where(TGoodSpecCombo.amount <= items['amount_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodSpecCombo.id.in_(set_items['id']))
        
        if 'good_spec_id' in set_items:
            q = q.where(TGoodSpecCombo.good_spec_id.in_(set_items['good_spec_id']))
        
        if 'value' in set_items:
            q = q.where(TGoodSpecCombo.value.in_(set_items['value']))
        
        if 'price' in set_items:
            q = q.where(TGoodSpecCombo.price.in_(set_items['price']))
        
        if 'amount' in set_items:
            q = q.where(TGoodSpecCombo.amount.in_(set_items['amount']))
        

        if 'value' in search_items:
            q = q.where(TGoodSpecCombo.value.like(search_items['value']))
        
        if 'amount' in search_items:
            q = q.where(TGoodSpecCombo.amount.like(search_items['amount']))
        
    
        c = q.count()
        return c

    
def insert_good_spec_detail(item: CreateGoodSpecDetail, db: Optional[SessionLocal] = None) -> SGoodSpecDetail:
    data = model2dict(item)
    t = TGoodSpecDetail(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SGoodSpecDetail.parse_obj(t.__dict__)

    
def delete_good_spec_detail(good_spec_detail_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TGoodSpecDetail).where(TGoodSpecDetail.id == good_spec_detail_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodSpecDetail).where(TGoodSpecDetail.id == good_spec_detail_id).delete()
        db.commit()

    
def update_good_spec_detail(item: SGoodSpecDetail, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TGoodSpecDetail).where(TGoodSpecDetail.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodSpecDetail).where(TGoodSpecDetail.id == item.id).update(data)
        db.commit()

    
def get_good_spec_detail(good_spec_detail_id: int) -> Optional[SGoodSpecDetail]:
    with Dao() as db:
        t = db.query(TGoodSpecDetail).where(TGoodSpecDetail.id == good_spec_detail_id).first()
        if t:
            return SGoodSpecDetail.parse_obj(t.__dict__)
        else:
            return None


def filter_good_spec_detail(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SGoodSpecDetail]:
    with Dao() as db:
        q = db.query(TGoodSpecDetail)


        if 'id' in items:
            q = q.where(TGoodSpecDetail.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodSpecDetail.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodSpecDetail.id <= items['id_end'])
        
        if 'good_spec_id' in items:
            q = q.where(TGoodSpecDetail.good_spec_id == items['good_spec_id'])
        if 'good_spec_id_start' in items:
            q = q.where(TGoodSpecDetail.good_spec_id >= items['good_spec_id_start'])
        if 'good_spec_id_end' in items:
            q = q.where(TGoodSpecDetail.good_spec_id <= items['good_spec_id_end'])
        
        if 'detail' in items:
            q = q.where(TGoodSpecDetail.detail == items['detail'])
        if 'detail_start' in items:
            q = q.where(TGoodSpecDetail.detail >= items['detail_start'])
        if 'detail_end' in items:
            q = q.where(TGoodSpecDetail.detail <= items['detail_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodSpecDetail.id.in_(set_items['id']))
        
        if 'good_spec_id' in set_items:
            q = q.where(TGoodSpecDetail.good_spec_id.in_(set_items['good_spec_id']))
        
        if 'detail' in set_items:
            q = q.where(TGoodSpecDetail.detail.in_(set_items['detail']))
        

        if 'detail' in search_items:
            q = q.where(TGoodSpecDetail.detail.like(search_items['detail']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TGoodSpecDetail.detail.asc())
                orders.append(TGoodSpecDetail.id.asc())
            elif val == 'desc':
                #orders.append(TGoodSpecDetail.detail.desc())
                orders.append(TGoodSpecDetail.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_good_spec_detail_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SGoodSpecDetail.parse_obj(t.__dict__) for t in t_good_spec_detail_list]


def filter_count_good_spec_detail(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TGoodSpecDetail)


        if 'id' in items:
            q = q.where(TGoodSpecDetail.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodSpecDetail.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodSpecDetail.id <= items['id_end'])
        
        if 'good_spec_id' in items:
            q = q.where(TGoodSpecDetail.good_spec_id == items['good_spec_id'])
        if 'good_spec_id_start' in items:
            q = q.where(TGoodSpecDetail.good_spec_id >= items['good_spec_id_start'])
        if 'good_spec_id_end' in items:
            q = q.where(TGoodSpecDetail.good_spec_id <= items['good_spec_id_end'])
        
        if 'detail' in items:
            q = q.where(TGoodSpecDetail.detail == items['detail'])
        if 'detail_start' in items:
            q = q.where(TGoodSpecDetail.detail >= items['detail_start'])
        if 'detail_end' in items:
            q = q.where(TGoodSpecDetail.detail <= items['detail_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodSpecDetail.id.in_(set_items['id']))
        
        if 'good_spec_id' in set_items:
            q = q.where(TGoodSpecDetail.good_spec_id.in_(set_items['good_spec_id']))
        
        if 'detail' in set_items:
            q = q.where(TGoodSpecDetail.detail.in_(set_items['detail']))
        

        if 'detail' in search_items:
            q = q.where(TGoodSpecDetail.detail.like(search_items['detail']))
        
    
        c = q.count()
        return c

    
def insert_good_spec_image(item: CreateGoodSpecImage, db: Optional[SessionLocal] = None) -> SGoodSpecImage:
    data = model2dict(item)
    t = TGoodSpecImage(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SGoodSpecImage.parse_obj(t.__dict__)

    
def delete_good_spec_image(good_spec_image_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TGoodSpecImage).where(TGoodSpecImage.id == good_spec_image_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodSpecImage).where(TGoodSpecImage.id == good_spec_image_id).delete()
        db.commit()

    
def update_good_spec_image(item: SGoodSpecImage, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TGoodSpecImage).where(TGoodSpecImage.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodSpecImage).where(TGoodSpecImage.id == item.id).update(data)
        db.commit()

    
def get_good_spec_image(good_spec_image_id: int) -> Optional[SGoodSpecImage]:
    with Dao() as db:
        t = db.query(TGoodSpecImage).where(TGoodSpecImage.id == good_spec_image_id).first()
        if t:
            return SGoodSpecImage.parse_obj(t.__dict__)
        else:
            return None


def filter_good_spec_image(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SGoodSpecImage]:
    with Dao() as db:
        q = db.query(TGoodSpecImage)


        if 'id' in items:
            q = q.where(TGoodSpecImage.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodSpecImage.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodSpecImage.id <= items['id_end'])
        
        if 'spec_id' in items:
            q = q.where(TGoodSpecImage.spec_id == items['spec_id'])
        if 'spec_id_start' in items:
            q = q.where(TGoodSpecImage.spec_id >= items['spec_id_start'])
        if 'spec_id_end' in items:
            q = q.where(TGoodSpecImage.spec_id <= items['spec_id_end'])
        
        if 'image' in items:
            q = q.where(TGoodSpecImage.image == items['image'])
        if 'image_start' in items:
            q = q.where(TGoodSpecImage.image >= items['image_start'])
        if 'image_end' in items:
            q = q.where(TGoodSpecImage.image <= items['image_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodSpecImage.id.in_(set_items['id']))
        
        if 'spec_id' in set_items:
            q = q.where(TGoodSpecImage.spec_id.in_(set_items['spec_id']))
        
        if 'image' in set_items:
            q = q.where(TGoodSpecImage.image.in_(set_items['image']))
        

        if 'image' in search_items:
            q = q.where(TGoodSpecImage.image.like(search_items['image']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TGoodSpecImage.image.asc())
                orders.append(TGoodSpecImage.id.asc())
            elif val == 'desc':
                #orders.append(TGoodSpecImage.image.desc())
                orders.append(TGoodSpecImage.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_good_spec_image_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SGoodSpecImage.parse_obj(t.__dict__) for t in t_good_spec_image_list]


def filter_count_good_spec_image(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TGoodSpecImage)


        if 'id' in items:
            q = q.where(TGoodSpecImage.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodSpecImage.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodSpecImage.id <= items['id_end'])
        
        if 'spec_id' in items:
            q = q.where(TGoodSpecImage.spec_id == items['spec_id'])
        if 'spec_id_start' in items:
            q = q.where(TGoodSpecImage.spec_id >= items['spec_id_start'])
        if 'spec_id_end' in items:
            q = q.where(TGoodSpecImage.spec_id <= items['spec_id_end'])
        
        if 'image' in items:
            q = q.where(TGoodSpecImage.image == items['image'])
        if 'image_start' in items:
            q = q.where(TGoodSpecImage.image >= items['image_start'])
        if 'image_end' in items:
            q = q.where(TGoodSpecImage.image <= items['image_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodSpecImage.id.in_(set_items['id']))
        
        if 'spec_id' in set_items:
            q = q.where(TGoodSpecImage.spec_id.in_(set_items['spec_id']))
        
        if 'image' in set_items:
            q = q.where(TGoodSpecImage.image.in_(set_items['image']))
        

        if 'image' in search_items:
            q = q.where(TGoodSpecImage.image.like(search_items['image']))
        
    
        c = q.count()
        return c

    
def insert_good_store(item: CreateGoodStore, db: Optional[SessionLocal] = None) -> SGoodStore:
    data = model2dict(item)
    t = TGoodStore(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SGoodStore.parse_obj(t.__dict__)

    
def delete_good_store(good_store_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TGoodStore).where(TGoodStore.id == good_store_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodStore).where(TGoodStore.id == good_store_id).delete()
        db.commit()

    
def update_good_store(item: SGoodStore, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TGoodStore).where(TGoodStore.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodStore).where(TGoodStore.id == item.id).update(data)
        db.commit()

    
def get_good_store(good_store_id: int) -> Optional[SGoodStore]:
    with Dao() as db:
        t = db.query(TGoodStore).where(TGoodStore.id == good_store_id).first()
        if t:
            return SGoodStore.parse_obj(t.__dict__)
        else:
            return None


def filter_good_store(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SGoodStore]:
    with Dao() as db:
        q = db.query(TGoodStore)


        if 'id' in items:
            q = q.where(TGoodStore.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodStore.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodStore.id <= items['id_end'])
        
        if 'good_id' in items:
            q = q.where(TGoodStore.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TGoodStore.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TGoodStore.good_id <= items['good_id_end'])
        
        if 'store_id' in items:
            q = q.where(TGoodStore.store_id == items['store_id'])
        if 'store_id_start' in items:
            q = q.where(TGoodStore.store_id >= items['store_id_start'])
        if 'store_id_end' in items:
            q = q.where(TGoodStore.store_id <= items['store_id_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodStore.id.in_(set_items['id']))
        
        if 'good_id' in set_items:
            q = q.where(TGoodStore.good_id.in_(set_items['good_id']))
        
        if 'store_id' in set_items:
            q = q.where(TGoodStore.store_id.in_(set_items['store_id']))
        

    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TGoodStore.store_id.asc())
                orders.append(TGoodStore.id.asc())
            elif val == 'desc':
                #orders.append(TGoodStore.store_id.desc())
                orders.append(TGoodStore.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_good_store_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SGoodStore.parse_obj(t.__dict__) for t in t_good_store_list]


def filter_count_good_store(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TGoodStore)


        if 'id' in items:
            q = q.where(TGoodStore.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodStore.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodStore.id <= items['id_end'])
        
        if 'good_id' in items:
            q = q.where(TGoodStore.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TGoodStore.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TGoodStore.good_id <= items['good_id_end'])
        
        if 'store_id' in items:
            q = q.where(TGoodStore.store_id == items['store_id'])
        if 'store_id_start' in items:
            q = q.where(TGoodStore.store_id >= items['store_id_start'])
        if 'store_id_end' in items:
            q = q.where(TGoodStore.store_id <= items['store_id_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodStore.id.in_(set_items['id']))
        
        if 'good_id' in set_items:
            q = q.where(TGoodStore.good_id.in_(set_items['good_id']))
        
        if 'store_id' in set_items:
            q = q.where(TGoodStore.store_id.in_(set_items['store_id']))
        

    
        c = q.count()
        return c

    
def insert_good_text(item: CreateGoodText, db: Optional[SessionLocal] = None) -> SGoodText:
    data = model2dict(item)
    t = TGoodText(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SGoodText.parse_obj(t.__dict__)

    
def delete_good_text(good_text_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TGoodText).where(TGoodText.id == good_text_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodText).where(TGoodText.id == good_text_id).delete()
        db.commit()

    
def update_good_text(item: SGoodText, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TGoodText).where(TGoodText.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodText).where(TGoodText.id == item.id).update(data)
        db.commit()

    
def get_good_text(good_text_id: int) -> Optional[SGoodText]:
    with Dao() as db:
        t = db.query(TGoodText).where(TGoodText.id == good_text_id).first()
        if t:
            return SGoodText.parse_obj(t.__dict__)
        else:
            return None


def filter_good_text(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SGoodText]:
    with Dao() as db:
        q = db.query(TGoodText)


        if 'id' in items:
            q = q.where(TGoodText.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodText.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodText.id <= items['id_end'])
        
        if 'good_id' in items:
            q = q.where(TGoodText.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TGoodText.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TGoodText.good_id <= items['good_id_end'])
        
        if 'description' in items:
            q = q.where(TGoodText.description == items['description'])
        if 'description_start' in items:
            q = q.where(TGoodText.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TGoodText.description <= items['description_end'])
        
        if 'create_time' in items:
            q = q.where(TGoodText.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TGoodText.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TGoodText.create_time <= items['create_time_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodText.id.in_(set_items['id']))
        
        if 'good_id' in set_items:
            q = q.where(TGoodText.good_id.in_(set_items['good_id']))
        
        if 'description' in set_items:
            q = q.where(TGoodText.description.in_(set_items['description']))
        
        if 'create_time' in set_items:
            q = q.where(TGoodText.create_time.in_(set_items['create_time']))
        

        if 'description' in search_items:
            q = q.where(TGoodText.description.like(search_items['description']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TGoodText.create_time.asc())
                orders.append(TGoodText.id.asc())
            elif val == 'desc':
                #orders.append(TGoodText.create_time.desc())
                orders.append(TGoodText.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_good_text_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SGoodText.parse_obj(t.__dict__) for t in t_good_text_list]


def filter_count_good_text(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TGoodText)


        if 'id' in items:
            q = q.where(TGoodText.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodText.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodText.id <= items['id_end'])
        
        if 'good_id' in items:
            q = q.where(TGoodText.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TGoodText.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TGoodText.good_id <= items['good_id_end'])
        
        if 'description' in items:
            q = q.where(TGoodText.description == items['description'])
        if 'description_start' in items:
            q = q.where(TGoodText.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TGoodText.description <= items['description_end'])
        
        if 'create_time' in items:
            q = q.where(TGoodText.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TGoodText.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TGoodText.create_time <= items['create_time_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodText.id.in_(set_items['id']))
        
        if 'good_id' in set_items:
            q = q.where(TGoodText.good_id.in_(set_items['good_id']))
        
        if 'description' in set_items:
            q = q.where(TGoodText.description.in_(set_items['description']))
        
        if 'create_time' in set_items:
            q = q.where(TGoodText.create_time.in_(set_items['create_time']))
        

        if 'description' in search_items:
            q = q.where(TGoodText.description.like(search_items['description']))
        
    
        c = q.count()
        return c

    
def insert_good_type(item: CreateGoodType, db: Optional[SessionLocal] = None) -> SGoodType:
    data = model2dict(item)
    t = TGoodType(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SGoodType.parse_obj(t.__dict__)

    
def delete_good_type(good_type_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TGoodType).where(TGoodType.id == good_type_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodType).where(TGoodType.id == good_type_id).delete()
        db.commit()

    
def update_good_type(item: SGoodType, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TGoodType).where(TGoodType.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGoodType).where(TGoodType.id == item.id).update(data)
        db.commit()

    
def get_good_type(good_type_id: int) -> Optional[SGoodType]:
    with Dao() as db:
        t = db.query(TGoodType).where(TGoodType.id == good_type_id).first()
        if t:
            return SGoodType.parse_obj(t.__dict__)
        else:
            return None


def filter_good_type(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SGoodType]:
    with Dao() as db:
        q = db.query(TGoodType)


        if 'id' in items:
            q = q.where(TGoodType.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodType.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodType.id <= items['id_end'])
        
        if 'type' in items:
            q = q.where(TGoodType.type == items['type'])
        if 'type_start' in items:
            q = q.where(TGoodType.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TGoodType.type <= items['type_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodType.id.in_(set_items['id']))
        
        if 'type' in set_items:
            q = q.where(TGoodType.type.in_(set_items['type']))
        

        if 'type' in search_items:
            q = q.where(TGoodType.type.like(search_items['type']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TGoodType.type.asc())
                orders.append(TGoodType.id.asc())
            elif val == 'desc':
                #orders.append(TGoodType.type.desc())
                orders.append(TGoodType.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_good_type_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SGoodType.parse_obj(t.__dict__) for t in t_good_type_list]


def filter_count_good_type(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TGoodType)


        if 'id' in items:
            q = q.where(TGoodType.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGoodType.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGoodType.id <= items['id_end'])
        
        if 'type' in items:
            q = q.where(TGoodType.type == items['type'])
        if 'type_start' in items:
            q = q.where(TGoodType.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TGoodType.type <= items['type_end'])
        

        if 'id' in set_items:
            q = q.where(TGoodType.id.in_(set_items['id']))
        
        if 'type' in set_items:
            q = q.where(TGoodType.type.in_(set_items['type']))
        

        if 'type' in search_items:
            q = q.where(TGoodType.type.like(search_items['type']))
        
    
        c = q.count()
        return c

    
def insert_groupsir(item: CreateGroupsir, db: Optional[SessionLocal] = None) -> SGroupsir:
    data = model2dict(item)
    t = TGroupsir(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SGroupsir.parse_obj(t.__dict__)

    
def delete_groupsir(groupsir_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TGroupsir).where(TGroupsir.id == groupsir_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGroupsir).where(TGroupsir.id == groupsir_id).delete()
        db.commit()

    
def update_groupsir(item: SGroupsir, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TGroupsir).where(TGroupsir.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TGroupsir).where(TGroupsir.id == item.id).update(data)
        db.commit()

    
def get_groupsir(groupsir_id: int) -> Optional[SGroupsir]:
    with Dao() as db:
        t = db.query(TGroupsir).where(TGroupsir.id == groupsir_id).first()
        if t:
            return SGroupsir.parse_obj(t.__dict__)
        else:
            return None


def filter_groupsir(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SGroupsir]:
    with Dao() as db:
        q = db.query(TGroupsir)


        if 'id' in items:
            q = q.where(TGroupsir.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGroupsir.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGroupsir.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TGroupsir.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TGroupsir.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TGroupsir.user_id <= items['user_id_end'])
        
        if 'parent_id' in items:
            q = q.where(TGroupsir.parent_id == items['parent_id'])
        if 'parent_id_start' in items:
            q = q.where(TGroupsir.parent_id >= items['parent_id_start'])
        if 'parent_id_end' in items:
            q = q.where(TGroupsir.parent_id <= items['parent_id_end'])
        
        if 'register_time' in items:
            q = q.where(TGroupsir.register_time == items['register_time'])
        if 'register_time_start' in items:
            q = q.where(TGroupsir.register_time >= items['register_time_start'])
        if 'register_time_end' in items:
            q = q.where(TGroupsir.register_time <= items['register_time_end'])
        
        if 'status' in items:
            q = q.where(TGroupsir.status == items['status'])
        if 'status_start' in items:
            q = q.where(TGroupsir.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TGroupsir.status <= items['status_end'])
        
        if 'is_empower' in items:
            q = q.where(TGroupsir.is_empower == items['is_empower'])
        if 'is_empower_start' in items:
            q = q.where(TGroupsir.is_empower >= items['is_empower_start'])
        if 'is_empower_end' in items:
            q = q.where(TGroupsir.is_empower <= items['is_empower_end'])
        
        if 'notes' in items:
            q = q.where(TGroupsir.notes == items['notes'])
        if 'notes_start' in items:
            q = q.where(TGroupsir.notes >= items['notes_start'])
        if 'notes_end' in items:
            q = q.where(TGroupsir.notes <= items['notes_end'])
        

        if 'id' in set_items:
            q = q.where(TGroupsir.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TGroupsir.user_id.in_(set_items['user_id']))
        
        if 'parent_id' in set_items:
            q = q.where(TGroupsir.parent_id.in_(set_items['parent_id']))
        
        if 'register_time' in set_items:
            q = q.where(TGroupsir.register_time.in_(set_items['register_time']))
        
        if 'status' in set_items:
            q = q.where(TGroupsir.status.in_(set_items['status']))
        
        if 'is_empower' in set_items:
            q = q.where(TGroupsir.is_empower.in_(set_items['is_empower']))
        
        if 'notes' in set_items:
            q = q.where(TGroupsir.notes.in_(set_items['notes']))
        

        if 'notes' in search_items:
            q = q.where(TGroupsir.notes.like(search_items['notes']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TGroupsir.notes.asc())
                orders.append(TGroupsir.id.asc())
            elif val == 'desc':
                #orders.append(TGroupsir.notes.desc())
                orders.append(TGroupsir.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_groupsir_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SGroupsir.parse_obj(t.__dict__) for t in t_groupsir_list]


def filter_count_groupsir(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TGroupsir)


        if 'id' in items:
            q = q.where(TGroupsir.id == items['id'])
        if 'id_start' in items:
            q = q.where(TGroupsir.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TGroupsir.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TGroupsir.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TGroupsir.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TGroupsir.user_id <= items['user_id_end'])
        
        if 'parent_id' in items:
            q = q.where(TGroupsir.parent_id == items['parent_id'])
        if 'parent_id_start' in items:
            q = q.where(TGroupsir.parent_id >= items['parent_id_start'])
        if 'parent_id_end' in items:
            q = q.where(TGroupsir.parent_id <= items['parent_id_end'])
        
        if 'register_time' in items:
            q = q.where(TGroupsir.register_time == items['register_time'])
        if 'register_time_start' in items:
            q = q.where(TGroupsir.register_time >= items['register_time_start'])
        if 'register_time_end' in items:
            q = q.where(TGroupsir.register_time <= items['register_time_end'])
        
        if 'status' in items:
            q = q.where(TGroupsir.status == items['status'])
        if 'status_start' in items:
            q = q.where(TGroupsir.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TGroupsir.status <= items['status_end'])
        
        if 'is_empower' in items:
            q = q.where(TGroupsir.is_empower == items['is_empower'])
        if 'is_empower_start' in items:
            q = q.where(TGroupsir.is_empower >= items['is_empower_start'])
        if 'is_empower_end' in items:
            q = q.where(TGroupsir.is_empower <= items['is_empower_end'])
        
        if 'notes' in items:
            q = q.where(TGroupsir.notes == items['notes'])
        if 'notes_start' in items:
            q = q.where(TGroupsir.notes >= items['notes_start'])
        if 'notes_end' in items:
            q = q.where(TGroupsir.notes <= items['notes_end'])
        

        if 'id' in set_items:
            q = q.where(TGroupsir.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TGroupsir.user_id.in_(set_items['user_id']))
        
        if 'parent_id' in set_items:
            q = q.where(TGroupsir.parent_id.in_(set_items['parent_id']))
        
        if 'register_time' in set_items:
            q = q.where(TGroupsir.register_time.in_(set_items['register_time']))
        
        if 'status' in set_items:
            q = q.where(TGroupsir.status.in_(set_items['status']))
        
        if 'is_empower' in set_items:
            q = q.where(TGroupsir.is_empower.in_(set_items['is_empower']))
        
        if 'notes' in set_items:
            q = q.where(TGroupsir.notes.in_(set_items['notes']))
        

        if 'notes' in search_items:
            q = q.where(TGroupsir.notes.like(search_items['notes']))
        
    
        c = q.count()
        return c

    
def insert_level(item: CreateLevel, db: Optional[SessionLocal] = None) -> SLevel:
    data = model2dict(item)
    t = TLevel(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SLevel.parse_obj(t.__dict__)

    
def delete_level(level_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TLevel).where(TLevel.id == level_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TLevel).where(TLevel.id == level_id).delete()
        db.commit()

    
def update_level(item: SLevel, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TLevel).where(TLevel.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TLevel).where(TLevel.id == item.id).update(data)
        db.commit()

    
def get_level(level_id: int) -> Optional[SLevel]:
    with Dao() as db:
        t = db.query(TLevel).where(TLevel.id == level_id).first()
        if t:
            return SLevel.parse_obj(t.__dict__)
        else:
            return None


def filter_level(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SLevel]:
    with Dao() as db:
        q = db.query(TLevel)


        if 'id' in items:
            q = q.where(TLevel.id == items['id'])
        if 'id_start' in items:
            q = q.where(TLevel.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TLevel.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TLevel.title == items['title'])
        if 'title_start' in items:
            q = q.where(TLevel.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TLevel.title <= items['title_end'])
        

        if 'id' in set_items:
            q = q.where(TLevel.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TLevel.title.in_(set_items['title']))
        

        if 'title' in search_items:
            q = q.where(TLevel.title.like(search_items['title']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TLevel.title.asc())
                orders.append(TLevel.id.asc())
            elif val == 'desc':
                #orders.append(TLevel.title.desc())
                orders.append(TLevel.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_level_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SLevel.parse_obj(t.__dict__) for t in t_level_list]


def filter_count_level(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TLevel)


        if 'id' in items:
            q = q.where(TLevel.id == items['id'])
        if 'id_start' in items:
            q = q.where(TLevel.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TLevel.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TLevel.title == items['title'])
        if 'title_start' in items:
            q = q.where(TLevel.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TLevel.title <= items['title_end'])
        

        if 'id' in set_items:
            q = q.where(TLevel.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TLevel.title.in_(set_items['title']))
        

        if 'title' in search_items:
            q = q.where(TLevel.title.like(search_items['title']))
        
    
        c = q.count()
        return c

    
def insert_lock_balance(item: CreateLockBalance, db: Optional[SessionLocal] = None) -> SLockBalance:
    data = model2dict(item)
    t = TLockBalance(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SLockBalance.parse_obj(t.__dict__)

    
def delete_lock_balance(lock_balance_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TLockBalance).where(TLockBalance.id == lock_balance_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TLockBalance).where(TLockBalance.id == lock_balance_id).delete()
        db.commit()

    
def update_lock_balance(item: SLockBalance, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TLockBalance).where(TLockBalance.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TLockBalance).where(TLockBalance.id == item.id).update(data)
        db.commit()

    
def get_lock_balance(lock_balance_id: int) -> Optional[SLockBalance]:
    with Dao() as db:
        t = db.query(TLockBalance).where(TLockBalance.id == lock_balance_id).first()
        if t:
            return SLockBalance.parse_obj(t.__dict__)
        else:
            return None


def filter_lock_balance(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SLockBalance]:
    with Dao() as db:
        q = db.query(TLockBalance)


        if 'id' in items:
            q = q.where(TLockBalance.id == items['id'])
        if 'id_start' in items:
            q = q.where(TLockBalance.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TLockBalance.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TLockBalance.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TLockBalance.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TLockBalance.user_id <= items['user_id_end'])
        
        if 'change' in items:
            q = q.where(TLockBalance.change == items['change'])
        if 'change_start' in items:
            q = q.where(TLockBalance.change >= items['change_start'])
        if 'change_end' in items:
            q = q.where(TLockBalance.change <= items['change_end'])
        
        if 'lock_balance' in items:
            q = q.where(TLockBalance.lock_balance == items['lock_balance'])
        if 'lock_balance_start' in items:
            q = q.where(TLockBalance.lock_balance >= items['lock_balance_start'])
        if 'lock_balance_end' in items:
            q = q.where(TLockBalance.lock_balance <= items['lock_balance_end'])
        
        if 'type' in items:
            q = q.where(TLockBalance.type == items['type'])
        if 'type_start' in items:
            q = q.where(TLockBalance.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TLockBalance.type <= items['type_end'])
        
        if 'description' in items:
            q = q.where(TLockBalance.description == items['description'])
        if 'description_start' in items:
            q = q.where(TLockBalance.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TLockBalance.description <= items['description_end'])
        
        if 'create_time' in items:
            q = q.where(TLockBalance.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TLockBalance.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TLockBalance.create_time <= items['create_time_end'])
        
        if 'out_trade_no' in items:
            q = q.where(TLockBalance.out_trade_no == items['out_trade_no'])
        if 'out_trade_no_start' in items:
            q = q.where(TLockBalance.out_trade_no >= items['out_trade_no_start'])
        if 'out_trade_no_end' in items:
            q = q.where(TLockBalance.out_trade_no <= items['out_trade_no_end'])
        

        if 'id' in set_items:
            q = q.where(TLockBalance.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TLockBalance.user_id.in_(set_items['user_id']))
        
        if 'change' in set_items:
            q = q.where(TLockBalance.change.in_(set_items['change']))
        
        if 'lock_balance' in set_items:
            q = q.where(TLockBalance.lock_balance.in_(set_items['lock_balance']))
        
        if 'type' in set_items:
            q = q.where(TLockBalance.type.in_(set_items['type']))
        
        if 'description' in set_items:
            q = q.where(TLockBalance.description.in_(set_items['description']))
        
        if 'create_time' in set_items:
            q = q.where(TLockBalance.create_time.in_(set_items['create_time']))
        
        if 'out_trade_no' in set_items:
            q = q.where(TLockBalance.out_trade_no.in_(set_items['out_trade_no']))
        

        if 'type' in search_items:
            q = q.where(TLockBalance.type.like(search_items['type']))
        
        if 'description' in search_items:
            q = q.where(TLockBalance.description.like(search_items['description']))
        
        if 'out_trade_no' in search_items:
            q = q.where(TLockBalance.out_trade_no.like(search_items['out_trade_no']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TLockBalance.out_trade_no.asc())
                orders.append(TLockBalance.id.asc())
            elif val == 'desc':
                #orders.append(TLockBalance.out_trade_no.desc())
                orders.append(TLockBalance.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_lock_balance_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SLockBalance.parse_obj(t.__dict__) for t in t_lock_balance_list]


def filter_count_lock_balance(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TLockBalance)


        if 'id' in items:
            q = q.where(TLockBalance.id == items['id'])
        if 'id_start' in items:
            q = q.where(TLockBalance.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TLockBalance.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TLockBalance.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TLockBalance.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TLockBalance.user_id <= items['user_id_end'])
        
        if 'change' in items:
            q = q.where(TLockBalance.change == items['change'])
        if 'change_start' in items:
            q = q.where(TLockBalance.change >= items['change_start'])
        if 'change_end' in items:
            q = q.where(TLockBalance.change <= items['change_end'])
        
        if 'lock_balance' in items:
            q = q.where(TLockBalance.lock_balance == items['lock_balance'])
        if 'lock_balance_start' in items:
            q = q.where(TLockBalance.lock_balance >= items['lock_balance_start'])
        if 'lock_balance_end' in items:
            q = q.where(TLockBalance.lock_balance <= items['lock_balance_end'])
        
        if 'type' in items:
            q = q.where(TLockBalance.type == items['type'])
        if 'type_start' in items:
            q = q.where(TLockBalance.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TLockBalance.type <= items['type_end'])
        
        if 'description' in items:
            q = q.where(TLockBalance.description == items['description'])
        if 'description_start' in items:
            q = q.where(TLockBalance.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TLockBalance.description <= items['description_end'])
        
        if 'create_time' in items:
            q = q.where(TLockBalance.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TLockBalance.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TLockBalance.create_time <= items['create_time_end'])
        
        if 'out_trade_no' in items:
            q = q.where(TLockBalance.out_trade_no == items['out_trade_no'])
        if 'out_trade_no_start' in items:
            q = q.where(TLockBalance.out_trade_no >= items['out_trade_no_start'])
        if 'out_trade_no_end' in items:
            q = q.where(TLockBalance.out_trade_no <= items['out_trade_no_end'])
        

        if 'id' in set_items:
            q = q.where(TLockBalance.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TLockBalance.user_id.in_(set_items['user_id']))
        
        if 'change' in set_items:
            q = q.where(TLockBalance.change.in_(set_items['change']))
        
        if 'lock_balance' in set_items:
            q = q.where(TLockBalance.lock_balance.in_(set_items['lock_balance']))
        
        if 'type' in set_items:
            q = q.where(TLockBalance.type.in_(set_items['type']))
        
        if 'description' in set_items:
            q = q.where(TLockBalance.description.in_(set_items['description']))
        
        if 'create_time' in set_items:
            q = q.where(TLockBalance.create_time.in_(set_items['create_time']))
        
        if 'out_trade_no' in set_items:
            q = q.where(TLockBalance.out_trade_no.in_(set_items['out_trade_no']))
        

        if 'type' in search_items:
            q = q.where(TLockBalance.type.like(search_items['type']))
        
        if 'description' in search_items:
            q = q.where(TLockBalance.description.like(search_items['description']))
        
        if 'out_trade_no' in search_items:
            q = q.where(TLockBalance.out_trade_no.like(search_items['out_trade_no']))
        
    
        c = q.count()
        return c

    
def insert_model(item: CreateModel, db: Optional[SessionLocal] = None) -> SModel:
    data = model2dict(item)
    t = TModel(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SModel.parse_obj(t.__dict__)

    
def delete_model(model_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TModel).where(TModel.id == model_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TModel).where(TModel.id == model_id).delete()
        db.commit()

    
def update_model(item: SModel, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TModel).where(TModel.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TModel).where(TModel.id == item.id).update(data)
        db.commit()

    
def get_model(model_id: int) -> Optional[SModel]:
    with Dao() as db:
        t = db.query(TModel).where(TModel.id == model_id).first()
        if t:
            return SModel.parse_obj(t.__dict__)
        else:
            return None


def filter_model(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SModel]:
    with Dao() as db:
        q = db.query(TModel)


        if 'id' in items:
            q = q.where(TModel.id == items['id'])
        if 'id_start' in items:
            q = q.where(TModel.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TModel.id <= items['id_end'])
        
        if 'product_id' in items:
            q = q.where(TModel.product_id == items['product_id'])
        if 'product_id_start' in items:
            q = q.where(TModel.product_id >= items['product_id_start'])
        if 'product_id_end' in items:
            q = q.where(TModel.product_id <= items['product_id_end'])
        

        if 'id' in set_items:
            q = q.where(TModel.id.in_(set_items['id']))
        
        if 'product_id' in set_items:
            q = q.where(TModel.product_id.in_(set_items['product_id']))
        

    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TModel.product_id.asc())
                orders.append(TModel.id.asc())
            elif val == 'desc':
                #orders.append(TModel.product_id.desc())
                orders.append(TModel.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_model_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SModel.parse_obj(t.__dict__) for t in t_model_list]


def filter_count_model(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TModel)


        if 'id' in items:
            q = q.where(TModel.id == items['id'])
        if 'id_start' in items:
            q = q.where(TModel.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TModel.id <= items['id_end'])
        
        if 'product_id' in items:
            q = q.where(TModel.product_id == items['product_id'])
        if 'product_id_start' in items:
            q = q.where(TModel.product_id >= items['product_id_start'])
        if 'product_id_end' in items:
            q = q.where(TModel.product_id <= items['product_id_end'])
        

        if 'id' in set_items:
            q = q.where(TModel.id.in_(set_items['id']))
        
        if 'product_id' in set_items:
            q = q.where(TModel.product_id.in_(set_items['product_id']))
        

    
        c = q.count()
        return c

    
def insert_order(item: CreateOrder, db: Optional[SessionLocal] = None) -> SOrder:
    data = model2dict(item)
    t = TOrder(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SOrder.parse_obj(t.__dict__)

    
def delete_order(order_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TOrder).where(TOrder.id == order_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TOrder).where(TOrder.id == order_id).delete()
        db.commit()

    
def update_order(item: SOrder, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TOrder).where(TOrder.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TOrder).where(TOrder.id == item.id).update(data)
        db.commit()

    
def get_order(order_id: int) -> Optional[SOrder]:
    with Dao() as db:
        t = db.query(TOrder).where(TOrder.id == order_id).first()
        if t:
            return SOrder.parse_obj(t.__dict__)
        else:
            return None


def filter_order(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SOrder]:
    with Dao() as db:
        q = db.query(TOrder)


        if 'id' in items:
            q = q.where(TOrder.id == items['id'])
        if 'id_start' in items:
            q = q.where(TOrder.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TOrder.id <= items['id_end'])
        
        if 'good_id' in items:
            q = q.where(TOrder.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TOrder.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TOrder.good_id <= items['good_id_end'])
        
        if 'paider_id' in items:
            q = q.where(TOrder.paider_id == items['paider_id'])
        if 'paider_id_start' in items:
            q = q.where(TOrder.paider_id >= items['paider_id_start'])
        if 'paider_id_end' in items:
            q = q.where(TOrder.paider_id <= items['paider_id_end'])
        
        if 'sale_price' in items:
            q = q.where(TOrder.sale_price == items['sale_price'])
        if 'sale_price_start' in items:
            q = q.where(TOrder.sale_price >= items['sale_price_start'])
        if 'sale_price_end' in items:
            q = q.where(TOrder.sale_price <= items['sale_price_end'])
        
        if 'cost_price' in items:
            q = q.where(TOrder.cost_price == items['cost_price'])
        if 'cost_price_start' in items:
            q = q.where(TOrder.cost_price >= items['cost_price_start'])
        if 'cost_price_end' in items:
            q = q.where(TOrder.cost_price <= items['cost_price_end'])
        
        if 'create_time' in items:
            q = q.where(TOrder.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TOrder.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TOrder.create_time <= items['create_time_end'])
        
        if 'paid_time' in items:
            q = q.where(TOrder.paid_time == items['paid_time'])
        if 'paid_time_start' in items:
            q = q.where(TOrder.paid_time >= items['paid_time_start'])
        if 'paid_time_end' in items:
            q = q.where(TOrder.paid_time <= items['paid_time_end'])
        
        if 'status_id' in items:
            q = q.where(TOrder.status_id == items['status_id'])
        if 'status_id_start' in items:
            q = q.where(TOrder.status_id >= items['status_id_start'])
        if 'status_id_end' in items:
            q = q.where(TOrder.status_id <= items['status_id_end'])
        
        if 'number' in items:
            q = q.where(TOrder.number == items['number'])
        if 'number_start' in items:
            q = q.where(TOrder.number >= items['number_start'])
        if 'number_end' in items:
            q = q.where(TOrder.number <= items['number_end'])
        
        if 'consignee_address' in items:
            q = q.where(TOrder.consignee_address == items['consignee_address'])
        if 'consignee_address_start' in items:
            q = q.where(TOrder.consignee_address >= items['consignee_address_start'])
        if 'consignee_address_end' in items:
            q = q.where(TOrder.consignee_address <= items['consignee_address_end'])
        
        if 'consignee_phone' in items:
            q = q.where(TOrder.consignee_phone == items['consignee_phone'])
        if 'consignee_phone_start' in items:
            q = q.where(TOrder.consignee_phone >= items['consignee_phone_start'])
        if 'consignee_phone_end' in items:
            q = q.where(TOrder.consignee_phone <= items['consignee_phone_end'])
        
        if 'store_id' in items:
            q = q.where(TOrder.store_id == items['store_id'])
        if 'store_id_start' in items:
            q = q.where(TOrder.store_id >= items['store_id_start'])
        if 'store_id_end' in items:
            q = q.where(TOrder.store_id <= items['store_id_end'])
        
        if 'paid_amount' in items:
            q = q.where(TOrder.paid_amount == items['paid_amount'])
        if 'paid_amount_start' in items:
            q = q.where(TOrder.paid_amount >= items['paid_amount_start'])
        if 'paid_amount_end' in items:
            q = q.where(TOrder.paid_amount <= items['paid_amount_end'])
        
        if 'delivery_fee' in items:
            q = q.where(TOrder.delivery_fee == items['delivery_fee'])
        if 'delivery_fee_start' in items:
            q = q.where(TOrder.delivery_fee >= items['delivery_fee_start'])
        if 'delivery_fee_end' in items:
            q = q.where(TOrder.delivery_fee <= items['delivery_fee_end'])
        
        if 'spec_id' in items:
            q = q.where(TOrder.spec_id == items['spec_id'])
        if 'spec_id_start' in items:
            q = q.where(TOrder.spec_id >= items['spec_id_start'])
        if 'spec_id_end' in items:
            q = q.where(TOrder.spec_id <= items['spec_id_end'])
        
        if 'paid_coin' in items:
            q = q.where(TOrder.paid_coin == items['paid_coin'])
        if 'paid_coin_start' in items:
            q = q.where(TOrder.paid_coin >= items['paid_coin_start'])
        if 'paid_coin_end' in items:
            q = q.where(TOrder.paid_coin <= items['paid_coin_end'])
        
        if 'delivery_track_code' in items:
            q = q.where(TOrder.delivery_track_code == items['delivery_track_code'])
        if 'delivery_track_code_start' in items:
            q = q.where(TOrder.delivery_track_code >= items['delivery_track_code_start'])
        if 'delivery_track_code_end' in items:
            q = q.where(TOrder.delivery_track_code <= items['delivery_track_code_end'])
        
        if 'paid_channel_id' in items:
            q = q.where(TOrder.paid_channel_id == items['paid_channel_id'])
        if 'paid_channel_id_start' in items:
            q = q.where(TOrder.paid_channel_id >= items['paid_channel_id_start'])
        if 'paid_channel_id_end' in items:
            q = q.where(TOrder.paid_channel_id <= items['paid_channel_id_end'])
        
        if 'consignee_name' in items:
            q = q.where(TOrder.consignee_name == items['consignee_name'])
        if 'consignee_name_start' in items:
            q = q.where(TOrder.consignee_name >= items['consignee_name_start'])
        if 'consignee_name_end' in items:
            q = q.where(TOrder.consignee_name <= items['consignee_name_end'])
        
        if 'delivery_time' in items:
            q = q.where(TOrder.delivery_time == items['delivery_time'])
        if 'delivery_time_start' in items:
            q = q.where(TOrder.delivery_time >= items['delivery_time_start'])
        if 'delivery_time_end' in items:
            q = q.where(TOrder.delivery_time <= items['delivery_time_end'])
        
        if 'good_name' in items:
            q = q.where(TOrder.good_name == items['good_name'])
        if 'good_name_start' in items:
            q = q.where(TOrder.good_name >= items['good_name_start'])
        if 'good_name_end' in items:
            q = q.where(TOrder.good_name <= items['good_name_end'])
        
        if 'paid_track_code' in items:
            q = q.where(TOrder.paid_track_code == items['paid_track_code'])
        if 'paid_track_code_start' in items:
            q = q.where(TOrder.paid_track_code >= items['paid_track_code_start'])
        if 'paid_track_code_end' in items:
            q = q.where(TOrder.paid_track_code <= items['paid_track_code_end'])
        
        if 'paider_name' in items:
            q = q.where(TOrder.paider_name == items['paider_name'])
        if 'paider_name_start' in items:
            q = q.where(TOrder.paider_name >= items['paider_name_start'])
        if 'paider_name_end' in items:
            q = q.where(TOrder.paider_name <= items['paider_name_end'])
        
        if 'paider_phone' in items:
            q = q.where(TOrder.paider_phone == items['paider_phone'])
        if 'paider_phone_start' in items:
            q = q.where(TOrder.paider_phone >= items['paider_phone_start'])
        if 'paider_phone_end' in items:
            q = q.where(TOrder.paider_phone <= items['paider_phone_end'])
        
        if 'paider_address' in items:
            q = q.where(TOrder.paider_address == items['paider_address'])
        if 'paider_address_start' in items:
            q = q.where(TOrder.paider_address >= items['paider_address_start'])
        if 'paider_address_end' in items:
            q = q.where(TOrder.paider_address <= items['paider_address_end'])
        
        if 'supplier_id' in items:
            q = q.where(TOrder.supplier_id == items['supplier_id'])
        if 'supplier_id_start' in items:
            q = q.where(TOrder.supplier_id >= items['supplier_id_start'])
        if 'supplier_id_end' in items:
            q = q.where(TOrder.supplier_id <= items['supplier_id_end'])
        
        if 'paid_balance' in items:
            q = q.where(TOrder.paid_balance == items['paid_balance'])
        if 'paid_balance_start' in items:
            q = q.where(TOrder.paid_balance >= items['paid_balance_start'])
        if 'paid_balance_end' in items:
            q = q.where(TOrder.paid_balance <= items['paid_balance_end'])
        
        if 'paid_lock_balance' in items:
            q = q.where(TOrder.paid_lock_balance == items['paid_lock_balance'])
        if 'paid_lock_balance_start' in items:
            q = q.where(TOrder.paid_lock_balance >= items['paid_lock_balance_start'])
        if 'paid_lock_balance_end' in items:
            q = q.where(TOrder.paid_lock_balance <= items['paid_lock_balance_end'])
        
        if 'delivery_company' in items:
            q = q.where(TOrder.delivery_company == items['delivery_company'])
        if 'delivery_company_start' in items:
            q = q.where(TOrder.delivery_company >= items['delivery_company_start'])
        if 'delivery_company_end' in items:
            q = q.where(TOrder.delivery_company <= items['delivery_company_end'])
        
        if 'complete_time' in items:
            q = q.where(TOrder.complete_time == items['complete_time'])
        if 'complete_time_start' in items:
            q = q.where(TOrder.complete_time >= items['complete_time_start'])
        if 'complete_time_end' in items:
            q = q.where(TOrder.complete_time <= items['complete_time_end'])
        
        if 'use_balance' in items:
            q = q.where(TOrder.use_balance == items['use_balance'])
        if 'use_balance_start' in items:
            q = q.where(TOrder.use_balance >= items['use_balance_start'])
        if 'use_balance_end' in items:
            q = q.where(TOrder.use_balance <= items['use_balance_end'])
        
        if 'use_coin' in items:
            q = q.where(TOrder.use_coin == items['use_coin'])
        if 'use_coin_start' in items:
            q = q.where(TOrder.use_coin >= items['use_coin_start'])
        if 'use_coin_end' in items:
            q = q.where(TOrder.use_coin <= items['use_coin_end'])
        
        if 'consignee_province' in items:
            q = q.where(TOrder.consignee_province == items['consignee_province'])
        if 'consignee_province_start' in items:
            q = q.where(TOrder.consignee_province >= items['consignee_province_start'])
        if 'consignee_province_end' in items:
            q = q.where(TOrder.consignee_province <= items['consignee_province_end'])
        
        if 'consignee_description' in items:
            q = q.where(TOrder.consignee_description == items['consignee_description'])
        if 'consignee_description_start' in items:
            q = q.where(TOrder.consignee_description >= items['consignee_description_start'])
        if 'consignee_description_end' in items:
            q = q.where(TOrder.consignee_description <= items['consignee_description_end'])
        
        if 'consignee_city' in items:
            q = q.where(TOrder.consignee_city == items['consignee_city'])
        if 'consignee_city_start' in items:
            q = q.where(TOrder.consignee_city >= items['consignee_city_start'])
        if 'consignee_city_end' in items:
            q = q.where(TOrder.consignee_city <= items['consignee_city_end'])
        
        if 'consignee_area' in items:
            q = q.where(TOrder.consignee_area == items['consignee_area'])
        if 'consignee_area_start' in items:
            q = q.where(TOrder.consignee_area >= items['consignee_area_start'])
        if 'consignee_area_end' in items:
            q = q.where(TOrder.consignee_area <= items['consignee_area_end'])
        
        if 'consignee_street' in items:
            q = q.where(TOrder.consignee_street == items['consignee_street'])
        if 'consignee_street_start' in items:
            q = q.where(TOrder.consignee_street >= items['consignee_street_start'])
        if 'consignee_street_end' in items:
            q = q.where(TOrder.consignee_street <= items['consignee_street_end'])
        
        if 'out_trade_no' in items:
            q = q.where(TOrder.out_trade_no == items['out_trade_no'])
        if 'out_trade_no_start' in items:
            q = q.where(TOrder.out_trade_no >= items['out_trade_no_start'])
        if 'out_trade_no_end' in items:
            q = q.where(TOrder.out_trade_no <= items['out_trade_no_end'])
        
        if 'code' in items:
            q = q.where(TOrder.code == items['code'])
        if 'code_start' in items:
            q = q.where(TOrder.code >= items['code_start'])
        if 'code_end' in items:
            q = q.where(TOrder.code <= items['code_end'])
        
        if 'code_expired_time' in items:
            q = q.where(TOrder.code_expired_time == items['code_expired_time'])
        if 'code_expired_time_start' in items:
            q = q.where(TOrder.code_expired_time >= items['code_expired_time_start'])
        if 'code_expired_time_end' in items:
            q = q.where(TOrder.code_expired_time <= items['code_expired_time_end'])
        
        if 'is_display' in items:
            q = q.where(TOrder.is_display == items['is_display'])
        if 'is_display_start' in items:
            q = q.where(TOrder.is_display >= items['is_display_start'])
        if 'is_display_end' in items:
            q = q.where(TOrder.is_display <= items['is_display_end'])
        
        if 'recommender_id' in items:
            q = q.where(TOrder.recommender_id == items['recommender_id'])
        if 'recommender_id_start' in items:
            q = q.where(TOrder.recommender_id >= items['recommender_id_start'])
        if 'recommender_id_end' in items:
            q = q.where(TOrder.recommender_id <= items['recommender_id_end'])
        
        if 'detail' in items:
            q = q.where(TOrder.detail == items['detail'])
        if 'detail_start' in items:
            q = q.where(TOrder.detail >= items['detail_start'])
        if 'detail_end' in items:
            q = q.where(TOrder.detail <= items['detail_end'])
        
        if 'is_assign_income' in items:
            q = q.where(TOrder.is_assign_income == items['is_assign_income'])
        if 'is_assign_income_start' in items:
            q = q.where(TOrder.is_assign_income >= items['is_assign_income_start'])
        if 'is_assign_income_end' in items:
            q = q.where(TOrder.is_assign_income <= items['is_assign_income_end'])
        
        if 'parent_uid' in items:
            q = q.where(TOrder.parent_uid == items['parent_uid'])
        if 'parent_uid_start' in items:
            q = q.where(TOrder.parent_uid >= items['parent_uid_start'])
        if 'parent_uid_end' in items:
            q = q.where(TOrder.parent_uid <= items['parent_uid_end'])
        
        if 'top_uid' in items:
            q = q.where(TOrder.top_uid == items['top_uid'])
        if 'top_uid_start' in items:
            q = q.where(TOrder.top_uid >= items['top_uid_start'])
        if 'top_uid_end' in items:
            q = q.where(TOrder.top_uid <= items['top_uid_end'])
        
        if 'invited_uid' in items:
            q = q.where(TOrder.invited_uid == items['invited_uid'])
        if 'invited_uid_start' in items:
            q = q.where(TOrder.invited_uid >= items['invited_uid_start'])
        if 'invited_uid_end' in items:
            q = q.where(TOrder.invited_uid <= items['invited_uid_end'])
        
        if 'supplier_uid' in items:
            q = q.where(TOrder.supplier_uid == items['supplier_uid'])
        if 'supplier_uid_start' in items:
            q = q.where(TOrder.supplier_uid >= items['supplier_uid_start'])
        if 'supplier_uid_end' in items:
            q = q.where(TOrder.supplier_uid <= items['supplier_uid_end'])
        
        if 'eqlevel_uid' in items:
            q = q.where(TOrder.eqlevel_uid == items['eqlevel_uid'])
        if 'eqlevel_uid_start' in items:
            q = q.where(TOrder.eqlevel_uid >= items['eqlevel_uid_start'])
        if 'eqlevel_uid_end' in items:
            q = q.where(TOrder.eqlevel_uid <= items['eqlevel_uid_end'])
        

        if 'id' in set_items:
            q = q.where(TOrder.id.in_(set_items['id']))
        
        if 'good_id' in set_items:
            q = q.where(TOrder.good_id.in_(set_items['good_id']))
        
        if 'paider_id' in set_items:
            q = q.where(TOrder.paider_id.in_(set_items['paider_id']))
        
        if 'sale_price' in set_items:
            q = q.where(TOrder.sale_price.in_(set_items['sale_price']))
        
        if 'cost_price' in set_items:
            q = q.where(TOrder.cost_price.in_(set_items['cost_price']))
        
        if 'create_time' in set_items:
            q = q.where(TOrder.create_time.in_(set_items['create_time']))
        
        if 'paid_time' in set_items:
            q = q.where(TOrder.paid_time.in_(set_items['paid_time']))
        
        if 'status_id' in set_items:
            q = q.where(TOrder.status_id.in_(set_items['status_id']))
        
        if 'number' in set_items:
            q = q.where(TOrder.number.in_(set_items['number']))
        
        if 'consignee_address' in set_items:
            q = q.where(TOrder.consignee_address.in_(set_items['consignee_address']))
        
        if 'consignee_phone' in set_items:
            q = q.where(TOrder.consignee_phone.in_(set_items['consignee_phone']))
        
        if 'store_id' in set_items:
            q = q.where(TOrder.store_id.in_(set_items['store_id']))
        
        if 'paid_amount' in set_items:
            q = q.where(TOrder.paid_amount.in_(set_items['paid_amount']))
        
        if 'delivery_fee' in set_items:
            q = q.where(TOrder.delivery_fee.in_(set_items['delivery_fee']))
        
        if 'spec_id' in set_items:
            q = q.where(TOrder.spec_id.in_(set_items['spec_id']))
        
        if 'paid_coin' in set_items:
            q = q.where(TOrder.paid_coin.in_(set_items['paid_coin']))
        
        if 'delivery_track_code' in set_items:
            q = q.where(TOrder.delivery_track_code.in_(set_items['delivery_track_code']))
        
        if 'paid_channel_id' in set_items:
            q = q.where(TOrder.paid_channel_id.in_(set_items['paid_channel_id']))
        
        if 'consignee_name' in set_items:
            q = q.where(TOrder.consignee_name.in_(set_items['consignee_name']))
        
        if 'delivery_time' in set_items:
            q = q.where(TOrder.delivery_time.in_(set_items['delivery_time']))
        
        if 'good_name' in set_items:
            q = q.where(TOrder.good_name.in_(set_items['good_name']))
        
        if 'paid_track_code' in set_items:
            q = q.where(TOrder.paid_track_code.in_(set_items['paid_track_code']))
        
        if 'paider_name' in set_items:
            q = q.where(TOrder.paider_name.in_(set_items['paider_name']))
        
        if 'paider_phone' in set_items:
            q = q.where(TOrder.paider_phone.in_(set_items['paider_phone']))
        
        if 'paider_address' in set_items:
            q = q.where(TOrder.paider_address.in_(set_items['paider_address']))
        
        if 'supplier_id' in set_items:
            q = q.where(TOrder.supplier_id.in_(set_items['supplier_id']))
        
        if 'paid_balance' in set_items:
            q = q.where(TOrder.paid_balance.in_(set_items['paid_balance']))
        
        if 'paid_lock_balance' in set_items:
            q = q.where(TOrder.paid_lock_balance.in_(set_items['paid_lock_balance']))
        
        if 'delivery_company' in set_items:
            q = q.where(TOrder.delivery_company.in_(set_items['delivery_company']))
        
        if 'complete_time' in set_items:
            q = q.where(TOrder.complete_time.in_(set_items['complete_time']))
        
        if 'use_balance' in set_items:
            q = q.where(TOrder.use_balance.in_(set_items['use_balance']))
        
        if 'use_coin' in set_items:
            q = q.where(TOrder.use_coin.in_(set_items['use_coin']))
        
        if 'consignee_province' in set_items:
            q = q.where(TOrder.consignee_province.in_(set_items['consignee_province']))
        
        if 'consignee_description' in set_items:
            q = q.where(TOrder.consignee_description.in_(set_items['consignee_description']))
        
        if 'consignee_city' in set_items:
            q = q.where(TOrder.consignee_city.in_(set_items['consignee_city']))
        
        if 'consignee_area' in set_items:
            q = q.where(TOrder.consignee_area.in_(set_items['consignee_area']))
        
        if 'consignee_street' in set_items:
            q = q.where(TOrder.consignee_street.in_(set_items['consignee_street']))
        
        if 'out_trade_no' in set_items:
            q = q.where(TOrder.out_trade_no.in_(set_items['out_trade_no']))
        
        if 'code' in set_items:
            q = q.where(TOrder.code.in_(set_items['code']))
        
        if 'code_expired_time' in set_items:
            q = q.where(TOrder.code_expired_time.in_(set_items['code_expired_time']))
        
        if 'is_display' in set_items:
            q = q.where(TOrder.is_display.in_(set_items['is_display']))
        
        if 'recommender_id' in set_items:
            q = q.where(TOrder.recommender_id.in_(set_items['recommender_id']))
        
        if 'detail' in set_items:
            q = q.where(TOrder.detail.in_(set_items['detail']))
        
        if 'is_assign_income' in set_items:
            q = q.where(TOrder.is_assign_income.in_(set_items['is_assign_income']))
        
        if 'parent_uid' in set_items:
            q = q.where(TOrder.parent_uid.in_(set_items['parent_uid']))
        
        if 'top_uid' in set_items:
            q = q.where(TOrder.top_uid.in_(set_items['top_uid']))
        
        if 'invited_uid' in set_items:
            q = q.where(TOrder.invited_uid.in_(set_items['invited_uid']))
        
        if 'supplier_uid' in set_items:
            q = q.where(TOrder.supplier_uid.in_(set_items['supplier_uid']))
        
        if 'eqlevel_uid' in set_items:
            q = q.where(TOrder.eqlevel_uid.in_(set_items['eqlevel_uid']))
        

        if 'consignee_address' in search_items:
            q = q.where(TOrder.consignee_address.like(search_items['consignee_address']))
        
        if 'consignee_phone' in search_items:
            q = q.where(TOrder.consignee_phone.like(search_items['consignee_phone']))
        
        if 'delivery_track_code' in search_items:
            q = q.where(TOrder.delivery_track_code.like(search_items['delivery_track_code']))
        
        if 'consignee_name' in search_items:
            q = q.where(TOrder.consignee_name.like(search_items['consignee_name']))
        
        if 'good_name' in search_items:
            q = q.where(TOrder.good_name.like(search_items['good_name']))
        
        if 'paid_track_code' in search_items:
            q = q.where(TOrder.paid_track_code.like(search_items['paid_track_code']))
        
        if 'paider_name' in search_items:
            q = q.where(TOrder.paider_name.like(search_items['paider_name']))
        
        if 'paider_phone' in search_items:
            q = q.where(TOrder.paider_phone.like(search_items['paider_phone']))
        
        if 'paider_address' in search_items:
            q = q.where(TOrder.paider_address.like(search_items['paider_address']))
        
        if 'delivery_company' in search_items:
            q = q.where(TOrder.delivery_company.like(search_items['delivery_company']))
        
        if 'consignee_province' in search_items:
            q = q.where(TOrder.consignee_province.like(search_items['consignee_province']))
        
        if 'consignee_description' in search_items:
            q = q.where(TOrder.consignee_description.like(search_items['consignee_description']))
        
        if 'consignee_city' in search_items:
            q = q.where(TOrder.consignee_city.like(search_items['consignee_city']))
        
        if 'consignee_area' in search_items:
            q = q.where(TOrder.consignee_area.like(search_items['consignee_area']))
        
        if 'consignee_street' in search_items:
            q = q.where(TOrder.consignee_street.like(search_items['consignee_street']))
        
        if 'out_trade_no' in search_items:
            q = q.where(TOrder.out_trade_no.like(search_items['out_trade_no']))
        
        if 'code' in search_items:
            q = q.where(TOrder.code.like(search_items['code']))
        
        if 'detail' in search_items:
            q = q.where(TOrder.detail.like(search_items['detail']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TOrder.eqlevel_uid.asc())
                orders.append(TOrder.id.asc())
            elif val == 'desc':
                #orders.append(TOrder.eqlevel_uid.desc())
                orders.append(TOrder.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_order_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SOrder.parse_obj(t.__dict__) for t in t_order_list]


def filter_count_order(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TOrder)


        if 'id' in items:
            q = q.where(TOrder.id == items['id'])
        if 'id_start' in items:
            q = q.where(TOrder.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TOrder.id <= items['id_end'])
        
        if 'good_id' in items:
            q = q.where(TOrder.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TOrder.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TOrder.good_id <= items['good_id_end'])
        
        if 'paider_id' in items:
            q = q.where(TOrder.paider_id == items['paider_id'])
        if 'paider_id_start' in items:
            q = q.where(TOrder.paider_id >= items['paider_id_start'])
        if 'paider_id_end' in items:
            q = q.where(TOrder.paider_id <= items['paider_id_end'])
        
        if 'sale_price' in items:
            q = q.where(TOrder.sale_price == items['sale_price'])
        if 'sale_price_start' in items:
            q = q.where(TOrder.sale_price >= items['sale_price_start'])
        if 'sale_price_end' in items:
            q = q.where(TOrder.sale_price <= items['sale_price_end'])
        
        if 'cost_price' in items:
            q = q.where(TOrder.cost_price == items['cost_price'])
        if 'cost_price_start' in items:
            q = q.where(TOrder.cost_price >= items['cost_price_start'])
        if 'cost_price_end' in items:
            q = q.where(TOrder.cost_price <= items['cost_price_end'])
        
        if 'create_time' in items:
            q = q.where(TOrder.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TOrder.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TOrder.create_time <= items['create_time_end'])
        
        if 'paid_time' in items:
            q = q.where(TOrder.paid_time == items['paid_time'])
        if 'paid_time_start' in items:
            q = q.where(TOrder.paid_time >= items['paid_time_start'])
        if 'paid_time_end' in items:
            q = q.where(TOrder.paid_time <= items['paid_time_end'])
        
        if 'status_id' in items:
            q = q.where(TOrder.status_id == items['status_id'])
        if 'status_id_start' in items:
            q = q.where(TOrder.status_id >= items['status_id_start'])
        if 'status_id_end' in items:
            q = q.where(TOrder.status_id <= items['status_id_end'])
        
        if 'number' in items:
            q = q.where(TOrder.number == items['number'])
        if 'number_start' in items:
            q = q.where(TOrder.number >= items['number_start'])
        if 'number_end' in items:
            q = q.where(TOrder.number <= items['number_end'])
        
        if 'consignee_address' in items:
            q = q.where(TOrder.consignee_address == items['consignee_address'])
        if 'consignee_address_start' in items:
            q = q.where(TOrder.consignee_address >= items['consignee_address_start'])
        if 'consignee_address_end' in items:
            q = q.where(TOrder.consignee_address <= items['consignee_address_end'])
        
        if 'consignee_phone' in items:
            q = q.where(TOrder.consignee_phone == items['consignee_phone'])
        if 'consignee_phone_start' in items:
            q = q.where(TOrder.consignee_phone >= items['consignee_phone_start'])
        if 'consignee_phone_end' in items:
            q = q.where(TOrder.consignee_phone <= items['consignee_phone_end'])
        
        if 'store_id' in items:
            q = q.where(TOrder.store_id == items['store_id'])
        if 'store_id_start' in items:
            q = q.where(TOrder.store_id >= items['store_id_start'])
        if 'store_id_end' in items:
            q = q.where(TOrder.store_id <= items['store_id_end'])
        
        if 'paid_amount' in items:
            q = q.where(TOrder.paid_amount == items['paid_amount'])
        if 'paid_amount_start' in items:
            q = q.where(TOrder.paid_amount >= items['paid_amount_start'])
        if 'paid_amount_end' in items:
            q = q.where(TOrder.paid_amount <= items['paid_amount_end'])
        
        if 'delivery_fee' in items:
            q = q.where(TOrder.delivery_fee == items['delivery_fee'])
        if 'delivery_fee_start' in items:
            q = q.where(TOrder.delivery_fee >= items['delivery_fee_start'])
        if 'delivery_fee_end' in items:
            q = q.where(TOrder.delivery_fee <= items['delivery_fee_end'])
        
        if 'spec_id' in items:
            q = q.where(TOrder.spec_id == items['spec_id'])
        if 'spec_id_start' in items:
            q = q.where(TOrder.spec_id >= items['spec_id_start'])
        if 'spec_id_end' in items:
            q = q.where(TOrder.spec_id <= items['spec_id_end'])
        
        if 'paid_coin' in items:
            q = q.where(TOrder.paid_coin == items['paid_coin'])
        if 'paid_coin_start' in items:
            q = q.where(TOrder.paid_coin >= items['paid_coin_start'])
        if 'paid_coin_end' in items:
            q = q.where(TOrder.paid_coin <= items['paid_coin_end'])
        
        if 'delivery_track_code' in items:
            q = q.where(TOrder.delivery_track_code == items['delivery_track_code'])
        if 'delivery_track_code_start' in items:
            q = q.where(TOrder.delivery_track_code >= items['delivery_track_code_start'])
        if 'delivery_track_code_end' in items:
            q = q.where(TOrder.delivery_track_code <= items['delivery_track_code_end'])
        
        if 'paid_channel_id' in items:
            q = q.where(TOrder.paid_channel_id == items['paid_channel_id'])
        if 'paid_channel_id_start' in items:
            q = q.where(TOrder.paid_channel_id >= items['paid_channel_id_start'])
        if 'paid_channel_id_end' in items:
            q = q.where(TOrder.paid_channel_id <= items['paid_channel_id_end'])
        
        if 'consignee_name' in items:
            q = q.where(TOrder.consignee_name == items['consignee_name'])
        if 'consignee_name_start' in items:
            q = q.where(TOrder.consignee_name >= items['consignee_name_start'])
        if 'consignee_name_end' in items:
            q = q.where(TOrder.consignee_name <= items['consignee_name_end'])
        
        if 'delivery_time' in items:
            q = q.where(TOrder.delivery_time == items['delivery_time'])
        if 'delivery_time_start' in items:
            q = q.where(TOrder.delivery_time >= items['delivery_time_start'])
        if 'delivery_time_end' in items:
            q = q.where(TOrder.delivery_time <= items['delivery_time_end'])
        
        if 'good_name' in items:
            q = q.where(TOrder.good_name == items['good_name'])
        if 'good_name_start' in items:
            q = q.where(TOrder.good_name >= items['good_name_start'])
        if 'good_name_end' in items:
            q = q.where(TOrder.good_name <= items['good_name_end'])
        
        if 'paid_track_code' in items:
            q = q.where(TOrder.paid_track_code == items['paid_track_code'])
        if 'paid_track_code_start' in items:
            q = q.where(TOrder.paid_track_code >= items['paid_track_code_start'])
        if 'paid_track_code_end' in items:
            q = q.where(TOrder.paid_track_code <= items['paid_track_code_end'])
        
        if 'paider_name' in items:
            q = q.where(TOrder.paider_name == items['paider_name'])
        if 'paider_name_start' in items:
            q = q.where(TOrder.paider_name >= items['paider_name_start'])
        if 'paider_name_end' in items:
            q = q.where(TOrder.paider_name <= items['paider_name_end'])
        
        if 'paider_phone' in items:
            q = q.where(TOrder.paider_phone == items['paider_phone'])
        if 'paider_phone_start' in items:
            q = q.where(TOrder.paider_phone >= items['paider_phone_start'])
        if 'paider_phone_end' in items:
            q = q.where(TOrder.paider_phone <= items['paider_phone_end'])
        
        if 'paider_address' in items:
            q = q.where(TOrder.paider_address == items['paider_address'])
        if 'paider_address_start' in items:
            q = q.where(TOrder.paider_address >= items['paider_address_start'])
        if 'paider_address_end' in items:
            q = q.where(TOrder.paider_address <= items['paider_address_end'])
        
        if 'supplier_id' in items:
            q = q.where(TOrder.supplier_id == items['supplier_id'])
        if 'supplier_id_start' in items:
            q = q.where(TOrder.supplier_id >= items['supplier_id_start'])
        if 'supplier_id_end' in items:
            q = q.where(TOrder.supplier_id <= items['supplier_id_end'])
        
        if 'paid_balance' in items:
            q = q.where(TOrder.paid_balance == items['paid_balance'])
        if 'paid_balance_start' in items:
            q = q.where(TOrder.paid_balance >= items['paid_balance_start'])
        if 'paid_balance_end' in items:
            q = q.where(TOrder.paid_balance <= items['paid_balance_end'])
        
        if 'paid_lock_balance' in items:
            q = q.where(TOrder.paid_lock_balance == items['paid_lock_balance'])
        if 'paid_lock_balance_start' in items:
            q = q.where(TOrder.paid_lock_balance >= items['paid_lock_balance_start'])
        if 'paid_lock_balance_end' in items:
            q = q.where(TOrder.paid_lock_balance <= items['paid_lock_balance_end'])
        
        if 'delivery_company' in items:
            q = q.where(TOrder.delivery_company == items['delivery_company'])
        if 'delivery_company_start' in items:
            q = q.where(TOrder.delivery_company >= items['delivery_company_start'])
        if 'delivery_company_end' in items:
            q = q.where(TOrder.delivery_company <= items['delivery_company_end'])
        
        if 'complete_time' in items:
            q = q.where(TOrder.complete_time == items['complete_time'])
        if 'complete_time_start' in items:
            q = q.where(TOrder.complete_time >= items['complete_time_start'])
        if 'complete_time_end' in items:
            q = q.where(TOrder.complete_time <= items['complete_time_end'])
        
        if 'use_balance' in items:
            q = q.where(TOrder.use_balance == items['use_balance'])
        if 'use_balance_start' in items:
            q = q.where(TOrder.use_balance >= items['use_balance_start'])
        if 'use_balance_end' in items:
            q = q.where(TOrder.use_balance <= items['use_balance_end'])
        
        if 'use_coin' in items:
            q = q.where(TOrder.use_coin == items['use_coin'])
        if 'use_coin_start' in items:
            q = q.where(TOrder.use_coin >= items['use_coin_start'])
        if 'use_coin_end' in items:
            q = q.where(TOrder.use_coin <= items['use_coin_end'])
        
        if 'consignee_province' in items:
            q = q.where(TOrder.consignee_province == items['consignee_province'])
        if 'consignee_province_start' in items:
            q = q.where(TOrder.consignee_province >= items['consignee_province_start'])
        if 'consignee_province_end' in items:
            q = q.where(TOrder.consignee_province <= items['consignee_province_end'])
        
        if 'consignee_description' in items:
            q = q.where(TOrder.consignee_description == items['consignee_description'])
        if 'consignee_description_start' in items:
            q = q.where(TOrder.consignee_description >= items['consignee_description_start'])
        if 'consignee_description_end' in items:
            q = q.where(TOrder.consignee_description <= items['consignee_description_end'])
        
        if 'consignee_city' in items:
            q = q.where(TOrder.consignee_city == items['consignee_city'])
        if 'consignee_city_start' in items:
            q = q.where(TOrder.consignee_city >= items['consignee_city_start'])
        if 'consignee_city_end' in items:
            q = q.where(TOrder.consignee_city <= items['consignee_city_end'])
        
        if 'consignee_area' in items:
            q = q.where(TOrder.consignee_area == items['consignee_area'])
        if 'consignee_area_start' in items:
            q = q.where(TOrder.consignee_area >= items['consignee_area_start'])
        if 'consignee_area_end' in items:
            q = q.where(TOrder.consignee_area <= items['consignee_area_end'])
        
        if 'consignee_street' in items:
            q = q.where(TOrder.consignee_street == items['consignee_street'])
        if 'consignee_street_start' in items:
            q = q.where(TOrder.consignee_street >= items['consignee_street_start'])
        if 'consignee_street_end' in items:
            q = q.where(TOrder.consignee_street <= items['consignee_street_end'])
        
        if 'out_trade_no' in items:
            q = q.where(TOrder.out_trade_no == items['out_trade_no'])
        if 'out_trade_no_start' in items:
            q = q.where(TOrder.out_trade_no >= items['out_trade_no_start'])
        if 'out_trade_no_end' in items:
            q = q.where(TOrder.out_trade_no <= items['out_trade_no_end'])
        
        if 'code' in items:
            q = q.where(TOrder.code == items['code'])
        if 'code_start' in items:
            q = q.where(TOrder.code >= items['code_start'])
        if 'code_end' in items:
            q = q.where(TOrder.code <= items['code_end'])
        
        if 'code_expired_time' in items:
            q = q.where(TOrder.code_expired_time == items['code_expired_time'])
        if 'code_expired_time_start' in items:
            q = q.where(TOrder.code_expired_time >= items['code_expired_time_start'])
        if 'code_expired_time_end' in items:
            q = q.where(TOrder.code_expired_time <= items['code_expired_time_end'])
        
        if 'is_display' in items:
            q = q.where(TOrder.is_display == items['is_display'])
        if 'is_display_start' in items:
            q = q.where(TOrder.is_display >= items['is_display_start'])
        if 'is_display_end' in items:
            q = q.where(TOrder.is_display <= items['is_display_end'])
        
        if 'recommender_id' in items:
            q = q.where(TOrder.recommender_id == items['recommender_id'])
        if 'recommender_id_start' in items:
            q = q.where(TOrder.recommender_id >= items['recommender_id_start'])
        if 'recommender_id_end' in items:
            q = q.where(TOrder.recommender_id <= items['recommender_id_end'])
        
        if 'detail' in items:
            q = q.where(TOrder.detail == items['detail'])
        if 'detail_start' in items:
            q = q.where(TOrder.detail >= items['detail_start'])
        if 'detail_end' in items:
            q = q.where(TOrder.detail <= items['detail_end'])
        
        if 'is_assign_income' in items:
            q = q.where(TOrder.is_assign_income == items['is_assign_income'])
        if 'is_assign_income_start' in items:
            q = q.where(TOrder.is_assign_income >= items['is_assign_income_start'])
        if 'is_assign_income_end' in items:
            q = q.where(TOrder.is_assign_income <= items['is_assign_income_end'])
        
        if 'parent_uid' in items:
            q = q.where(TOrder.parent_uid == items['parent_uid'])
        if 'parent_uid_start' in items:
            q = q.where(TOrder.parent_uid >= items['parent_uid_start'])
        if 'parent_uid_end' in items:
            q = q.where(TOrder.parent_uid <= items['parent_uid_end'])
        
        if 'top_uid' in items:
            q = q.where(TOrder.top_uid == items['top_uid'])
        if 'top_uid_start' in items:
            q = q.where(TOrder.top_uid >= items['top_uid_start'])
        if 'top_uid_end' in items:
            q = q.where(TOrder.top_uid <= items['top_uid_end'])
        
        if 'invited_uid' in items:
            q = q.where(TOrder.invited_uid == items['invited_uid'])
        if 'invited_uid_start' in items:
            q = q.where(TOrder.invited_uid >= items['invited_uid_start'])
        if 'invited_uid_end' in items:
            q = q.where(TOrder.invited_uid <= items['invited_uid_end'])
        
        if 'supplier_uid' in items:
            q = q.where(TOrder.supplier_uid == items['supplier_uid'])
        if 'supplier_uid_start' in items:
            q = q.where(TOrder.supplier_uid >= items['supplier_uid_start'])
        if 'supplier_uid_end' in items:
            q = q.where(TOrder.supplier_uid <= items['supplier_uid_end'])
        
        if 'eqlevel_uid' in items:
            q = q.where(TOrder.eqlevel_uid == items['eqlevel_uid'])
        if 'eqlevel_uid_start' in items:
            q = q.where(TOrder.eqlevel_uid >= items['eqlevel_uid_start'])
        if 'eqlevel_uid_end' in items:
            q = q.where(TOrder.eqlevel_uid <= items['eqlevel_uid_end'])
        

        if 'id' in set_items:
            q = q.where(TOrder.id.in_(set_items['id']))
        
        if 'good_id' in set_items:
            q = q.where(TOrder.good_id.in_(set_items['good_id']))
        
        if 'paider_id' in set_items:
            q = q.where(TOrder.paider_id.in_(set_items['paider_id']))
        
        if 'sale_price' in set_items:
            q = q.where(TOrder.sale_price.in_(set_items['sale_price']))
        
        if 'cost_price' in set_items:
            q = q.where(TOrder.cost_price.in_(set_items['cost_price']))
        
        if 'create_time' in set_items:
            q = q.where(TOrder.create_time.in_(set_items['create_time']))
        
        if 'paid_time' in set_items:
            q = q.where(TOrder.paid_time.in_(set_items['paid_time']))
        
        if 'status_id' in set_items:
            q = q.where(TOrder.status_id.in_(set_items['status_id']))
        
        if 'number' in set_items:
            q = q.where(TOrder.number.in_(set_items['number']))
        
        if 'consignee_address' in set_items:
            q = q.where(TOrder.consignee_address.in_(set_items['consignee_address']))
        
        if 'consignee_phone' in set_items:
            q = q.where(TOrder.consignee_phone.in_(set_items['consignee_phone']))
        
        if 'store_id' in set_items:
            q = q.where(TOrder.store_id.in_(set_items['store_id']))
        
        if 'paid_amount' in set_items:
            q = q.where(TOrder.paid_amount.in_(set_items['paid_amount']))
        
        if 'delivery_fee' in set_items:
            q = q.where(TOrder.delivery_fee.in_(set_items['delivery_fee']))
        
        if 'spec_id' in set_items:
            q = q.where(TOrder.spec_id.in_(set_items['spec_id']))
        
        if 'paid_coin' in set_items:
            q = q.where(TOrder.paid_coin.in_(set_items['paid_coin']))
        
        if 'delivery_track_code' in set_items:
            q = q.where(TOrder.delivery_track_code.in_(set_items['delivery_track_code']))
        
        if 'paid_channel_id' in set_items:
            q = q.where(TOrder.paid_channel_id.in_(set_items['paid_channel_id']))
        
        if 'consignee_name' in set_items:
            q = q.where(TOrder.consignee_name.in_(set_items['consignee_name']))
        
        if 'delivery_time' in set_items:
            q = q.where(TOrder.delivery_time.in_(set_items['delivery_time']))
        
        if 'good_name' in set_items:
            q = q.where(TOrder.good_name.in_(set_items['good_name']))
        
        if 'paid_track_code' in set_items:
            q = q.where(TOrder.paid_track_code.in_(set_items['paid_track_code']))
        
        if 'paider_name' in set_items:
            q = q.where(TOrder.paider_name.in_(set_items['paider_name']))
        
        if 'paider_phone' in set_items:
            q = q.where(TOrder.paider_phone.in_(set_items['paider_phone']))
        
        if 'paider_address' in set_items:
            q = q.where(TOrder.paider_address.in_(set_items['paider_address']))
        
        if 'supplier_id' in set_items:
            q = q.where(TOrder.supplier_id.in_(set_items['supplier_id']))
        
        if 'paid_balance' in set_items:
            q = q.where(TOrder.paid_balance.in_(set_items['paid_balance']))
        
        if 'paid_lock_balance' in set_items:
            q = q.where(TOrder.paid_lock_balance.in_(set_items['paid_lock_balance']))
        
        if 'delivery_company' in set_items:
            q = q.where(TOrder.delivery_company.in_(set_items['delivery_company']))
        
        if 'complete_time' in set_items:
            q = q.where(TOrder.complete_time.in_(set_items['complete_time']))
        
        if 'use_balance' in set_items:
            q = q.where(TOrder.use_balance.in_(set_items['use_balance']))
        
        if 'use_coin' in set_items:
            q = q.where(TOrder.use_coin.in_(set_items['use_coin']))
        
        if 'consignee_province' in set_items:
            q = q.where(TOrder.consignee_province.in_(set_items['consignee_province']))
        
        if 'consignee_description' in set_items:
            q = q.where(TOrder.consignee_description.in_(set_items['consignee_description']))
        
        if 'consignee_city' in set_items:
            q = q.where(TOrder.consignee_city.in_(set_items['consignee_city']))
        
        if 'consignee_area' in set_items:
            q = q.where(TOrder.consignee_area.in_(set_items['consignee_area']))
        
        if 'consignee_street' in set_items:
            q = q.where(TOrder.consignee_street.in_(set_items['consignee_street']))
        
        if 'out_trade_no' in set_items:
            q = q.where(TOrder.out_trade_no.in_(set_items['out_trade_no']))
        
        if 'code' in set_items:
            q = q.where(TOrder.code.in_(set_items['code']))
        
        if 'code_expired_time' in set_items:
            q = q.where(TOrder.code_expired_time.in_(set_items['code_expired_time']))
        
        if 'is_display' in set_items:
            q = q.where(TOrder.is_display.in_(set_items['is_display']))
        
        if 'recommender_id' in set_items:
            q = q.where(TOrder.recommender_id.in_(set_items['recommender_id']))
        
        if 'detail' in set_items:
            q = q.where(TOrder.detail.in_(set_items['detail']))
        
        if 'is_assign_income' in set_items:
            q = q.where(TOrder.is_assign_income.in_(set_items['is_assign_income']))
        
        if 'parent_uid' in set_items:
            q = q.where(TOrder.parent_uid.in_(set_items['parent_uid']))
        
        if 'top_uid' in set_items:
            q = q.where(TOrder.top_uid.in_(set_items['top_uid']))
        
        if 'invited_uid' in set_items:
            q = q.where(TOrder.invited_uid.in_(set_items['invited_uid']))
        
        if 'supplier_uid' in set_items:
            q = q.where(TOrder.supplier_uid.in_(set_items['supplier_uid']))
        
        if 'eqlevel_uid' in set_items:
            q = q.where(TOrder.eqlevel_uid.in_(set_items['eqlevel_uid']))
        

        if 'consignee_address' in search_items:
            q = q.where(TOrder.consignee_address.like(search_items['consignee_address']))
        
        if 'consignee_phone' in search_items:
            q = q.where(TOrder.consignee_phone.like(search_items['consignee_phone']))
        
        if 'delivery_track_code' in search_items:
            q = q.where(TOrder.delivery_track_code.like(search_items['delivery_track_code']))
        
        if 'consignee_name' in search_items:
            q = q.where(TOrder.consignee_name.like(search_items['consignee_name']))
        
        if 'good_name' in search_items:
            q = q.where(TOrder.good_name.like(search_items['good_name']))
        
        if 'paid_track_code' in search_items:
            q = q.where(TOrder.paid_track_code.like(search_items['paid_track_code']))
        
        if 'paider_name' in search_items:
            q = q.where(TOrder.paider_name.like(search_items['paider_name']))
        
        if 'paider_phone' in search_items:
            q = q.where(TOrder.paider_phone.like(search_items['paider_phone']))
        
        if 'paider_address' in search_items:
            q = q.where(TOrder.paider_address.like(search_items['paider_address']))
        
        if 'delivery_company' in search_items:
            q = q.where(TOrder.delivery_company.like(search_items['delivery_company']))
        
        if 'consignee_province' in search_items:
            q = q.where(TOrder.consignee_province.like(search_items['consignee_province']))
        
        if 'consignee_description' in search_items:
            q = q.where(TOrder.consignee_description.like(search_items['consignee_description']))
        
        if 'consignee_city' in search_items:
            q = q.where(TOrder.consignee_city.like(search_items['consignee_city']))
        
        if 'consignee_area' in search_items:
            q = q.where(TOrder.consignee_area.like(search_items['consignee_area']))
        
        if 'consignee_street' in search_items:
            q = q.where(TOrder.consignee_street.like(search_items['consignee_street']))
        
        if 'out_trade_no' in search_items:
            q = q.where(TOrder.out_trade_no.like(search_items['out_trade_no']))
        
        if 'code' in search_items:
            q = q.where(TOrder.code.like(search_items['code']))
        
        if 'detail' in search_items:
            q = q.where(TOrder.detail.like(search_items['detail']))
        
    
        c = q.count()
        return c

    
def insert_order_batch(item: CreateOrderBatch, db: Optional[SessionLocal] = None) -> SOrderBatch:
    data = model2dict(item)
    t = TOrderBatch(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SOrderBatch.parse_obj(t.__dict__)

    
def delete_order_batch(order_batch_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TOrderBatch).where(TOrderBatch.id == order_batch_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TOrderBatch).where(TOrderBatch.id == order_batch_id).delete()
        db.commit()

    
def update_order_batch(item: SOrderBatch, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TOrderBatch).where(TOrderBatch.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TOrderBatch).where(TOrderBatch.id == item.id).update(data)
        db.commit()

    
def get_order_batch(order_batch_id: int) -> Optional[SOrderBatch]:
    with Dao() as db:
        t = db.query(TOrderBatch).where(TOrderBatch.id == order_batch_id).first()
        if t:
            return SOrderBatch.parse_obj(t.__dict__)
        else:
            return None


def filter_order_batch(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SOrderBatch]:
    with Dao() as db:
        q = db.query(TOrderBatch)


        if 'id' in items:
            q = q.where(TOrderBatch.id == items['id'])
        if 'id_start' in items:
            q = q.where(TOrderBatch.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TOrderBatch.id <= items['id_end'])
        
        if 'create_time' in items:
            q = q.where(TOrderBatch.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TOrderBatch.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TOrderBatch.create_time <= items['create_time_end'])
        

        if 'id' in set_items:
            q = q.where(TOrderBatch.id.in_(set_items['id']))
        
        if 'create_time' in set_items:
            q = q.where(TOrderBatch.create_time.in_(set_items['create_time']))
        

    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TOrderBatch.create_time.asc())
                orders.append(TOrderBatch.id.asc())
            elif val == 'desc':
                #orders.append(TOrderBatch.create_time.desc())
                orders.append(TOrderBatch.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_order_batch_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SOrderBatch.parse_obj(t.__dict__) for t in t_order_batch_list]


def filter_count_order_batch(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TOrderBatch)


        if 'id' in items:
            q = q.where(TOrderBatch.id == items['id'])
        if 'id_start' in items:
            q = q.where(TOrderBatch.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TOrderBatch.id <= items['id_end'])
        
        if 'create_time' in items:
            q = q.where(TOrderBatch.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TOrderBatch.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TOrderBatch.create_time <= items['create_time_end'])
        

        if 'id' in set_items:
            q = q.where(TOrderBatch.id.in_(set_items['id']))
        
        if 'create_time' in set_items:
            q = q.where(TOrderBatch.create_time.in_(set_items['create_time']))
        

    
        c = q.count()
        return c

    
def insert_order_check(item: CreateOrderCheck, db: Optional[SessionLocal] = None) -> SOrderCheck:
    data = model2dict(item)
    t = TOrderCheck(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SOrderCheck.parse_obj(t.__dict__)

    
def delete_order_check(order_check_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TOrderCheck).where(TOrderCheck.id == order_check_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TOrderCheck).where(TOrderCheck.id == order_check_id).delete()
        db.commit()

    
def update_order_check(item: SOrderCheck, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TOrderCheck).where(TOrderCheck.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TOrderCheck).where(TOrderCheck.id == item.id).update(data)
        db.commit()

    
def get_order_check(order_check_id: int) -> Optional[SOrderCheck]:
    with Dao() as db:
        t = db.query(TOrderCheck).where(TOrderCheck.id == order_check_id).first()
        if t:
            return SOrderCheck.parse_obj(t.__dict__)
        else:
            return None


def filter_order_check(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SOrderCheck]:
    with Dao() as db:
        q = db.query(TOrderCheck)


        if 'id' in items:
            q = q.where(TOrderCheck.id == items['id'])
        if 'id_start' in items:
            q = q.where(TOrderCheck.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TOrderCheck.id <= items['id_end'])
        
        if 'order_id' in items:
            q = q.where(TOrderCheck.order_id == items['order_id'])
        if 'order_id_start' in items:
            q = q.where(TOrderCheck.order_id >= items['order_id_start'])
        if 'order_id_end' in items:
            q = q.where(TOrderCheck.order_id <= items['order_id_end'])
        
        if 'check_num' in items:
            q = q.where(TOrderCheck.check_num == items['check_num'])
        if 'check_num_start' in items:
            q = q.where(TOrderCheck.check_num >= items['check_num_start'])
        if 'check_num_end' in items:
            q = q.where(TOrderCheck.check_num <= items['check_num_end'])
        
        if 'check_time' in items:
            q = q.where(TOrderCheck.check_time == items['check_time'])
        if 'check_time_start' in items:
            q = q.where(TOrderCheck.check_time >= items['check_time_start'])
        if 'check_time_end' in items:
            q = q.where(TOrderCheck.check_time <= items['check_time_end'])
        
        if 'worker_id' in items:
            q = q.where(TOrderCheck.worker_id == items['worker_id'])
        if 'worker_id_start' in items:
            q = q.where(TOrderCheck.worker_id >= items['worker_id_start'])
        if 'worker_id_end' in items:
            q = q.where(TOrderCheck.worker_id <= items['worker_id_end'])
        
        if 'check_amount' in items:
            q = q.where(TOrderCheck.check_amount == items['check_amount'])
        if 'check_amount_start' in items:
            q = q.where(TOrderCheck.check_amount >= items['check_amount_start'])
        if 'check_amount_end' in items:
            q = q.where(TOrderCheck.check_amount <= items['check_amount_end'])
        

        if 'id' in set_items:
            q = q.where(TOrderCheck.id.in_(set_items['id']))
        
        if 'order_id' in set_items:
            q = q.where(TOrderCheck.order_id.in_(set_items['order_id']))
        
        if 'check_num' in set_items:
            q = q.where(TOrderCheck.check_num.in_(set_items['check_num']))
        
        if 'check_time' in set_items:
            q = q.where(TOrderCheck.check_time.in_(set_items['check_time']))
        
        if 'worker_id' in set_items:
            q = q.where(TOrderCheck.worker_id.in_(set_items['worker_id']))
        
        if 'check_amount' in set_items:
            q = q.where(TOrderCheck.check_amount.in_(set_items['check_amount']))
        

    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TOrderCheck.check_amount.asc())
                orders.append(TOrderCheck.id.asc())
            elif val == 'desc':
                #orders.append(TOrderCheck.check_amount.desc())
                orders.append(TOrderCheck.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_order_check_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SOrderCheck.parse_obj(t.__dict__) for t in t_order_check_list]


def filter_count_order_check(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TOrderCheck)


        if 'id' in items:
            q = q.where(TOrderCheck.id == items['id'])
        if 'id_start' in items:
            q = q.where(TOrderCheck.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TOrderCheck.id <= items['id_end'])
        
        if 'order_id' in items:
            q = q.where(TOrderCheck.order_id == items['order_id'])
        if 'order_id_start' in items:
            q = q.where(TOrderCheck.order_id >= items['order_id_start'])
        if 'order_id_end' in items:
            q = q.where(TOrderCheck.order_id <= items['order_id_end'])
        
        if 'check_num' in items:
            q = q.where(TOrderCheck.check_num == items['check_num'])
        if 'check_num_start' in items:
            q = q.where(TOrderCheck.check_num >= items['check_num_start'])
        if 'check_num_end' in items:
            q = q.where(TOrderCheck.check_num <= items['check_num_end'])
        
        if 'check_time' in items:
            q = q.where(TOrderCheck.check_time == items['check_time'])
        if 'check_time_start' in items:
            q = q.where(TOrderCheck.check_time >= items['check_time_start'])
        if 'check_time_end' in items:
            q = q.where(TOrderCheck.check_time <= items['check_time_end'])
        
        if 'worker_id' in items:
            q = q.where(TOrderCheck.worker_id == items['worker_id'])
        if 'worker_id_start' in items:
            q = q.where(TOrderCheck.worker_id >= items['worker_id_start'])
        if 'worker_id_end' in items:
            q = q.where(TOrderCheck.worker_id <= items['worker_id_end'])
        
        if 'check_amount' in items:
            q = q.where(TOrderCheck.check_amount == items['check_amount'])
        if 'check_amount_start' in items:
            q = q.where(TOrderCheck.check_amount >= items['check_amount_start'])
        if 'check_amount_end' in items:
            q = q.where(TOrderCheck.check_amount <= items['check_amount_end'])
        

        if 'id' in set_items:
            q = q.where(TOrderCheck.id.in_(set_items['id']))
        
        if 'order_id' in set_items:
            q = q.where(TOrderCheck.order_id.in_(set_items['order_id']))
        
        if 'check_num' in set_items:
            q = q.where(TOrderCheck.check_num.in_(set_items['check_num']))
        
        if 'check_time' in set_items:
            q = q.where(TOrderCheck.check_time.in_(set_items['check_time']))
        
        if 'worker_id' in set_items:
            q = q.where(TOrderCheck.worker_id.in_(set_items['worker_id']))
        
        if 'check_amount' in set_items:
            q = q.where(TOrderCheck.check_amount.in_(set_items['check_amount']))
        

    
        c = q.count()
        return c

    
def insert_order_return(item: CreateOrderReturn, db: Optional[SessionLocal] = None) -> SOrderReturn:
    data = model2dict(item)
    t = TOrderReturn(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SOrderReturn.parse_obj(t.__dict__)

    
def delete_order_return(order_return_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TOrderReturn).where(TOrderReturn.id == order_return_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TOrderReturn).where(TOrderReturn.id == order_return_id).delete()
        db.commit()

    
def update_order_return(item: SOrderReturn, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TOrderReturn).where(TOrderReturn.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TOrderReturn).where(TOrderReturn.id == item.id).update(data)
        db.commit()

    
def get_order_return(order_return_id: int) -> Optional[SOrderReturn]:
    with Dao() as db:
        t = db.query(TOrderReturn).where(TOrderReturn.id == order_return_id).first()
        if t:
            return SOrderReturn.parse_obj(t.__dict__)
        else:
            return None


def filter_order_return(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SOrderReturn]:
    with Dao() as db:
        q = db.query(TOrderReturn)


        if 'id' in items:
            q = q.where(TOrderReturn.id == items['id'])
        if 'id_start' in items:
            q = q.where(TOrderReturn.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TOrderReturn.id <= items['id_end'])
        
        if 'returner_name' in items:
            q = q.where(TOrderReturn.returner_name == items['returner_name'])
        if 'returner_name_start' in items:
            q = q.where(TOrderReturn.returner_name >= items['returner_name_start'])
        if 'returner_name_end' in items:
            q = q.where(TOrderReturn.returner_name <= items['returner_name_end'])
        
        if 'returner_phone' in items:
            q = q.where(TOrderReturn.returner_phone == items['returner_phone'])
        if 'returner_phone_start' in items:
            q = q.where(TOrderReturn.returner_phone >= items['returner_phone_start'])
        if 'returner_phone_end' in items:
            q = q.where(TOrderReturn.returner_phone <= items['returner_phone_end'])
        
        if 'returner_address' in items:
            q = q.where(TOrderReturn.returner_address == items['returner_address'])
        if 'returner_address_start' in items:
            q = q.where(TOrderReturn.returner_address >= items['returner_address_start'])
        if 'returner_address_end' in items:
            q = q.where(TOrderReturn.returner_address <= items['returner_address_end'])
        
        if 'delivery_fee' in items:
            q = q.where(TOrderReturn.delivery_fee == items['delivery_fee'])
        if 'delivery_fee_start' in items:
            q = q.where(TOrderReturn.delivery_fee >= items['delivery_fee_start'])
        if 'delivery_fee_end' in items:
            q = q.where(TOrderReturn.delivery_fee <= items['delivery_fee_end'])
        
        if 'return_amount' in items:
            q = q.where(TOrderReturn.return_amount == items['return_amount'])
        if 'return_amount_start' in items:
            q = q.where(TOrderReturn.return_amount >= items['return_amount_start'])
        if 'return_amount_end' in items:
            q = q.where(TOrderReturn.return_amount <= items['return_amount_end'])
        
        if 'return_submit_time' in items:
            q = q.where(TOrderReturn.return_submit_time == items['return_submit_time'])
        if 'return_submit_time_start' in items:
            q = q.where(TOrderReturn.return_submit_time >= items['return_submit_time_start'])
        if 'return_submit_time_end' in items:
            q = q.where(TOrderReturn.return_submit_time <= items['return_submit_time_end'])
        
        if 'return_reason' in items:
            q = q.where(TOrderReturn.return_reason == items['return_reason'])
        if 'return_reason_start' in items:
            q = q.where(TOrderReturn.return_reason >= items['return_reason_start'])
        if 'return_reason_end' in items:
            q = q.where(TOrderReturn.return_reason <= items['return_reason_end'])
        
        if 'order_id' in items:
            q = q.where(TOrderReturn.order_id == items['order_id'])
        if 'order_id_start' in items:
            q = q.where(TOrderReturn.order_id >= items['order_id_start'])
        if 'order_id_end' in items:
            q = q.where(TOrderReturn.order_id <= items['order_id_end'])
        
        if 'good_id' in items:
            q = q.where(TOrderReturn.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TOrderReturn.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TOrderReturn.good_id <= items['good_id_end'])
        
        if 'return_num' in items:
            q = q.where(TOrderReturn.return_num == items['return_num'])
        if 'return_num_start' in items:
            q = q.where(TOrderReturn.return_num >= items['return_num_start'])
        if 'return_num_end' in items:
            q = q.where(TOrderReturn.return_num <= items['return_num_end'])
        
        if 'store_id' in items:
            q = q.where(TOrderReturn.store_id == items['store_id'])
        if 'store_id_start' in items:
            q = q.where(TOrderReturn.store_id >= items['store_id_start'])
        if 'store_id_end' in items:
            q = q.where(TOrderReturn.store_id <= items['store_id_end'])
        
        if 'return_delivery_track_code' in items:
            q = q.where(TOrderReturn.return_delivery_track_code == items['return_delivery_track_code'])
        if 'return_delivery_track_code_start' in items:
            q = q.where(TOrderReturn.return_delivery_track_code >= items['return_delivery_track_code_start'])
        if 'return_delivery_track_code_end' in items:
            q = q.where(TOrderReturn.return_delivery_track_code <= items['return_delivery_track_code_end'])
        
        if 'status_id' in items:
            q = q.where(TOrderReturn.status_id == items['status_id'])
        if 'status_id_start' in items:
            q = q.where(TOrderReturn.status_id >= items['status_id_start'])
        if 'status_id_end' in items:
            q = q.where(TOrderReturn.status_id <= items['status_id_end'])
        
        if 'consignee_name' in items:
            q = q.where(TOrderReturn.consignee_name == items['consignee_name'])
        if 'consignee_name_start' in items:
            q = q.where(TOrderReturn.consignee_name >= items['consignee_name_start'])
        if 'consignee_name_end' in items:
            q = q.where(TOrderReturn.consignee_name <= items['consignee_name_end'])
        
        if 'consignee_phone' in items:
            q = q.where(TOrderReturn.consignee_phone == items['consignee_phone'])
        if 'consignee_phone_start' in items:
            q = q.where(TOrderReturn.consignee_phone >= items['consignee_phone_start'])
        if 'consignee_phone_end' in items:
            q = q.where(TOrderReturn.consignee_phone <= items['consignee_phone_end'])
        
        if 'consignee_address' in items:
            q = q.where(TOrderReturn.consignee_address == items['consignee_address'])
        if 'consignee_address_start' in items:
            q = q.where(TOrderReturn.consignee_address >= items['consignee_address_start'])
        if 'consignee_address_end' in items:
            q = q.where(TOrderReturn.consignee_address <= items['consignee_address_end'])
        
        if 'return_balance' in items:
            q = q.where(TOrderReturn.return_balance == items['return_balance'])
        if 'return_balance_start' in items:
            q = q.where(TOrderReturn.return_balance >= items['return_balance_start'])
        if 'return_balance_end' in items:
            q = q.where(TOrderReturn.return_balance <= items['return_balance_end'])
        
        if 'return_lock_balance' in items:
            q = q.where(TOrderReturn.return_lock_balance == items['return_lock_balance'])
        if 'return_lock_balance_start' in items:
            q = q.where(TOrderReturn.return_lock_balance >= items['return_lock_balance_start'])
        if 'return_lock_balance_end' in items:
            q = q.where(TOrderReturn.return_lock_balance <= items['return_lock_balance_end'])
        
        if 'return_coin' in items:
            q = q.where(TOrderReturn.return_coin == items['return_coin'])
        if 'return_coin_start' in items:
            q = q.where(TOrderReturn.return_coin >= items['return_coin_start'])
        if 'return_coin_end' in items:
            q = q.where(TOrderReturn.return_coin <= items['return_coin_end'])
        
        if 'return_delivery_company' in items:
            q = q.where(TOrderReturn.return_delivery_company == items['return_delivery_company'])
        if 'return_delivery_company_start' in items:
            q = q.where(TOrderReturn.return_delivery_company >= items['return_delivery_company_start'])
        if 'return_delivery_company_end' in items:
            q = q.where(TOrderReturn.return_delivery_company <= items['return_delivery_company_end'])
        
        if 'return_paid_track_code' in items:
            q = q.where(TOrderReturn.return_paid_track_code == items['return_paid_track_code'])
        if 'return_paid_track_code_start' in items:
            q = q.where(TOrderReturn.return_paid_track_code >= items['return_paid_track_code_start'])
        if 'return_paid_track_code_end' in items:
            q = q.where(TOrderReturn.return_paid_track_code <= items['return_paid_track_code_end'])
        

        if 'id' in set_items:
            q = q.where(TOrderReturn.id.in_(set_items['id']))
        
        if 'returner_name' in set_items:
            q = q.where(TOrderReturn.returner_name.in_(set_items['returner_name']))
        
        if 'returner_phone' in set_items:
            q = q.where(TOrderReturn.returner_phone.in_(set_items['returner_phone']))
        
        if 'returner_address' in set_items:
            q = q.where(TOrderReturn.returner_address.in_(set_items['returner_address']))
        
        if 'delivery_fee' in set_items:
            q = q.where(TOrderReturn.delivery_fee.in_(set_items['delivery_fee']))
        
        if 'return_amount' in set_items:
            q = q.where(TOrderReturn.return_amount.in_(set_items['return_amount']))
        
        if 'return_submit_time' in set_items:
            q = q.where(TOrderReturn.return_submit_time.in_(set_items['return_submit_time']))
        
        if 'return_reason' in set_items:
            q = q.where(TOrderReturn.return_reason.in_(set_items['return_reason']))
        
        if 'order_id' in set_items:
            q = q.where(TOrderReturn.order_id.in_(set_items['order_id']))
        
        if 'good_id' in set_items:
            q = q.where(TOrderReturn.good_id.in_(set_items['good_id']))
        
        if 'return_num' in set_items:
            q = q.where(TOrderReturn.return_num.in_(set_items['return_num']))
        
        if 'store_id' in set_items:
            q = q.where(TOrderReturn.store_id.in_(set_items['store_id']))
        
        if 'return_delivery_track_code' in set_items:
            q = q.where(TOrderReturn.return_delivery_track_code.in_(set_items['return_delivery_track_code']))
        
        if 'status_id' in set_items:
            q = q.where(TOrderReturn.status_id.in_(set_items['status_id']))
        
        if 'consignee_name' in set_items:
            q = q.where(TOrderReturn.consignee_name.in_(set_items['consignee_name']))
        
        if 'consignee_phone' in set_items:
            q = q.where(TOrderReturn.consignee_phone.in_(set_items['consignee_phone']))
        
        if 'consignee_address' in set_items:
            q = q.where(TOrderReturn.consignee_address.in_(set_items['consignee_address']))
        
        if 'return_balance' in set_items:
            q = q.where(TOrderReturn.return_balance.in_(set_items['return_balance']))
        
        if 'return_lock_balance' in set_items:
            q = q.where(TOrderReturn.return_lock_balance.in_(set_items['return_lock_balance']))
        
        if 'return_coin' in set_items:
            q = q.where(TOrderReturn.return_coin.in_(set_items['return_coin']))
        
        if 'return_delivery_company' in set_items:
            q = q.where(TOrderReturn.return_delivery_company.in_(set_items['return_delivery_company']))
        
        if 'return_paid_track_code' in set_items:
            q = q.where(TOrderReturn.return_paid_track_code.in_(set_items['return_paid_track_code']))
        

        if 'returner_name' in search_items:
            q = q.where(TOrderReturn.returner_name.like(search_items['returner_name']))
        
        if 'returner_phone' in search_items:
            q = q.where(TOrderReturn.returner_phone.like(search_items['returner_phone']))
        
        if 'returner_address' in search_items:
            q = q.where(TOrderReturn.returner_address.like(search_items['returner_address']))
        
        if 'return_reason' in search_items:
            q = q.where(TOrderReturn.return_reason.like(search_items['return_reason']))
        
        if 'return_delivery_track_code' in search_items:
            q = q.where(TOrderReturn.return_delivery_track_code.like(search_items['return_delivery_track_code']))
        
        if 'consignee_name' in search_items:
            q = q.where(TOrderReturn.consignee_name.like(search_items['consignee_name']))
        
        if 'consignee_phone' in search_items:
            q = q.where(TOrderReturn.consignee_phone.like(search_items['consignee_phone']))
        
        if 'consignee_address' in search_items:
            q = q.where(TOrderReturn.consignee_address.like(search_items['consignee_address']))
        
        if 'return_delivery_company' in search_items:
            q = q.where(TOrderReturn.return_delivery_company.like(search_items['return_delivery_company']))
        
        if 'return_paid_track_code' in search_items:
            q = q.where(TOrderReturn.return_paid_track_code.like(search_items['return_paid_track_code']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TOrderReturn.return_paid_track_code.asc())
                orders.append(TOrderReturn.id.asc())
            elif val == 'desc':
                #orders.append(TOrderReturn.return_paid_track_code.desc())
                orders.append(TOrderReturn.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_order_return_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SOrderReturn.parse_obj(t.__dict__) for t in t_order_return_list]


def filter_count_order_return(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TOrderReturn)


        if 'id' in items:
            q = q.where(TOrderReturn.id == items['id'])
        if 'id_start' in items:
            q = q.where(TOrderReturn.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TOrderReturn.id <= items['id_end'])
        
        if 'returner_name' in items:
            q = q.where(TOrderReturn.returner_name == items['returner_name'])
        if 'returner_name_start' in items:
            q = q.where(TOrderReturn.returner_name >= items['returner_name_start'])
        if 'returner_name_end' in items:
            q = q.where(TOrderReturn.returner_name <= items['returner_name_end'])
        
        if 'returner_phone' in items:
            q = q.where(TOrderReturn.returner_phone == items['returner_phone'])
        if 'returner_phone_start' in items:
            q = q.where(TOrderReturn.returner_phone >= items['returner_phone_start'])
        if 'returner_phone_end' in items:
            q = q.where(TOrderReturn.returner_phone <= items['returner_phone_end'])
        
        if 'returner_address' in items:
            q = q.where(TOrderReturn.returner_address == items['returner_address'])
        if 'returner_address_start' in items:
            q = q.where(TOrderReturn.returner_address >= items['returner_address_start'])
        if 'returner_address_end' in items:
            q = q.where(TOrderReturn.returner_address <= items['returner_address_end'])
        
        if 'delivery_fee' in items:
            q = q.where(TOrderReturn.delivery_fee == items['delivery_fee'])
        if 'delivery_fee_start' in items:
            q = q.where(TOrderReturn.delivery_fee >= items['delivery_fee_start'])
        if 'delivery_fee_end' in items:
            q = q.where(TOrderReturn.delivery_fee <= items['delivery_fee_end'])
        
        if 'return_amount' in items:
            q = q.where(TOrderReturn.return_amount == items['return_amount'])
        if 'return_amount_start' in items:
            q = q.where(TOrderReturn.return_amount >= items['return_amount_start'])
        if 'return_amount_end' in items:
            q = q.where(TOrderReturn.return_amount <= items['return_amount_end'])
        
        if 'return_submit_time' in items:
            q = q.where(TOrderReturn.return_submit_time == items['return_submit_time'])
        if 'return_submit_time_start' in items:
            q = q.where(TOrderReturn.return_submit_time >= items['return_submit_time_start'])
        if 'return_submit_time_end' in items:
            q = q.where(TOrderReturn.return_submit_time <= items['return_submit_time_end'])
        
        if 'return_reason' in items:
            q = q.where(TOrderReturn.return_reason == items['return_reason'])
        if 'return_reason_start' in items:
            q = q.where(TOrderReturn.return_reason >= items['return_reason_start'])
        if 'return_reason_end' in items:
            q = q.where(TOrderReturn.return_reason <= items['return_reason_end'])
        
        if 'order_id' in items:
            q = q.where(TOrderReturn.order_id == items['order_id'])
        if 'order_id_start' in items:
            q = q.where(TOrderReturn.order_id >= items['order_id_start'])
        if 'order_id_end' in items:
            q = q.where(TOrderReturn.order_id <= items['order_id_end'])
        
        if 'good_id' in items:
            q = q.where(TOrderReturn.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TOrderReturn.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TOrderReturn.good_id <= items['good_id_end'])
        
        if 'return_num' in items:
            q = q.where(TOrderReturn.return_num == items['return_num'])
        if 'return_num_start' in items:
            q = q.where(TOrderReturn.return_num >= items['return_num_start'])
        if 'return_num_end' in items:
            q = q.where(TOrderReturn.return_num <= items['return_num_end'])
        
        if 'store_id' in items:
            q = q.where(TOrderReturn.store_id == items['store_id'])
        if 'store_id_start' in items:
            q = q.where(TOrderReturn.store_id >= items['store_id_start'])
        if 'store_id_end' in items:
            q = q.where(TOrderReturn.store_id <= items['store_id_end'])
        
        if 'return_delivery_track_code' in items:
            q = q.where(TOrderReturn.return_delivery_track_code == items['return_delivery_track_code'])
        if 'return_delivery_track_code_start' in items:
            q = q.where(TOrderReturn.return_delivery_track_code >= items['return_delivery_track_code_start'])
        if 'return_delivery_track_code_end' in items:
            q = q.where(TOrderReturn.return_delivery_track_code <= items['return_delivery_track_code_end'])
        
        if 'status_id' in items:
            q = q.where(TOrderReturn.status_id == items['status_id'])
        if 'status_id_start' in items:
            q = q.where(TOrderReturn.status_id >= items['status_id_start'])
        if 'status_id_end' in items:
            q = q.where(TOrderReturn.status_id <= items['status_id_end'])
        
        if 'consignee_name' in items:
            q = q.where(TOrderReturn.consignee_name == items['consignee_name'])
        if 'consignee_name_start' in items:
            q = q.where(TOrderReturn.consignee_name >= items['consignee_name_start'])
        if 'consignee_name_end' in items:
            q = q.where(TOrderReturn.consignee_name <= items['consignee_name_end'])
        
        if 'consignee_phone' in items:
            q = q.where(TOrderReturn.consignee_phone == items['consignee_phone'])
        if 'consignee_phone_start' in items:
            q = q.where(TOrderReturn.consignee_phone >= items['consignee_phone_start'])
        if 'consignee_phone_end' in items:
            q = q.where(TOrderReturn.consignee_phone <= items['consignee_phone_end'])
        
        if 'consignee_address' in items:
            q = q.where(TOrderReturn.consignee_address == items['consignee_address'])
        if 'consignee_address_start' in items:
            q = q.where(TOrderReturn.consignee_address >= items['consignee_address_start'])
        if 'consignee_address_end' in items:
            q = q.where(TOrderReturn.consignee_address <= items['consignee_address_end'])
        
        if 'return_balance' in items:
            q = q.where(TOrderReturn.return_balance == items['return_balance'])
        if 'return_balance_start' in items:
            q = q.where(TOrderReturn.return_balance >= items['return_balance_start'])
        if 'return_balance_end' in items:
            q = q.where(TOrderReturn.return_balance <= items['return_balance_end'])
        
        if 'return_lock_balance' in items:
            q = q.where(TOrderReturn.return_lock_balance == items['return_lock_balance'])
        if 'return_lock_balance_start' in items:
            q = q.where(TOrderReturn.return_lock_balance >= items['return_lock_balance_start'])
        if 'return_lock_balance_end' in items:
            q = q.where(TOrderReturn.return_lock_balance <= items['return_lock_balance_end'])
        
        if 'return_coin' in items:
            q = q.where(TOrderReturn.return_coin == items['return_coin'])
        if 'return_coin_start' in items:
            q = q.where(TOrderReturn.return_coin >= items['return_coin_start'])
        if 'return_coin_end' in items:
            q = q.where(TOrderReturn.return_coin <= items['return_coin_end'])
        
        if 'return_delivery_company' in items:
            q = q.where(TOrderReturn.return_delivery_company == items['return_delivery_company'])
        if 'return_delivery_company_start' in items:
            q = q.where(TOrderReturn.return_delivery_company >= items['return_delivery_company_start'])
        if 'return_delivery_company_end' in items:
            q = q.where(TOrderReturn.return_delivery_company <= items['return_delivery_company_end'])
        
        if 'return_paid_track_code' in items:
            q = q.where(TOrderReturn.return_paid_track_code == items['return_paid_track_code'])
        if 'return_paid_track_code_start' in items:
            q = q.where(TOrderReturn.return_paid_track_code >= items['return_paid_track_code_start'])
        if 'return_paid_track_code_end' in items:
            q = q.where(TOrderReturn.return_paid_track_code <= items['return_paid_track_code_end'])
        

        if 'id' in set_items:
            q = q.where(TOrderReturn.id.in_(set_items['id']))
        
        if 'returner_name' in set_items:
            q = q.where(TOrderReturn.returner_name.in_(set_items['returner_name']))
        
        if 'returner_phone' in set_items:
            q = q.where(TOrderReturn.returner_phone.in_(set_items['returner_phone']))
        
        if 'returner_address' in set_items:
            q = q.where(TOrderReturn.returner_address.in_(set_items['returner_address']))
        
        if 'delivery_fee' in set_items:
            q = q.where(TOrderReturn.delivery_fee.in_(set_items['delivery_fee']))
        
        if 'return_amount' in set_items:
            q = q.where(TOrderReturn.return_amount.in_(set_items['return_amount']))
        
        if 'return_submit_time' in set_items:
            q = q.where(TOrderReturn.return_submit_time.in_(set_items['return_submit_time']))
        
        if 'return_reason' in set_items:
            q = q.where(TOrderReturn.return_reason.in_(set_items['return_reason']))
        
        if 'order_id' in set_items:
            q = q.where(TOrderReturn.order_id.in_(set_items['order_id']))
        
        if 'good_id' in set_items:
            q = q.where(TOrderReturn.good_id.in_(set_items['good_id']))
        
        if 'return_num' in set_items:
            q = q.where(TOrderReturn.return_num.in_(set_items['return_num']))
        
        if 'store_id' in set_items:
            q = q.where(TOrderReturn.store_id.in_(set_items['store_id']))
        
        if 'return_delivery_track_code' in set_items:
            q = q.where(TOrderReturn.return_delivery_track_code.in_(set_items['return_delivery_track_code']))
        
        if 'status_id' in set_items:
            q = q.where(TOrderReturn.status_id.in_(set_items['status_id']))
        
        if 'consignee_name' in set_items:
            q = q.where(TOrderReturn.consignee_name.in_(set_items['consignee_name']))
        
        if 'consignee_phone' in set_items:
            q = q.where(TOrderReturn.consignee_phone.in_(set_items['consignee_phone']))
        
        if 'consignee_address' in set_items:
            q = q.where(TOrderReturn.consignee_address.in_(set_items['consignee_address']))
        
        if 'return_balance' in set_items:
            q = q.where(TOrderReturn.return_balance.in_(set_items['return_balance']))
        
        if 'return_lock_balance' in set_items:
            q = q.where(TOrderReturn.return_lock_balance.in_(set_items['return_lock_balance']))
        
        if 'return_coin' in set_items:
            q = q.where(TOrderReturn.return_coin.in_(set_items['return_coin']))
        
        if 'return_delivery_company' in set_items:
            q = q.where(TOrderReturn.return_delivery_company.in_(set_items['return_delivery_company']))
        
        if 'return_paid_track_code' in set_items:
            q = q.where(TOrderReturn.return_paid_track_code.in_(set_items['return_paid_track_code']))
        

        if 'returner_name' in search_items:
            q = q.where(TOrderReturn.returner_name.like(search_items['returner_name']))
        
        if 'returner_phone' in search_items:
            q = q.where(TOrderReturn.returner_phone.like(search_items['returner_phone']))
        
        if 'returner_address' in search_items:
            q = q.where(TOrderReturn.returner_address.like(search_items['returner_address']))
        
        if 'return_reason' in search_items:
            q = q.where(TOrderReturn.return_reason.like(search_items['return_reason']))
        
        if 'return_delivery_track_code' in search_items:
            q = q.where(TOrderReturn.return_delivery_track_code.like(search_items['return_delivery_track_code']))
        
        if 'consignee_name' in search_items:
            q = q.where(TOrderReturn.consignee_name.like(search_items['consignee_name']))
        
        if 'consignee_phone' in search_items:
            q = q.where(TOrderReturn.consignee_phone.like(search_items['consignee_phone']))
        
        if 'consignee_address' in search_items:
            q = q.where(TOrderReturn.consignee_address.like(search_items['consignee_address']))
        
        if 'return_delivery_company' in search_items:
            q = q.where(TOrderReturn.return_delivery_company.like(search_items['return_delivery_company']))
        
        if 'return_paid_track_code' in search_items:
            q = q.where(TOrderReturn.return_paid_track_code.like(search_items['return_paid_track_code']))
        
    
        c = q.count()
        return c

    
def insert_order_return_state(item: CreateOrderReturnState, db: Optional[SessionLocal] = None) -> SOrderReturnState:
    data = model2dict(item)
    t = TOrderReturnState(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SOrderReturnState.parse_obj(t.__dict__)

    
def delete_order_return_state(order_return_state_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TOrderReturnState).where(TOrderReturnState.id == order_return_state_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TOrderReturnState).where(TOrderReturnState.id == order_return_state_id).delete()
        db.commit()

    
def update_order_return_state(item: SOrderReturnState, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TOrderReturnState).where(TOrderReturnState.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TOrderReturnState).where(TOrderReturnState.id == item.id).update(data)
        db.commit()

    
def get_order_return_state(order_return_state_id: int) -> Optional[SOrderReturnState]:
    with Dao() as db:
        t = db.query(TOrderReturnState).where(TOrderReturnState.id == order_return_state_id).first()
        if t:
            return SOrderReturnState.parse_obj(t.__dict__)
        else:
            return None


def filter_order_return_state(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SOrderReturnState]:
    with Dao() as db:
        q = db.query(TOrderReturnState)


        if 'id' in items:
            q = q.where(TOrderReturnState.id == items['id'])
        if 'id_start' in items:
            q = q.where(TOrderReturnState.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TOrderReturnState.id <= items['id_end'])
        
        if 'state' in items:
            q = q.where(TOrderReturnState.state == items['state'])
        if 'state_start' in items:
            q = q.where(TOrderReturnState.state >= items['state_start'])
        if 'state_end' in items:
            q = q.where(TOrderReturnState.state <= items['state_end'])
        

        if 'id' in set_items:
            q = q.where(TOrderReturnState.id.in_(set_items['id']))
        
        if 'state' in set_items:
            q = q.where(TOrderReturnState.state.in_(set_items['state']))
        

        if 'state' in search_items:
            q = q.where(TOrderReturnState.state.like(search_items['state']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TOrderReturnState.state.asc())
                orders.append(TOrderReturnState.id.asc())
            elif val == 'desc':
                #orders.append(TOrderReturnState.state.desc())
                orders.append(TOrderReturnState.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_order_return_state_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SOrderReturnState.parse_obj(t.__dict__) for t in t_order_return_state_list]


def filter_count_order_return_state(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TOrderReturnState)


        if 'id' in items:
            q = q.where(TOrderReturnState.id == items['id'])
        if 'id_start' in items:
            q = q.where(TOrderReturnState.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TOrderReturnState.id <= items['id_end'])
        
        if 'state' in items:
            q = q.where(TOrderReturnState.state == items['state'])
        if 'state_start' in items:
            q = q.where(TOrderReturnState.state >= items['state_start'])
        if 'state_end' in items:
            q = q.where(TOrderReturnState.state <= items['state_end'])
        

        if 'id' in set_items:
            q = q.where(TOrderReturnState.id.in_(set_items['id']))
        
        if 'state' in set_items:
            q = q.where(TOrderReturnState.state.in_(set_items['state']))
        

        if 'state' in search_items:
            q = q.where(TOrderReturnState.state.like(search_items['state']))
        
    
        c = q.count()
        return c

    
def insert_order_return_type(item: CreateOrderReturnType, db: Optional[SessionLocal] = None) -> SOrderReturnType:
    data = model2dict(item)
    t = TOrderReturnType(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SOrderReturnType.parse_obj(t.__dict__)

    
def delete_order_return_type(order_return_type_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TOrderReturnType).where(TOrderReturnType.id == order_return_type_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TOrderReturnType).where(TOrderReturnType.id == order_return_type_id).delete()
        db.commit()

    
def update_order_return_type(item: SOrderReturnType, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TOrderReturnType).where(TOrderReturnType.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TOrderReturnType).where(TOrderReturnType.id == item.id).update(data)
        db.commit()

    
def get_order_return_type(order_return_type_id: int) -> Optional[SOrderReturnType]:
    with Dao() as db:
        t = db.query(TOrderReturnType).where(TOrderReturnType.id == order_return_type_id).first()
        if t:
            return SOrderReturnType.parse_obj(t.__dict__)
        else:
            return None


def filter_order_return_type(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SOrderReturnType]:
    with Dao() as db:
        q = db.query(TOrderReturnType)


        if 'id' in items:
            q = q.where(TOrderReturnType.id == items['id'])
        if 'id_start' in items:
            q = q.where(TOrderReturnType.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TOrderReturnType.id <= items['id_end'])
        
        if 'type' in items:
            q = q.where(TOrderReturnType.type == items['type'])
        if 'type_start' in items:
            q = q.where(TOrderReturnType.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TOrderReturnType.type <= items['type_end'])
        

        if 'id' in set_items:
            q = q.where(TOrderReturnType.id.in_(set_items['id']))
        
        if 'type' in set_items:
            q = q.where(TOrderReturnType.type.in_(set_items['type']))
        

        if 'type' in search_items:
            q = q.where(TOrderReturnType.type.like(search_items['type']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TOrderReturnType.type.asc())
                orders.append(TOrderReturnType.id.asc())
            elif val == 'desc':
                #orders.append(TOrderReturnType.type.desc())
                orders.append(TOrderReturnType.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_order_return_type_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SOrderReturnType.parse_obj(t.__dict__) for t in t_order_return_type_list]


def filter_count_order_return_type(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TOrderReturnType)


        if 'id' in items:
            q = q.where(TOrderReturnType.id == items['id'])
        if 'id_start' in items:
            q = q.where(TOrderReturnType.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TOrderReturnType.id <= items['id_end'])
        
        if 'type' in items:
            q = q.where(TOrderReturnType.type == items['type'])
        if 'type_start' in items:
            q = q.where(TOrderReturnType.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TOrderReturnType.type <= items['type_end'])
        

        if 'id' in set_items:
            q = q.where(TOrderReturnType.id.in_(set_items['id']))
        
        if 'type' in set_items:
            q = q.where(TOrderReturnType.type.in_(set_items['type']))
        

        if 'type' in search_items:
            q = q.where(TOrderReturnType.type.like(search_items['type']))
        
    
        c = q.count()
        return c

    
def insert_order_source(item: CreateOrderSource, db: Optional[SessionLocal] = None) -> SOrderSource:
    data = model2dict(item)
    t = TOrderSource(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SOrderSource.parse_obj(t.__dict__)

    
def delete_order_source(order_source_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TOrderSource).where(TOrderSource.id == order_source_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TOrderSource).where(TOrderSource.id == order_source_id).delete()
        db.commit()

    
def update_order_source(item: SOrderSource, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TOrderSource).where(TOrderSource.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TOrderSource).where(TOrderSource.id == item.id).update(data)
        db.commit()

    
def get_order_source(order_source_id: int) -> Optional[SOrderSource]:
    with Dao() as db:
        t = db.query(TOrderSource).where(TOrderSource.id == order_source_id).first()
        if t:
            return SOrderSource.parse_obj(t.__dict__)
        else:
            return None


def filter_order_source(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SOrderSource]:
    with Dao() as db:
        q = db.query(TOrderSource)


        if 'id' in items:
            q = q.where(TOrderSource.id == items['id'])
        if 'id_start' in items:
            q = q.where(TOrderSource.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TOrderSource.id <= items['id_end'])
        
        if 'order_id' in items:
            q = q.where(TOrderSource.order_id == items['order_id'])
        if 'order_id_start' in items:
            q = q.where(TOrderSource.order_id >= items['order_id_start'])
        if 'order_id_end' in items:
            q = q.where(TOrderSource.order_id <= items['order_id_end'])
        
        if 'source_id' in items:
            q = q.where(TOrderSource.source_id == items['source_id'])
        if 'source_id_start' in items:
            q = q.where(TOrderSource.source_id >= items['source_id_start'])
        if 'source_id_end' in items:
            q = q.where(TOrderSource.source_id <= items['source_id_end'])
        
        if 'amount' in items:
            q = q.where(TOrderSource.amount == items['amount'])
        if 'amount_start' in items:
            q = q.where(TOrderSource.amount >= items['amount_start'])
        if 'amount_end' in items:
            q = q.where(TOrderSource.amount <= items['amount_end'])
        
        if 'create_time' in items:
            q = q.where(TOrderSource.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TOrderSource.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TOrderSource.create_time <= items['create_time_end'])
        
        if 'order_user_id' in items:
            q = q.where(TOrderSource.order_user_id == items['order_user_id'])
        if 'order_user_id_start' in items:
            q = q.where(TOrderSource.order_user_id >= items['order_user_id_start'])
        if 'order_user_id_end' in items:
            q = q.where(TOrderSource.order_user_id <= items['order_user_id_end'])
        
        if 'package_user_id' in items:
            q = q.where(TOrderSource.package_user_id == items['package_user_id'])
        if 'package_user_id_start' in items:
            q = q.where(TOrderSource.package_user_id >= items['package_user_id_start'])
        if 'package_user_id_end' in items:
            q = q.where(TOrderSource.package_user_id <= items['package_user_id_end'])
        

        if 'id' in set_items:
            q = q.where(TOrderSource.id.in_(set_items['id']))
        
        if 'order_id' in set_items:
            q = q.where(TOrderSource.order_id.in_(set_items['order_id']))
        
        if 'source_id' in set_items:
            q = q.where(TOrderSource.source_id.in_(set_items['source_id']))
        
        if 'amount' in set_items:
            q = q.where(TOrderSource.amount.in_(set_items['amount']))
        
        if 'create_time' in set_items:
            q = q.where(TOrderSource.create_time.in_(set_items['create_time']))
        
        if 'order_user_id' in set_items:
            q = q.where(TOrderSource.order_user_id.in_(set_items['order_user_id']))
        
        if 'package_user_id' in set_items:
            q = q.where(TOrderSource.package_user_id.in_(set_items['package_user_id']))
        

    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TOrderSource.package_user_id.asc())
                orders.append(TOrderSource.id.asc())
            elif val == 'desc':
                #orders.append(TOrderSource.package_user_id.desc())
                orders.append(TOrderSource.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_order_source_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SOrderSource.parse_obj(t.__dict__) for t in t_order_source_list]


def filter_count_order_source(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TOrderSource)


        if 'id' in items:
            q = q.where(TOrderSource.id == items['id'])
        if 'id_start' in items:
            q = q.where(TOrderSource.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TOrderSource.id <= items['id_end'])
        
        if 'order_id' in items:
            q = q.where(TOrderSource.order_id == items['order_id'])
        if 'order_id_start' in items:
            q = q.where(TOrderSource.order_id >= items['order_id_start'])
        if 'order_id_end' in items:
            q = q.where(TOrderSource.order_id <= items['order_id_end'])
        
        if 'source_id' in items:
            q = q.where(TOrderSource.source_id == items['source_id'])
        if 'source_id_start' in items:
            q = q.where(TOrderSource.source_id >= items['source_id_start'])
        if 'source_id_end' in items:
            q = q.where(TOrderSource.source_id <= items['source_id_end'])
        
        if 'amount' in items:
            q = q.where(TOrderSource.amount == items['amount'])
        if 'amount_start' in items:
            q = q.where(TOrderSource.amount >= items['amount_start'])
        if 'amount_end' in items:
            q = q.where(TOrderSource.amount <= items['amount_end'])
        
        if 'create_time' in items:
            q = q.where(TOrderSource.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TOrderSource.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TOrderSource.create_time <= items['create_time_end'])
        
        if 'order_user_id' in items:
            q = q.where(TOrderSource.order_user_id == items['order_user_id'])
        if 'order_user_id_start' in items:
            q = q.where(TOrderSource.order_user_id >= items['order_user_id_start'])
        if 'order_user_id_end' in items:
            q = q.where(TOrderSource.order_user_id <= items['order_user_id_end'])
        
        if 'package_user_id' in items:
            q = q.where(TOrderSource.package_user_id == items['package_user_id'])
        if 'package_user_id_start' in items:
            q = q.where(TOrderSource.package_user_id >= items['package_user_id_start'])
        if 'package_user_id_end' in items:
            q = q.where(TOrderSource.package_user_id <= items['package_user_id_end'])
        

        if 'id' in set_items:
            q = q.where(TOrderSource.id.in_(set_items['id']))
        
        if 'order_id' in set_items:
            q = q.where(TOrderSource.order_id.in_(set_items['order_id']))
        
        if 'source_id' in set_items:
            q = q.where(TOrderSource.source_id.in_(set_items['source_id']))
        
        if 'amount' in set_items:
            q = q.where(TOrderSource.amount.in_(set_items['amount']))
        
        if 'create_time' in set_items:
            q = q.where(TOrderSource.create_time.in_(set_items['create_time']))
        
        if 'order_user_id' in set_items:
            q = q.where(TOrderSource.order_user_id.in_(set_items['order_user_id']))
        
        if 'package_user_id' in set_items:
            q = q.where(TOrderSource.package_user_id.in_(set_items['package_user_id']))
        

    
        c = q.count()
        return c

    
def insert_order_state(item: CreateOrderState, db: Optional[SessionLocal] = None) -> SOrderState:
    data = model2dict(item)
    t = TOrderState(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SOrderState.parse_obj(t.__dict__)

    
def delete_order_state(order_state_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TOrderState).where(TOrderState.id == order_state_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TOrderState).where(TOrderState.id == order_state_id).delete()
        db.commit()

    
def update_order_state(item: SOrderState, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TOrderState).where(TOrderState.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TOrderState).where(TOrderState.id == item.id).update(data)
        db.commit()

    
def get_order_state(order_state_id: int) -> Optional[SOrderState]:
    with Dao() as db:
        t = db.query(TOrderState).where(TOrderState.id == order_state_id).first()
        if t:
            return SOrderState.parse_obj(t.__dict__)
        else:
            return None


def filter_order_state(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SOrderState]:
    with Dao() as db:
        q = db.query(TOrderState)


        if 'id' in items:
            q = q.where(TOrderState.id == items['id'])
        if 'id_start' in items:
            q = q.where(TOrderState.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TOrderState.id <= items['id_end'])
        
        if 'state' in items:
            q = q.where(TOrderState.state == items['state'])
        if 'state_start' in items:
            q = q.where(TOrderState.state >= items['state_start'])
        if 'state_end' in items:
            q = q.where(TOrderState.state <= items['state_end'])
        
        if 'belong' in items:
            q = q.where(TOrderState.belong == items['belong'])
        if 'belong_start' in items:
            q = q.where(TOrderState.belong >= items['belong_start'])
        if 'belong_end' in items:
            q = q.where(TOrderState.belong <= items['belong_end'])
        

        if 'id' in set_items:
            q = q.where(TOrderState.id.in_(set_items['id']))
        
        if 'state' in set_items:
            q = q.where(TOrderState.state.in_(set_items['state']))
        
        if 'belong' in set_items:
            q = q.where(TOrderState.belong.in_(set_items['belong']))
        

        if 'state' in search_items:
            q = q.where(TOrderState.state.like(search_items['state']))
        
        if 'belong' in search_items:
            q = q.where(TOrderState.belong.like(search_items['belong']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TOrderState.belong.asc())
                orders.append(TOrderState.id.asc())
            elif val == 'desc':
                #orders.append(TOrderState.belong.desc())
                orders.append(TOrderState.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_order_state_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SOrderState.parse_obj(t.__dict__) for t in t_order_state_list]


def filter_count_order_state(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TOrderState)


        if 'id' in items:
            q = q.where(TOrderState.id == items['id'])
        if 'id_start' in items:
            q = q.where(TOrderState.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TOrderState.id <= items['id_end'])
        
        if 'state' in items:
            q = q.where(TOrderState.state == items['state'])
        if 'state_start' in items:
            q = q.where(TOrderState.state >= items['state_start'])
        if 'state_end' in items:
            q = q.where(TOrderState.state <= items['state_end'])
        
        if 'belong' in items:
            q = q.where(TOrderState.belong == items['belong'])
        if 'belong_start' in items:
            q = q.where(TOrderState.belong >= items['belong_start'])
        if 'belong_end' in items:
            q = q.where(TOrderState.belong <= items['belong_end'])
        

        if 'id' in set_items:
            q = q.where(TOrderState.id.in_(set_items['id']))
        
        if 'state' in set_items:
            q = q.where(TOrderState.state.in_(set_items['state']))
        
        if 'belong' in set_items:
            q = q.where(TOrderState.belong.in_(set_items['belong']))
        

        if 'state' in search_items:
            q = q.where(TOrderState.state.like(search_items['state']))
        
        if 'belong' in search_items:
            q = q.where(TOrderState.belong.like(search_items['belong']))
        
    
        c = q.count()
        return c

    
def insert_package(item: CreatePackage, db: Optional[SessionLocal] = None) -> SPackage:
    data = model2dict(item)
    t = TPackage(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SPackage.parse_obj(t.__dict__)

    
def delete_package(package_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TPackage).where(TPackage.id == package_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPackage).where(TPackage.id == package_id).delete()
        db.commit()

    
def update_package(item: SPackage, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TPackage).where(TPackage.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPackage).where(TPackage.id == item.id).update(data)
        db.commit()

    
def get_package(package_id: int) -> Optional[SPackage]:
    with Dao() as db:
        t = db.query(TPackage).where(TPackage.id == package_id).first()
        if t:
            return SPackage.parse_obj(t.__dict__)
        else:
            return None


def filter_package(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SPackage]:
    with Dao() as db:
        q = db.query(TPackage)


        if 'id' in items:
            q = q.where(TPackage.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPackage.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPackage.id <= items['id_end'])
        
        if 'good_id' in items:
            q = q.where(TPackage.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TPackage.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TPackage.good_id <= items['good_id_end'])
        
        if 'amount' in items:
            q = q.where(TPackage.amount == items['amount'])
        if 'amount_start' in items:
            q = q.where(TPackage.amount >= items['amount_start'])
        if 'amount_end' in items:
            q = q.where(TPackage.amount <= items['amount_end'])
        
        if 'flash_sale_price' in items:
            q = q.where(TPackage.flash_sale_price == items['flash_sale_price'])
        if 'flash_sale_price_start' in items:
            q = q.where(TPackage.flash_sale_price >= items['flash_sale_price_start'])
        if 'flash_sale_price_end' in items:
            q = q.where(TPackage.flash_sale_price <= items['flash_sale_price_end'])
        
        if 'num' in items:
            q = q.where(TPackage.num == items['num'])
        if 'num_start' in items:
            q = q.where(TPackage.num >= items['num_start'])
        if 'num_end' in items:
            q = q.where(TPackage.num <= items['num_end'])
        
        if 'stock' in items:
            q = q.where(TPackage.stock == items['stock'])
        if 'stock_start' in items:
            q = q.where(TPackage.stock >= items['stock_start'])
        if 'stock_end' in items:
            q = q.where(TPackage.stock <= items['stock_end'])
        
        if 'seller_id' in items:
            q = q.where(TPackage.seller_id == items['seller_id'])
        if 'seller_id_start' in items:
            q = q.where(TPackage.seller_id >= items['seller_id_start'])
        if 'seller_id_end' in items:
            q = q.where(TPackage.seller_id <= items['seller_id_end'])
        
        if 'spec_id' in items:
            q = q.where(TPackage.spec_id == items['spec_id'])
        if 'spec_id_start' in items:
            q = q.where(TPackage.spec_id >= items['spec_id_start'])
        if 'spec_id_end' in items:
            q = q.where(TPackage.spec_id <= items['spec_id_end'])
        
        if 'share_fee' in items:
            q = q.where(TPackage.share_fee == items['share_fee'])
        if 'share_fee_start' in items:
            q = q.where(TPackage.share_fee >= items['share_fee_start'])
        if 'share_fee_end' in items:
            q = q.where(TPackage.share_fee <= items['share_fee_end'])
        
        if 'status' in items:
            q = q.where(TPackage.status == items['status'])
        if 'status_start' in items:
            q = q.where(TPackage.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TPackage.status <= items['status_end'])
        

        if 'id' in set_items:
            q = q.where(TPackage.id.in_(set_items['id']))
        
        if 'good_id' in set_items:
            q = q.where(TPackage.good_id.in_(set_items['good_id']))
        
        if 'amount' in set_items:
            q = q.where(TPackage.amount.in_(set_items['amount']))
        
        if 'flash_sale_price' in set_items:
            q = q.where(TPackage.flash_sale_price.in_(set_items['flash_sale_price']))
        
        if 'num' in set_items:
            q = q.where(TPackage.num.in_(set_items['num']))
        
        if 'stock' in set_items:
            q = q.where(TPackage.stock.in_(set_items['stock']))
        
        if 'seller_id' in set_items:
            q = q.where(TPackage.seller_id.in_(set_items['seller_id']))
        
        if 'spec_id' in set_items:
            q = q.where(TPackage.spec_id.in_(set_items['spec_id']))
        
        if 'share_fee' in set_items:
            q = q.where(TPackage.share_fee.in_(set_items['share_fee']))
        
        if 'status' in set_items:
            q = q.where(TPackage.status.in_(set_items['status']))
        

    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TPackage.status.asc())
                orders.append(TPackage.id.asc())
            elif val == 'desc':
                #orders.append(TPackage.status.desc())
                orders.append(TPackage.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_package_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SPackage.parse_obj(t.__dict__) for t in t_package_list]


def filter_count_package(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TPackage)


        if 'id' in items:
            q = q.where(TPackage.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPackage.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPackage.id <= items['id_end'])
        
        if 'good_id' in items:
            q = q.where(TPackage.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TPackage.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TPackage.good_id <= items['good_id_end'])
        
        if 'amount' in items:
            q = q.where(TPackage.amount == items['amount'])
        if 'amount_start' in items:
            q = q.where(TPackage.amount >= items['amount_start'])
        if 'amount_end' in items:
            q = q.where(TPackage.amount <= items['amount_end'])
        
        if 'flash_sale_price' in items:
            q = q.where(TPackage.flash_sale_price == items['flash_sale_price'])
        if 'flash_sale_price_start' in items:
            q = q.where(TPackage.flash_sale_price >= items['flash_sale_price_start'])
        if 'flash_sale_price_end' in items:
            q = q.where(TPackage.flash_sale_price <= items['flash_sale_price_end'])
        
        if 'num' in items:
            q = q.where(TPackage.num == items['num'])
        if 'num_start' in items:
            q = q.where(TPackage.num >= items['num_start'])
        if 'num_end' in items:
            q = q.where(TPackage.num <= items['num_end'])
        
        if 'stock' in items:
            q = q.where(TPackage.stock == items['stock'])
        if 'stock_start' in items:
            q = q.where(TPackage.stock >= items['stock_start'])
        if 'stock_end' in items:
            q = q.where(TPackage.stock <= items['stock_end'])
        
        if 'seller_id' in items:
            q = q.where(TPackage.seller_id == items['seller_id'])
        if 'seller_id_start' in items:
            q = q.where(TPackage.seller_id >= items['seller_id_start'])
        if 'seller_id_end' in items:
            q = q.where(TPackage.seller_id <= items['seller_id_end'])
        
        if 'spec_id' in items:
            q = q.where(TPackage.spec_id == items['spec_id'])
        if 'spec_id_start' in items:
            q = q.where(TPackage.spec_id >= items['spec_id_start'])
        if 'spec_id_end' in items:
            q = q.where(TPackage.spec_id <= items['spec_id_end'])
        
        if 'share_fee' in items:
            q = q.where(TPackage.share_fee == items['share_fee'])
        if 'share_fee_start' in items:
            q = q.where(TPackage.share_fee >= items['share_fee_start'])
        if 'share_fee_end' in items:
            q = q.where(TPackage.share_fee <= items['share_fee_end'])
        
        if 'status' in items:
            q = q.where(TPackage.status == items['status'])
        if 'status_start' in items:
            q = q.where(TPackage.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TPackage.status <= items['status_end'])
        

        if 'id' in set_items:
            q = q.where(TPackage.id.in_(set_items['id']))
        
        if 'good_id' in set_items:
            q = q.where(TPackage.good_id.in_(set_items['good_id']))
        
        if 'amount' in set_items:
            q = q.where(TPackage.amount.in_(set_items['amount']))
        
        if 'flash_sale_price' in set_items:
            q = q.where(TPackage.flash_sale_price.in_(set_items['flash_sale_price']))
        
        if 'num' in set_items:
            q = q.where(TPackage.num.in_(set_items['num']))
        
        if 'stock' in set_items:
            q = q.where(TPackage.stock.in_(set_items['stock']))
        
        if 'seller_id' in set_items:
            q = q.where(TPackage.seller_id.in_(set_items['seller_id']))
        
        if 'spec_id' in set_items:
            q = q.where(TPackage.spec_id.in_(set_items['spec_id']))
        
        if 'share_fee' in set_items:
            q = q.where(TPackage.share_fee.in_(set_items['share_fee']))
        
        if 'status' in set_items:
            q = q.where(TPackage.status.in_(set_items['status']))
        

    
        c = q.count()
        return c

    
def insert_package_express(item: CreatePackageExpress, db: Optional[SessionLocal] = None) -> SPackageExpress:
    data = model2dict(item)
    t = TPackageExpress(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SPackageExpress.parse_obj(t.__dict__)

    
def delete_package_express(package_express_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TPackageExpress).where(TPackageExpress.id == package_express_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPackageExpress).where(TPackageExpress.id == package_express_id).delete()
        db.commit()

    
def update_package_express(item: SPackageExpress, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TPackageExpress).where(TPackageExpress.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPackageExpress).where(TPackageExpress.id == item.id).update(data)
        db.commit()

    
def get_package_express(package_express_id: int) -> Optional[SPackageExpress]:
    with Dao() as db:
        t = db.query(TPackageExpress).where(TPackageExpress.id == package_express_id).first()
        if t:
            return SPackageExpress.parse_obj(t.__dict__)
        else:
            return None


def filter_package_express(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SPackageExpress]:
    with Dao() as db:
        q = db.query(TPackageExpress)


        if 'id' in items:
            q = q.where(TPackageExpress.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPackageExpress.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPackageExpress.id <= items['id_end'])
        
        if 'flash_order_id' in items:
            q = q.where(TPackageExpress.flash_order_id == items['flash_order_id'])
        if 'flash_order_id_start' in items:
            q = q.where(TPackageExpress.flash_order_id >= items['flash_order_id_start'])
        if 'flash_order_id_end' in items:
            q = q.where(TPackageExpress.flash_order_id <= items['flash_order_id_end'])
        
        if 'status' in items:
            q = q.where(TPackageExpress.status == items['status'])
        if 'status_start' in items:
            q = q.where(TPackageExpress.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TPackageExpress.status <= items['status_end'])
        
        if 'address_id' in items:
            q = q.where(TPackageExpress.address_id == items['address_id'])
        if 'address_id_start' in items:
            q = q.where(TPackageExpress.address_id >= items['address_id_start'])
        if 'address_id_end' in items:
            q = q.where(TPackageExpress.address_id <= items['address_id_end'])
        
        if 'amount' in items:
            q = q.where(TPackageExpress.amount == items['amount'])
        if 'amount_start' in items:
            q = q.where(TPackageExpress.amount >= items['amount_start'])
        if 'amount_end' in items:
            q = q.where(TPackageExpress.amount <= items['amount_end'])
        
        if 'express_num' in items:
            q = q.where(TPackageExpress.express_num == items['express_num'])
        if 'express_num_start' in items:
            q = q.where(TPackageExpress.express_num >= items['express_num_start'])
        if 'express_num_end' in items:
            q = q.where(TPackageExpress.express_num <= items['express_num_end'])
        
        if 'apply_time' in items:
            q = q.where(TPackageExpress.apply_time == items['apply_time'])
        if 'apply_time_start' in items:
            q = q.where(TPackageExpress.apply_time >= items['apply_time_start'])
        if 'apply_time_end' in items:
            q = q.where(TPackageExpress.apply_time <= items['apply_time_end'])
        
        if 'delivery_time' in items:
            q = q.where(TPackageExpress.delivery_time == items['delivery_time'])
        if 'delivery_time_start' in items:
            q = q.where(TPackageExpress.delivery_time >= items['delivery_time_start'])
        if 'delivery_time_end' in items:
            q = q.where(TPackageExpress.delivery_time <= items['delivery_time_end'])
        
        if 'complete_time' in items:
            q = q.where(TPackageExpress.complete_time == items['complete_time'])
        if 'complete_time_start' in items:
            q = q.where(TPackageExpress.complete_time >= items['complete_time_start'])
        if 'complete_time_end' in items:
            q = q.where(TPackageExpress.complete_time <= items['complete_time_end'])
        
        if 'detail' in items:
            q = q.where(TPackageExpress.detail == items['detail'])
        if 'detail_start' in items:
            q = q.where(TPackageExpress.detail >= items['detail_start'])
        if 'detail_end' in items:
            q = q.where(TPackageExpress.detail <= items['detail_end'])
        

        if 'id' in set_items:
            q = q.where(TPackageExpress.id.in_(set_items['id']))
        
        if 'flash_order_id' in set_items:
            q = q.where(TPackageExpress.flash_order_id.in_(set_items['flash_order_id']))
        
        if 'status' in set_items:
            q = q.where(TPackageExpress.status.in_(set_items['status']))
        
        if 'address_id' in set_items:
            q = q.where(TPackageExpress.address_id.in_(set_items['address_id']))
        
        if 'amount' in set_items:
            q = q.where(TPackageExpress.amount.in_(set_items['amount']))
        
        if 'express_num' in set_items:
            q = q.where(TPackageExpress.express_num.in_(set_items['express_num']))
        
        if 'apply_time' in set_items:
            q = q.where(TPackageExpress.apply_time.in_(set_items['apply_time']))
        
        if 'delivery_time' in set_items:
            q = q.where(TPackageExpress.delivery_time.in_(set_items['delivery_time']))
        
        if 'complete_time' in set_items:
            q = q.where(TPackageExpress.complete_time.in_(set_items['complete_time']))
        
        if 'detail' in set_items:
            q = q.where(TPackageExpress.detail.in_(set_items['detail']))
        

        if 'express_num' in search_items:
            q = q.where(TPackageExpress.express_num.like(search_items['express_num']))
        
        if 'detail' in search_items:
            q = q.where(TPackageExpress.detail.like(search_items['detail']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TPackageExpress.detail.asc())
                orders.append(TPackageExpress.id.asc())
            elif val == 'desc':
                #orders.append(TPackageExpress.detail.desc())
                orders.append(TPackageExpress.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_package_express_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SPackageExpress.parse_obj(t.__dict__) for t in t_package_express_list]


def filter_count_package_express(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TPackageExpress)


        if 'id' in items:
            q = q.where(TPackageExpress.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPackageExpress.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPackageExpress.id <= items['id_end'])
        
        if 'flash_order_id' in items:
            q = q.where(TPackageExpress.flash_order_id == items['flash_order_id'])
        if 'flash_order_id_start' in items:
            q = q.where(TPackageExpress.flash_order_id >= items['flash_order_id_start'])
        if 'flash_order_id_end' in items:
            q = q.where(TPackageExpress.flash_order_id <= items['flash_order_id_end'])
        
        if 'status' in items:
            q = q.where(TPackageExpress.status == items['status'])
        if 'status_start' in items:
            q = q.where(TPackageExpress.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TPackageExpress.status <= items['status_end'])
        
        if 'address_id' in items:
            q = q.where(TPackageExpress.address_id == items['address_id'])
        if 'address_id_start' in items:
            q = q.where(TPackageExpress.address_id >= items['address_id_start'])
        if 'address_id_end' in items:
            q = q.where(TPackageExpress.address_id <= items['address_id_end'])
        
        if 'amount' in items:
            q = q.where(TPackageExpress.amount == items['amount'])
        if 'amount_start' in items:
            q = q.where(TPackageExpress.amount >= items['amount_start'])
        if 'amount_end' in items:
            q = q.where(TPackageExpress.amount <= items['amount_end'])
        
        if 'express_num' in items:
            q = q.where(TPackageExpress.express_num == items['express_num'])
        if 'express_num_start' in items:
            q = q.where(TPackageExpress.express_num >= items['express_num_start'])
        if 'express_num_end' in items:
            q = q.where(TPackageExpress.express_num <= items['express_num_end'])
        
        if 'apply_time' in items:
            q = q.where(TPackageExpress.apply_time == items['apply_time'])
        if 'apply_time_start' in items:
            q = q.where(TPackageExpress.apply_time >= items['apply_time_start'])
        if 'apply_time_end' in items:
            q = q.where(TPackageExpress.apply_time <= items['apply_time_end'])
        
        if 'delivery_time' in items:
            q = q.where(TPackageExpress.delivery_time == items['delivery_time'])
        if 'delivery_time_start' in items:
            q = q.where(TPackageExpress.delivery_time >= items['delivery_time_start'])
        if 'delivery_time_end' in items:
            q = q.where(TPackageExpress.delivery_time <= items['delivery_time_end'])
        
        if 'complete_time' in items:
            q = q.where(TPackageExpress.complete_time == items['complete_time'])
        if 'complete_time_start' in items:
            q = q.where(TPackageExpress.complete_time >= items['complete_time_start'])
        if 'complete_time_end' in items:
            q = q.where(TPackageExpress.complete_time <= items['complete_time_end'])
        
        if 'detail' in items:
            q = q.where(TPackageExpress.detail == items['detail'])
        if 'detail_start' in items:
            q = q.where(TPackageExpress.detail >= items['detail_start'])
        if 'detail_end' in items:
            q = q.where(TPackageExpress.detail <= items['detail_end'])
        

        if 'id' in set_items:
            q = q.where(TPackageExpress.id.in_(set_items['id']))
        
        if 'flash_order_id' in set_items:
            q = q.where(TPackageExpress.flash_order_id.in_(set_items['flash_order_id']))
        
        if 'status' in set_items:
            q = q.where(TPackageExpress.status.in_(set_items['status']))
        
        if 'address_id' in set_items:
            q = q.where(TPackageExpress.address_id.in_(set_items['address_id']))
        
        if 'amount' in set_items:
            q = q.where(TPackageExpress.amount.in_(set_items['amount']))
        
        if 'express_num' in set_items:
            q = q.where(TPackageExpress.express_num.in_(set_items['express_num']))
        
        if 'apply_time' in set_items:
            q = q.where(TPackageExpress.apply_time.in_(set_items['apply_time']))
        
        if 'delivery_time' in set_items:
            q = q.where(TPackageExpress.delivery_time.in_(set_items['delivery_time']))
        
        if 'complete_time' in set_items:
            q = q.where(TPackageExpress.complete_time.in_(set_items['complete_time']))
        
        if 'detail' in set_items:
            q = q.where(TPackageExpress.detail.in_(set_items['detail']))
        

        if 'express_num' in search_items:
            q = q.where(TPackageExpress.express_num.like(search_items['express_num']))
        
        if 'detail' in search_items:
            q = q.where(TPackageExpress.detail.like(search_items['detail']))
        
    
        c = q.count()
        return c

    
def insert_package_express_status(item: CreatePackageExpressStatus, db: Optional[SessionLocal] = None) -> SPackageExpressStatus:
    data = model2dict(item)
    t = TPackageExpressStatus(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SPackageExpressStatus.parse_obj(t.__dict__)

    
def delete_package_express_status(package_express_status_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TPackageExpressStatus).where(TPackageExpressStatus.id == package_express_status_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPackageExpressStatus).where(TPackageExpressStatus.id == package_express_status_id).delete()
        db.commit()

    
def update_package_express_status(item: SPackageExpressStatus, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TPackageExpressStatus).where(TPackageExpressStatus.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPackageExpressStatus).where(TPackageExpressStatus.id == item.id).update(data)
        db.commit()

    
def get_package_express_status(package_express_status_id: int) -> Optional[SPackageExpressStatus]:
    with Dao() as db:
        t = db.query(TPackageExpressStatus).where(TPackageExpressStatus.id == package_express_status_id).first()
        if t:
            return SPackageExpressStatus.parse_obj(t.__dict__)
        else:
            return None


def filter_package_express_status(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SPackageExpressStatus]:
    with Dao() as db:
        q = db.query(TPackageExpressStatus)


        if 'id' in items:
            q = q.where(TPackageExpressStatus.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPackageExpressStatus.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPackageExpressStatus.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TPackageExpressStatus.title == items['title'])
        if 'title_start' in items:
            q = q.where(TPackageExpressStatus.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TPackageExpressStatus.title <= items['title_end'])
        

        if 'id' in set_items:
            q = q.where(TPackageExpressStatus.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TPackageExpressStatus.title.in_(set_items['title']))
        

        if 'title' in search_items:
            q = q.where(TPackageExpressStatus.title.like(search_items['title']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TPackageExpressStatus.title.asc())
                orders.append(TPackageExpressStatus.id.asc())
            elif val == 'desc':
                #orders.append(TPackageExpressStatus.title.desc())
                orders.append(TPackageExpressStatus.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_package_express_status_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SPackageExpressStatus.parse_obj(t.__dict__) for t in t_package_express_status_list]


def filter_count_package_express_status(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TPackageExpressStatus)


        if 'id' in items:
            q = q.where(TPackageExpressStatus.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPackageExpressStatus.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPackageExpressStatus.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TPackageExpressStatus.title == items['title'])
        if 'title_start' in items:
            q = q.where(TPackageExpressStatus.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TPackageExpressStatus.title <= items['title_end'])
        

        if 'id' in set_items:
            q = q.where(TPackageExpressStatus.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TPackageExpressStatus.title.in_(set_items['title']))
        

        if 'title' in search_items:
            q = q.where(TPackageExpressStatus.title.like(search_items['title']))
        
    
        c = q.count()
        return c

    
def insert_package_time(item: CreatePackageTime, db: Optional[SessionLocal] = None) -> SPackageTime:
    data = model2dict(item)
    t = TPackageTime(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SPackageTime.parse_obj(t.__dict__)

    
def delete_package_time(package_time_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TPackageTime).where(TPackageTime.id == package_time_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPackageTime).where(TPackageTime.id == package_time_id).delete()
        db.commit()

    
def update_package_time(item: SPackageTime, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TPackageTime).where(TPackageTime.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPackageTime).where(TPackageTime.id == item.id).update(data)
        db.commit()

    
def get_package_time(package_time_id: int) -> Optional[SPackageTime]:
    with Dao() as db:
        t = db.query(TPackageTime).where(TPackageTime.id == package_time_id).first()
        if t:
            return SPackageTime.parse_obj(t.__dict__)
        else:
            return None


def filter_package_time(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SPackageTime]:
    with Dao() as db:
        q = db.query(TPackageTime)


        if 'id' in items:
            q = q.where(TPackageTime.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPackageTime.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPackageTime.id <= items['id_end'])
        
        if 'start_time' in items:
            q = q.where(TPackageTime.start_time == items['start_time'])
        if 'start_time_start' in items:
            q = q.where(TPackageTime.start_time >= items['start_time_start'])
        if 'start_time_end' in items:
            q = q.where(TPackageTime.start_time <= items['start_time_end'])
        
        if 'end_time' in items:
            q = q.where(TPackageTime.end_time == items['end_time'])
        if 'end_time_start' in items:
            q = q.where(TPackageTime.end_time >= items['end_time_start'])
        if 'end_time_end' in items:
            q = q.where(TPackageTime.end_time <= items['end_time_end'])
        

        if 'id' in set_items:
            q = q.where(TPackageTime.id.in_(set_items['id']))
        
        if 'start_time' in set_items:
            q = q.where(TPackageTime.start_time.in_(set_items['start_time']))
        
        if 'end_time' in set_items:
            q = q.where(TPackageTime.end_time.in_(set_items['end_time']))
        

    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TPackageTime.end_time.asc())
                orders.append(TPackageTime.id.asc())
            elif val == 'desc':
                #orders.append(TPackageTime.end_time.desc())
                orders.append(TPackageTime.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_package_time_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SPackageTime.parse_obj(t.__dict__) for t in t_package_time_list]


def filter_count_package_time(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TPackageTime)


        if 'id' in items:
            q = q.where(TPackageTime.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPackageTime.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPackageTime.id <= items['id_end'])
        
        if 'start_time' in items:
            q = q.where(TPackageTime.start_time == items['start_time'])
        if 'start_time_start' in items:
            q = q.where(TPackageTime.start_time >= items['start_time_start'])
        if 'start_time_end' in items:
            q = q.where(TPackageTime.start_time <= items['start_time_end'])
        
        if 'end_time' in items:
            q = q.where(TPackageTime.end_time == items['end_time'])
        if 'end_time_start' in items:
            q = q.where(TPackageTime.end_time >= items['end_time_start'])
        if 'end_time_end' in items:
            q = q.where(TPackageTime.end_time <= items['end_time_end'])
        

        if 'id' in set_items:
            q = q.where(TPackageTime.id.in_(set_items['id']))
        
        if 'start_time' in set_items:
            q = q.where(TPackageTime.start_time.in_(set_items['start_time']))
        
        if 'end_time' in set_items:
            q = q.where(TPackageTime.end_time.in_(set_items['end_time']))
        

    
        c = q.count()
        return c

    
def insert_package_time_pair(item: CreatePackageTimePair, db: Optional[SessionLocal] = None) -> SPackageTimePair:
    data = model2dict(item)
    t = TPackageTimePair(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SPackageTimePair.parse_obj(t.__dict__)

    
def delete_package_time_pair(package_time_pair_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TPackageTimePair).where(TPackageTimePair.id == package_time_pair_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPackageTimePair).where(TPackageTimePair.id == package_time_pair_id).delete()
        db.commit()

    
def update_package_time_pair(item: SPackageTimePair, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TPackageTimePair).where(TPackageTimePair.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPackageTimePair).where(TPackageTimePair.id == item.id).update(data)
        db.commit()

    
def get_package_time_pair(package_time_pair_id: int) -> Optional[SPackageTimePair]:
    with Dao() as db:
        t = db.query(TPackageTimePair).where(TPackageTimePair.id == package_time_pair_id).first()
        if t:
            return SPackageTimePair.parse_obj(t.__dict__)
        else:
            return None


def filter_package_time_pair(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SPackageTimePair]:
    with Dao() as db:
        q = db.query(TPackageTimePair)


        if 'id' in items:
            q = q.where(TPackageTimePair.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPackageTimePair.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPackageTimePair.id <= items['id_end'])
        
        if 'package_id' in items:
            q = q.where(TPackageTimePair.package_id == items['package_id'])
        if 'package_id_start' in items:
            q = q.where(TPackageTimePair.package_id >= items['package_id_start'])
        if 'package_id_end' in items:
            q = q.where(TPackageTimePair.package_id <= items['package_id_end'])
        
        if 'package_time_id' in items:
            q = q.where(TPackageTimePair.package_time_id == items['package_time_id'])
        if 'package_time_id_start' in items:
            q = q.where(TPackageTimePair.package_time_id >= items['package_time_id_start'])
        if 'package_time_id_end' in items:
            q = q.where(TPackageTimePair.package_time_id <= items['package_time_id_end'])
        
        if 'status' in items:
            q = q.where(TPackageTimePair.status == items['status'])
        if 'status_start' in items:
            q = q.where(TPackageTimePair.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TPackageTimePair.status <= items['status_end'])
        
        if 'package_num' in items:
            q = q.where(TPackageTimePair.package_num == items['package_num'])
        if 'package_num_start' in items:
            q = q.where(TPackageTimePair.package_num >= items['package_num_start'])
        if 'package_num_end' in items:
            q = q.where(TPackageTimePair.package_num <= items['package_num_end'])
        

        if 'id' in set_items:
            q = q.where(TPackageTimePair.id.in_(set_items['id']))
        
        if 'package_id' in set_items:
            q = q.where(TPackageTimePair.package_id.in_(set_items['package_id']))
        
        if 'package_time_id' in set_items:
            q = q.where(TPackageTimePair.package_time_id.in_(set_items['package_time_id']))
        
        if 'status' in set_items:
            q = q.where(TPackageTimePair.status.in_(set_items['status']))
        
        if 'package_num' in set_items:
            q = q.where(TPackageTimePair.package_num.in_(set_items['package_num']))
        

    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TPackageTimePair.package_num.asc())
                orders.append(TPackageTimePair.id.asc())
            elif val == 'desc':
                #orders.append(TPackageTimePair.package_num.desc())
                orders.append(TPackageTimePair.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_package_time_pair_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SPackageTimePair.parse_obj(t.__dict__) for t in t_package_time_pair_list]


def filter_count_package_time_pair(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TPackageTimePair)


        if 'id' in items:
            q = q.where(TPackageTimePair.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPackageTimePair.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPackageTimePair.id <= items['id_end'])
        
        if 'package_id' in items:
            q = q.where(TPackageTimePair.package_id == items['package_id'])
        if 'package_id_start' in items:
            q = q.where(TPackageTimePair.package_id >= items['package_id_start'])
        if 'package_id_end' in items:
            q = q.where(TPackageTimePair.package_id <= items['package_id_end'])
        
        if 'package_time_id' in items:
            q = q.where(TPackageTimePair.package_time_id == items['package_time_id'])
        if 'package_time_id_start' in items:
            q = q.where(TPackageTimePair.package_time_id >= items['package_time_id_start'])
        if 'package_time_id_end' in items:
            q = q.where(TPackageTimePair.package_time_id <= items['package_time_id_end'])
        
        if 'status' in items:
            q = q.where(TPackageTimePair.status == items['status'])
        if 'status_start' in items:
            q = q.where(TPackageTimePair.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TPackageTimePair.status <= items['status_end'])
        
        if 'package_num' in items:
            q = q.where(TPackageTimePair.package_num == items['package_num'])
        if 'package_num_start' in items:
            q = q.where(TPackageTimePair.package_num >= items['package_num_start'])
        if 'package_num_end' in items:
            q = q.where(TPackageTimePair.package_num <= items['package_num_end'])
        

        if 'id' in set_items:
            q = q.where(TPackageTimePair.id.in_(set_items['id']))
        
        if 'package_id' in set_items:
            q = q.where(TPackageTimePair.package_id.in_(set_items['package_id']))
        
        if 'package_time_id' in set_items:
            q = q.where(TPackageTimePair.package_time_id.in_(set_items['package_time_id']))
        
        if 'status' in set_items:
            q = q.where(TPackageTimePair.status.in_(set_items['status']))
        
        if 'package_num' in set_items:
            q = q.where(TPackageTimePair.package_num.in_(set_items['package_num']))
        

    
        c = q.count()
        return c

    
def insert_pay_channel(item: CreatePayChannel, db: Optional[SessionLocal] = None) -> SPayChannel:
    data = model2dict(item)
    t = TPayChannel(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SPayChannel.parse_obj(t.__dict__)

    
def delete_pay_channel(pay_channel_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TPayChannel).where(TPayChannel.id == pay_channel_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPayChannel).where(TPayChannel.id == pay_channel_id).delete()
        db.commit()

    
def update_pay_channel(item: SPayChannel, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TPayChannel).where(TPayChannel.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPayChannel).where(TPayChannel.id == item.id).update(data)
        db.commit()

    
def get_pay_channel(pay_channel_id: int) -> Optional[SPayChannel]:
    with Dao() as db:
        t = db.query(TPayChannel).where(TPayChannel.id == pay_channel_id).first()
        if t:
            return SPayChannel.parse_obj(t.__dict__)
        else:
            return None


def filter_pay_channel(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SPayChannel]:
    with Dao() as db:
        q = db.query(TPayChannel)


        if 'id' in items:
            q = q.where(TPayChannel.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPayChannel.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPayChannel.id <= items['id_end'])
        
        if 'type' in items:
            q = q.where(TPayChannel.type == items['type'])
        if 'type_start' in items:
            q = q.where(TPayChannel.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TPayChannel.type <= items['type_end'])
        

        if 'id' in set_items:
            q = q.where(TPayChannel.id.in_(set_items['id']))
        
        if 'type' in set_items:
            q = q.where(TPayChannel.type.in_(set_items['type']))
        

        if 'type' in search_items:
            q = q.where(TPayChannel.type.like(search_items['type']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TPayChannel.type.asc())
                orders.append(TPayChannel.id.asc())
            elif val == 'desc':
                #orders.append(TPayChannel.type.desc())
                orders.append(TPayChannel.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_pay_channel_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SPayChannel.parse_obj(t.__dict__) for t in t_pay_channel_list]


def filter_count_pay_channel(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TPayChannel)


        if 'id' in items:
            q = q.where(TPayChannel.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPayChannel.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPayChannel.id <= items['id_end'])
        
        if 'type' in items:
            q = q.where(TPayChannel.type == items['type'])
        if 'type_start' in items:
            q = q.where(TPayChannel.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TPayChannel.type <= items['type_end'])
        

        if 'id' in set_items:
            q = q.where(TPayChannel.id.in_(set_items['id']))
        
        if 'type' in set_items:
            q = q.where(TPayChannel.type.in_(set_items['type']))
        

        if 'type' in search_items:
            q = q.where(TPayChannel.type.like(search_items['type']))
        
    
        c = q.count()
        return c

    
def insert_platform_law(item: CreatePlatformLaw, db: Optional[SessionLocal] = None) -> SPlatformLaw:
    data = model2dict(item)
    t = TPlatformLaw(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SPlatformLaw.parse_obj(t.__dict__)

    
def delete_platform_law(platform_law_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TPlatformLaw).where(TPlatformLaw.id == platform_law_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPlatformLaw).where(TPlatformLaw.id == platform_law_id).delete()
        db.commit()

    
def update_platform_law(item: SPlatformLaw, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TPlatformLaw).where(TPlatformLaw.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPlatformLaw).where(TPlatformLaw.id == item.id).update(data)
        db.commit()

    
def get_platform_law(platform_law_id: int) -> Optional[SPlatformLaw]:
    with Dao() as db:
        t = db.query(TPlatformLaw).where(TPlatformLaw.id == platform_law_id).first()
        if t:
            return SPlatformLaw.parse_obj(t.__dict__)
        else:
            return None


def filter_platform_law(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SPlatformLaw]:
    with Dao() as db:
        q = db.query(TPlatformLaw)


        if 'id' in items:
            q = q.where(TPlatformLaw.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPlatformLaw.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPlatformLaw.id <= items['id_end'])
        
        if 'create_time' in items:
            q = q.where(TPlatformLaw.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TPlatformLaw.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TPlatformLaw.create_time <= items['create_time_end'])
        
        if 'admin_id' in items:
            q = q.where(TPlatformLaw.admin_id == items['admin_id'])
        if 'admin_id_start' in items:
            q = q.where(TPlatformLaw.admin_id >= items['admin_id_start'])
        if 'admin_id_end' in items:
            q = q.where(TPlatformLaw.admin_id <= items['admin_id_end'])
        
        if 'law' in items:
            q = q.where(TPlatformLaw.law == items['law'])
        if 'law_start' in items:
            q = q.where(TPlatformLaw.law >= items['law_start'])
        if 'law_end' in items:
            q = q.where(TPlatformLaw.law <= items['law_end'])
        
        if 'privacy' in items:
            q = q.where(TPlatformLaw.privacy == items['privacy'])
        if 'privacy_start' in items:
            q = q.where(TPlatformLaw.privacy >= items['privacy_start'])
        if 'privacy_end' in items:
            q = q.where(TPlatformLaw.privacy <= items['privacy_end'])
        
        if 'purchase' in items:
            q = q.where(TPlatformLaw.purchase == items['purchase'])
        if 'purchase_start' in items:
            q = q.where(TPlatformLaw.purchase >= items['purchase_start'])
        if 'purchase_end' in items:
            q = q.where(TPlatformLaw.purchase <= items['purchase_end'])
        
        if 'flash_law' in items:
            q = q.where(TPlatformLaw.flash_law == items['flash_law'])
        if 'flash_law_start' in items:
            q = q.where(TPlatformLaw.flash_law >= items['flash_law_start'])
        if 'flash_law_end' in items:
            q = q.where(TPlatformLaw.flash_law <= items['flash_law_end'])
        
        if 'withdraw_law' in items:
            q = q.where(TPlatformLaw.withdraw_law == items['withdraw_law'])
        if 'withdraw_law_start' in items:
            q = q.where(TPlatformLaw.withdraw_law >= items['withdraw_law_start'])
        if 'withdraw_law_end' in items:
            q = q.where(TPlatformLaw.withdraw_law <= items['withdraw_law_end'])
        

        if 'id' in set_items:
            q = q.where(TPlatformLaw.id.in_(set_items['id']))
        
        if 'create_time' in set_items:
            q = q.where(TPlatformLaw.create_time.in_(set_items['create_time']))
        
        if 'admin_id' in set_items:
            q = q.where(TPlatformLaw.admin_id.in_(set_items['admin_id']))
        
        if 'law' in set_items:
            q = q.where(TPlatformLaw.law.in_(set_items['law']))
        
        if 'privacy' in set_items:
            q = q.where(TPlatformLaw.privacy.in_(set_items['privacy']))
        
        if 'purchase' in set_items:
            q = q.where(TPlatformLaw.purchase.in_(set_items['purchase']))
        
        if 'flash_law' in set_items:
            q = q.where(TPlatformLaw.flash_law.in_(set_items['flash_law']))
        
        if 'withdraw_law' in set_items:
            q = q.where(TPlatformLaw.withdraw_law.in_(set_items['withdraw_law']))
        

        if 'law' in search_items:
            q = q.where(TPlatformLaw.law.like(search_items['law']))
        
        if 'privacy' in search_items:
            q = q.where(TPlatformLaw.privacy.like(search_items['privacy']))
        
        if 'purchase' in search_items:
            q = q.where(TPlatformLaw.purchase.like(search_items['purchase']))
        
        if 'flash_law' in search_items:
            q = q.where(TPlatformLaw.flash_law.like(search_items['flash_law']))
        
        if 'withdraw_law' in search_items:
            q = q.where(TPlatformLaw.withdraw_law.like(search_items['withdraw_law']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TPlatformLaw.withdraw_law.asc())
                orders.append(TPlatformLaw.id.asc())
            elif val == 'desc':
                #orders.append(TPlatformLaw.withdraw_law.desc())
                orders.append(TPlatformLaw.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_platform_law_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SPlatformLaw.parse_obj(t.__dict__) for t in t_platform_law_list]


def filter_count_platform_law(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TPlatformLaw)


        if 'id' in items:
            q = q.where(TPlatformLaw.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPlatformLaw.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPlatformLaw.id <= items['id_end'])
        
        if 'create_time' in items:
            q = q.where(TPlatformLaw.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TPlatformLaw.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TPlatformLaw.create_time <= items['create_time_end'])
        
        if 'admin_id' in items:
            q = q.where(TPlatformLaw.admin_id == items['admin_id'])
        if 'admin_id_start' in items:
            q = q.where(TPlatformLaw.admin_id >= items['admin_id_start'])
        if 'admin_id_end' in items:
            q = q.where(TPlatformLaw.admin_id <= items['admin_id_end'])
        
        if 'law' in items:
            q = q.where(TPlatformLaw.law == items['law'])
        if 'law_start' in items:
            q = q.where(TPlatformLaw.law >= items['law_start'])
        if 'law_end' in items:
            q = q.where(TPlatformLaw.law <= items['law_end'])
        
        if 'privacy' in items:
            q = q.where(TPlatformLaw.privacy == items['privacy'])
        if 'privacy_start' in items:
            q = q.where(TPlatformLaw.privacy >= items['privacy_start'])
        if 'privacy_end' in items:
            q = q.where(TPlatformLaw.privacy <= items['privacy_end'])
        
        if 'purchase' in items:
            q = q.where(TPlatformLaw.purchase == items['purchase'])
        if 'purchase_start' in items:
            q = q.where(TPlatformLaw.purchase >= items['purchase_start'])
        if 'purchase_end' in items:
            q = q.where(TPlatformLaw.purchase <= items['purchase_end'])
        
        if 'flash_law' in items:
            q = q.where(TPlatformLaw.flash_law == items['flash_law'])
        if 'flash_law_start' in items:
            q = q.where(TPlatformLaw.flash_law >= items['flash_law_start'])
        if 'flash_law_end' in items:
            q = q.where(TPlatformLaw.flash_law <= items['flash_law_end'])
        
        if 'withdraw_law' in items:
            q = q.where(TPlatformLaw.withdraw_law == items['withdraw_law'])
        if 'withdraw_law_start' in items:
            q = q.where(TPlatformLaw.withdraw_law >= items['withdraw_law_start'])
        if 'withdraw_law_end' in items:
            q = q.where(TPlatformLaw.withdraw_law <= items['withdraw_law_end'])
        

        if 'id' in set_items:
            q = q.where(TPlatformLaw.id.in_(set_items['id']))
        
        if 'create_time' in set_items:
            q = q.where(TPlatformLaw.create_time.in_(set_items['create_time']))
        
        if 'admin_id' in set_items:
            q = q.where(TPlatformLaw.admin_id.in_(set_items['admin_id']))
        
        if 'law' in set_items:
            q = q.where(TPlatformLaw.law.in_(set_items['law']))
        
        if 'privacy' in set_items:
            q = q.where(TPlatformLaw.privacy.in_(set_items['privacy']))
        
        if 'purchase' in set_items:
            q = q.where(TPlatformLaw.purchase.in_(set_items['purchase']))
        
        if 'flash_law' in set_items:
            q = q.where(TPlatformLaw.flash_law.in_(set_items['flash_law']))
        
        if 'withdraw_law' in set_items:
            q = q.where(TPlatformLaw.withdraw_law.in_(set_items['withdraw_law']))
        

        if 'law' in search_items:
            q = q.where(TPlatformLaw.law.like(search_items['law']))
        
        if 'privacy' in search_items:
            q = q.where(TPlatformLaw.privacy.like(search_items['privacy']))
        
        if 'purchase' in search_items:
            q = q.where(TPlatformLaw.purchase.like(search_items['purchase']))
        
        if 'flash_law' in search_items:
            q = q.where(TPlatformLaw.flash_law.like(search_items['flash_law']))
        
        if 'withdraw_law' in search_items:
            q = q.where(TPlatformLaw.withdraw_law.like(search_items['withdraw_law']))
        
    
        c = q.count()
        return c

    
def insert_platform_notice(item: CreatePlatformNotice, db: Optional[SessionLocal] = None) -> SPlatformNotice:
    data = model2dict(item)
    t = TPlatformNotice(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SPlatformNotice.parse_obj(t.__dict__)

    
def delete_platform_notice(platform_notice_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TPlatformNotice).where(TPlatformNotice.id == platform_notice_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPlatformNotice).where(TPlatformNotice.id == platform_notice_id).delete()
        db.commit()

    
def update_platform_notice(item: SPlatformNotice, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TPlatformNotice).where(TPlatformNotice.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPlatformNotice).where(TPlatformNotice.id == item.id).update(data)
        db.commit()

    
def get_platform_notice(platform_notice_id: int) -> Optional[SPlatformNotice]:
    with Dao() as db:
        t = db.query(TPlatformNotice).where(TPlatformNotice.id == platform_notice_id).first()
        if t:
            return SPlatformNotice.parse_obj(t.__dict__)
        else:
            return None


def filter_platform_notice(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SPlatformNotice]:
    with Dao() as db:
        q = db.query(TPlatformNotice)


        if 'id' in items:
            q = q.where(TPlatformNotice.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPlatformNotice.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPlatformNotice.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TPlatformNotice.title == items['title'])
        if 'title_start' in items:
            q = q.where(TPlatformNotice.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TPlatformNotice.title <= items['title_end'])
        
        if 'create_time' in items:
            q = q.where(TPlatformNotice.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TPlatformNotice.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TPlatformNotice.create_time <= items['create_time_end'])
        
        if 'admin_id' in items:
            q = q.where(TPlatformNotice.admin_id == items['admin_id'])
        if 'admin_id_start' in items:
            q = q.where(TPlatformNotice.admin_id >= items['admin_id_start'])
        if 'admin_id_end' in items:
            q = q.where(TPlatformNotice.admin_id <= items['admin_id_end'])
        

        if 'id' in set_items:
            q = q.where(TPlatformNotice.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TPlatformNotice.title.in_(set_items['title']))
        
        if 'create_time' in set_items:
            q = q.where(TPlatformNotice.create_time.in_(set_items['create_time']))
        
        if 'admin_id' in set_items:
            q = q.where(TPlatformNotice.admin_id.in_(set_items['admin_id']))
        

        if 'title' in search_items:
            q = q.where(TPlatformNotice.title.like(search_items['title']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TPlatformNotice.admin_id.asc())
                orders.append(TPlatformNotice.id.asc())
            elif val == 'desc':
                #orders.append(TPlatformNotice.admin_id.desc())
                orders.append(TPlatformNotice.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_platform_notice_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SPlatformNotice.parse_obj(t.__dict__) for t in t_platform_notice_list]


def filter_count_platform_notice(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TPlatformNotice)


        if 'id' in items:
            q = q.where(TPlatformNotice.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPlatformNotice.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPlatformNotice.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TPlatformNotice.title == items['title'])
        if 'title_start' in items:
            q = q.where(TPlatformNotice.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TPlatformNotice.title <= items['title_end'])
        
        if 'create_time' in items:
            q = q.where(TPlatformNotice.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TPlatformNotice.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TPlatformNotice.create_time <= items['create_time_end'])
        
        if 'admin_id' in items:
            q = q.where(TPlatformNotice.admin_id == items['admin_id'])
        if 'admin_id_start' in items:
            q = q.where(TPlatformNotice.admin_id >= items['admin_id_start'])
        if 'admin_id_end' in items:
            q = q.where(TPlatformNotice.admin_id <= items['admin_id_end'])
        

        if 'id' in set_items:
            q = q.where(TPlatformNotice.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TPlatformNotice.title.in_(set_items['title']))
        
        if 'create_time' in set_items:
            q = q.where(TPlatformNotice.create_time.in_(set_items['create_time']))
        
        if 'admin_id' in set_items:
            q = q.where(TPlatformNotice.admin_id.in_(set_items['admin_id']))
        

        if 'title' in search_items:
            q = q.where(TPlatformNotice.title.like(search_items['title']))
        
    
        c = q.count()
        return c

    
def insert_poster(item: CreatePoster, db: Optional[SessionLocal] = None) -> SPoster:
    data = model2dict(item)
    t = TPoster(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SPoster.parse_obj(t.__dict__)

    
def delete_poster(poster_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TPoster).where(TPoster.id == poster_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPoster).where(TPoster.id == poster_id).delete()
        db.commit()

    
def update_poster(item: SPoster, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TPoster).where(TPoster.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TPoster).where(TPoster.id == item.id).update(data)
        db.commit()

    
def get_poster(poster_id: int) -> Optional[SPoster]:
    with Dao() as db:
        t = db.query(TPoster).where(TPoster.id == poster_id).first()
        if t:
            return SPoster.parse_obj(t.__dict__)
        else:
            return None


def filter_poster(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SPoster]:
    with Dao() as db:
        q = db.query(TPoster)


        if 'id' in items:
            q = q.where(TPoster.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPoster.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPoster.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TPoster.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TPoster.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TPoster.user_id <= items['user_id_end'])
        
        if 'poster_url' in items:
            q = q.where(TPoster.poster_url == items['poster_url'])
        if 'poster_url_start' in items:
            q = q.where(TPoster.poster_url >= items['poster_url_start'])
        if 'poster_url_end' in items:
            q = q.where(TPoster.poster_url <= items['poster_url_end'])
        
        if 'status' in items:
            q = q.where(TPoster.status == items['status'])
        if 'status_start' in items:
            q = q.where(TPoster.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TPoster.status <= items['status_end'])
        
        if 'description' in items:
            q = q.where(TPoster.description == items['description'])
        if 'description_start' in items:
            q = q.where(TPoster.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TPoster.description <= items['description_end'])
        
        if 'create_time' in items:
            q = q.where(TPoster.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TPoster.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TPoster.create_time <= items['create_time_end'])
        

        if 'id' in set_items:
            q = q.where(TPoster.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TPoster.user_id.in_(set_items['user_id']))
        
        if 'poster_url' in set_items:
            q = q.where(TPoster.poster_url.in_(set_items['poster_url']))
        
        if 'status' in set_items:
            q = q.where(TPoster.status.in_(set_items['status']))
        
        if 'description' in set_items:
            q = q.where(TPoster.description.in_(set_items['description']))
        
        if 'create_time' in set_items:
            q = q.where(TPoster.create_time.in_(set_items['create_time']))
        

        if 'poster_url' in search_items:
            q = q.where(TPoster.poster_url.like(search_items['poster_url']))
        
        if 'status' in search_items:
            q = q.where(TPoster.status.like(search_items['status']))
        
        if 'description' in search_items:
            q = q.where(TPoster.description.like(search_items['description']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TPoster.create_time.asc())
                orders.append(TPoster.id.asc())
            elif val == 'desc':
                #orders.append(TPoster.create_time.desc())
                orders.append(TPoster.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_poster_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SPoster.parse_obj(t.__dict__) for t in t_poster_list]


def filter_count_poster(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TPoster)


        if 'id' in items:
            q = q.where(TPoster.id == items['id'])
        if 'id_start' in items:
            q = q.where(TPoster.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TPoster.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TPoster.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TPoster.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TPoster.user_id <= items['user_id_end'])
        
        if 'poster_url' in items:
            q = q.where(TPoster.poster_url == items['poster_url'])
        if 'poster_url_start' in items:
            q = q.where(TPoster.poster_url >= items['poster_url_start'])
        if 'poster_url_end' in items:
            q = q.where(TPoster.poster_url <= items['poster_url_end'])
        
        if 'status' in items:
            q = q.where(TPoster.status == items['status'])
        if 'status_start' in items:
            q = q.where(TPoster.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TPoster.status <= items['status_end'])
        
        if 'description' in items:
            q = q.where(TPoster.description == items['description'])
        if 'description_start' in items:
            q = q.where(TPoster.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TPoster.description <= items['description_end'])
        
        if 'create_time' in items:
            q = q.where(TPoster.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TPoster.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TPoster.create_time <= items['create_time_end'])
        

        if 'id' in set_items:
            q = q.where(TPoster.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TPoster.user_id.in_(set_items['user_id']))
        
        if 'poster_url' in set_items:
            q = q.where(TPoster.poster_url.in_(set_items['poster_url']))
        
        if 'status' in set_items:
            q = q.where(TPoster.status.in_(set_items['status']))
        
        if 'description' in set_items:
            q = q.where(TPoster.description.in_(set_items['description']))
        
        if 'create_time' in set_items:
            q = q.where(TPoster.create_time.in_(set_items['create_time']))
        

        if 'poster_url' in search_items:
            q = q.where(TPoster.poster_url.like(search_items['poster_url']))
        
        if 'status' in search_items:
            q = q.where(TPoster.status.like(search_items['status']))
        
        if 'description' in search_items:
            q = q.where(TPoster.description.like(search_items['description']))
        
    
        c = q.count()
        return c

    
def insert_setting(item: CreateSetting, db: Optional[SessionLocal] = None) -> SSetting:
    data = model2dict(item)
    t = TSetting(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SSetting.parse_obj(t.__dict__)

    
def delete_setting(setting_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TSetting).where(TSetting.id == setting_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSetting).where(TSetting.id == setting_id).delete()
        db.commit()

    
def update_setting(item: SSetting, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TSetting).where(TSetting.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSetting).where(TSetting.id == item.id).update(data)
        db.commit()

    
def get_setting(setting_id: int) -> Optional[SSetting]:
    with Dao() as db:
        t = db.query(TSetting).where(TSetting.id == setting_id).first()
        if t:
            return SSetting.parse_obj(t.__dict__)
        else:
            return None


def filter_setting(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SSetting]:
    with Dao() as db:
        q = db.query(TSetting)


        if 'id' in items:
            q = q.where(TSetting.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSetting.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSetting.id <= items['id_end'])
        
        if 'recommend_num' in items:
            q = q.where(TSetting.recommend_num == items['recommend_num'])
        if 'recommend_num_start' in items:
            q = q.where(TSetting.recommend_num >= items['recommend_num_start'])
        if 'recommend_num_end' in items:
            q = q.where(TSetting.recommend_num <= items['recommend_num_end'])
        
        if 'flash_order_income' in items:
            q = q.where(TSetting.flash_order_income == items['flash_order_income'])
        if 'flash_order_income_start' in items:
            q = q.where(TSetting.flash_order_income >= items['flash_order_income_start'])
        if 'flash_order_income_end' in items:
            q = q.where(TSetting.flash_order_income <= items['flash_order_income_end'])
        
        if 'tuan_order_income' in items:
            q = q.where(TSetting.tuan_order_income == items['tuan_order_income'])
        if 'tuan_order_income_start' in items:
            q = q.where(TSetting.tuan_order_income >= items['tuan_order_income_start'])
        if 'tuan_order_income_end' in items:
            q = q.where(TSetting.tuan_order_income <= items['tuan_order_income_end'])
        
        if 'flash_order_max' in items:
            q = q.where(TSetting.flash_order_max == items['flash_order_max'])
        if 'flash_order_max_start' in items:
            q = q.where(TSetting.flash_order_max >= items['flash_order_max_start'])
        if 'flash_order_max_end' in items:
            q = q.where(TSetting.flash_order_max <= items['flash_order_max_end'])
        
        if 'flash_order_money_max' in items:
            q = q.where(TSetting.flash_order_money_max == items['flash_order_money_max'])
        if 'flash_order_money_max_start' in items:
            q = q.where(TSetting.flash_order_money_max >= items['flash_order_money_max_start'])
        if 'flash_order_money_max_end' in items:
            q = q.where(TSetting.flash_order_money_max <= items['flash_order_money_max_end'])
        
        if 'flash_order_active_user' in items:
            q = q.where(TSetting.flash_order_active_user == items['flash_order_active_user'])
        if 'flash_order_active_user_start' in items:
            q = q.where(TSetting.flash_order_active_user >= items['flash_order_active_user_start'])
        if 'flash_order_active_user_end' in items:
            q = q.where(TSetting.flash_order_active_user <= items['flash_order_active_user_end'])
        
        if 'consume_money_active_user' in items:
            q = q.where(TSetting.consume_money_active_user == items['consume_money_active_user'])
        if 'consume_money_active_user_start' in items:
            q = q.where(TSetting.consume_money_active_user >= items['consume_money_active_user_start'])
        if 'consume_money_active_user_end' in items:
            q = q.where(TSetting.consume_money_active_user <= items['consume_money_active_user_end'])
        
        if 'many_high_user' in items:
            q = q.where(TSetting.many_high_user == items['many_high_user'])
        if 'many_high_user_start' in items:
            q = q.where(TSetting.many_high_user >= items['many_high_user_start'])
        if 'many_high_user_end' in items:
            q = q.where(TSetting.many_high_user <= items['many_high_user_end'])
        
        if 'many_top_user' in items:
            q = q.where(TSetting.many_top_user == items['many_top_user'])
        if 'many_top_user_start' in items:
            q = q.where(TSetting.many_top_user >= items['many_top_user_start'])
        if 'many_top_user_end' in items:
            q = q.where(TSetting.many_top_user <= items['many_top_user_end'])
        
        if 'flash_order_income_retio' in items:
            q = q.where(TSetting.flash_order_income_retio == items['flash_order_income_retio'])
        if 'flash_order_income_retio_start' in items:
            q = q.where(TSetting.flash_order_income_retio >= items['flash_order_income_retio_start'])
        if 'flash_order_income_retio_end' in items:
            q = q.where(TSetting.flash_order_income_retio <= items['flash_order_income_retio_end'])
        
        if 'flash_order_income_layer' in items:
            q = q.where(TSetting.flash_order_income_layer == items['flash_order_income_layer'])
        if 'flash_order_income_layer_start' in items:
            q = q.where(TSetting.flash_order_income_layer >= items['flash_order_income_layer_start'])
        if 'flash_order_income_layer_end' in items:
            q = q.where(TSetting.flash_order_income_layer <= items['flash_order_income_layer_end'])
        
        if 'flash_order_income_toper' in items:
            q = q.where(TSetting.flash_order_income_toper == items['flash_order_income_toper'])
        if 'flash_order_income_toper_start' in items:
            q = q.where(TSetting.flash_order_income_toper >= items['flash_order_income_toper_start'])
        if 'flash_order_income_toper_end' in items:
            q = q.where(TSetting.flash_order_income_toper <= items['flash_order_income_toper_end'])
        
        if 'flash_order_income_groupsir' in items:
            q = q.where(TSetting.flash_order_income_groupsir == items['flash_order_income_groupsir'])
        if 'flash_order_income_groupsir_start' in items:
            q = q.where(TSetting.flash_order_income_groupsir >= items['flash_order_income_groupsir_start'])
        if 'flash_order_income_groupsir_end' in items:
            q = q.where(TSetting.flash_order_income_groupsir <= items['flash_order_income_groupsir_end'])
        
        if 'flash_order_owner_times' in items:
            q = q.where(TSetting.flash_order_owner_times == items['flash_order_owner_times'])
        if 'flash_order_owner_times_start' in items:
            q = q.where(TSetting.flash_order_owner_times >= items['flash_order_owner_times_start'])
        if 'flash_order_owner_times_end' in items:
            q = q.where(TSetting.flash_order_owner_times <= items['flash_order_owner_times_end'])
        
        if 'parent_user_limit' in items:
            q = q.where(TSetting.parent_user_limit == items['parent_user_limit'])
        if 'parent_user_limit_start' in items:
            q = q.where(TSetting.parent_user_limit >= items['parent_user_limit_start'])
        if 'parent_user_limit_end' in items:
            q = q.where(TSetting.parent_user_limit <= items['parent_user_limit_end'])
        
        if 'flash_order_income_subsidy' in items:
            q = q.where(TSetting.flash_order_income_subsidy == items['flash_order_income_subsidy'])
        if 'flash_order_income_subsidy_start' in items:
            q = q.where(TSetting.flash_order_income_subsidy >= items['flash_order_income_subsidy_start'])
        if 'flash_order_income_subsidy_end' in items:
            q = q.where(TSetting.flash_order_income_subsidy <= items['flash_order_income_subsidy_end'])
        

        if 'id' in set_items:
            q = q.where(TSetting.id.in_(set_items['id']))
        
        if 'recommend_num' in set_items:
            q = q.where(TSetting.recommend_num.in_(set_items['recommend_num']))
        
        if 'flash_order_income' in set_items:
            q = q.where(TSetting.flash_order_income.in_(set_items['flash_order_income']))
        
        if 'tuan_order_income' in set_items:
            q = q.where(TSetting.tuan_order_income.in_(set_items['tuan_order_income']))
        
        if 'flash_order_max' in set_items:
            q = q.where(TSetting.flash_order_max.in_(set_items['flash_order_max']))
        
        if 'flash_order_money_max' in set_items:
            q = q.where(TSetting.flash_order_money_max.in_(set_items['flash_order_money_max']))
        
        if 'flash_order_active_user' in set_items:
            q = q.where(TSetting.flash_order_active_user.in_(set_items['flash_order_active_user']))
        
        if 'consume_money_active_user' in set_items:
            q = q.where(TSetting.consume_money_active_user.in_(set_items['consume_money_active_user']))
        
        if 'many_high_user' in set_items:
            q = q.where(TSetting.many_high_user.in_(set_items['many_high_user']))
        
        if 'many_top_user' in set_items:
            q = q.where(TSetting.many_top_user.in_(set_items['many_top_user']))
        
        if 'flash_order_income_retio' in set_items:
            q = q.where(TSetting.flash_order_income_retio.in_(set_items['flash_order_income_retio']))
        
        if 'flash_order_income_layer' in set_items:
            q = q.where(TSetting.flash_order_income_layer.in_(set_items['flash_order_income_layer']))
        
        if 'flash_order_income_toper' in set_items:
            q = q.where(TSetting.flash_order_income_toper.in_(set_items['flash_order_income_toper']))
        
        if 'flash_order_income_groupsir' in set_items:
            q = q.where(TSetting.flash_order_income_groupsir.in_(set_items['flash_order_income_groupsir']))
        
        if 'flash_order_owner_times' in set_items:
            q = q.where(TSetting.flash_order_owner_times.in_(set_items['flash_order_owner_times']))
        
        if 'parent_user_limit' in set_items:
            q = q.where(TSetting.parent_user_limit.in_(set_items['parent_user_limit']))
        
        if 'flash_order_income_subsidy' in set_items:
            q = q.where(TSetting.flash_order_income_subsidy.in_(set_items['flash_order_income_subsidy']))
        

    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TSetting.flash_order_income_subsidy.asc())
                orders.append(TSetting.id.asc())
            elif val == 'desc':
                #orders.append(TSetting.flash_order_income_subsidy.desc())
                orders.append(TSetting.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_setting_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SSetting.parse_obj(t.__dict__) for t in t_setting_list]


def filter_count_setting(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TSetting)


        if 'id' in items:
            q = q.where(TSetting.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSetting.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSetting.id <= items['id_end'])
        
        if 'recommend_num' in items:
            q = q.where(TSetting.recommend_num == items['recommend_num'])
        if 'recommend_num_start' in items:
            q = q.where(TSetting.recommend_num >= items['recommend_num_start'])
        if 'recommend_num_end' in items:
            q = q.where(TSetting.recommend_num <= items['recommend_num_end'])
        
        if 'flash_order_income' in items:
            q = q.where(TSetting.flash_order_income == items['flash_order_income'])
        if 'flash_order_income_start' in items:
            q = q.where(TSetting.flash_order_income >= items['flash_order_income_start'])
        if 'flash_order_income_end' in items:
            q = q.where(TSetting.flash_order_income <= items['flash_order_income_end'])
        
        if 'tuan_order_income' in items:
            q = q.where(TSetting.tuan_order_income == items['tuan_order_income'])
        if 'tuan_order_income_start' in items:
            q = q.where(TSetting.tuan_order_income >= items['tuan_order_income_start'])
        if 'tuan_order_income_end' in items:
            q = q.where(TSetting.tuan_order_income <= items['tuan_order_income_end'])
        
        if 'flash_order_max' in items:
            q = q.where(TSetting.flash_order_max == items['flash_order_max'])
        if 'flash_order_max_start' in items:
            q = q.where(TSetting.flash_order_max >= items['flash_order_max_start'])
        if 'flash_order_max_end' in items:
            q = q.where(TSetting.flash_order_max <= items['flash_order_max_end'])
        
        if 'flash_order_money_max' in items:
            q = q.where(TSetting.flash_order_money_max == items['flash_order_money_max'])
        if 'flash_order_money_max_start' in items:
            q = q.where(TSetting.flash_order_money_max >= items['flash_order_money_max_start'])
        if 'flash_order_money_max_end' in items:
            q = q.where(TSetting.flash_order_money_max <= items['flash_order_money_max_end'])
        
        if 'flash_order_active_user' in items:
            q = q.where(TSetting.flash_order_active_user == items['flash_order_active_user'])
        if 'flash_order_active_user_start' in items:
            q = q.where(TSetting.flash_order_active_user >= items['flash_order_active_user_start'])
        if 'flash_order_active_user_end' in items:
            q = q.where(TSetting.flash_order_active_user <= items['flash_order_active_user_end'])
        
        if 'consume_money_active_user' in items:
            q = q.where(TSetting.consume_money_active_user == items['consume_money_active_user'])
        if 'consume_money_active_user_start' in items:
            q = q.where(TSetting.consume_money_active_user >= items['consume_money_active_user_start'])
        if 'consume_money_active_user_end' in items:
            q = q.where(TSetting.consume_money_active_user <= items['consume_money_active_user_end'])
        
        if 'many_high_user' in items:
            q = q.where(TSetting.many_high_user == items['many_high_user'])
        if 'many_high_user_start' in items:
            q = q.where(TSetting.many_high_user >= items['many_high_user_start'])
        if 'many_high_user_end' in items:
            q = q.where(TSetting.many_high_user <= items['many_high_user_end'])
        
        if 'many_top_user' in items:
            q = q.where(TSetting.many_top_user == items['many_top_user'])
        if 'many_top_user_start' in items:
            q = q.where(TSetting.many_top_user >= items['many_top_user_start'])
        if 'many_top_user_end' in items:
            q = q.where(TSetting.many_top_user <= items['many_top_user_end'])
        
        if 'flash_order_income_retio' in items:
            q = q.where(TSetting.flash_order_income_retio == items['flash_order_income_retio'])
        if 'flash_order_income_retio_start' in items:
            q = q.where(TSetting.flash_order_income_retio >= items['flash_order_income_retio_start'])
        if 'flash_order_income_retio_end' in items:
            q = q.where(TSetting.flash_order_income_retio <= items['flash_order_income_retio_end'])
        
        if 'flash_order_income_layer' in items:
            q = q.where(TSetting.flash_order_income_layer == items['flash_order_income_layer'])
        if 'flash_order_income_layer_start' in items:
            q = q.where(TSetting.flash_order_income_layer >= items['flash_order_income_layer_start'])
        if 'flash_order_income_layer_end' in items:
            q = q.where(TSetting.flash_order_income_layer <= items['flash_order_income_layer_end'])
        
        if 'flash_order_income_toper' in items:
            q = q.where(TSetting.flash_order_income_toper == items['flash_order_income_toper'])
        if 'flash_order_income_toper_start' in items:
            q = q.where(TSetting.flash_order_income_toper >= items['flash_order_income_toper_start'])
        if 'flash_order_income_toper_end' in items:
            q = q.where(TSetting.flash_order_income_toper <= items['flash_order_income_toper_end'])
        
        if 'flash_order_income_groupsir' in items:
            q = q.where(TSetting.flash_order_income_groupsir == items['flash_order_income_groupsir'])
        if 'flash_order_income_groupsir_start' in items:
            q = q.where(TSetting.flash_order_income_groupsir >= items['flash_order_income_groupsir_start'])
        if 'flash_order_income_groupsir_end' in items:
            q = q.where(TSetting.flash_order_income_groupsir <= items['flash_order_income_groupsir_end'])
        
        if 'flash_order_owner_times' in items:
            q = q.where(TSetting.flash_order_owner_times == items['flash_order_owner_times'])
        if 'flash_order_owner_times_start' in items:
            q = q.where(TSetting.flash_order_owner_times >= items['flash_order_owner_times_start'])
        if 'flash_order_owner_times_end' in items:
            q = q.where(TSetting.flash_order_owner_times <= items['flash_order_owner_times_end'])
        
        if 'parent_user_limit' in items:
            q = q.where(TSetting.parent_user_limit == items['parent_user_limit'])
        if 'parent_user_limit_start' in items:
            q = q.where(TSetting.parent_user_limit >= items['parent_user_limit_start'])
        if 'parent_user_limit_end' in items:
            q = q.where(TSetting.parent_user_limit <= items['parent_user_limit_end'])
        
        if 'flash_order_income_subsidy' in items:
            q = q.where(TSetting.flash_order_income_subsidy == items['flash_order_income_subsidy'])
        if 'flash_order_income_subsidy_start' in items:
            q = q.where(TSetting.flash_order_income_subsidy >= items['flash_order_income_subsidy_start'])
        if 'flash_order_income_subsidy_end' in items:
            q = q.where(TSetting.flash_order_income_subsidy <= items['flash_order_income_subsidy_end'])
        

        if 'id' in set_items:
            q = q.where(TSetting.id.in_(set_items['id']))
        
        if 'recommend_num' in set_items:
            q = q.where(TSetting.recommend_num.in_(set_items['recommend_num']))
        
        if 'flash_order_income' in set_items:
            q = q.where(TSetting.flash_order_income.in_(set_items['flash_order_income']))
        
        if 'tuan_order_income' in set_items:
            q = q.where(TSetting.tuan_order_income.in_(set_items['tuan_order_income']))
        
        if 'flash_order_max' in set_items:
            q = q.where(TSetting.flash_order_max.in_(set_items['flash_order_max']))
        
        if 'flash_order_money_max' in set_items:
            q = q.where(TSetting.flash_order_money_max.in_(set_items['flash_order_money_max']))
        
        if 'flash_order_active_user' in set_items:
            q = q.where(TSetting.flash_order_active_user.in_(set_items['flash_order_active_user']))
        
        if 'consume_money_active_user' in set_items:
            q = q.where(TSetting.consume_money_active_user.in_(set_items['consume_money_active_user']))
        
        if 'many_high_user' in set_items:
            q = q.where(TSetting.many_high_user.in_(set_items['many_high_user']))
        
        if 'many_top_user' in set_items:
            q = q.where(TSetting.many_top_user.in_(set_items['many_top_user']))
        
        if 'flash_order_income_retio' in set_items:
            q = q.where(TSetting.flash_order_income_retio.in_(set_items['flash_order_income_retio']))
        
        if 'flash_order_income_layer' in set_items:
            q = q.where(TSetting.flash_order_income_layer.in_(set_items['flash_order_income_layer']))
        
        if 'flash_order_income_toper' in set_items:
            q = q.where(TSetting.flash_order_income_toper.in_(set_items['flash_order_income_toper']))
        
        if 'flash_order_income_groupsir' in set_items:
            q = q.where(TSetting.flash_order_income_groupsir.in_(set_items['flash_order_income_groupsir']))
        
        if 'flash_order_owner_times' in set_items:
            q = q.where(TSetting.flash_order_owner_times.in_(set_items['flash_order_owner_times']))
        
        if 'parent_user_limit' in set_items:
            q = q.where(TSetting.parent_user_limit.in_(set_items['parent_user_limit']))
        
        if 'flash_order_income_subsidy' in set_items:
            q = q.where(TSetting.flash_order_income_subsidy.in_(set_items['flash_order_income_subsidy']))
        

    
        c = q.count()
        return c

    
def insert_store(item: CreateStore, db: Optional[SessionLocal] = None) -> SStore:
    data = model2dict(item)
    t = TStore(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SStore.parse_obj(t.__dict__)

    
def delete_store(store_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TStore).where(TStore.id == store_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TStore).where(TStore.id == store_id).delete()
        db.commit()

    
def update_store(item: SStore, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TStore).where(TStore.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TStore).where(TStore.id == item.id).update(data)
        db.commit()

    
def get_store(store_id: int) -> Optional[SStore]:
    with Dao() as db:
        t = db.query(TStore).where(TStore.id == store_id).first()
        if t:
            return SStore.parse_obj(t.__dict__)
        else:
            return None


def filter_store(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SStore]:
    with Dao() as db:
        q = db.query(TStore)


        if 'id' in items:
            q = q.where(TStore.id == items['id'])
        if 'id_start' in items:
            q = q.where(TStore.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TStore.id <= items['id_end'])
        
        if 'name' in items:
            q = q.where(TStore.name == items['name'])
        if 'name_start' in items:
            q = q.where(TStore.name >= items['name_start'])
        if 'name_end' in items:
            q = q.where(TStore.name <= items['name_end'])
        
        if 'phone' in items:
            q = q.where(TStore.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TStore.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TStore.phone <= items['phone_end'])
        
        if 'province' in items:
            q = q.where(TStore.province == items['province'])
        if 'province_start' in items:
            q = q.where(TStore.province >= items['province_start'])
        if 'province_end' in items:
            q = q.where(TStore.province <= items['province_end'])
        
        if 'city' in items:
            q = q.where(TStore.city == items['city'])
        if 'city_start' in items:
            q = q.where(TStore.city >= items['city_start'])
        if 'city_end' in items:
            q = q.where(TStore.city <= items['city_end'])
        
        if 'area' in items:
            q = q.where(TStore.area == items['area'])
        if 'area_start' in items:
            q = q.where(TStore.area >= items['area_start'])
        if 'area_end' in items:
            q = q.where(TStore.area <= items['area_end'])
        
        if 'street' in items:
            q = q.where(TStore.street == items['street'])
        if 'street_start' in items:
            q = q.where(TStore.street >= items['street_start'])
        if 'street_end' in items:
            q = q.where(TStore.street <= items['street_end'])
        
        if 'address' in items:
            q = q.where(TStore.address == items['address'])
        if 'address_start' in items:
            q = q.where(TStore.address >= items['address_start'])
        if 'address_end' in items:
            q = q.where(TStore.address <= items['address_end'])
        
        if 'status' in items:
            q = q.where(TStore.status == items['status'])
        if 'status_start' in items:
            q = q.where(TStore.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TStore.status <= items['status_end'])
        
        if 'owner' in items:
            q = q.where(TStore.owner == items['owner'])
        if 'owner_start' in items:
            q = q.where(TStore.owner >= items['owner_start'])
        if 'owner_end' in items:
            q = q.where(TStore.owner <= items['owner_end'])
        
        if 'recommender_id' in items:
            q = q.where(TStore.recommender_id == items['recommender_id'])
        if 'recommender_id_start' in items:
            q = q.where(TStore.recommender_id >= items['recommender_id_start'])
        if 'recommender_id_end' in items:
            q = q.where(TStore.recommender_id <= items['recommender_id_end'])
        
        if 'register_time' in items:
            q = q.where(TStore.register_time == items['register_time'])
        if 'register_time_start' in items:
            q = q.where(TStore.register_time >= items['register_time_start'])
        if 'register_time_end' in items:
            q = q.where(TStore.register_time <= items['register_time_end'])
        
        if 'type' in items:
            q = q.where(TStore.type == items['type'])
        if 'type_start' in items:
            q = q.where(TStore.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TStore.type <= items['type_end'])
        
        if 'expired_time' in items:
            q = q.where(TStore.expired_time == items['expired_time'])
        if 'expired_time_start' in items:
            q = q.where(TStore.expired_time >= items['expired_time_start'])
        if 'expired_time_end' in items:
            q = q.where(TStore.expired_time <= items['expired_time_end'])
        
        if 'open_time' in items:
            q = q.where(TStore.open_time == items['open_time'])
        if 'open_time_start' in items:
            q = q.where(TStore.open_time >= items['open_time_start'])
        if 'open_time_end' in items:
            q = q.where(TStore.open_time <= items['open_time_end'])
        
        if 'close_time' in items:
            q = q.where(TStore.close_time == items['close_time'])
        if 'close_time_start' in items:
            q = q.where(TStore.close_time >= items['close_time_start'])
        if 'close_time_end' in items:
            q = q.where(TStore.close_time <= items['close_time_end'])
        
        if 'image' in items:
            q = q.where(TStore.image == items['image'])
        if 'image_start' in items:
            q = q.where(TStore.image >= items['image_start'])
        if 'image_end' in items:
            q = q.where(TStore.image <= items['image_end'])
        
        if 'owner_id' in items:
            q = q.where(TStore.owner_id == items['owner_id'])
        if 'owner_id_start' in items:
            q = q.where(TStore.owner_id >= items['owner_id_start'])
        if 'owner_id_end' in items:
            q = q.where(TStore.owner_id <= items['owner_id_end'])
        
        if 'supplier_id' in items:
            q = q.where(TStore.supplier_id == items['supplier_id'])
        if 'supplier_id_start' in items:
            q = q.where(TStore.supplier_id >= items['supplier_id_start'])
        if 'supplier_id_end' in items:
            q = q.where(TStore.supplier_id <= items['supplier_id_end'])
        
        if 'company_name' in items:
            q = q.where(TStore.company_name == items['company_name'])
        if 'company_name_start' in items:
            q = q.where(TStore.company_name >= items['company_name_start'])
        if 'company_name_end' in items:
            q = q.where(TStore.company_name <= items['company_name_end'])
        
        if 'reject_reason' in items:
            q = q.where(TStore.reject_reason == items['reject_reason'])
        if 'reject_reason_start' in items:
            q = q.where(TStore.reject_reason >= items['reject_reason_start'])
        if 'reject_reason_end' in items:
            q = q.where(TStore.reject_reason <= items['reject_reason_end'])
        
        if 'reject_time' in items:
            q = q.where(TStore.reject_time == items['reject_time'])
        if 'reject_time_start' in items:
            q = q.where(TStore.reject_time >= items['reject_time_start'])
        if 'reject_time_end' in items:
            q = q.where(TStore.reject_time <= items['reject_time_end'])
        
        if 'reject_admin_id' in items:
            q = q.where(TStore.reject_admin_id == items['reject_admin_id'])
        if 'reject_admin_id_start' in items:
            q = q.where(TStore.reject_admin_id >= items['reject_admin_id_start'])
        if 'reject_admin_id_end' in items:
            q = q.where(TStore.reject_admin_id <= items['reject_admin_id_end'])
        
        if 'is_default' in items:
            q = q.where(TStore.is_default == items['is_default'])
        if 'is_default_start' in items:
            q = q.where(TStore.is_default >= items['is_default_start'])
        if 'is_default_end' in items:
            q = q.where(TStore.is_default <= items['is_default_end'])
        

        if 'id' in set_items:
            q = q.where(TStore.id.in_(set_items['id']))
        
        if 'name' in set_items:
            q = q.where(TStore.name.in_(set_items['name']))
        
        if 'phone' in set_items:
            q = q.where(TStore.phone.in_(set_items['phone']))
        
        if 'province' in set_items:
            q = q.where(TStore.province.in_(set_items['province']))
        
        if 'city' in set_items:
            q = q.where(TStore.city.in_(set_items['city']))
        
        if 'area' in set_items:
            q = q.where(TStore.area.in_(set_items['area']))
        
        if 'street' in set_items:
            q = q.where(TStore.street.in_(set_items['street']))
        
        if 'address' in set_items:
            q = q.where(TStore.address.in_(set_items['address']))
        
        if 'status' in set_items:
            q = q.where(TStore.status.in_(set_items['status']))
        
        if 'owner' in set_items:
            q = q.where(TStore.owner.in_(set_items['owner']))
        
        if 'recommender_id' in set_items:
            q = q.where(TStore.recommender_id.in_(set_items['recommender_id']))
        
        if 'register_time' in set_items:
            q = q.where(TStore.register_time.in_(set_items['register_time']))
        
        if 'type' in set_items:
            q = q.where(TStore.type.in_(set_items['type']))
        
        if 'expired_time' in set_items:
            q = q.where(TStore.expired_time.in_(set_items['expired_time']))
        
        if 'open_time' in set_items:
            q = q.where(TStore.open_time.in_(set_items['open_time']))
        
        if 'close_time' in set_items:
            q = q.where(TStore.close_time.in_(set_items['close_time']))
        
        if 'image' in set_items:
            q = q.where(TStore.image.in_(set_items['image']))
        
        if 'owner_id' in set_items:
            q = q.where(TStore.owner_id.in_(set_items['owner_id']))
        
        if 'supplier_id' in set_items:
            q = q.where(TStore.supplier_id.in_(set_items['supplier_id']))
        
        if 'company_name' in set_items:
            q = q.where(TStore.company_name.in_(set_items['company_name']))
        
        if 'reject_reason' in set_items:
            q = q.where(TStore.reject_reason.in_(set_items['reject_reason']))
        
        if 'reject_time' in set_items:
            q = q.where(TStore.reject_time.in_(set_items['reject_time']))
        
        if 'reject_admin_id' in set_items:
            q = q.where(TStore.reject_admin_id.in_(set_items['reject_admin_id']))
        
        if 'is_default' in set_items:
            q = q.where(TStore.is_default.in_(set_items['is_default']))
        

        if 'name' in search_items:
            q = q.where(TStore.name.like(search_items['name']))
        
        if 'phone' in search_items:
            q = q.where(TStore.phone.like(search_items['phone']))
        
        if 'province' in search_items:
            q = q.where(TStore.province.like(search_items['province']))
        
        if 'city' in search_items:
            q = q.where(TStore.city.like(search_items['city']))
        
        if 'area' in search_items:
            q = q.where(TStore.area.like(search_items['area']))
        
        if 'street' in search_items:
            q = q.where(TStore.street.like(search_items['street']))
        
        if 'address' in search_items:
            q = q.where(TStore.address.like(search_items['address']))
        
        if 'owner' in search_items:
            q = q.where(TStore.owner.like(search_items['owner']))
        
        if 'image' in search_items:
            q = q.where(TStore.image.like(search_items['image']))
        
        if 'company_name' in search_items:
            q = q.where(TStore.company_name.like(search_items['company_name']))
        
        if 'reject_reason' in search_items:
            q = q.where(TStore.reject_reason.like(search_items['reject_reason']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TStore.is_default.asc())
                orders.append(TStore.id.asc())
            elif val == 'desc':
                #orders.append(TStore.is_default.desc())
                orders.append(TStore.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_store_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SStore.parse_obj(t.__dict__) for t in t_store_list]


def filter_count_store(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TStore)


        if 'id' in items:
            q = q.where(TStore.id == items['id'])
        if 'id_start' in items:
            q = q.where(TStore.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TStore.id <= items['id_end'])
        
        if 'name' in items:
            q = q.where(TStore.name == items['name'])
        if 'name_start' in items:
            q = q.where(TStore.name >= items['name_start'])
        if 'name_end' in items:
            q = q.where(TStore.name <= items['name_end'])
        
        if 'phone' in items:
            q = q.where(TStore.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TStore.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TStore.phone <= items['phone_end'])
        
        if 'province' in items:
            q = q.where(TStore.province == items['province'])
        if 'province_start' in items:
            q = q.where(TStore.province >= items['province_start'])
        if 'province_end' in items:
            q = q.where(TStore.province <= items['province_end'])
        
        if 'city' in items:
            q = q.where(TStore.city == items['city'])
        if 'city_start' in items:
            q = q.where(TStore.city >= items['city_start'])
        if 'city_end' in items:
            q = q.where(TStore.city <= items['city_end'])
        
        if 'area' in items:
            q = q.where(TStore.area == items['area'])
        if 'area_start' in items:
            q = q.where(TStore.area >= items['area_start'])
        if 'area_end' in items:
            q = q.where(TStore.area <= items['area_end'])
        
        if 'street' in items:
            q = q.where(TStore.street == items['street'])
        if 'street_start' in items:
            q = q.where(TStore.street >= items['street_start'])
        if 'street_end' in items:
            q = q.where(TStore.street <= items['street_end'])
        
        if 'address' in items:
            q = q.where(TStore.address == items['address'])
        if 'address_start' in items:
            q = q.where(TStore.address >= items['address_start'])
        if 'address_end' in items:
            q = q.where(TStore.address <= items['address_end'])
        
        if 'status' in items:
            q = q.where(TStore.status == items['status'])
        if 'status_start' in items:
            q = q.where(TStore.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TStore.status <= items['status_end'])
        
        if 'owner' in items:
            q = q.where(TStore.owner == items['owner'])
        if 'owner_start' in items:
            q = q.where(TStore.owner >= items['owner_start'])
        if 'owner_end' in items:
            q = q.where(TStore.owner <= items['owner_end'])
        
        if 'recommender_id' in items:
            q = q.where(TStore.recommender_id == items['recommender_id'])
        if 'recommender_id_start' in items:
            q = q.where(TStore.recommender_id >= items['recommender_id_start'])
        if 'recommender_id_end' in items:
            q = q.where(TStore.recommender_id <= items['recommender_id_end'])
        
        if 'register_time' in items:
            q = q.where(TStore.register_time == items['register_time'])
        if 'register_time_start' in items:
            q = q.where(TStore.register_time >= items['register_time_start'])
        if 'register_time_end' in items:
            q = q.where(TStore.register_time <= items['register_time_end'])
        
        if 'type' in items:
            q = q.where(TStore.type == items['type'])
        if 'type_start' in items:
            q = q.where(TStore.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TStore.type <= items['type_end'])
        
        if 'expired_time' in items:
            q = q.where(TStore.expired_time == items['expired_time'])
        if 'expired_time_start' in items:
            q = q.where(TStore.expired_time >= items['expired_time_start'])
        if 'expired_time_end' in items:
            q = q.where(TStore.expired_time <= items['expired_time_end'])
        
        if 'open_time' in items:
            q = q.where(TStore.open_time == items['open_time'])
        if 'open_time_start' in items:
            q = q.where(TStore.open_time >= items['open_time_start'])
        if 'open_time_end' in items:
            q = q.where(TStore.open_time <= items['open_time_end'])
        
        if 'close_time' in items:
            q = q.where(TStore.close_time == items['close_time'])
        if 'close_time_start' in items:
            q = q.where(TStore.close_time >= items['close_time_start'])
        if 'close_time_end' in items:
            q = q.where(TStore.close_time <= items['close_time_end'])
        
        if 'image' in items:
            q = q.where(TStore.image == items['image'])
        if 'image_start' in items:
            q = q.where(TStore.image >= items['image_start'])
        if 'image_end' in items:
            q = q.where(TStore.image <= items['image_end'])
        
        if 'owner_id' in items:
            q = q.where(TStore.owner_id == items['owner_id'])
        if 'owner_id_start' in items:
            q = q.where(TStore.owner_id >= items['owner_id_start'])
        if 'owner_id_end' in items:
            q = q.where(TStore.owner_id <= items['owner_id_end'])
        
        if 'supplier_id' in items:
            q = q.where(TStore.supplier_id == items['supplier_id'])
        if 'supplier_id_start' in items:
            q = q.where(TStore.supplier_id >= items['supplier_id_start'])
        if 'supplier_id_end' in items:
            q = q.where(TStore.supplier_id <= items['supplier_id_end'])
        
        if 'company_name' in items:
            q = q.where(TStore.company_name == items['company_name'])
        if 'company_name_start' in items:
            q = q.where(TStore.company_name >= items['company_name_start'])
        if 'company_name_end' in items:
            q = q.where(TStore.company_name <= items['company_name_end'])
        
        if 'reject_reason' in items:
            q = q.where(TStore.reject_reason == items['reject_reason'])
        if 'reject_reason_start' in items:
            q = q.where(TStore.reject_reason >= items['reject_reason_start'])
        if 'reject_reason_end' in items:
            q = q.where(TStore.reject_reason <= items['reject_reason_end'])
        
        if 'reject_time' in items:
            q = q.where(TStore.reject_time == items['reject_time'])
        if 'reject_time_start' in items:
            q = q.where(TStore.reject_time >= items['reject_time_start'])
        if 'reject_time_end' in items:
            q = q.where(TStore.reject_time <= items['reject_time_end'])
        
        if 'reject_admin_id' in items:
            q = q.where(TStore.reject_admin_id == items['reject_admin_id'])
        if 'reject_admin_id_start' in items:
            q = q.where(TStore.reject_admin_id >= items['reject_admin_id_start'])
        if 'reject_admin_id_end' in items:
            q = q.where(TStore.reject_admin_id <= items['reject_admin_id_end'])
        
        if 'is_default' in items:
            q = q.where(TStore.is_default == items['is_default'])
        if 'is_default_start' in items:
            q = q.where(TStore.is_default >= items['is_default_start'])
        if 'is_default_end' in items:
            q = q.where(TStore.is_default <= items['is_default_end'])
        

        if 'id' in set_items:
            q = q.where(TStore.id.in_(set_items['id']))
        
        if 'name' in set_items:
            q = q.where(TStore.name.in_(set_items['name']))
        
        if 'phone' in set_items:
            q = q.where(TStore.phone.in_(set_items['phone']))
        
        if 'province' in set_items:
            q = q.where(TStore.province.in_(set_items['province']))
        
        if 'city' in set_items:
            q = q.where(TStore.city.in_(set_items['city']))
        
        if 'area' in set_items:
            q = q.where(TStore.area.in_(set_items['area']))
        
        if 'street' in set_items:
            q = q.where(TStore.street.in_(set_items['street']))
        
        if 'address' in set_items:
            q = q.where(TStore.address.in_(set_items['address']))
        
        if 'status' in set_items:
            q = q.where(TStore.status.in_(set_items['status']))
        
        if 'owner' in set_items:
            q = q.where(TStore.owner.in_(set_items['owner']))
        
        if 'recommender_id' in set_items:
            q = q.where(TStore.recommender_id.in_(set_items['recommender_id']))
        
        if 'register_time' in set_items:
            q = q.where(TStore.register_time.in_(set_items['register_time']))
        
        if 'type' in set_items:
            q = q.where(TStore.type.in_(set_items['type']))
        
        if 'expired_time' in set_items:
            q = q.where(TStore.expired_time.in_(set_items['expired_time']))
        
        if 'open_time' in set_items:
            q = q.where(TStore.open_time.in_(set_items['open_time']))
        
        if 'close_time' in set_items:
            q = q.where(TStore.close_time.in_(set_items['close_time']))
        
        if 'image' in set_items:
            q = q.where(TStore.image.in_(set_items['image']))
        
        if 'owner_id' in set_items:
            q = q.where(TStore.owner_id.in_(set_items['owner_id']))
        
        if 'supplier_id' in set_items:
            q = q.where(TStore.supplier_id.in_(set_items['supplier_id']))
        
        if 'company_name' in set_items:
            q = q.where(TStore.company_name.in_(set_items['company_name']))
        
        if 'reject_reason' in set_items:
            q = q.where(TStore.reject_reason.in_(set_items['reject_reason']))
        
        if 'reject_time' in set_items:
            q = q.where(TStore.reject_time.in_(set_items['reject_time']))
        
        if 'reject_admin_id' in set_items:
            q = q.where(TStore.reject_admin_id.in_(set_items['reject_admin_id']))
        
        if 'is_default' in set_items:
            q = q.where(TStore.is_default.in_(set_items['is_default']))
        

        if 'name' in search_items:
            q = q.where(TStore.name.like(search_items['name']))
        
        if 'phone' in search_items:
            q = q.where(TStore.phone.like(search_items['phone']))
        
        if 'province' in search_items:
            q = q.where(TStore.province.like(search_items['province']))
        
        if 'city' in search_items:
            q = q.where(TStore.city.like(search_items['city']))
        
        if 'area' in search_items:
            q = q.where(TStore.area.like(search_items['area']))
        
        if 'street' in search_items:
            q = q.where(TStore.street.like(search_items['street']))
        
        if 'address' in search_items:
            q = q.where(TStore.address.like(search_items['address']))
        
        if 'owner' in search_items:
            q = q.where(TStore.owner.like(search_items['owner']))
        
        if 'image' in search_items:
            q = q.where(TStore.image.like(search_items['image']))
        
        if 'company_name' in search_items:
            q = q.where(TStore.company_name.like(search_items['company_name']))
        
        if 'reject_reason' in search_items:
            q = q.where(TStore.reject_reason.like(search_items['reject_reason']))
        
    
        c = q.count()
        return c

    
def insert_store_amount(item: CreateStoreAmount, db: Optional[SessionLocal] = None) -> SStoreAmount:
    data = model2dict(item)
    t = TStoreAmount(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SStoreAmount.parse_obj(t.__dict__)

    
def delete_store_amount(store_amount_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TStoreAmount).where(TStoreAmount.id == store_amount_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TStoreAmount).where(TStoreAmount.id == store_amount_id).delete()
        db.commit()

    
def update_store_amount(item: SStoreAmount, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TStoreAmount).where(TStoreAmount.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TStoreAmount).where(TStoreAmount.id == item.id).update(data)
        db.commit()

    
def get_store_amount(store_amount_id: int) -> Optional[SStoreAmount]:
    with Dao() as db:
        t = db.query(TStoreAmount).where(TStoreAmount.id == store_amount_id).first()
        if t:
            return SStoreAmount.parse_obj(t.__dict__)
        else:
            return None


def filter_store_amount(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SStoreAmount]:
    with Dao() as db:
        q = db.query(TStoreAmount)


        if 'id' in items:
            q = q.where(TStoreAmount.id == items['id'])
        if 'id_start' in items:
            q = q.where(TStoreAmount.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TStoreAmount.id <= items['id_end'])
        
        if 'type' in items:
            q = q.where(TStoreAmount.type == items['type'])
        if 'type_start' in items:
            q = q.where(TStoreAmount.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TStoreAmount.type <= items['type_end'])
        
        if 'change' in items:
            q = q.where(TStoreAmount.change == items['change'])
        if 'change_start' in items:
            q = q.where(TStoreAmount.change >= items['change_start'])
        if 'change_end' in items:
            q = q.where(TStoreAmount.change <= items['change_end'])
        
        if 'amount' in items:
            q = q.where(TStoreAmount.amount == items['amount'])
        if 'amount_start' in items:
            q = q.where(TStoreAmount.amount >= items['amount_start'])
        if 'amount_end' in items:
            q = q.where(TStoreAmount.amount <= items['amount_end'])
        
        if 'create_time' in items:
            q = q.where(TStoreAmount.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TStoreAmount.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TStoreAmount.create_time <= items['create_time_end'])
        
        if 'store_id' in items:
            q = q.where(TStoreAmount.store_id == items['store_id'])
        if 'store_id_start' in items:
            q = q.where(TStoreAmount.store_id >= items['store_id_start'])
        if 'store_id_end' in items:
            q = q.where(TStoreAmount.store_id <= items['store_id_end'])
        

        if 'id' in set_items:
            q = q.where(TStoreAmount.id.in_(set_items['id']))
        
        if 'type' in set_items:
            q = q.where(TStoreAmount.type.in_(set_items['type']))
        
        if 'change' in set_items:
            q = q.where(TStoreAmount.change.in_(set_items['change']))
        
        if 'amount' in set_items:
            q = q.where(TStoreAmount.amount.in_(set_items['amount']))
        
        if 'create_time' in set_items:
            q = q.where(TStoreAmount.create_time.in_(set_items['create_time']))
        
        if 'store_id' in set_items:
            q = q.where(TStoreAmount.store_id.in_(set_items['store_id']))
        

    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TStoreAmount.store_id.asc())
                orders.append(TStoreAmount.id.asc())
            elif val == 'desc':
                #orders.append(TStoreAmount.store_id.desc())
                orders.append(TStoreAmount.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_store_amount_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SStoreAmount.parse_obj(t.__dict__) for t in t_store_amount_list]


def filter_count_store_amount(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TStoreAmount)


        if 'id' in items:
            q = q.where(TStoreAmount.id == items['id'])
        if 'id_start' in items:
            q = q.where(TStoreAmount.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TStoreAmount.id <= items['id_end'])
        
        if 'type' in items:
            q = q.where(TStoreAmount.type == items['type'])
        if 'type_start' in items:
            q = q.where(TStoreAmount.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TStoreAmount.type <= items['type_end'])
        
        if 'change' in items:
            q = q.where(TStoreAmount.change == items['change'])
        if 'change_start' in items:
            q = q.where(TStoreAmount.change >= items['change_start'])
        if 'change_end' in items:
            q = q.where(TStoreAmount.change <= items['change_end'])
        
        if 'amount' in items:
            q = q.where(TStoreAmount.amount == items['amount'])
        if 'amount_start' in items:
            q = q.where(TStoreAmount.amount >= items['amount_start'])
        if 'amount_end' in items:
            q = q.where(TStoreAmount.amount <= items['amount_end'])
        
        if 'create_time' in items:
            q = q.where(TStoreAmount.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TStoreAmount.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TStoreAmount.create_time <= items['create_time_end'])
        
        if 'store_id' in items:
            q = q.where(TStoreAmount.store_id == items['store_id'])
        if 'store_id_start' in items:
            q = q.where(TStoreAmount.store_id >= items['store_id_start'])
        if 'store_id_end' in items:
            q = q.where(TStoreAmount.store_id <= items['store_id_end'])
        

        if 'id' in set_items:
            q = q.where(TStoreAmount.id.in_(set_items['id']))
        
        if 'type' in set_items:
            q = q.where(TStoreAmount.type.in_(set_items['type']))
        
        if 'change' in set_items:
            q = q.where(TStoreAmount.change.in_(set_items['change']))
        
        if 'amount' in set_items:
            q = q.where(TStoreAmount.amount.in_(set_items['amount']))
        
        if 'create_time' in set_items:
            q = q.where(TStoreAmount.create_time.in_(set_items['create_time']))
        
        if 'store_id' in set_items:
            q = q.where(TStoreAmount.store_id.in_(set_items['store_id']))
        

    
        c = q.count()
        return c

    
def insert_store_change_type(item: CreateStoreChangeType, db: Optional[SessionLocal] = None) -> SStoreChangeType:
    data = model2dict(item)
    t = TStoreChangeType(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SStoreChangeType.parse_obj(t.__dict__)

    
def delete_store_change_type(store_change_type_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TStoreChangeType).where(TStoreChangeType.id == store_change_type_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TStoreChangeType).where(TStoreChangeType.id == store_change_type_id).delete()
        db.commit()

    
def update_store_change_type(item: SStoreChangeType, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TStoreChangeType).where(TStoreChangeType.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TStoreChangeType).where(TStoreChangeType.id == item.id).update(data)
        db.commit()

    
def get_store_change_type(store_change_type_id: int) -> Optional[SStoreChangeType]:
    with Dao() as db:
        t = db.query(TStoreChangeType).where(TStoreChangeType.id == store_change_type_id).first()
        if t:
            return SStoreChangeType.parse_obj(t.__dict__)
        else:
            return None


def filter_store_change_type(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SStoreChangeType]:
    with Dao() as db:
        q = db.query(TStoreChangeType)


        if 'id' in items:
            q = q.where(TStoreChangeType.id == items['id'])
        if 'id_start' in items:
            q = q.where(TStoreChangeType.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TStoreChangeType.id <= items['id_end'])
        
        if 'type' in items:
            q = q.where(TStoreChangeType.type == items['type'])
        if 'type_start' in items:
            q = q.where(TStoreChangeType.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TStoreChangeType.type <= items['type_end'])
        

        if 'id' in set_items:
            q = q.where(TStoreChangeType.id.in_(set_items['id']))
        
        if 'type' in set_items:
            q = q.where(TStoreChangeType.type.in_(set_items['type']))
        

        if 'type' in search_items:
            q = q.where(TStoreChangeType.type.like(search_items['type']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TStoreChangeType.type.asc())
                orders.append(TStoreChangeType.id.asc())
            elif val == 'desc':
                #orders.append(TStoreChangeType.type.desc())
                orders.append(TStoreChangeType.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_store_change_type_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SStoreChangeType.parse_obj(t.__dict__) for t in t_store_change_type_list]


def filter_count_store_change_type(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TStoreChangeType)


        if 'id' in items:
            q = q.where(TStoreChangeType.id == items['id'])
        if 'id_start' in items:
            q = q.where(TStoreChangeType.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TStoreChangeType.id <= items['id_end'])
        
        if 'type' in items:
            q = q.where(TStoreChangeType.type == items['type'])
        if 'type_start' in items:
            q = q.where(TStoreChangeType.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TStoreChangeType.type <= items['type_end'])
        

        if 'id' in set_items:
            q = q.where(TStoreChangeType.id.in_(set_items['id']))
        
        if 'type' in set_items:
            q = q.where(TStoreChangeType.type.in_(set_items['type']))
        

        if 'type' in search_items:
            q = q.where(TStoreChangeType.type.like(search_items['type']))
        
    
        c = q.count()
        return c

    
def insert_store_contract(item: CreateStoreContract, db: Optional[SessionLocal] = None) -> SStoreContract:
    data = model2dict(item)
    t = TStoreContract(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SStoreContract.parse_obj(t.__dict__)

    
def delete_store_contract(store_contract_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TStoreContract).where(TStoreContract.id == store_contract_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TStoreContract).where(TStoreContract.id == store_contract_id).delete()
        db.commit()

    
def update_store_contract(item: SStoreContract, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TStoreContract).where(TStoreContract.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TStoreContract).where(TStoreContract.id == item.id).update(data)
        db.commit()

    
def get_store_contract(store_contract_id: int) -> Optional[SStoreContract]:
    with Dao() as db:
        t = db.query(TStoreContract).where(TStoreContract.id == store_contract_id).first()
        if t:
            return SStoreContract.parse_obj(t.__dict__)
        else:
            return None


def filter_store_contract(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SStoreContract]:
    with Dao() as db:
        q = db.query(TStoreContract)


        if 'contract' in items:
            q = q.where(TStoreContract.contract == items['contract'])
        if 'contract_start' in items:
            q = q.where(TStoreContract.contract >= items['contract_start'])
        if 'contract_end' in items:
            q = q.where(TStoreContract.contract <= items['contract_end'])
        
        if 'id' in items:
            q = q.where(TStoreContract.id == items['id'])
        if 'id_start' in items:
            q = q.where(TStoreContract.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TStoreContract.id <= items['id_end'])
        
        if 'store_id' in items:
            q = q.where(TStoreContract.store_id == items['store_id'])
        if 'store_id_start' in items:
            q = q.where(TStoreContract.store_id >= items['store_id_start'])
        if 'store_id_end' in items:
            q = q.where(TStoreContract.store_id <= items['store_id_end'])
        
        if 'create_time' in items:
            q = q.where(TStoreContract.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TStoreContract.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TStoreContract.create_time <= items['create_time_end'])
        
        if 'expired_time' in items:
            q = q.where(TStoreContract.expired_time == items['expired_time'])
        if 'expired_time_start' in items:
            q = q.where(TStoreContract.expired_time >= items['expired_time_start'])
        if 'expired_time_end' in items:
            q = q.where(TStoreContract.expired_time <= items['expired_time_end'])
        

        if 'contract' in set_items:
            q = q.where(TStoreContract.contract.in_(set_items['contract']))
        
        if 'id' in set_items:
            q = q.where(TStoreContract.id.in_(set_items['id']))
        
        if 'store_id' in set_items:
            q = q.where(TStoreContract.store_id.in_(set_items['store_id']))
        
        if 'create_time' in set_items:
            q = q.where(TStoreContract.create_time.in_(set_items['create_time']))
        
        if 'expired_time' in set_items:
            q = q.where(TStoreContract.expired_time.in_(set_items['expired_time']))
        

        if 'contract' in search_items:
            q = q.where(TStoreContract.contract.like(search_items['contract']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TStoreContract.expired_time.asc())
                orders.append(TStoreContract.id.asc())
            elif val == 'desc':
                #orders.append(TStoreContract.expired_time.desc())
                orders.append(TStoreContract.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_store_contract_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SStoreContract.parse_obj(t.__dict__) for t in t_store_contract_list]


def filter_count_store_contract(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TStoreContract)


        if 'contract' in items:
            q = q.where(TStoreContract.contract == items['contract'])
        if 'contract_start' in items:
            q = q.where(TStoreContract.contract >= items['contract_start'])
        if 'contract_end' in items:
            q = q.where(TStoreContract.contract <= items['contract_end'])
        
        if 'id' in items:
            q = q.where(TStoreContract.id == items['id'])
        if 'id_start' in items:
            q = q.where(TStoreContract.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TStoreContract.id <= items['id_end'])
        
        if 'store_id' in items:
            q = q.where(TStoreContract.store_id == items['store_id'])
        if 'store_id_start' in items:
            q = q.where(TStoreContract.store_id >= items['store_id_start'])
        if 'store_id_end' in items:
            q = q.where(TStoreContract.store_id <= items['store_id_end'])
        
        if 'create_time' in items:
            q = q.where(TStoreContract.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TStoreContract.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TStoreContract.create_time <= items['create_time_end'])
        
        if 'expired_time' in items:
            q = q.where(TStoreContract.expired_time == items['expired_time'])
        if 'expired_time_start' in items:
            q = q.where(TStoreContract.expired_time >= items['expired_time_start'])
        if 'expired_time_end' in items:
            q = q.where(TStoreContract.expired_time <= items['expired_time_end'])
        

        if 'contract' in set_items:
            q = q.where(TStoreContract.contract.in_(set_items['contract']))
        
        if 'id' in set_items:
            q = q.where(TStoreContract.id.in_(set_items['id']))
        
        if 'store_id' in set_items:
            q = q.where(TStoreContract.store_id.in_(set_items['store_id']))
        
        if 'create_time' in set_items:
            q = q.where(TStoreContract.create_time.in_(set_items['create_time']))
        
        if 'expired_time' in set_items:
            q = q.where(TStoreContract.expired_time.in_(set_items['expired_time']))
        

        if 'contract' in search_items:
            q = q.where(TStoreContract.contract.like(search_items['contract']))
        
    
        c = q.count()
        return c

    
def insert_store_income(item: CreateStoreIncome, db: Optional[SessionLocal] = None) -> SStoreIncome:
    data = model2dict(item)
    t = TStoreIncome(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SStoreIncome.parse_obj(t.__dict__)

    
def delete_store_income(store_income_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TStoreIncome).where(TStoreIncome.id == store_income_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TStoreIncome).where(TStoreIncome.id == store_income_id).delete()
        db.commit()

    
def update_store_income(item: SStoreIncome, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TStoreIncome).where(TStoreIncome.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TStoreIncome).where(TStoreIncome.id == item.id).update(data)
        db.commit()

    
def get_store_income(store_income_id: int) -> Optional[SStoreIncome]:
    with Dao() as db:
        t = db.query(TStoreIncome).where(TStoreIncome.id == store_income_id).first()
        if t:
            return SStoreIncome.parse_obj(t.__dict__)
        else:
            return None


def filter_store_income(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SStoreIncome]:
    with Dao() as db:
        q = db.query(TStoreIncome)


        if 'id' in items:
            q = q.where(TStoreIncome.id == items['id'])
        if 'id_start' in items:
            q = q.where(TStoreIncome.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TStoreIncome.id <= items['id_end'])
        
        if 'income_add' in items:
            q = q.where(TStoreIncome.income_add == items['income_add'])
        if 'income_add_start' in items:
            q = q.where(TStoreIncome.income_add >= items['income_add_start'])
        if 'income_add_end' in items:
            q = q.where(TStoreIncome.income_add <= items['income_add_end'])
        
        if 'income_total' in items:
            q = q.where(TStoreIncome.income_total == items['income_total'])
        if 'income_total_start' in items:
            q = q.where(TStoreIncome.income_total >= items['income_total_start'])
        if 'income_total_end' in items:
            q = q.where(TStoreIncome.income_total <= items['income_total_end'])
        
        if 'create_time' in items:
            q = q.where(TStoreIncome.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TStoreIncome.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TStoreIncome.create_time <= items['create_time_end'])
        
        if 'store_id' in items:
            q = q.where(TStoreIncome.store_id == items['store_id'])
        if 'store_id_start' in items:
            q = q.where(TStoreIncome.store_id >= items['store_id_start'])
        if 'store_id_end' in items:
            q = q.where(TStoreIncome.store_id <= items['store_id_end'])
        

        if 'id' in set_items:
            q = q.where(TStoreIncome.id.in_(set_items['id']))
        
        if 'income_add' in set_items:
            q = q.where(TStoreIncome.income_add.in_(set_items['income_add']))
        
        if 'income_total' in set_items:
            q = q.where(TStoreIncome.income_total.in_(set_items['income_total']))
        
        if 'create_time' in set_items:
            q = q.where(TStoreIncome.create_time.in_(set_items['create_time']))
        
        if 'store_id' in set_items:
            q = q.where(TStoreIncome.store_id.in_(set_items['store_id']))
        

    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TStoreIncome.store_id.asc())
                orders.append(TStoreIncome.id.asc())
            elif val == 'desc':
                #orders.append(TStoreIncome.store_id.desc())
                orders.append(TStoreIncome.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_store_income_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SStoreIncome.parse_obj(t.__dict__) for t in t_store_income_list]


def filter_count_store_income(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TStoreIncome)


        if 'id' in items:
            q = q.where(TStoreIncome.id == items['id'])
        if 'id_start' in items:
            q = q.where(TStoreIncome.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TStoreIncome.id <= items['id_end'])
        
        if 'income_add' in items:
            q = q.where(TStoreIncome.income_add == items['income_add'])
        if 'income_add_start' in items:
            q = q.where(TStoreIncome.income_add >= items['income_add_start'])
        if 'income_add_end' in items:
            q = q.where(TStoreIncome.income_add <= items['income_add_end'])
        
        if 'income_total' in items:
            q = q.where(TStoreIncome.income_total == items['income_total'])
        if 'income_total_start' in items:
            q = q.where(TStoreIncome.income_total >= items['income_total_start'])
        if 'income_total_end' in items:
            q = q.where(TStoreIncome.income_total <= items['income_total_end'])
        
        if 'create_time' in items:
            q = q.where(TStoreIncome.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TStoreIncome.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TStoreIncome.create_time <= items['create_time_end'])
        
        if 'store_id' in items:
            q = q.where(TStoreIncome.store_id == items['store_id'])
        if 'store_id_start' in items:
            q = q.where(TStoreIncome.store_id >= items['store_id_start'])
        if 'store_id_end' in items:
            q = q.where(TStoreIncome.store_id <= items['store_id_end'])
        

        if 'id' in set_items:
            q = q.where(TStoreIncome.id.in_(set_items['id']))
        
        if 'income_add' in set_items:
            q = q.where(TStoreIncome.income_add.in_(set_items['income_add']))
        
        if 'income_total' in set_items:
            q = q.where(TStoreIncome.income_total.in_(set_items['income_total']))
        
        if 'create_time' in set_items:
            q = q.where(TStoreIncome.create_time.in_(set_items['create_time']))
        
        if 'store_id' in set_items:
            q = q.where(TStoreIncome.store_id.in_(set_items['store_id']))
        

    
        c = q.count()
        return c

    
def insert_store_license(item: CreateStoreLicense, db: Optional[SessionLocal] = None) -> SStoreLicense:
    data = model2dict(item)
    t = TStoreLicense(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SStoreLicense.parse_obj(t.__dict__)

    
def delete_store_license(store_license_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TStoreLicense).where(TStoreLicense.id == store_license_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TStoreLicense).where(TStoreLicense.id == store_license_id).delete()
        db.commit()

    
def update_store_license(item: SStoreLicense, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TStoreLicense).where(TStoreLicense.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TStoreLicense).where(TStoreLicense.id == item.id).update(data)
        db.commit()

    
def get_store_license(store_license_id: int) -> Optional[SStoreLicense]:
    with Dao() as db:
        t = db.query(TStoreLicense).where(TStoreLicense.id == store_license_id).first()
        if t:
            return SStoreLicense.parse_obj(t.__dict__)
        else:
            return None


def filter_store_license(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SStoreLicense]:
    with Dao() as db:
        q = db.query(TStoreLicense)


        if 'id' in items:
            q = q.where(TStoreLicense.id == items['id'])
        if 'id_start' in items:
            q = q.where(TStoreLicense.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TStoreLicense.id <= items['id_end'])
        
        if 'license' in items:
            q = q.where(TStoreLicense.license == items['license'])
        if 'license_start' in items:
            q = q.where(TStoreLicense.license >= items['license_start'])
        if 'license_end' in items:
            q = q.where(TStoreLicense.license <= items['license_end'])
        
        if 'store_id' in items:
            q = q.where(TStoreLicense.store_id == items['store_id'])
        if 'store_id_start' in items:
            q = q.where(TStoreLicense.store_id >= items['store_id_start'])
        if 'store_id_end' in items:
            q = q.where(TStoreLicense.store_id <= items['store_id_end'])
        
        if 'create_time' in items:
            q = q.where(TStoreLicense.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TStoreLicense.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TStoreLicense.create_time <= items['create_time_end'])
        

        if 'id' in set_items:
            q = q.where(TStoreLicense.id.in_(set_items['id']))
        
        if 'license' in set_items:
            q = q.where(TStoreLicense.license.in_(set_items['license']))
        
        if 'store_id' in set_items:
            q = q.where(TStoreLicense.store_id.in_(set_items['store_id']))
        
        if 'create_time' in set_items:
            q = q.where(TStoreLicense.create_time.in_(set_items['create_time']))
        

        if 'license' in search_items:
            q = q.where(TStoreLicense.license.like(search_items['license']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TStoreLicense.create_time.asc())
                orders.append(TStoreLicense.id.asc())
            elif val == 'desc':
                #orders.append(TStoreLicense.create_time.desc())
                orders.append(TStoreLicense.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_store_license_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SStoreLicense.parse_obj(t.__dict__) for t in t_store_license_list]


def filter_count_store_license(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TStoreLicense)


        if 'id' in items:
            q = q.where(TStoreLicense.id == items['id'])
        if 'id_start' in items:
            q = q.where(TStoreLicense.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TStoreLicense.id <= items['id_end'])
        
        if 'license' in items:
            q = q.where(TStoreLicense.license == items['license'])
        if 'license_start' in items:
            q = q.where(TStoreLicense.license >= items['license_start'])
        if 'license_end' in items:
            q = q.where(TStoreLicense.license <= items['license_end'])
        
        if 'store_id' in items:
            q = q.where(TStoreLicense.store_id == items['store_id'])
        if 'store_id_start' in items:
            q = q.where(TStoreLicense.store_id >= items['store_id_start'])
        if 'store_id_end' in items:
            q = q.where(TStoreLicense.store_id <= items['store_id_end'])
        
        if 'create_time' in items:
            q = q.where(TStoreLicense.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TStoreLicense.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TStoreLicense.create_time <= items['create_time_end'])
        

        if 'id' in set_items:
            q = q.where(TStoreLicense.id.in_(set_items['id']))
        
        if 'license' in set_items:
            q = q.where(TStoreLicense.license.in_(set_items['license']))
        
        if 'store_id' in set_items:
            q = q.where(TStoreLicense.store_id.in_(set_items['store_id']))
        
        if 'create_time' in set_items:
            q = q.where(TStoreLicense.create_time.in_(set_items['create_time']))
        

        if 'license' in search_items:
            q = q.where(TStoreLicense.license.like(search_items['license']))
        
    
        c = q.count()
        return c

    
def insert_store_membership(item: CreateStoreMembership, db: Optional[SessionLocal] = None) -> SStoreMembership:
    data = model2dict(item)
    t = TStoreMembership(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SStoreMembership.parse_obj(t.__dict__)

    
def delete_store_membership(store_membership_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TStoreMembership).where(TStoreMembership.id == store_membership_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TStoreMembership).where(TStoreMembership.id == store_membership_id).delete()
        db.commit()

    
def update_store_membership(item: SStoreMembership, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TStoreMembership).where(TStoreMembership.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TStoreMembership).where(TStoreMembership.id == item.id).update(data)
        db.commit()

    
def get_store_membership(store_membership_id: int) -> Optional[SStoreMembership]:
    with Dao() as db:
        t = db.query(TStoreMembership).where(TStoreMembership.id == store_membership_id).first()
        if t:
            return SStoreMembership.parse_obj(t.__dict__)
        else:
            return None


def filter_store_membership(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SStoreMembership]:
    with Dao() as db:
        q = db.query(TStoreMembership)


        if 'id' in items:
            q = q.where(TStoreMembership.id == items['id'])
        if 'id_start' in items:
            q = q.where(TStoreMembership.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TStoreMembership.id <= items['id_end'])
        
        if 'store_id' in items:
            q = q.where(TStoreMembership.store_id == items['store_id'])
        if 'store_id_start' in items:
            q = q.where(TStoreMembership.store_id >= items['store_id_start'])
        if 'store_id_end' in items:
            q = q.where(TStoreMembership.store_id <= items['store_id_end'])
        
        if 'user_id' in items:
            q = q.where(TStoreMembership.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TStoreMembership.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TStoreMembership.user_id <= items['user_id_end'])
        
        if 'status' in items:
            q = q.where(TStoreMembership.status == items['status'])
        if 'status_start' in items:
            q = q.where(TStoreMembership.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TStoreMembership.status <= items['status_end'])
        
        if 'create_time' in items:
            q = q.where(TStoreMembership.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TStoreMembership.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TStoreMembership.create_time <= items['create_time_end'])
        
        if 'expired_time' in items:
            q = q.where(TStoreMembership.expired_time == items['expired_time'])
        if 'expired_time_start' in items:
            q = q.where(TStoreMembership.expired_time >= items['expired_time_start'])
        if 'expired_time_end' in items:
            q = q.where(TStoreMembership.expired_time <= items['expired_time_end'])
        

        if 'id' in set_items:
            q = q.where(TStoreMembership.id.in_(set_items['id']))
        
        if 'store_id' in set_items:
            q = q.where(TStoreMembership.store_id.in_(set_items['store_id']))
        
        if 'user_id' in set_items:
            q = q.where(TStoreMembership.user_id.in_(set_items['user_id']))
        
        if 'status' in set_items:
            q = q.where(TStoreMembership.status.in_(set_items['status']))
        
        if 'create_time' in set_items:
            q = q.where(TStoreMembership.create_time.in_(set_items['create_time']))
        
        if 'expired_time' in set_items:
            q = q.where(TStoreMembership.expired_time.in_(set_items['expired_time']))
        

        if 'status' in search_items:
            q = q.where(TStoreMembership.status.like(search_items['status']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TStoreMembership.expired_time.asc())
                orders.append(TStoreMembership.id.asc())
            elif val == 'desc':
                #orders.append(TStoreMembership.expired_time.desc())
                orders.append(TStoreMembership.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_store_membership_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SStoreMembership.parse_obj(t.__dict__) for t in t_store_membership_list]


def filter_count_store_membership(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TStoreMembership)


        if 'id' in items:
            q = q.where(TStoreMembership.id == items['id'])
        if 'id_start' in items:
            q = q.where(TStoreMembership.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TStoreMembership.id <= items['id_end'])
        
        if 'store_id' in items:
            q = q.where(TStoreMembership.store_id == items['store_id'])
        if 'store_id_start' in items:
            q = q.where(TStoreMembership.store_id >= items['store_id_start'])
        if 'store_id_end' in items:
            q = q.where(TStoreMembership.store_id <= items['store_id_end'])
        
        if 'user_id' in items:
            q = q.where(TStoreMembership.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TStoreMembership.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TStoreMembership.user_id <= items['user_id_end'])
        
        if 'status' in items:
            q = q.where(TStoreMembership.status == items['status'])
        if 'status_start' in items:
            q = q.where(TStoreMembership.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TStoreMembership.status <= items['status_end'])
        
        if 'create_time' in items:
            q = q.where(TStoreMembership.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TStoreMembership.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TStoreMembership.create_time <= items['create_time_end'])
        
        if 'expired_time' in items:
            q = q.where(TStoreMembership.expired_time == items['expired_time'])
        if 'expired_time_start' in items:
            q = q.where(TStoreMembership.expired_time >= items['expired_time_start'])
        if 'expired_time_end' in items:
            q = q.where(TStoreMembership.expired_time <= items['expired_time_end'])
        

        if 'id' in set_items:
            q = q.where(TStoreMembership.id.in_(set_items['id']))
        
        if 'store_id' in set_items:
            q = q.where(TStoreMembership.store_id.in_(set_items['store_id']))
        
        if 'user_id' in set_items:
            q = q.where(TStoreMembership.user_id.in_(set_items['user_id']))
        
        if 'status' in set_items:
            q = q.where(TStoreMembership.status.in_(set_items['status']))
        
        if 'create_time' in set_items:
            q = q.where(TStoreMembership.create_time.in_(set_items['create_time']))
        
        if 'expired_time' in set_items:
            q = q.where(TStoreMembership.expired_time.in_(set_items['expired_time']))
        

        if 'status' in search_items:
            q = q.where(TStoreMembership.status.like(search_items['status']))
        
    
        c = q.count()
        return c

    
def insert_store_owner(item: CreateStoreOwner, db: Optional[SessionLocal] = None) -> SStoreOwner:
    data = model2dict(item)
    t = TStoreOwner(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SStoreOwner.parse_obj(t.__dict__)

    
def delete_store_owner(store_owner_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TStoreOwner).where(TStoreOwner.id == store_owner_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TStoreOwner).where(TStoreOwner.id == store_owner_id).delete()
        db.commit()

    
def update_store_owner(item: SStoreOwner, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TStoreOwner).where(TStoreOwner.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TStoreOwner).where(TStoreOwner.id == item.id).update(data)
        db.commit()

    
def get_store_owner(store_owner_id: int) -> Optional[SStoreOwner]:
    with Dao() as db:
        t = db.query(TStoreOwner).where(TStoreOwner.id == store_owner_id).first()
        if t:
            return SStoreOwner.parse_obj(t.__dict__)
        else:
            return None


def filter_store_owner(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SStoreOwner]:
    with Dao() as db:
        q = db.query(TStoreOwner)


        if 'id' in items:
            q = q.where(TStoreOwner.id == items['id'])
        if 'id_start' in items:
            q = q.where(TStoreOwner.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TStoreOwner.id <= items['id_end'])
        
        if 'name' in items:
            q = q.where(TStoreOwner.name == items['name'])
        if 'name_start' in items:
            q = q.where(TStoreOwner.name >= items['name_start'])
        if 'name_end' in items:
            q = q.where(TStoreOwner.name <= items['name_end'])
        
        if 'phone' in items:
            q = q.where(TStoreOwner.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TStoreOwner.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TStoreOwner.phone <= items['phone_end'])
        
        if 'password' in items:
            q = q.where(TStoreOwner.password == items['password'])
        if 'password_start' in items:
            q = q.where(TStoreOwner.password >= items['password_start'])
        if 'password_end' in items:
            q = q.where(TStoreOwner.password <= items['password_end'])
        
        if 'id_card' in items:
            q = q.where(TStoreOwner.id_card == items['id_card'])
        if 'id_card_start' in items:
            q = q.where(TStoreOwner.id_card >= items['id_card_start'])
        if 'id_card_end' in items:
            q = q.where(TStoreOwner.id_card <= items['id_card_end'])
        
        if 'front_image' in items:
            q = q.where(TStoreOwner.front_image == items['front_image'])
        if 'front_image_start' in items:
            q = q.where(TStoreOwner.front_image >= items['front_image_start'])
        if 'front_image_end' in items:
            q = q.where(TStoreOwner.front_image <= items['front_image_end'])
        
        if 'back_image' in items:
            q = q.where(TStoreOwner.back_image == items['back_image'])
        if 'back_image_start' in items:
            q = q.where(TStoreOwner.back_image >= items['back_image_start'])
        if 'back_image_end' in items:
            q = q.where(TStoreOwner.back_image <= items['back_image_end'])
        

        if 'id' in set_items:
            q = q.where(TStoreOwner.id.in_(set_items['id']))
        
        if 'name' in set_items:
            q = q.where(TStoreOwner.name.in_(set_items['name']))
        
        if 'phone' in set_items:
            q = q.where(TStoreOwner.phone.in_(set_items['phone']))
        
        if 'password' in set_items:
            q = q.where(TStoreOwner.password.in_(set_items['password']))
        
        if 'id_card' in set_items:
            q = q.where(TStoreOwner.id_card.in_(set_items['id_card']))
        
        if 'front_image' in set_items:
            q = q.where(TStoreOwner.front_image.in_(set_items['front_image']))
        
        if 'back_image' in set_items:
            q = q.where(TStoreOwner.back_image.in_(set_items['back_image']))
        

        if 'name' in search_items:
            q = q.where(TStoreOwner.name.like(search_items['name']))
        
        if 'phone' in search_items:
            q = q.where(TStoreOwner.phone.like(search_items['phone']))
        
        if 'password' in search_items:
            q = q.where(TStoreOwner.password.like(search_items['password']))
        
        if 'id_card' in search_items:
            q = q.where(TStoreOwner.id_card.like(search_items['id_card']))
        
        if 'front_image' in search_items:
            q = q.where(TStoreOwner.front_image.like(search_items['front_image']))
        
        if 'back_image' in search_items:
            q = q.where(TStoreOwner.back_image.like(search_items['back_image']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TStoreOwner.back_image.asc())
                orders.append(TStoreOwner.id.asc())
            elif val == 'desc':
                #orders.append(TStoreOwner.back_image.desc())
                orders.append(TStoreOwner.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_store_owner_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SStoreOwner.parse_obj(t.__dict__) for t in t_store_owner_list]


def filter_count_store_owner(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TStoreOwner)


        if 'id' in items:
            q = q.where(TStoreOwner.id == items['id'])
        if 'id_start' in items:
            q = q.where(TStoreOwner.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TStoreOwner.id <= items['id_end'])
        
        if 'name' in items:
            q = q.where(TStoreOwner.name == items['name'])
        if 'name_start' in items:
            q = q.where(TStoreOwner.name >= items['name_start'])
        if 'name_end' in items:
            q = q.where(TStoreOwner.name <= items['name_end'])
        
        if 'phone' in items:
            q = q.where(TStoreOwner.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TStoreOwner.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TStoreOwner.phone <= items['phone_end'])
        
        if 'password' in items:
            q = q.where(TStoreOwner.password == items['password'])
        if 'password_start' in items:
            q = q.where(TStoreOwner.password >= items['password_start'])
        if 'password_end' in items:
            q = q.where(TStoreOwner.password <= items['password_end'])
        
        if 'id_card' in items:
            q = q.where(TStoreOwner.id_card == items['id_card'])
        if 'id_card_start' in items:
            q = q.where(TStoreOwner.id_card >= items['id_card_start'])
        if 'id_card_end' in items:
            q = q.where(TStoreOwner.id_card <= items['id_card_end'])
        
        if 'front_image' in items:
            q = q.where(TStoreOwner.front_image == items['front_image'])
        if 'front_image_start' in items:
            q = q.where(TStoreOwner.front_image >= items['front_image_start'])
        if 'front_image_end' in items:
            q = q.where(TStoreOwner.front_image <= items['front_image_end'])
        
        if 'back_image' in items:
            q = q.where(TStoreOwner.back_image == items['back_image'])
        if 'back_image_start' in items:
            q = q.where(TStoreOwner.back_image >= items['back_image_start'])
        if 'back_image_end' in items:
            q = q.where(TStoreOwner.back_image <= items['back_image_end'])
        

        if 'id' in set_items:
            q = q.where(TStoreOwner.id.in_(set_items['id']))
        
        if 'name' in set_items:
            q = q.where(TStoreOwner.name.in_(set_items['name']))
        
        if 'phone' in set_items:
            q = q.where(TStoreOwner.phone.in_(set_items['phone']))
        
        if 'password' in set_items:
            q = q.where(TStoreOwner.password.in_(set_items['password']))
        
        if 'id_card' in set_items:
            q = q.where(TStoreOwner.id_card.in_(set_items['id_card']))
        
        if 'front_image' in set_items:
            q = q.where(TStoreOwner.front_image.in_(set_items['front_image']))
        
        if 'back_image' in set_items:
            q = q.where(TStoreOwner.back_image.in_(set_items['back_image']))
        

        if 'name' in search_items:
            q = q.where(TStoreOwner.name.like(search_items['name']))
        
        if 'phone' in search_items:
            q = q.where(TStoreOwner.phone.like(search_items['phone']))
        
        if 'password' in search_items:
            q = q.where(TStoreOwner.password.like(search_items['password']))
        
        if 'id_card' in search_items:
            q = q.where(TStoreOwner.id_card.like(search_items['id_card']))
        
        if 'front_image' in search_items:
            q = q.where(TStoreOwner.front_image.like(search_items['front_image']))
        
        if 'back_image' in search_items:
            q = q.where(TStoreOwner.back_image.like(search_items['back_image']))
        
    
        c = q.count()
        return c

    
def insert_store_state(item: CreateStoreState, db: Optional[SessionLocal] = None) -> SStoreState:
    data = model2dict(item)
    t = TStoreState(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SStoreState.parse_obj(t.__dict__)

    
def delete_store_state(store_state_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TStoreState).where(TStoreState.id == store_state_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TStoreState).where(TStoreState.id == store_state_id).delete()
        db.commit()

    
def update_store_state(item: SStoreState, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TStoreState).where(TStoreState.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TStoreState).where(TStoreState.id == item.id).update(data)
        db.commit()

    
def get_store_state(store_state_id: int) -> Optional[SStoreState]:
    with Dao() as db:
        t = db.query(TStoreState).where(TStoreState.id == store_state_id).first()
        if t:
            return SStoreState.parse_obj(t.__dict__)
        else:
            return None


def filter_store_state(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SStoreState]:
    with Dao() as db:
        q = db.query(TStoreState)


        if 'id' in items:
            q = q.where(TStoreState.id == items['id'])
        if 'id_start' in items:
            q = q.where(TStoreState.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TStoreState.id <= items['id_end'])
        
        if 'status' in items:
            q = q.where(TStoreState.status == items['status'])
        if 'status_start' in items:
            q = q.where(TStoreState.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TStoreState.status <= items['status_end'])
        

        if 'id' in set_items:
            q = q.where(TStoreState.id.in_(set_items['id']))
        
        if 'status' in set_items:
            q = q.where(TStoreState.status.in_(set_items['status']))
        

        if 'status' in search_items:
            q = q.where(TStoreState.status.like(search_items['status']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TStoreState.status.asc())
                orders.append(TStoreState.id.asc())
            elif val == 'desc':
                #orders.append(TStoreState.status.desc())
                orders.append(TStoreState.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_store_state_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SStoreState.parse_obj(t.__dict__) for t in t_store_state_list]


def filter_count_store_state(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TStoreState)


        if 'id' in items:
            q = q.where(TStoreState.id == items['id'])
        if 'id_start' in items:
            q = q.where(TStoreState.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TStoreState.id <= items['id_end'])
        
        if 'status' in items:
            q = q.where(TStoreState.status == items['status'])
        if 'status_start' in items:
            q = q.where(TStoreState.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TStoreState.status <= items['status_end'])
        

        if 'id' in set_items:
            q = q.where(TStoreState.id.in_(set_items['id']))
        
        if 'status' in set_items:
            q = q.where(TStoreState.status.in_(set_items['status']))
        

        if 'status' in search_items:
            q = q.where(TStoreState.status.like(search_items['status']))
        
    
        c = q.count()
        return c

    
def insert_supplier(item: CreateSupplier, db: Optional[SessionLocal] = None) -> SSupplier:
    data = model2dict(item)
    t = TSupplier(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SSupplier.parse_obj(t.__dict__)

    
def delete_supplier(supplier_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TSupplier).where(TSupplier.id == supplier_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSupplier).where(TSupplier.id == supplier_id).delete()
        db.commit()

    
def update_supplier(item: SSupplier, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TSupplier).where(TSupplier.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSupplier).where(TSupplier.id == item.id).update(data)
        db.commit()

    
def get_supplier(supplier_id: int) -> Optional[SSupplier]:
    with Dao() as db:
        t = db.query(TSupplier).where(TSupplier.id == supplier_id).first()
        if t:
            return SSupplier.parse_obj(t.__dict__)
        else:
            return None


def filter_supplier(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SSupplier]:
    with Dao() as db:
        q = db.query(TSupplier)


        if 'id' in items:
            q = q.where(TSupplier.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSupplier.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSupplier.id <= items['id_end'])
        
        if 'name' in items:
            q = q.where(TSupplier.name == items['name'])
        if 'name_start' in items:
            q = q.where(TSupplier.name >= items['name_start'])
        if 'name_end' in items:
            q = q.where(TSupplier.name <= items['name_end'])
        
        if 'phone' in items:
            q = q.where(TSupplier.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TSupplier.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TSupplier.phone <= items['phone_end'])
        
        if 'province' in items:
            q = q.where(TSupplier.province == items['province'])
        if 'province_start' in items:
            q = q.where(TSupplier.province >= items['province_start'])
        if 'province_end' in items:
            q = q.where(TSupplier.province <= items['province_end'])
        
        if 'city' in items:
            q = q.where(TSupplier.city == items['city'])
        if 'city_start' in items:
            q = q.where(TSupplier.city >= items['city_start'])
        if 'city_end' in items:
            q = q.where(TSupplier.city <= items['city_end'])
        
        if 'area' in items:
            q = q.where(TSupplier.area == items['area'])
        if 'area_start' in items:
            q = q.where(TSupplier.area >= items['area_start'])
        if 'area_end' in items:
            q = q.where(TSupplier.area <= items['area_end'])
        
        if 'street' in items:
            q = q.where(TSupplier.street == items['street'])
        if 'street_start' in items:
            q = q.where(TSupplier.street >= items['street_start'])
        if 'street_end' in items:
            q = q.where(TSupplier.street <= items['street_end'])
        
        if 'address' in items:
            q = q.where(TSupplier.address == items['address'])
        if 'address_start' in items:
            q = q.where(TSupplier.address >= items['address_start'])
        if 'address_end' in items:
            q = q.where(TSupplier.address <= items['address_end'])
        
        if 'status' in items:
            q = q.where(TSupplier.status == items['status'])
        if 'status_start' in items:
            q = q.where(TSupplier.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TSupplier.status <= items['status_end'])
        
        if 'owner' in items:
            q = q.where(TSupplier.owner == items['owner'])
        if 'owner_start' in items:
            q = q.where(TSupplier.owner >= items['owner_start'])
        if 'owner_end' in items:
            q = q.where(TSupplier.owner <= items['owner_end'])
        
        if 'recommender_id' in items:
            q = q.where(TSupplier.recommender_id == items['recommender_id'])
        if 'recommender_id_start' in items:
            q = q.where(TSupplier.recommender_id >= items['recommender_id_start'])
        if 'recommender_id_end' in items:
            q = q.where(TSupplier.recommender_id <= items['recommender_id_end'])
        
        if 'register_time' in items:
            q = q.where(TSupplier.register_time == items['register_time'])
        if 'register_time_start' in items:
            q = q.where(TSupplier.register_time >= items['register_time_start'])
        if 'register_time_end' in items:
            q = q.where(TSupplier.register_time <= items['register_time_end'])
        
        if 'type' in items:
            q = q.where(TSupplier.type == items['type'])
        if 'type_start' in items:
            q = q.where(TSupplier.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TSupplier.type <= items['type_end'])
        
        if 'expired_time' in items:
            q = q.where(TSupplier.expired_time == items['expired_time'])
        if 'expired_time_start' in items:
            q = q.where(TSupplier.expired_time >= items['expired_time_start'])
        if 'expired_time_end' in items:
            q = q.where(TSupplier.expired_time <= items['expired_time_end'])
        
        if 'open_time' in items:
            q = q.where(TSupplier.open_time == items['open_time'])
        if 'open_time_start' in items:
            q = q.where(TSupplier.open_time >= items['open_time_start'])
        if 'open_time_end' in items:
            q = q.where(TSupplier.open_time <= items['open_time_end'])
        
        if 'close_time' in items:
            q = q.where(TSupplier.close_time == items['close_time'])
        if 'close_time_start' in items:
            q = q.where(TSupplier.close_time >= items['close_time_start'])
        if 'close_time_end' in items:
            q = q.where(TSupplier.close_time <= items['close_time_end'])
        
        if 'image' in items:
            q = q.where(TSupplier.image == items['image'])
        if 'image_start' in items:
            q = q.where(TSupplier.image >= items['image_start'])
        if 'image_end' in items:
            q = q.where(TSupplier.image <= items['image_end'])
        
        if 'owner_id' in items:
            q = q.where(TSupplier.owner_id == items['owner_id'])
        if 'owner_id_start' in items:
            q = q.where(TSupplier.owner_id >= items['owner_id_start'])
        if 'owner_id_end' in items:
            q = q.where(TSupplier.owner_id <= items['owner_id_end'])
        
        if 'category' in items:
            q = q.where(TSupplier.category == items['category'])
        if 'category_start' in items:
            q = q.where(TSupplier.category >= items['category_start'])
        if 'category_end' in items:
            q = q.where(TSupplier.category <= items['category_end'])
        
        if 'balance' in items:
            q = q.where(TSupplier.balance == items['balance'])
        if 'balance_start' in items:
            q = q.where(TSupplier.balance >= items['balance_start'])
        if 'balance_end' in items:
            q = q.where(TSupplier.balance <= items['balance_end'])
        
        if 'reject_reason' in items:
            q = q.where(TSupplier.reject_reason == items['reject_reason'])
        if 'reject_reason_start' in items:
            q = q.where(TSupplier.reject_reason >= items['reject_reason_start'])
        if 'reject_reason_end' in items:
            q = q.where(TSupplier.reject_reason <= items['reject_reason_end'])
        
        if 'reject_admin_id' in items:
            q = q.where(TSupplier.reject_admin_id == items['reject_admin_id'])
        if 'reject_admin_id_start' in items:
            q = q.where(TSupplier.reject_admin_id >= items['reject_admin_id_start'])
        if 'reject_admin_id_end' in items:
            q = q.where(TSupplier.reject_admin_id <= items['reject_admin_id_end'])
        
        if 'reject_time' in items:
            q = q.where(TSupplier.reject_time == items['reject_time'])
        if 'reject_time_start' in items:
            q = q.where(TSupplier.reject_time >= items['reject_time_start'])
        if 'reject_time_end' in items:
            q = q.where(TSupplier.reject_time <= items['reject_time_end'])
        
        if 'company_name' in items:
            q = q.where(TSupplier.company_name == items['company_name'])
        if 'company_name_start' in items:
            q = q.where(TSupplier.company_name >= items['company_name_start'])
        if 'company_name_end' in items:
            q = q.where(TSupplier.company_name <= items['company_name_end'])
        

        if 'id' in set_items:
            q = q.where(TSupplier.id.in_(set_items['id']))
        
        if 'name' in set_items:
            q = q.where(TSupplier.name.in_(set_items['name']))
        
        if 'phone' in set_items:
            q = q.where(TSupplier.phone.in_(set_items['phone']))
        
        if 'province' in set_items:
            q = q.where(TSupplier.province.in_(set_items['province']))
        
        if 'city' in set_items:
            q = q.where(TSupplier.city.in_(set_items['city']))
        
        if 'area' in set_items:
            q = q.where(TSupplier.area.in_(set_items['area']))
        
        if 'street' in set_items:
            q = q.where(TSupplier.street.in_(set_items['street']))
        
        if 'address' in set_items:
            q = q.where(TSupplier.address.in_(set_items['address']))
        
        if 'status' in set_items:
            q = q.where(TSupplier.status.in_(set_items['status']))
        
        if 'owner' in set_items:
            q = q.where(TSupplier.owner.in_(set_items['owner']))
        
        if 'recommender_id' in set_items:
            q = q.where(TSupplier.recommender_id.in_(set_items['recommender_id']))
        
        if 'register_time' in set_items:
            q = q.where(TSupplier.register_time.in_(set_items['register_time']))
        
        if 'type' in set_items:
            q = q.where(TSupplier.type.in_(set_items['type']))
        
        if 'expired_time' in set_items:
            q = q.where(TSupplier.expired_time.in_(set_items['expired_time']))
        
        if 'open_time' in set_items:
            q = q.where(TSupplier.open_time.in_(set_items['open_time']))
        
        if 'close_time' in set_items:
            q = q.where(TSupplier.close_time.in_(set_items['close_time']))
        
        if 'image' in set_items:
            q = q.where(TSupplier.image.in_(set_items['image']))
        
        if 'owner_id' in set_items:
            q = q.where(TSupplier.owner_id.in_(set_items['owner_id']))
        
        if 'category' in set_items:
            q = q.where(TSupplier.category.in_(set_items['category']))
        
        if 'balance' in set_items:
            q = q.where(TSupplier.balance.in_(set_items['balance']))
        
        if 'reject_reason' in set_items:
            q = q.where(TSupplier.reject_reason.in_(set_items['reject_reason']))
        
        if 'reject_admin_id' in set_items:
            q = q.where(TSupplier.reject_admin_id.in_(set_items['reject_admin_id']))
        
        if 'reject_time' in set_items:
            q = q.where(TSupplier.reject_time.in_(set_items['reject_time']))
        
        if 'company_name' in set_items:
            q = q.where(TSupplier.company_name.in_(set_items['company_name']))
        

        if 'name' in search_items:
            q = q.where(TSupplier.name.like(search_items['name']))
        
        if 'phone' in search_items:
            q = q.where(TSupplier.phone.like(search_items['phone']))
        
        if 'province' in search_items:
            q = q.where(TSupplier.province.like(search_items['province']))
        
        if 'city' in search_items:
            q = q.where(TSupplier.city.like(search_items['city']))
        
        if 'area' in search_items:
            q = q.where(TSupplier.area.like(search_items['area']))
        
        if 'street' in search_items:
            q = q.where(TSupplier.street.like(search_items['street']))
        
        if 'address' in search_items:
            q = q.where(TSupplier.address.like(search_items['address']))
        
        if 'owner' in search_items:
            q = q.where(TSupplier.owner.like(search_items['owner']))
        
        if 'image' in search_items:
            q = q.where(TSupplier.image.like(search_items['image']))
        
        if 'reject_reason' in search_items:
            q = q.where(TSupplier.reject_reason.like(search_items['reject_reason']))
        
        if 'company_name' in search_items:
            q = q.where(TSupplier.company_name.like(search_items['company_name']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TSupplier.company_name.asc())
                orders.append(TSupplier.id.asc())
            elif val == 'desc':
                #orders.append(TSupplier.company_name.desc())
                orders.append(TSupplier.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_supplier_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SSupplier.parse_obj(t.__dict__) for t in t_supplier_list]


def filter_count_supplier(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TSupplier)


        if 'id' in items:
            q = q.where(TSupplier.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSupplier.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSupplier.id <= items['id_end'])
        
        if 'name' in items:
            q = q.where(TSupplier.name == items['name'])
        if 'name_start' in items:
            q = q.where(TSupplier.name >= items['name_start'])
        if 'name_end' in items:
            q = q.where(TSupplier.name <= items['name_end'])
        
        if 'phone' in items:
            q = q.where(TSupplier.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TSupplier.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TSupplier.phone <= items['phone_end'])
        
        if 'province' in items:
            q = q.where(TSupplier.province == items['province'])
        if 'province_start' in items:
            q = q.where(TSupplier.province >= items['province_start'])
        if 'province_end' in items:
            q = q.where(TSupplier.province <= items['province_end'])
        
        if 'city' in items:
            q = q.where(TSupplier.city == items['city'])
        if 'city_start' in items:
            q = q.where(TSupplier.city >= items['city_start'])
        if 'city_end' in items:
            q = q.where(TSupplier.city <= items['city_end'])
        
        if 'area' in items:
            q = q.where(TSupplier.area == items['area'])
        if 'area_start' in items:
            q = q.where(TSupplier.area >= items['area_start'])
        if 'area_end' in items:
            q = q.where(TSupplier.area <= items['area_end'])
        
        if 'street' in items:
            q = q.where(TSupplier.street == items['street'])
        if 'street_start' in items:
            q = q.where(TSupplier.street >= items['street_start'])
        if 'street_end' in items:
            q = q.where(TSupplier.street <= items['street_end'])
        
        if 'address' in items:
            q = q.where(TSupplier.address == items['address'])
        if 'address_start' in items:
            q = q.where(TSupplier.address >= items['address_start'])
        if 'address_end' in items:
            q = q.where(TSupplier.address <= items['address_end'])
        
        if 'status' in items:
            q = q.where(TSupplier.status == items['status'])
        if 'status_start' in items:
            q = q.where(TSupplier.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TSupplier.status <= items['status_end'])
        
        if 'owner' in items:
            q = q.where(TSupplier.owner == items['owner'])
        if 'owner_start' in items:
            q = q.where(TSupplier.owner >= items['owner_start'])
        if 'owner_end' in items:
            q = q.where(TSupplier.owner <= items['owner_end'])
        
        if 'recommender_id' in items:
            q = q.where(TSupplier.recommender_id == items['recommender_id'])
        if 'recommender_id_start' in items:
            q = q.where(TSupplier.recommender_id >= items['recommender_id_start'])
        if 'recommender_id_end' in items:
            q = q.where(TSupplier.recommender_id <= items['recommender_id_end'])
        
        if 'register_time' in items:
            q = q.where(TSupplier.register_time == items['register_time'])
        if 'register_time_start' in items:
            q = q.where(TSupplier.register_time >= items['register_time_start'])
        if 'register_time_end' in items:
            q = q.where(TSupplier.register_time <= items['register_time_end'])
        
        if 'type' in items:
            q = q.where(TSupplier.type == items['type'])
        if 'type_start' in items:
            q = q.where(TSupplier.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TSupplier.type <= items['type_end'])
        
        if 'expired_time' in items:
            q = q.where(TSupplier.expired_time == items['expired_time'])
        if 'expired_time_start' in items:
            q = q.where(TSupplier.expired_time >= items['expired_time_start'])
        if 'expired_time_end' in items:
            q = q.where(TSupplier.expired_time <= items['expired_time_end'])
        
        if 'open_time' in items:
            q = q.where(TSupplier.open_time == items['open_time'])
        if 'open_time_start' in items:
            q = q.where(TSupplier.open_time >= items['open_time_start'])
        if 'open_time_end' in items:
            q = q.where(TSupplier.open_time <= items['open_time_end'])
        
        if 'close_time' in items:
            q = q.where(TSupplier.close_time == items['close_time'])
        if 'close_time_start' in items:
            q = q.where(TSupplier.close_time >= items['close_time_start'])
        if 'close_time_end' in items:
            q = q.where(TSupplier.close_time <= items['close_time_end'])
        
        if 'image' in items:
            q = q.where(TSupplier.image == items['image'])
        if 'image_start' in items:
            q = q.where(TSupplier.image >= items['image_start'])
        if 'image_end' in items:
            q = q.where(TSupplier.image <= items['image_end'])
        
        if 'owner_id' in items:
            q = q.where(TSupplier.owner_id == items['owner_id'])
        if 'owner_id_start' in items:
            q = q.where(TSupplier.owner_id >= items['owner_id_start'])
        if 'owner_id_end' in items:
            q = q.where(TSupplier.owner_id <= items['owner_id_end'])
        
        if 'category' in items:
            q = q.where(TSupplier.category == items['category'])
        if 'category_start' in items:
            q = q.where(TSupplier.category >= items['category_start'])
        if 'category_end' in items:
            q = q.where(TSupplier.category <= items['category_end'])
        
        if 'balance' in items:
            q = q.where(TSupplier.balance == items['balance'])
        if 'balance_start' in items:
            q = q.where(TSupplier.balance >= items['balance_start'])
        if 'balance_end' in items:
            q = q.where(TSupplier.balance <= items['balance_end'])
        
        if 'reject_reason' in items:
            q = q.where(TSupplier.reject_reason == items['reject_reason'])
        if 'reject_reason_start' in items:
            q = q.where(TSupplier.reject_reason >= items['reject_reason_start'])
        if 'reject_reason_end' in items:
            q = q.where(TSupplier.reject_reason <= items['reject_reason_end'])
        
        if 'reject_admin_id' in items:
            q = q.where(TSupplier.reject_admin_id == items['reject_admin_id'])
        if 'reject_admin_id_start' in items:
            q = q.where(TSupplier.reject_admin_id >= items['reject_admin_id_start'])
        if 'reject_admin_id_end' in items:
            q = q.where(TSupplier.reject_admin_id <= items['reject_admin_id_end'])
        
        if 'reject_time' in items:
            q = q.where(TSupplier.reject_time == items['reject_time'])
        if 'reject_time_start' in items:
            q = q.where(TSupplier.reject_time >= items['reject_time_start'])
        if 'reject_time_end' in items:
            q = q.where(TSupplier.reject_time <= items['reject_time_end'])
        
        if 'company_name' in items:
            q = q.where(TSupplier.company_name == items['company_name'])
        if 'company_name_start' in items:
            q = q.where(TSupplier.company_name >= items['company_name_start'])
        if 'company_name_end' in items:
            q = q.where(TSupplier.company_name <= items['company_name_end'])
        

        if 'id' in set_items:
            q = q.where(TSupplier.id.in_(set_items['id']))
        
        if 'name' in set_items:
            q = q.where(TSupplier.name.in_(set_items['name']))
        
        if 'phone' in set_items:
            q = q.where(TSupplier.phone.in_(set_items['phone']))
        
        if 'province' in set_items:
            q = q.where(TSupplier.province.in_(set_items['province']))
        
        if 'city' in set_items:
            q = q.where(TSupplier.city.in_(set_items['city']))
        
        if 'area' in set_items:
            q = q.where(TSupplier.area.in_(set_items['area']))
        
        if 'street' in set_items:
            q = q.where(TSupplier.street.in_(set_items['street']))
        
        if 'address' in set_items:
            q = q.where(TSupplier.address.in_(set_items['address']))
        
        if 'status' in set_items:
            q = q.where(TSupplier.status.in_(set_items['status']))
        
        if 'owner' in set_items:
            q = q.where(TSupplier.owner.in_(set_items['owner']))
        
        if 'recommender_id' in set_items:
            q = q.where(TSupplier.recommender_id.in_(set_items['recommender_id']))
        
        if 'register_time' in set_items:
            q = q.where(TSupplier.register_time.in_(set_items['register_time']))
        
        if 'type' in set_items:
            q = q.where(TSupplier.type.in_(set_items['type']))
        
        if 'expired_time' in set_items:
            q = q.where(TSupplier.expired_time.in_(set_items['expired_time']))
        
        if 'open_time' in set_items:
            q = q.where(TSupplier.open_time.in_(set_items['open_time']))
        
        if 'close_time' in set_items:
            q = q.where(TSupplier.close_time.in_(set_items['close_time']))
        
        if 'image' in set_items:
            q = q.where(TSupplier.image.in_(set_items['image']))
        
        if 'owner_id' in set_items:
            q = q.where(TSupplier.owner_id.in_(set_items['owner_id']))
        
        if 'category' in set_items:
            q = q.where(TSupplier.category.in_(set_items['category']))
        
        if 'balance' in set_items:
            q = q.where(TSupplier.balance.in_(set_items['balance']))
        
        if 'reject_reason' in set_items:
            q = q.where(TSupplier.reject_reason.in_(set_items['reject_reason']))
        
        if 'reject_admin_id' in set_items:
            q = q.where(TSupplier.reject_admin_id.in_(set_items['reject_admin_id']))
        
        if 'reject_time' in set_items:
            q = q.where(TSupplier.reject_time.in_(set_items['reject_time']))
        
        if 'company_name' in set_items:
            q = q.where(TSupplier.company_name.in_(set_items['company_name']))
        

        if 'name' in search_items:
            q = q.where(TSupplier.name.like(search_items['name']))
        
        if 'phone' in search_items:
            q = q.where(TSupplier.phone.like(search_items['phone']))
        
        if 'province' in search_items:
            q = q.where(TSupplier.province.like(search_items['province']))
        
        if 'city' in search_items:
            q = q.where(TSupplier.city.like(search_items['city']))
        
        if 'area' in search_items:
            q = q.where(TSupplier.area.like(search_items['area']))
        
        if 'street' in search_items:
            q = q.where(TSupplier.street.like(search_items['street']))
        
        if 'address' in search_items:
            q = q.where(TSupplier.address.like(search_items['address']))
        
        if 'owner' in search_items:
            q = q.where(TSupplier.owner.like(search_items['owner']))
        
        if 'image' in search_items:
            q = q.where(TSupplier.image.like(search_items['image']))
        
        if 'reject_reason' in search_items:
            q = q.where(TSupplier.reject_reason.like(search_items['reject_reason']))
        
        if 'company_name' in search_items:
            q = q.where(TSupplier.company_name.like(search_items['company_name']))
        
    
        c = q.count()
        return c

    
def insert_supplier_amount(item: CreateSupplierAmount, db: Optional[SessionLocal] = None) -> SSupplierAmount:
    data = model2dict(item)
    t = TSupplierAmount(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SSupplierAmount.parse_obj(t.__dict__)

    
def delete_supplier_amount(supplier_amount_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TSupplierAmount).where(TSupplierAmount.id == supplier_amount_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSupplierAmount).where(TSupplierAmount.id == supplier_amount_id).delete()
        db.commit()

    
def update_supplier_amount(item: SSupplierAmount, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TSupplierAmount).where(TSupplierAmount.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSupplierAmount).where(TSupplierAmount.id == item.id).update(data)
        db.commit()

    
def get_supplier_amount(supplier_amount_id: int) -> Optional[SSupplierAmount]:
    with Dao() as db:
        t = db.query(TSupplierAmount).where(TSupplierAmount.id == supplier_amount_id).first()
        if t:
            return SSupplierAmount.parse_obj(t.__dict__)
        else:
            return None


def filter_supplier_amount(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SSupplierAmount]:
    with Dao() as db:
        q = db.query(TSupplierAmount)


        if 'id' in items:
            q = q.where(TSupplierAmount.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSupplierAmount.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSupplierAmount.id <= items['id_end'])
        
        if 'type' in items:
            q = q.where(TSupplierAmount.type == items['type'])
        if 'type_start' in items:
            q = q.where(TSupplierAmount.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TSupplierAmount.type <= items['type_end'])
        
        if 'change' in items:
            q = q.where(TSupplierAmount.change == items['change'])
        if 'change_start' in items:
            q = q.where(TSupplierAmount.change >= items['change_start'])
        if 'change_end' in items:
            q = q.where(TSupplierAmount.change <= items['change_end'])
        
        if 'amount' in items:
            q = q.where(TSupplierAmount.amount == items['amount'])
        if 'amount_start' in items:
            q = q.where(TSupplierAmount.amount >= items['amount_start'])
        if 'amount_end' in items:
            q = q.where(TSupplierAmount.amount <= items['amount_end'])
        
        if 'create_time' in items:
            q = q.where(TSupplierAmount.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TSupplierAmount.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TSupplierAmount.create_time <= items['create_time_end'])
        
        if 'supplier_id' in items:
            q = q.where(TSupplierAmount.supplier_id == items['supplier_id'])
        if 'supplier_id_start' in items:
            q = q.where(TSupplierAmount.supplier_id >= items['supplier_id_start'])
        if 'supplier_id_end' in items:
            q = q.where(TSupplierAmount.supplier_id <= items['supplier_id_end'])
        
        if 'order_id' in items:
            q = q.where(TSupplierAmount.order_id == items['order_id'])
        if 'order_id_start' in items:
            q = q.where(TSupplierAmount.order_id >= items['order_id_start'])
        if 'order_id_end' in items:
            q = q.where(TSupplierAmount.order_id <= items['order_id_end'])
        
        if 'description' in items:
            q = q.where(TSupplierAmount.description == items['description'])
        if 'description_start' in items:
            q = q.where(TSupplierAmount.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TSupplierAmount.description <= items['description_end'])
        

        if 'id' in set_items:
            q = q.where(TSupplierAmount.id.in_(set_items['id']))
        
        if 'type' in set_items:
            q = q.where(TSupplierAmount.type.in_(set_items['type']))
        
        if 'change' in set_items:
            q = q.where(TSupplierAmount.change.in_(set_items['change']))
        
        if 'amount' in set_items:
            q = q.where(TSupplierAmount.amount.in_(set_items['amount']))
        
        if 'create_time' in set_items:
            q = q.where(TSupplierAmount.create_time.in_(set_items['create_time']))
        
        if 'supplier_id' in set_items:
            q = q.where(TSupplierAmount.supplier_id.in_(set_items['supplier_id']))
        
        if 'order_id' in set_items:
            q = q.where(TSupplierAmount.order_id.in_(set_items['order_id']))
        
        if 'description' in set_items:
            q = q.where(TSupplierAmount.description.in_(set_items['description']))
        

        if 'description' in search_items:
            q = q.where(TSupplierAmount.description.like(search_items['description']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TSupplierAmount.description.asc())
                orders.append(TSupplierAmount.id.asc())
            elif val == 'desc':
                #orders.append(TSupplierAmount.description.desc())
                orders.append(TSupplierAmount.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_supplier_amount_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SSupplierAmount.parse_obj(t.__dict__) for t in t_supplier_amount_list]


def filter_count_supplier_amount(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TSupplierAmount)


        if 'id' in items:
            q = q.where(TSupplierAmount.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSupplierAmount.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSupplierAmount.id <= items['id_end'])
        
        if 'type' in items:
            q = q.where(TSupplierAmount.type == items['type'])
        if 'type_start' in items:
            q = q.where(TSupplierAmount.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TSupplierAmount.type <= items['type_end'])
        
        if 'change' in items:
            q = q.where(TSupplierAmount.change == items['change'])
        if 'change_start' in items:
            q = q.where(TSupplierAmount.change >= items['change_start'])
        if 'change_end' in items:
            q = q.where(TSupplierAmount.change <= items['change_end'])
        
        if 'amount' in items:
            q = q.where(TSupplierAmount.amount == items['amount'])
        if 'amount_start' in items:
            q = q.where(TSupplierAmount.amount >= items['amount_start'])
        if 'amount_end' in items:
            q = q.where(TSupplierAmount.amount <= items['amount_end'])
        
        if 'create_time' in items:
            q = q.where(TSupplierAmount.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TSupplierAmount.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TSupplierAmount.create_time <= items['create_time_end'])
        
        if 'supplier_id' in items:
            q = q.where(TSupplierAmount.supplier_id == items['supplier_id'])
        if 'supplier_id_start' in items:
            q = q.where(TSupplierAmount.supplier_id >= items['supplier_id_start'])
        if 'supplier_id_end' in items:
            q = q.where(TSupplierAmount.supplier_id <= items['supplier_id_end'])
        
        if 'order_id' in items:
            q = q.where(TSupplierAmount.order_id == items['order_id'])
        if 'order_id_start' in items:
            q = q.where(TSupplierAmount.order_id >= items['order_id_start'])
        if 'order_id_end' in items:
            q = q.where(TSupplierAmount.order_id <= items['order_id_end'])
        
        if 'description' in items:
            q = q.where(TSupplierAmount.description == items['description'])
        if 'description_start' in items:
            q = q.where(TSupplierAmount.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TSupplierAmount.description <= items['description_end'])
        

        if 'id' in set_items:
            q = q.where(TSupplierAmount.id.in_(set_items['id']))
        
        if 'type' in set_items:
            q = q.where(TSupplierAmount.type.in_(set_items['type']))
        
        if 'change' in set_items:
            q = q.where(TSupplierAmount.change.in_(set_items['change']))
        
        if 'amount' in set_items:
            q = q.where(TSupplierAmount.amount.in_(set_items['amount']))
        
        if 'create_time' in set_items:
            q = q.where(TSupplierAmount.create_time.in_(set_items['create_time']))
        
        if 'supplier_id' in set_items:
            q = q.where(TSupplierAmount.supplier_id.in_(set_items['supplier_id']))
        
        if 'order_id' in set_items:
            q = q.where(TSupplierAmount.order_id.in_(set_items['order_id']))
        
        if 'description' in set_items:
            q = q.where(TSupplierAmount.description.in_(set_items['description']))
        

        if 'description' in search_items:
            q = q.where(TSupplierAmount.description.like(search_items['description']))
        
    
        c = q.count()
        return c

    
def insert_supplier_change_type(item: CreateSupplierChangeType, db: Optional[SessionLocal] = None) -> SSupplierChangeType:
    data = model2dict(item)
    t = TSupplierChangeType(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SSupplierChangeType.parse_obj(t.__dict__)

    
def delete_supplier_change_type(supplier_change_type_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TSupplierChangeType).where(TSupplierChangeType.id == supplier_change_type_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSupplierChangeType).where(TSupplierChangeType.id == supplier_change_type_id).delete()
        db.commit()

    
def update_supplier_change_type(item: SSupplierChangeType, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TSupplierChangeType).where(TSupplierChangeType.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSupplierChangeType).where(TSupplierChangeType.id == item.id).update(data)
        db.commit()

    
def get_supplier_change_type(supplier_change_type_id: int) -> Optional[SSupplierChangeType]:
    with Dao() as db:
        t = db.query(TSupplierChangeType).where(TSupplierChangeType.id == supplier_change_type_id).first()
        if t:
            return SSupplierChangeType.parse_obj(t.__dict__)
        else:
            return None


def filter_supplier_change_type(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SSupplierChangeType]:
    with Dao() as db:
        q = db.query(TSupplierChangeType)


        if 'id' in items:
            q = q.where(TSupplierChangeType.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSupplierChangeType.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSupplierChangeType.id <= items['id_end'])
        
        if 'type' in items:
            q = q.where(TSupplierChangeType.type == items['type'])
        if 'type_start' in items:
            q = q.where(TSupplierChangeType.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TSupplierChangeType.type <= items['type_end'])
        

        if 'id' in set_items:
            q = q.where(TSupplierChangeType.id.in_(set_items['id']))
        
        if 'type' in set_items:
            q = q.where(TSupplierChangeType.type.in_(set_items['type']))
        

        if 'type' in search_items:
            q = q.where(TSupplierChangeType.type.like(search_items['type']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TSupplierChangeType.type.asc())
                orders.append(TSupplierChangeType.id.asc())
            elif val == 'desc':
                #orders.append(TSupplierChangeType.type.desc())
                orders.append(TSupplierChangeType.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_supplier_change_type_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SSupplierChangeType.parse_obj(t.__dict__) for t in t_supplier_change_type_list]


def filter_count_supplier_change_type(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TSupplierChangeType)


        if 'id' in items:
            q = q.where(TSupplierChangeType.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSupplierChangeType.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSupplierChangeType.id <= items['id_end'])
        
        if 'type' in items:
            q = q.where(TSupplierChangeType.type == items['type'])
        if 'type_start' in items:
            q = q.where(TSupplierChangeType.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TSupplierChangeType.type <= items['type_end'])
        

        if 'id' in set_items:
            q = q.where(TSupplierChangeType.id.in_(set_items['id']))
        
        if 'type' in set_items:
            q = q.where(TSupplierChangeType.type.in_(set_items['type']))
        

        if 'type' in search_items:
            q = q.where(TSupplierChangeType.type.like(search_items['type']))
        
    
        c = q.count()
        return c

    
def insert_supplier_income(item: CreateSupplierIncome, db: Optional[SessionLocal] = None) -> SSupplierIncome:
    data = model2dict(item)
    t = TSupplierIncome(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SSupplierIncome.parse_obj(t.__dict__)

    
def delete_supplier_income(supplier_income_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TSupplierIncome).where(TSupplierIncome.id == supplier_income_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSupplierIncome).where(TSupplierIncome.id == supplier_income_id).delete()
        db.commit()

    
def update_supplier_income(item: SSupplierIncome, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TSupplierIncome).where(TSupplierIncome.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSupplierIncome).where(TSupplierIncome.id == item.id).update(data)
        db.commit()

    
def get_supplier_income(supplier_income_id: int) -> Optional[SSupplierIncome]:
    with Dao() as db:
        t = db.query(TSupplierIncome).where(TSupplierIncome.id == supplier_income_id).first()
        if t:
            return SSupplierIncome.parse_obj(t.__dict__)
        else:
            return None


def filter_supplier_income(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SSupplierIncome]:
    with Dao() as db:
        q = db.query(TSupplierIncome)


        if 'id' in items:
            q = q.where(TSupplierIncome.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSupplierIncome.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSupplierIncome.id <= items['id_end'])
        
        if 'supplier_id' in items:
            q = q.where(TSupplierIncome.supplier_id == items['supplier_id'])
        if 'supplier_id_start' in items:
            q = q.where(TSupplierIncome.supplier_id >= items['supplier_id_start'])
        if 'supplier_id_end' in items:
            q = q.where(TSupplierIncome.supplier_id <= items['supplier_id_end'])
        
        if 'change' in items:
            q = q.where(TSupplierIncome.change == items['change'])
        if 'change_start' in items:
            q = q.where(TSupplierIncome.change >= items['change_start'])
        if 'change_end' in items:
            q = q.where(TSupplierIncome.change <= items['change_end'])
        
        if 'balance' in items:
            q = q.where(TSupplierIncome.balance == items['balance'])
        if 'balance_start' in items:
            q = q.where(TSupplierIncome.balance >= items['balance_start'])
        if 'balance_end' in items:
            q = q.where(TSupplierIncome.balance <= items['balance_end'])
        
        if 'type' in items:
            q = q.where(TSupplierIncome.type == items['type'])
        if 'type_start' in items:
            q = q.where(TSupplierIncome.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TSupplierIncome.type <= items['type_end'])
        
        if 'description' in items:
            q = q.where(TSupplierIncome.description == items['description'])
        if 'description_start' in items:
            q = q.where(TSupplierIncome.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TSupplierIncome.description <= items['description_end'])
        
        if 'create_time' in items:
            q = q.where(TSupplierIncome.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TSupplierIncome.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TSupplierIncome.create_time <= items['create_time_end'])
        
        if 'user_withdraw_id' in items:
            q = q.where(TSupplierIncome.user_withdraw_id == items['user_withdraw_id'])
        if 'user_withdraw_id_start' in items:
            q = q.where(TSupplierIncome.user_withdraw_id >= items['user_withdraw_id_start'])
        if 'user_withdraw_id_end' in items:
            q = q.where(TSupplierIncome.user_withdraw_id <= items['user_withdraw_id_end'])
        
        if 'operator_id' in items:
            q = q.where(TSupplierIncome.operator_id == items['operator_id'])
        if 'operator_id_start' in items:
            q = q.where(TSupplierIncome.operator_id >= items['operator_id_start'])
        if 'operator_id_end' in items:
            q = q.where(TSupplierIncome.operator_id <= items['operator_id_end'])
        
        if 'out_trade_no' in items:
            q = q.where(TSupplierIncome.out_trade_no == items['out_trade_no'])
        if 'out_trade_no_start' in items:
            q = q.where(TSupplierIncome.out_trade_no >= items['out_trade_no_start'])
        if 'out_trade_no_end' in items:
            q = q.where(TSupplierIncome.out_trade_no <= items['out_trade_no_end'])
        

        if 'id' in set_items:
            q = q.where(TSupplierIncome.id.in_(set_items['id']))
        
        if 'supplier_id' in set_items:
            q = q.where(TSupplierIncome.supplier_id.in_(set_items['supplier_id']))
        
        if 'change' in set_items:
            q = q.where(TSupplierIncome.change.in_(set_items['change']))
        
        if 'balance' in set_items:
            q = q.where(TSupplierIncome.balance.in_(set_items['balance']))
        
        if 'type' in set_items:
            q = q.where(TSupplierIncome.type.in_(set_items['type']))
        
        if 'description' in set_items:
            q = q.where(TSupplierIncome.description.in_(set_items['description']))
        
        if 'create_time' in set_items:
            q = q.where(TSupplierIncome.create_time.in_(set_items['create_time']))
        
        if 'user_withdraw_id' in set_items:
            q = q.where(TSupplierIncome.user_withdraw_id.in_(set_items['user_withdraw_id']))
        
        if 'operator_id' in set_items:
            q = q.where(TSupplierIncome.operator_id.in_(set_items['operator_id']))
        
        if 'out_trade_no' in set_items:
            q = q.where(TSupplierIncome.out_trade_no.in_(set_items['out_trade_no']))
        

        if 'type' in search_items:
            q = q.where(TSupplierIncome.type.like(search_items['type']))
        
        if 'description' in search_items:
            q = q.where(TSupplierIncome.description.like(search_items['description']))
        
        if 'out_trade_no' in search_items:
            q = q.where(TSupplierIncome.out_trade_no.like(search_items['out_trade_no']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TSupplierIncome.out_trade_no.asc())
                orders.append(TSupplierIncome.id.asc())
            elif val == 'desc':
                #orders.append(TSupplierIncome.out_trade_no.desc())
                orders.append(TSupplierIncome.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_supplier_income_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SSupplierIncome.parse_obj(t.__dict__) for t in t_supplier_income_list]


def filter_count_supplier_income(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TSupplierIncome)


        if 'id' in items:
            q = q.where(TSupplierIncome.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSupplierIncome.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSupplierIncome.id <= items['id_end'])
        
        if 'supplier_id' in items:
            q = q.where(TSupplierIncome.supplier_id == items['supplier_id'])
        if 'supplier_id_start' in items:
            q = q.where(TSupplierIncome.supplier_id >= items['supplier_id_start'])
        if 'supplier_id_end' in items:
            q = q.where(TSupplierIncome.supplier_id <= items['supplier_id_end'])
        
        if 'change' in items:
            q = q.where(TSupplierIncome.change == items['change'])
        if 'change_start' in items:
            q = q.where(TSupplierIncome.change >= items['change_start'])
        if 'change_end' in items:
            q = q.where(TSupplierIncome.change <= items['change_end'])
        
        if 'balance' in items:
            q = q.where(TSupplierIncome.balance == items['balance'])
        if 'balance_start' in items:
            q = q.where(TSupplierIncome.balance >= items['balance_start'])
        if 'balance_end' in items:
            q = q.where(TSupplierIncome.balance <= items['balance_end'])
        
        if 'type' in items:
            q = q.where(TSupplierIncome.type == items['type'])
        if 'type_start' in items:
            q = q.where(TSupplierIncome.type >= items['type_start'])
        if 'type_end' in items:
            q = q.where(TSupplierIncome.type <= items['type_end'])
        
        if 'description' in items:
            q = q.where(TSupplierIncome.description == items['description'])
        if 'description_start' in items:
            q = q.where(TSupplierIncome.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TSupplierIncome.description <= items['description_end'])
        
        if 'create_time' in items:
            q = q.where(TSupplierIncome.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TSupplierIncome.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TSupplierIncome.create_time <= items['create_time_end'])
        
        if 'user_withdraw_id' in items:
            q = q.where(TSupplierIncome.user_withdraw_id == items['user_withdraw_id'])
        if 'user_withdraw_id_start' in items:
            q = q.where(TSupplierIncome.user_withdraw_id >= items['user_withdraw_id_start'])
        if 'user_withdraw_id_end' in items:
            q = q.where(TSupplierIncome.user_withdraw_id <= items['user_withdraw_id_end'])
        
        if 'operator_id' in items:
            q = q.where(TSupplierIncome.operator_id == items['operator_id'])
        if 'operator_id_start' in items:
            q = q.where(TSupplierIncome.operator_id >= items['operator_id_start'])
        if 'operator_id_end' in items:
            q = q.where(TSupplierIncome.operator_id <= items['operator_id_end'])
        
        if 'out_trade_no' in items:
            q = q.where(TSupplierIncome.out_trade_no == items['out_trade_no'])
        if 'out_trade_no_start' in items:
            q = q.where(TSupplierIncome.out_trade_no >= items['out_trade_no_start'])
        if 'out_trade_no_end' in items:
            q = q.where(TSupplierIncome.out_trade_no <= items['out_trade_no_end'])
        

        if 'id' in set_items:
            q = q.where(TSupplierIncome.id.in_(set_items['id']))
        
        if 'supplier_id' in set_items:
            q = q.where(TSupplierIncome.supplier_id.in_(set_items['supplier_id']))
        
        if 'change' in set_items:
            q = q.where(TSupplierIncome.change.in_(set_items['change']))
        
        if 'balance' in set_items:
            q = q.where(TSupplierIncome.balance.in_(set_items['balance']))
        
        if 'type' in set_items:
            q = q.where(TSupplierIncome.type.in_(set_items['type']))
        
        if 'description' in set_items:
            q = q.where(TSupplierIncome.description.in_(set_items['description']))
        
        if 'create_time' in set_items:
            q = q.where(TSupplierIncome.create_time.in_(set_items['create_time']))
        
        if 'user_withdraw_id' in set_items:
            q = q.where(TSupplierIncome.user_withdraw_id.in_(set_items['user_withdraw_id']))
        
        if 'operator_id' in set_items:
            q = q.where(TSupplierIncome.operator_id.in_(set_items['operator_id']))
        
        if 'out_trade_no' in set_items:
            q = q.where(TSupplierIncome.out_trade_no.in_(set_items['out_trade_no']))
        

        if 'type' in search_items:
            q = q.where(TSupplierIncome.type.like(search_items['type']))
        
        if 'description' in search_items:
            q = q.where(TSupplierIncome.description.like(search_items['description']))
        
        if 'out_trade_no' in search_items:
            q = q.where(TSupplierIncome.out_trade_no.like(search_items['out_trade_no']))
        
    
        c = q.count()
        return c

    
def insert_supplier_license(item: CreateSupplierLicense, db: Optional[SessionLocal] = None) -> SSupplierLicense:
    data = model2dict(item)
    t = TSupplierLicense(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SSupplierLicense.parse_obj(t.__dict__)

    
def delete_supplier_license(supplier_license_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TSupplierLicense).where(TSupplierLicense.id == supplier_license_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSupplierLicense).where(TSupplierLicense.id == supplier_license_id).delete()
        db.commit()

    
def update_supplier_license(item: SSupplierLicense, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TSupplierLicense).where(TSupplierLicense.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSupplierLicense).where(TSupplierLicense.id == item.id).update(data)
        db.commit()

    
def get_supplier_license(supplier_license_id: int) -> Optional[SSupplierLicense]:
    with Dao() as db:
        t = db.query(TSupplierLicense).where(TSupplierLicense.id == supplier_license_id).first()
        if t:
            return SSupplierLicense.parse_obj(t.__dict__)
        else:
            return None


def filter_supplier_license(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SSupplierLicense]:
    with Dao() as db:
        q = db.query(TSupplierLicense)


        if 'id' in items:
            q = q.where(TSupplierLicense.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSupplierLicense.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSupplierLicense.id <= items['id_end'])
        
        if 'license' in items:
            q = q.where(TSupplierLicense.license == items['license'])
        if 'license_start' in items:
            q = q.where(TSupplierLicense.license >= items['license_start'])
        if 'license_end' in items:
            q = q.where(TSupplierLicense.license <= items['license_end'])
        
        if 'supplier_id' in items:
            q = q.where(TSupplierLicense.supplier_id == items['supplier_id'])
        if 'supplier_id_start' in items:
            q = q.where(TSupplierLicense.supplier_id >= items['supplier_id_start'])
        if 'supplier_id_end' in items:
            q = q.where(TSupplierLicense.supplier_id <= items['supplier_id_end'])
        
        if 'create_time' in items:
            q = q.where(TSupplierLicense.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TSupplierLicense.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TSupplierLicense.create_time <= items['create_time_end'])
        

        if 'id' in set_items:
            q = q.where(TSupplierLicense.id.in_(set_items['id']))
        
        if 'license' in set_items:
            q = q.where(TSupplierLicense.license.in_(set_items['license']))
        
        if 'supplier_id' in set_items:
            q = q.where(TSupplierLicense.supplier_id.in_(set_items['supplier_id']))
        
        if 'create_time' in set_items:
            q = q.where(TSupplierLicense.create_time.in_(set_items['create_time']))
        

        if 'license' in search_items:
            q = q.where(TSupplierLicense.license.like(search_items['license']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TSupplierLicense.create_time.asc())
                orders.append(TSupplierLicense.id.asc())
            elif val == 'desc':
                #orders.append(TSupplierLicense.create_time.desc())
                orders.append(TSupplierLicense.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_supplier_license_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SSupplierLicense.parse_obj(t.__dict__) for t in t_supplier_license_list]


def filter_count_supplier_license(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TSupplierLicense)


        if 'id' in items:
            q = q.where(TSupplierLicense.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSupplierLicense.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSupplierLicense.id <= items['id_end'])
        
        if 'license' in items:
            q = q.where(TSupplierLicense.license == items['license'])
        if 'license_start' in items:
            q = q.where(TSupplierLicense.license >= items['license_start'])
        if 'license_end' in items:
            q = q.where(TSupplierLicense.license <= items['license_end'])
        
        if 'supplier_id' in items:
            q = q.where(TSupplierLicense.supplier_id == items['supplier_id'])
        if 'supplier_id_start' in items:
            q = q.where(TSupplierLicense.supplier_id >= items['supplier_id_start'])
        if 'supplier_id_end' in items:
            q = q.where(TSupplierLicense.supplier_id <= items['supplier_id_end'])
        
        if 'create_time' in items:
            q = q.where(TSupplierLicense.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TSupplierLicense.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TSupplierLicense.create_time <= items['create_time_end'])
        

        if 'id' in set_items:
            q = q.where(TSupplierLicense.id.in_(set_items['id']))
        
        if 'license' in set_items:
            q = q.where(TSupplierLicense.license.in_(set_items['license']))
        
        if 'supplier_id' in set_items:
            q = q.where(TSupplierLicense.supplier_id.in_(set_items['supplier_id']))
        
        if 'create_time' in set_items:
            q = q.where(TSupplierLicense.create_time.in_(set_items['create_time']))
        

        if 'license' in search_items:
            q = q.where(TSupplierLicense.license.like(search_items['license']))
        
    
        c = q.count()
        return c

    
def insert_supplier_membership(item: CreateSupplierMembership, db: Optional[SessionLocal] = None) -> SSupplierMembership:
    data = model2dict(item)
    t = TSupplierMembership(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SSupplierMembership.parse_obj(t.__dict__)

    
def delete_supplier_membership(supplier_membership_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TSupplierMembership).where(TSupplierMembership.id == supplier_membership_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSupplierMembership).where(TSupplierMembership.id == supplier_membership_id).delete()
        db.commit()

    
def update_supplier_membership(item: SSupplierMembership, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TSupplierMembership).where(TSupplierMembership.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSupplierMembership).where(TSupplierMembership.id == item.id).update(data)
        db.commit()

    
def get_supplier_membership(supplier_membership_id: int) -> Optional[SSupplierMembership]:
    with Dao() as db:
        t = db.query(TSupplierMembership).where(TSupplierMembership.id == supplier_membership_id).first()
        if t:
            return SSupplierMembership.parse_obj(t.__dict__)
        else:
            return None


def filter_supplier_membership(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SSupplierMembership]:
    with Dao() as db:
        q = db.query(TSupplierMembership)


        if 'id' in items:
            q = q.where(TSupplierMembership.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSupplierMembership.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSupplierMembership.id <= items['id_end'])
        
        if 'supplier_id' in items:
            q = q.where(TSupplierMembership.supplier_id == items['supplier_id'])
        if 'supplier_id_start' in items:
            q = q.where(TSupplierMembership.supplier_id >= items['supplier_id_start'])
        if 'supplier_id_end' in items:
            q = q.where(TSupplierMembership.supplier_id <= items['supplier_id_end'])
        
        if 'user_id' in items:
            q = q.where(TSupplierMembership.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TSupplierMembership.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TSupplierMembership.user_id <= items['user_id_end'])
        
        if 'status' in items:
            q = q.where(TSupplierMembership.status == items['status'])
        if 'status_start' in items:
            q = q.where(TSupplierMembership.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TSupplierMembership.status <= items['status_end'])
        
        if 'create_time' in items:
            q = q.where(TSupplierMembership.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TSupplierMembership.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TSupplierMembership.create_time <= items['create_time_end'])
        
        if 'expired_time' in items:
            q = q.where(TSupplierMembership.expired_time == items['expired_time'])
        if 'expired_time_start' in items:
            q = q.where(TSupplierMembership.expired_time >= items['expired_time_start'])
        if 'expired_time_end' in items:
            q = q.where(TSupplierMembership.expired_time <= items['expired_time_end'])
        

        if 'id' in set_items:
            q = q.where(TSupplierMembership.id.in_(set_items['id']))
        
        if 'supplier_id' in set_items:
            q = q.where(TSupplierMembership.supplier_id.in_(set_items['supplier_id']))
        
        if 'user_id' in set_items:
            q = q.where(TSupplierMembership.user_id.in_(set_items['user_id']))
        
        if 'status' in set_items:
            q = q.where(TSupplierMembership.status.in_(set_items['status']))
        
        if 'create_time' in set_items:
            q = q.where(TSupplierMembership.create_time.in_(set_items['create_time']))
        
        if 'expired_time' in set_items:
            q = q.where(TSupplierMembership.expired_time.in_(set_items['expired_time']))
        

        if 'status' in search_items:
            q = q.where(TSupplierMembership.status.like(search_items['status']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TSupplierMembership.expired_time.asc())
                orders.append(TSupplierMembership.id.asc())
            elif val == 'desc':
                #orders.append(TSupplierMembership.expired_time.desc())
                orders.append(TSupplierMembership.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_supplier_membership_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SSupplierMembership.parse_obj(t.__dict__) for t in t_supplier_membership_list]


def filter_count_supplier_membership(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TSupplierMembership)


        if 'id' in items:
            q = q.where(TSupplierMembership.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSupplierMembership.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSupplierMembership.id <= items['id_end'])
        
        if 'supplier_id' in items:
            q = q.where(TSupplierMembership.supplier_id == items['supplier_id'])
        if 'supplier_id_start' in items:
            q = q.where(TSupplierMembership.supplier_id >= items['supplier_id_start'])
        if 'supplier_id_end' in items:
            q = q.where(TSupplierMembership.supplier_id <= items['supplier_id_end'])
        
        if 'user_id' in items:
            q = q.where(TSupplierMembership.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TSupplierMembership.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TSupplierMembership.user_id <= items['user_id_end'])
        
        if 'status' in items:
            q = q.where(TSupplierMembership.status == items['status'])
        if 'status_start' in items:
            q = q.where(TSupplierMembership.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TSupplierMembership.status <= items['status_end'])
        
        if 'create_time' in items:
            q = q.where(TSupplierMembership.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TSupplierMembership.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TSupplierMembership.create_time <= items['create_time_end'])
        
        if 'expired_time' in items:
            q = q.where(TSupplierMembership.expired_time == items['expired_time'])
        if 'expired_time_start' in items:
            q = q.where(TSupplierMembership.expired_time >= items['expired_time_start'])
        if 'expired_time_end' in items:
            q = q.where(TSupplierMembership.expired_time <= items['expired_time_end'])
        

        if 'id' in set_items:
            q = q.where(TSupplierMembership.id.in_(set_items['id']))
        
        if 'supplier_id' in set_items:
            q = q.where(TSupplierMembership.supplier_id.in_(set_items['supplier_id']))
        
        if 'user_id' in set_items:
            q = q.where(TSupplierMembership.user_id.in_(set_items['user_id']))
        
        if 'status' in set_items:
            q = q.where(TSupplierMembership.status.in_(set_items['status']))
        
        if 'create_time' in set_items:
            q = q.where(TSupplierMembership.create_time.in_(set_items['create_time']))
        
        if 'expired_time' in set_items:
            q = q.where(TSupplierMembership.expired_time.in_(set_items['expired_time']))
        

        if 'status' in search_items:
            q = q.where(TSupplierMembership.status.like(search_items['status']))
        
    
        c = q.count()
        return c

    
def insert_supplier_owner(item: CreateSupplierOwner, db: Optional[SessionLocal] = None) -> SSupplierOwner:
    data = model2dict(item)
    t = TSupplierOwner(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SSupplierOwner.parse_obj(t.__dict__)

    
def delete_supplier_owner(supplier_owner_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TSupplierOwner).where(TSupplierOwner.id == supplier_owner_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSupplierOwner).where(TSupplierOwner.id == supplier_owner_id).delete()
        db.commit()

    
def update_supplier_owner(item: SSupplierOwner, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TSupplierOwner).where(TSupplierOwner.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSupplierOwner).where(TSupplierOwner.id == item.id).update(data)
        db.commit()

    
def get_supplier_owner(supplier_owner_id: int) -> Optional[SSupplierOwner]:
    with Dao() as db:
        t = db.query(TSupplierOwner).where(TSupplierOwner.id == supplier_owner_id).first()
        if t:
            return SSupplierOwner.parse_obj(t.__dict__)
        else:
            return None


def filter_supplier_owner(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SSupplierOwner]:
    with Dao() as db:
        q = db.query(TSupplierOwner)


        if 'id' in items:
            q = q.where(TSupplierOwner.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSupplierOwner.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSupplierOwner.id <= items['id_end'])
        
        if 'name' in items:
            q = q.where(TSupplierOwner.name == items['name'])
        if 'name_start' in items:
            q = q.where(TSupplierOwner.name >= items['name_start'])
        if 'name_end' in items:
            q = q.where(TSupplierOwner.name <= items['name_end'])
        
        if 'phone' in items:
            q = q.where(TSupplierOwner.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TSupplierOwner.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TSupplierOwner.phone <= items['phone_end'])
        
        if 'password' in items:
            q = q.where(TSupplierOwner.password == items['password'])
        if 'password_start' in items:
            q = q.where(TSupplierOwner.password >= items['password_start'])
        if 'password_end' in items:
            q = q.where(TSupplierOwner.password <= items['password_end'])
        
        if 'id_card' in items:
            q = q.where(TSupplierOwner.id_card == items['id_card'])
        if 'id_card_start' in items:
            q = q.where(TSupplierOwner.id_card >= items['id_card_start'])
        if 'id_card_end' in items:
            q = q.where(TSupplierOwner.id_card <= items['id_card_end'])
        
        if 'front_image' in items:
            q = q.where(TSupplierOwner.front_image == items['front_image'])
        if 'front_image_start' in items:
            q = q.where(TSupplierOwner.front_image >= items['front_image_start'])
        if 'front_image_end' in items:
            q = q.where(TSupplierOwner.front_image <= items['front_image_end'])
        
        if 'back_image' in items:
            q = q.where(TSupplierOwner.back_image == items['back_image'])
        if 'back_image_start' in items:
            q = q.where(TSupplierOwner.back_image >= items['back_image_start'])
        if 'back_image_end' in items:
            q = q.where(TSupplierOwner.back_image <= items['back_image_end'])
        
        if 'open_id' in items:
            q = q.where(TSupplierOwner.open_id == items['open_id'])
        if 'open_id_start' in items:
            q = q.where(TSupplierOwner.open_id >= items['open_id_start'])
        if 'open_id_end' in items:
            q = q.where(TSupplierOwner.open_id <= items['open_id_end'])
        
        if 'union_id' in items:
            q = q.where(TSupplierOwner.union_id == items['union_id'])
        if 'union_id_start' in items:
            q = q.where(TSupplierOwner.union_id >= items['union_id_start'])
        if 'union_id_end' in items:
            q = q.where(TSupplierOwner.union_id <= items['union_id_end'])
        
        if 'level_id' in items:
            q = q.where(TSupplierOwner.level_id == items['level_id'])
        if 'level_id_start' in items:
            q = q.where(TSupplierOwner.level_id >= items['level_id_start'])
        if 'level_id_end' in items:
            q = q.where(TSupplierOwner.level_id <= items['level_id_end'])
        

        if 'id' in set_items:
            q = q.where(TSupplierOwner.id.in_(set_items['id']))
        
        if 'name' in set_items:
            q = q.where(TSupplierOwner.name.in_(set_items['name']))
        
        if 'phone' in set_items:
            q = q.where(TSupplierOwner.phone.in_(set_items['phone']))
        
        if 'password' in set_items:
            q = q.where(TSupplierOwner.password.in_(set_items['password']))
        
        if 'id_card' in set_items:
            q = q.where(TSupplierOwner.id_card.in_(set_items['id_card']))
        
        if 'front_image' in set_items:
            q = q.where(TSupplierOwner.front_image.in_(set_items['front_image']))
        
        if 'back_image' in set_items:
            q = q.where(TSupplierOwner.back_image.in_(set_items['back_image']))
        
        if 'open_id' in set_items:
            q = q.where(TSupplierOwner.open_id.in_(set_items['open_id']))
        
        if 'union_id' in set_items:
            q = q.where(TSupplierOwner.union_id.in_(set_items['union_id']))
        
        if 'level_id' in set_items:
            q = q.where(TSupplierOwner.level_id.in_(set_items['level_id']))
        

        if 'name' in search_items:
            q = q.where(TSupplierOwner.name.like(search_items['name']))
        
        if 'phone' in search_items:
            q = q.where(TSupplierOwner.phone.like(search_items['phone']))
        
        if 'password' in search_items:
            q = q.where(TSupplierOwner.password.like(search_items['password']))
        
        if 'id_card' in search_items:
            q = q.where(TSupplierOwner.id_card.like(search_items['id_card']))
        
        if 'front_image' in search_items:
            q = q.where(TSupplierOwner.front_image.like(search_items['front_image']))
        
        if 'back_image' in search_items:
            q = q.where(TSupplierOwner.back_image.like(search_items['back_image']))
        
        if 'open_id' in search_items:
            q = q.where(TSupplierOwner.open_id.like(search_items['open_id']))
        
        if 'union_id' in search_items:
            q = q.where(TSupplierOwner.union_id.like(search_items['union_id']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TSupplierOwner.level_id.asc())
                orders.append(TSupplierOwner.id.asc())
            elif val == 'desc':
                #orders.append(TSupplierOwner.level_id.desc())
                orders.append(TSupplierOwner.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_supplier_owner_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SSupplierOwner.parse_obj(t.__dict__) for t in t_supplier_owner_list]


def filter_count_supplier_owner(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TSupplierOwner)


        if 'id' in items:
            q = q.where(TSupplierOwner.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSupplierOwner.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSupplierOwner.id <= items['id_end'])
        
        if 'name' in items:
            q = q.where(TSupplierOwner.name == items['name'])
        if 'name_start' in items:
            q = q.where(TSupplierOwner.name >= items['name_start'])
        if 'name_end' in items:
            q = q.where(TSupplierOwner.name <= items['name_end'])
        
        if 'phone' in items:
            q = q.where(TSupplierOwner.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TSupplierOwner.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TSupplierOwner.phone <= items['phone_end'])
        
        if 'password' in items:
            q = q.where(TSupplierOwner.password == items['password'])
        if 'password_start' in items:
            q = q.where(TSupplierOwner.password >= items['password_start'])
        if 'password_end' in items:
            q = q.where(TSupplierOwner.password <= items['password_end'])
        
        if 'id_card' in items:
            q = q.where(TSupplierOwner.id_card == items['id_card'])
        if 'id_card_start' in items:
            q = q.where(TSupplierOwner.id_card >= items['id_card_start'])
        if 'id_card_end' in items:
            q = q.where(TSupplierOwner.id_card <= items['id_card_end'])
        
        if 'front_image' in items:
            q = q.where(TSupplierOwner.front_image == items['front_image'])
        if 'front_image_start' in items:
            q = q.where(TSupplierOwner.front_image >= items['front_image_start'])
        if 'front_image_end' in items:
            q = q.where(TSupplierOwner.front_image <= items['front_image_end'])
        
        if 'back_image' in items:
            q = q.where(TSupplierOwner.back_image == items['back_image'])
        if 'back_image_start' in items:
            q = q.where(TSupplierOwner.back_image >= items['back_image_start'])
        if 'back_image_end' in items:
            q = q.where(TSupplierOwner.back_image <= items['back_image_end'])
        
        if 'open_id' in items:
            q = q.where(TSupplierOwner.open_id == items['open_id'])
        if 'open_id_start' in items:
            q = q.where(TSupplierOwner.open_id >= items['open_id_start'])
        if 'open_id_end' in items:
            q = q.where(TSupplierOwner.open_id <= items['open_id_end'])
        
        if 'union_id' in items:
            q = q.where(TSupplierOwner.union_id == items['union_id'])
        if 'union_id_start' in items:
            q = q.where(TSupplierOwner.union_id >= items['union_id_start'])
        if 'union_id_end' in items:
            q = q.where(TSupplierOwner.union_id <= items['union_id_end'])
        
        if 'level_id' in items:
            q = q.where(TSupplierOwner.level_id == items['level_id'])
        if 'level_id_start' in items:
            q = q.where(TSupplierOwner.level_id >= items['level_id_start'])
        if 'level_id_end' in items:
            q = q.where(TSupplierOwner.level_id <= items['level_id_end'])
        

        if 'id' in set_items:
            q = q.where(TSupplierOwner.id.in_(set_items['id']))
        
        if 'name' in set_items:
            q = q.where(TSupplierOwner.name.in_(set_items['name']))
        
        if 'phone' in set_items:
            q = q.where(TSupplierOwner.phone.in_(set_items['phone']))
        
        if 'password' in set_items:
            q = q.where(TSupplierOwner.password.in_(set_items['password']))
        
        if 'id_card' in set_items:
            q = q.where(TSupplierOwner.id_card.in_(set_items['id_card']))
        
        if 'front_image' in set_items:
            q = q.where(TSupplierOwner.front_image.in_(set_items['front_image']))
        
        if 'back_image' in set_items:
            q = q.where(TSupplierOwner.back_image.in_(set_items['back_image']))
        
        if 'open_id' in set_items:
            q = q.where(TSupplierOwner.open_id.in_(set_items['open_id']))
        
        if 'union_id' in set_items:
            q = q.where(TSupplierOwner.union_id.in_(set_items['union_id']))
        
        if 'level_id' in set_items:
            q = q.where(TSupplierOwner.level_id.in_(set_items['level_id']))
        

        if 'name' in search_items:
            q = q.where(TSupplierOwner.name.like(search_items['name']))
        
        if 'phone' in search_items:
            q = q.where(TSupplierOwner.phone.like(search_items['phone']))
        
        if 'password' in search_items:
            q = q.where(TSupplierOwner.password.like(search_items['password']))
        
        if 'id_card' in search_items:
            q = q.where(TSupplierOwner.id_card.like(search_items['id_card']))
        
        if 'front_image' in search_items:
            q = q.where(TSupplierOwner.front_image.like(search_items['front_image']))
        
        if 'back_image' in search_items:
            q = q.where(TSupplierOwner.back_image.like(search_items['back_image']))
        
        if 'open_id' in search_items:
            q = q.where(TSupplierOwner.open_id.like(search_items['open_id']))
        
        if 'union_id' in search_items:
            q = q.where(TSupplierOwner.union_id.like(search_items['union_id']))
        
    
        c = q.count()
        return c

    
def insert_supplier_state(item: CreateSupplierState, db: Optional[SessionLocal] = None) -> SSupplierState:
    data = model2dict(item)
    t = TSupplierState(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SSupplierState.parse_obj(t.__dict__)

    
def delete_supplier_state(supplier_state_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TSupplierState).where(TSupplierState.id == supplier_state_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSupplierState).where(TSupplierState.id == supplier_state_id).delete()
        db.commit()

    
def update_supplier_state(item: SSupplierState, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TSupplierState).where(TSupplierState.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSupplierState).where(TSupplierState.id == item.id).update(data)
        db.commit()

    
def get_supplier_state(supplier_state_id: int) -> Optional[SSupplierState]:
    with Dao() as db:
        t = db.query(TSupplierState).where(TSupplierState.id == supplier_state_id).first()
        if t:
            return SSupplierState.parse_obj(t.__dict__)
        else:
            return None


def filter_supplier_state(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SSupplierState]:
    with Dao() as db:
        q = db.query(TSupplierState)


        if 'id' in items:
            q = q.where(TSupplierState.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSupplierState.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSupplierState.id <= items['id_end'])
        
        if 'status' in items:
            q = q.where(TSupplierState.status == items['status'])
        if 'status_start' in items:
            q = q.where(TSupplierState.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TSupplierState.status <= items['status_end'])
        

        if 'id' in set_items:
            q = q.where(TSupplierState.id.in_(set_items['id']))
        
        if 'status' in set_items:
            q = q.where(TSupplierState.status.in_(set_items['status']))
        

        if 'status' in search_items:
            q = q.where(TSupplierState.status.like(search_items['status']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TSupplierState.status.asc())
                orders.append(TSupplierState.id.asc())
            elif val == 'desc':
                #orders.append(TSupplierState.status.desc())
                orders.append(TSupplierState.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_supplier_state_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SSupplierState.parse_obj(t.__dict__) for t in t_supplier_state_list]


def filter_count_supplier_state(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TSupplierState)


        if 'id' in items:
            q = q.where(TSupplierState.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSupplierState.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSupplierState.id <= items['id_end'])
        
        if 'status' in items:
            q = q.where(TSupplierState.status == items['status'])
        if 'status_start' in items:
            q = q.where(TSupplierState.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TSupplierState.status <= items['status_end'])
        

        if 'id' in set_items:
            q = q.where(TSupplierState.id.in_(set_items['id']))
        
        if 'status' in set_items:
            q = q.where(TSupplierState.status.in_(set_items['status']))
        

        if 'status' in search_items:
            q = q.where(TSupplierState.status.like(search_items['status']))
        
    
        c = q.count()
        return c

    
def insert_supplier_type(item: CreateSupplierType, db: Optional[SessionLocal] = None) -> SSupplierType:
    data = model2dict(item)
    t = TSupplierType(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SSupplierType.parse_obj(t.__dict__)

    
def delete_supplier_type(supplier_type_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TSupplierType).where(TSupplierType.id == supplier_type_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSupplierType).where(TSupplierType.id == supplier_type_id).delete()
        db.commit()

    
def update_supplier_type(item: SSupplierType, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TSupplierType).where(TSupplierType.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TSupplierType).where(TSupplierType.id == item.id).update(data)
        db.commit()

    
def get_supplier_type(supplier_type_id: int) -> Optional[SSupplierType]:
    with Dao() as db:
        t = db.query(TSupplierType).where(TSupplierType.id == supplier_type_id).first()
        if t:
            return SSupplierType.parse_obj(t.__dict__)
        else:
            return None


def filter_supplier_type(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SSupplierType]:
    with Dao() as db:
        q = db.query(TSupplierType)


        if 'id' in items:
            q = q.where(TSupplierType.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSupplierType.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSupplierType.id <= items['id_end'])
        
        if 'type_' in items:
            q = q.where(TSupplierType.type_ == items['type_'])
        if 'type__start' in items:
            q = q.where(TSupplierType.type_ >= items['type__start'])
        if 'type__end' in items:
            q = q.where(TSupplierType.type_ <= items['type__end'])
        

        if 'id' in set_items:
            q = q.where(TSupplierType.id.in_(set_items['id']))
        
        if 'type_' in set_items:
            q = q.where(TSupplierType.type_.in_(set_items['type_']))
        

        if 'type_' in search_items:
            q = q.where(TSupplierType.type_.like(search_items['type_']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TSupplierType.type_.asc())
                orders.append(TSupplierType.id.asc())
            elif val == 'desc':
                #orders.append(TSupplierType.type_.desc())
                orders.append(TSupplierType.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_supplier_type_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SSupplierType.parse_obj(t.__dict__) for t in t_supplier_type_list]


def filter_count_supplier_type(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TSupplierType)


        if 'id' in items:
            q = q.where(TSupplierType.id == items['id'])
        if 'id_start' in items:
            q = q.where(TSupplierType.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TSupplierType.id <= items['id_end'])
        
        if 'type_' in items:
            q = q.where(TSupplierType.type_ == items['type_'])
        if 'type__start' in items:
            q = q.where(TSupplierType.type_ >= items['type__start'])
        if 'type__end' in items:
            q = q.where(TSupplierType.type_ <= items['type__end'])
        

        if 'id' in set_items:
            q = q.where(TSupplierType.id.in_(set_items['id']))
        
        if 'type_' in set_items:
            q = q.where(TSupplierType.type_.in_(set_items['type_']))
        

        if 'type_' in search_items:
            q = q.where(TSupplierType.type_.like(search_items['type_']))
        
    
        c = q.count()
        return c

    
def insert_user(item: CreateUser, db: Optional[SessionLocal] = None) -> SUser:
    data = model2dict(item)
    t = TUser(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SUser.parse_obj(t.__dict__)

    
def delete_user(user_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TUser).where(TUser.id == user_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUser).where(TUser.id == user_id).delete()
        db.commit()

    
def update_user(item: SUser, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TUser).where(TUser.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUser).where(TUser.id == item.id).update(data)
        db.commit()

    
def get_user(user_id: int) -> Optional[SUser]:
    with Dao() as db:
        t = db.query(TUser).where(TUser.id == user_id).first()
        if t:
            return SUser.parse_obj(t.__dict__)
        else:
            return None


def filter_user(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SUser]:
    with Dao() as db:
        q = db.query(TUser)


        if 'id' in items:
            q = q.where(TUser.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUser.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUser.id <= items['id_end'])
        
        if 'username' in items:
            q = q.where(TUser.username == items['username'])
        if 'username_start' in items:
            q = q.where(TUser.username >= items['username_start'])
        if 'username_end' in items:
            q = q.where(TUser.username <= items['username_end'])
        
        if 'email' in items:
            q = q.where(TUser.email == items['email'])
        if 'email_start' in items:
            q = q.where(TUser.email >= items['email_start'])
        if 'email_end' in items:
            q = q.where(TUser.email <= items['email_end'])
        
        if 'open_id' in items:
            q = q.where(TUser.open_id == items['open_id'])
        if 'open_id_start' in items:
            q = q.where(TUser.open_id >= items['open_id_start'])
        if 'open_id_end' in items:
            q = q.where(TUser.open_id <= items['open_id_end'])
        
        if 'union_id' in items:
            q = q.where(TUser.union_id == items['union_id'])
        if 'union_id_start' in items:
            q = q.where(TUser.union_id >= items['union_id_start'])
        if 'union_id_end' in items:
            q = q.where(TUser.union_id <= items['union_id_end'])
        
        if 'password' in items:
            q = q.where(TUser.password == items['password'])
        if 'password_start' in items:
            q = q.where(TUser.password >= items['password_start'])
        if 'password_end' in items:
            q = q.where(TUser.password <= items['password_end'])
        
        if 'nickname' in items:
            q = q.where(TUser.nickname == items['nickname'])
        if 'nickname_start' in items:
            q = q.where(TUser.nickname >= items['nickname_start'])
        if 'nickname_end' in items:
            q = q.where(TUser.nickname <= items['nickname_end'])
        
        if 'phone' in items:
            q = q.where(TUser.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TUser.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TUser.phone <= items['phone_end'])
        
        if 'id_card' in items:
            q = q.where(TUser.id_card == items['id_card'])
        if 'id_card_start' in items:
            q = q.where(TUser.id_card >= items['id_card_start'])
        if 'id_card_end' in items:
            q = q.where(TUser.id_card <= items['id_card_end'])
        
        if 'level_id' in items:
            q = q.where(TUser.level_id == items['level_id'])
        if 'level_id_start' in items:
            q = q.where(TUser.level_id >= items['level_id_start'])
        if 'level_id_end' in items:
            q = q.where(TUser.level_id <= items['level_id_end'])
        
        if 'status' in items:
            q = q.where(TUser.status == items['status'])
        if 'status_start' in items:
            q = q.where(TUser.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TUser.status <= items['status_end'])
        
        if 'register_time' in items:
            q = q.where(TUser.register_time == items['register_time'])
        if 'register_time_start' in items:
            q = q.where(TUser.register_time >= items['register_time_start'])
        if 'register_time_end' in items:
            q = q.where(TUser.register_time <= items['register_time_end'])
        
        if 'avatar' in items:
            q = q.where(TUser.avatar == items['avatar'])
        if 'avatar_start' in items:
            q = q.where(TUser.avatar >= items['avatar_start'])
        if 'avatar_end' in items:
            q = q.where(TUser.avatar <= items['avatar_end'])
        
        if 'invited_user_id' in items:
            q = q.where(TUser.invited_user_id == items['invited_user_id'])
        if 'invited_user_id_start' in items:
            q = q.where(TUser.invited_user_id >= items['invited_user_id_start'])
        if 'invited_user_id_end' in items:
            q = q.where(TUser.invited_user_id <= items['invited_user_id_end'])
        
        if 'coin' in items:
            q = q.where(TUser.coin == items['coin'])
        if 'coin_start' in items:
            q = q.where(TUser.coin >= items['coin_start'])
        if 'coin_end' in items:
            q = q.where(TUser.coin <= items['coin_end'])
        
        if 'gender' in items:
            q = q.where(TUser.gender == items['gender'])
        if 'gender_start' in items:
            q = q.where(TUser.gender >= items['gender_start'])
        if 'gender_end' in items:
            q = q.where(TUser.gender <= items['gender_end'])
        
        if 'last_active_time' in items:
            q = q.where(TUser.last_active_time == items['last_active_time'])
        if 'last_active_time_start' in items:
            q = q.where(TUser.last_active_time >= items['last_active_time_start'])
        if 'last_active_time_end' in items:
            q = q.where(TUser.last_active_time <= items['last_active_time_end'])
        
        if 'name' in items:
            q = q.where(TUser.name == items['name'])
        if 'name_start' in items:
            q = q.where(TUser.name >= items['name_start'])
        if 'name_end' in items:
            q = q.where(TUser.name <= items['name_end'])
        
        if 'is_agree' in items:
            q = q.where(TUser.is_agree == items['is_agree'])
        if 'is_agree_start' in items:
            q = q.where(TUser.is_agree >= items['is_agree_start'])
        if 'is_agree_end' in items:
            q = q.where(TUser.is_agree <= items['is_agree_end'])
        
        if 'parent_id' in items:
            q = q.where(TUser.parent_id == items['parent_id'])
        if 'parent_id_start' in items:
            q = q.where(TUser.parent_id >= items['parent_id_start'])
        if 'parent_id_end' in items:
            q = q.where(TUser.parent_id <= items['parent_id_end'])
        
        if 'parent_id_history' in items:
            q = q.where(TUser.parent_id_history == items['parent_id_history'])
        if 'parent_id_history_start' in items:
            q = q.where(TUser.parent_id_history >= items['parent_id_history_start'])
        if 'parent_id_history_end' in items:
            q = q.where(TUser.parent_id_history <= items['parent_id_history_end'])
        
        if 'level_one_time' in items:
            q = q.where(TUser.level_one_time == items['level_one_time'])
        if 'level_one_time_start' in items:
            q = q.where(TUser.level_one_time >= items['level_one_time_start'])
        if 'level_one_time_end' in items:
            q = q.where(TUser.level_one_time <= items['level_one_time_end'])
        
        if 'level_two_time' in items:
            q = q.where(TUser.level_two_time == items['level_two_time'])
        if 'level_two_time_start' in items:
            q = q.where(TUser.level_two_time >= items['level_two_time_start'])
        if 'level_two_time_end' in items:
            q = q.where(TUser.level_two_time <= items['level_two_time_end'])
        
        if 'level_three_time' in items:
            q = q.where(TUser.level_three_time == items['level_three_time'])
        if 'level_three_time_start' in items:
            q = q.where(TUser.level_three_time >= items['level_three_time_start'])
        if 'level_three_time_end' in items:
            q = q.where(TUser.level_three_time <= items['level_three_time_end'])
        
        if 'level_top_time' in items:
            q = q.where(TUser.level_top_time == items['level_top_time'])
        if 'level_top_time_start' in items:
            q = q.where(TUser.level_top_time >= items['level_top_time_start'])
        if 'level_top_time_end' in items:
            q = q.where(TUser.level_top_time <= items['level_top_time_end'])
        

        if 'id' in set_items:
            q = q.where(TUser.id.in_(set_items['id']))
        
        if 'username' in set_items:
            q = q.where(TUser.username.in_(set_items['username']))
        
        if 'email' in set_items:
            q = q.where(TUser.email.in_(set_items['email']))
        
        if 'open_id' in set_items:
            q = q.where(TUser.open_id.in_(set_items['open_id']))
        
        if 'union_id' in set_items:
            q = q.where(TUser.union_id.in_(set_items['union_id']))
        
        if 'password' in set_items:
            q = q.where(TUser.password.in_(set_items['password']))
        
        if 'nickname' in set_items:
            q = q.where(TUser.nickname.in_(set_items['nickname']))
        
        if 'phone' in set_items:
            q = q.where(TUser.phone.in_(set_items['phone']))
        
        if 'id_card' in set_items:
            q = q.where(TUser.id_card.in_(set_items['id_card']))
        
        if 'level_id' in set_items:
            q = q.where(TUser.level_id.in_(set_items['level_id']))
        
        if 'status' in set_items:
            q = q.where(TUser.status.in_(set_items['status']))
        
        if 'register_time' in set_items:
            q = q.where(TUser.register_time.in_(set_items['register_time']))
        
        if 'avatar' in set_items:
            q = q.where(TUser.avatar.in_(set_items['avatar']))
        
        if 'invited_user_id' in set_items:
            q = q.where(TUser.invited_user_id.in_(set_items['invited_user_id']))
        
        if 'coin' in set_items:
            q = q.where(TUser.coin.in_(set_items['coin']))
        
        if 'gender' in set_items:
            q = q.where(TUser.gender.in_(set_items['gender']))
        
        if 'last_active_time' in set_items:
            q = q.where(TUser.last_active_time.in_(set_items['last_active_time']))
        
        if 'name' in set_items:
            q = q.where(TUser.name.in_(set_items['name']))
        
        if 'is_agree' in set_items:
            q = q.where(TUser.is_agree.in_(set_items['is_agree']))
        
        if 'parent_id' in set_items:
            q = q.where(TUser.parent_id.in_(set_items['parent_id']))
        
        if 'parent_id_history' in set_items:
            q = q.where(TUser.parent_id_history.in_(set_items['parent_id_history']))
        
        if 'level_one_time' in set_items:
            q = q.where(TUser.level_one_time.in_(set_items['level_one_time']))
        
        if 'level_two_time' in set_items:
            q = q.where(TUser.level_two_time.in_(set_items['level_two_time']))
        
        if 'level_three_time' in set_items:
            q = q.where(TUser.level_three_time.in_(set_items['level_three_time']))
        
        if 'level_top_time' in set_items:
            q = q.where(TUser.level_top_time.in_(set_items['level_top_time']))
        

        if 'username' in search_items:
            q = q.where(TUser.username.like(search_items['username']))
        
        if 'email' in search_items:
            q = q.where(TUser.email.like(search_items['email']))
        
        if 'open_id' in search_items:
            q = q.where(TUser.open_id.like(search_items['open_id']))
        
        if 'union_id' in search_items:
            q = q.where(TUser.union_id.like(search_items['union_id']))
        
        if 'password' in search_items:
            q = q.where(TUser.password.like(search_items['password']))
        
        if 'nickname' in search_items:
            q = q.where(TUser.nickname.like(search_items['nickname']))
        
        if 'phone' in search_items:
            q = q.where(TUser.phone.like(search_items['phone']))
        
        if 'id_card' in search_items:
            q = q.where(TUser.id_card.like(search_items['id_card']))
        
        if 'avatar' in search_items:
            q = q.where(TUser.avatar.like(search_items['avatar']))
        
        if 'name' in search_items:
            q = q.where(TUser.name.like(search_items['name']))
        
        if 'parent_id_history' in search_items:
            q = q.where(TUser.parent_id_history.like(search_items['parent_id_history']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TUser.level_top_time.asc())
                orders.append(TUser.id.asc())
            elif val == 'desc':
                #orders.append(TUser.level_top_time.desc())
                orders.append(TUser.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_user_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SUser.parse_obj(t.__dict__) for t in t_user_list]


def filter_count_user(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TUser)


        if 'id' in items:
            q = q.where(TUser.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUser.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUser.id <= items['id_end'])
        
        if 'username' in items:
            q = q.where(TUser.username == items['username'])
        if 'username_start' in items:
            q = q.where(TUser.username >= items['username_start'])
        if 'username_end' in items:
            q = q.where(TUser.username <= items['username_end'])
        
        if 'email' in items:
            q = q.where(TUser.email == items['email'])
        if 'email_start' in items:
            q = q.where(TUser.email >= items['email_start'])
        if 'email_end' in items:
            q = q.where(TUser.email <= items['email_end'])
        
        if 'open_id' in items:
            q = q.where(TUser.open_id == items['open_id'])
        if 'open_id_start' in items:
            q = q.where(TUser.open_id >= items['open_id_start'])
        if 'open_id_end' in items:
            q = q.where(TUser.open_id <= items['open_id_end'])
        
        if 'union_id' in items:
            q = q.where(TUser.union_id == items['union_id'])
        if 'union_id_start' in items:
            q = q.where(TUser.union_id >= items['union_id_start'])
        if 'union_id_end' in items:
            q = q.where(TUser.union_id <= items['union_id_end'])
        
        if 'password' in items:
            q = q.where(TUser.password == items['password'])
        if 'password_start' in items:
            q = q.where(TUser.password >= items['password_start'])
        if 'password_end' in items:
            q = q.where(TUser.password <= items['password_end'])
        
        if 'nickname' in items:
            q = q.where(TUser.nickname == items['nickname'])
        if 'nickname_start' in items:
            q = q.where(TUser.nickname >= items['nickname_start'])
        if 'nickname_end' in items:
            q = q.where(TUser.nickname <= items['nickname_end'])
        
        if 'phone' in items:
            q = q.where(TUser.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TUser.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TUser.phone <= items['phone_end'])
        
        if 'id_card' in items:
            q = q.where(TUser.id_card == items['id_card'])
        if 'id_card_start' in items:
            q = q.where(TUser.id_card >= items['id_card_start'])
        if 'id_card_end' in items:
            q = q.where(TUser.id_card <= items['id_card_end'])
        
        if 'level_id' in items:
            q = q.where(TUser.level_id == items['level_id'])
        if 'level_id_start' in items:
            q = q.where(TUser.level_id >= items['level_id_start'])
        if 'level_id_end' in items:
            q = q.where(TUser.level_id <= items['level_id_end'])
        
        if 'status' in items:
            q = q.where(TUser.status == items['status'])
        if 'status_start' in items:
            q = q.where(TUser.status >= items['status_start'])
        if 'status_end' in items:
            q = q.where(TUser.status <= items['status_end'])
        
        if 'register_time' in items:
            q = q.where(TUser.register_time == items['register_time'])
        if 'register_time_start' in items:
            q = q.where(TUser.register_time >= items['register_time_start'])
        if 'register_time_end' in items:
            q = q.where(TUser.register_time <= items['register_time_end'])
        
        if 'avatar' in items:
            q = q.where(TUser.avatar == items['avatar'])
        if 'avatar_start' in items:
            q = q.where(TUser.avatar >= items['avatar_start'])
        if 'avatar_end' in items:
            q = q.where(TUser.avatar <= items['avatar_end'])
        
        if 'invited_user_id' in items:
            q = q.where(TUser.invited_user_id == items['invited_user_id'])
        if 'invited_user_id_start' in items:
            q = q.where(TUser.invited_user_id >= items['invited_user_id_start'])
        if 'invited_user_id_end' in items:
            q = q.where(TUser.invited_user_id <= items['invited_user_id_end'])
        
        if 'coin' in items:
            q = q.where(TUser.coin == items['coin'])
        if 'coin_start' in items:
            q = q.where(TUser.coin >= items['coin_start'])
        if 'coin_end' in items:
            q = q.where(TUser.coin <= items['coin_end'])
        
        if 'gender' in items:
            q = q.where(TUser.gender == items['gender'])
        if 'gender_start' in items:
            q = q.where(TUser.gender >= items['gender_start'])
        if 'gender_end' in items:
            q = q.where(TUser.gender <= items['gender_end'])
        
        if 'last_active_time' in items:
            q = q.where(TUser.last_active_time == items['last_active_time'])
        if 'last_active_time_start' in items:
            q = q.where(TUser.last_active_time >= items['last_active_time_start'])
        if 'last_active_time_end' in items:
            q = q.where(TUser.last_active_time <= items['last_active_time_end'])
        
        if 'name' in items:
            q = q.where(TUser.name == items['name'])
        if 'name_start' in items:
            q = q.where(TUser.name >= items['name_start'])
        if 'name_end' in items:
            q = q.where(TUser.name <= items['name_end'])
        
        if 'is_agree' in items:
            q = q.where(TUser.is_agree == items['is_agree'])
        if 'is_agree_start' in items:
            q = q.where(TUser.is_agree >= items['is_agree_start'])
        if 'is_agree_end' in items:
            q = q.where(TUser.is_agree <= items['is_agree_end'])
        
        if 'parent_id' in items:
            q = q.where(TUser.parent_id == items['parent_id'])
        if 'parent_id_start' in items:
            q = q.where(TUser.parent_id >= items['parent_id_start'])
        if 'parent_id_end' in items:
            q = q.where(TUser.parent_id <= items['parent_id_end'])
        
        if 'parent_id_history' in items:
            q = q.where(TUser.parent_id_history == items['parent_id_history'])
        if 'parent_id_history_start' in items:
            q = q.where(TUser.parent_id_history >= items['parent_id_history_start'])
        if 'parent_id_history_end' in items:
            q = q.where(TUser.parent_id_history <= items['parent_id_history_end'])
        
        if 'level_one_time' in items:
            q = q.where(TUser.level_one_time == items['level_one_time'])
        if 'level_one_time_start' in items:
            q = q.where(TUser.level_one_time >= items['level_one_time_start'])
        if 'level_one_time_end' in items:
            q = q.where(TUser.level_one_time <= items['level_one_time_end'])
        
        if 'level_two_time' in items:
            q = q.where(TUser.level_two_time == items['level_two_time'])
        if 'level_two_time_start' in items:
            q = q.where(TUser.level_two_time >= items['level_two_time_start'])
        if 'level_two_time_end' in items:
            q = q.where(TUser.level_two_time <= items['level_two_time_end'])
        
        if 'level_three_time' in items:
            q = q.where(TUser.level_three_time == items['level_three_time'])
        if 'level_three_time_start' in items:
            q = q.where(TUser.level_three_time >= items['level_three_time_start'])
        if 'level_three_time_end' in items:
            q = q.where(TUser.level_three_time <= items['level_three_time_end'])
        
        if 'level_top_time' in items:
            q = q.where(TUser.level_top_time == items['level_top_time'])
        if 'level_top_time_start' in items:
            q = q.where(TUser.level_top_time >= items['level_top_time_start'])
        if 'level_top_time_end' in items:
            q = q.where(TUser.level_top_time <= items['level_top_time_end'])
        

        if 'id' in set_items:
            q = q.where(TUser.id.in_(set_items['id']))
        
        if 'username' in set_items:
            q = q.where(TUser.username.in_(set_items['username']))
        
        if 'email' in set_items:
            q = q.where(TUser.email.in_(set_items['email']))
        
        if 'open_id' in set_items:
            q = q.where(TUser.open_id.in_(set_items['open_id']))
        
        if 'union_id' in set_items:
            q = q.where(TUser.union_id.in_(set_items['union_id']))
        
        if 'password' in set_items:
            q = q.where(TUser.password.in_(set_items['password']))
        
        if 'nickname' in set_items:
            q = q.where(TUser.nickname.in_(set_items['nickname']))
        
        if 'phone' in set_items:
            q = q.where(TUser.phone.in_(set_items['phone']))
        
        if 'id_card' in set_items:
            q = q.where(TUser.id_card.in_(set_items['id_card']))
        
        if 'level_id' in set_items:
            q = q.where(TUser.level_id.in_(set_items['level_id']))
        
        if 'status' in set_items:
            q = q.where(TUser.status.in_(set_items['status']))
        
        if 'register_time' in set_items:
            q = q.where(TUser.register_time.in_(set_items['register_time']))
        
        if 'avatar' in set_items:
            q = q.where(TUser.avatar.in_(set_items['avatar']))
        
        if 'invited_user_id' in set_items:
            q = q.where(TUser.invited_user_id.in_(set_items['invited_user_id']))
        
        if 'coin' in set_items:
            q = q.where(TUser.coin.in_(set_items['coin']))
        
        if 'gender' in set_items:
            q = q.where(TUser.gender.in_(set_items['gender']))
        
        if 'last_active_time' in set_items:
            q = q.where(TUser.last_active_time.in_(set_items['last_active_time']))
        
        if 'name' in set_items:
            q = q.where(TUser.name.in_(set_items['name']))
        
        if 'is_agree' in set_items:
            q = q.where(TUser.is_agree.in_(set_items['is_agree']))
        
        if 'parent_id' in set_items:
            q = q.where(TUser.parent_id.in_(set_items['parent_id']))
        
        if 'parent_id_history' in set_items:
            q = q.where(TUser.parent_id_history.in_(set_items['parent_id_history']))
        
        if 'level_one_time' in set_items:
            q = q.where(TUser.level_one_time.in_(set_items['level_one_time']))
        
        if 'level_two_time' in set_items:
            q = q.where(TUser.level_two_time.in_(set_items['level_two_time']))
        
        if 'level_three_time' in set_items:
            q = q.where(TUser.level_three_time.in_(set_items['level_three_time']))
        
        if 'level_top_time' in set_items:
            q = q.where(TUser.level_top_time.in_(set_items['level_top_time']))
        

        if 'username' in search_items:
            q = q.where(TUser.username.like(search_items['username']))
        
        if 'email' in search_items:
            q = q.where(TUser.email.like(search_items['email']))
        
        if 'open_id' in search_items:
            q = q.where(TUser.open_id.like(search_items['open_id']))
        
        if 'union_id' in search_items:
            q = q.where(TUser.union_id.like(search_items['union_id']))
        
        if 'password' in search_items:
            q = q.where(TUser.password.like(search_items['password']))
        
        if 'nickname' in search_items:
            q = q.where(TUser.nickname.like(search_items['nickname']))
        
        if 'phone' in search_items:
            q = q.where(TUser.phone.like(search_items['phone']))
        
        if 'id_card' in search_items:
            q = q.where(TUser.id_card.like(search_items['id_card']))
        
        if 'avatar' in search_items:
            q = q.where(TUser.avatar.like(search_items['avatar']))
        
        if 'name' in search_items:
            q = q.where(TUser.name.like(search_items['name']))
        
        if 'parent_id_history' in search_items:
            q = q.where(TUser.parent_id_history.like(search_items['parent_id_history']))
        
    
        c = q.count()
        return c

    
def insert_user_account(item: CreateUserAccount, db: Optional[SessionLocal] = None) -> SUserAccount:
    data = model2dict(item)
    t = TUserAccount(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SUserAccount.parse_obj(t.__dict__)

    
def delete_user_account(user_account_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TUserAccount).where(TUserAccount.id == user_account_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUserAccount).where(TUserAccount.id == user_account_id).delete()
        db.commit()

    
def update_user_account(item: SUserAccount, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TUserAccount).where(TUserAccount.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUserAccount).where(TUserAccount.id == item.id).update(data)
        db.commit()

    
def get_user_account(user_account_id: int) -> Optional[SUserAccount]:
    with Dao() as db:
        t = db.query(TUserAccount).where(TUserAccount.id == user_account_id).first()
        if t:
            return SUserAccount.parse_obj(t.__dict__)
        else:
            return None


def filter_user_account(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SUserAccount]:
    with Dao() as db:
        q = db.query(TUserAccount)


        if 'id' in items:
            q = q.where(TUserAccount.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUserAccount.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUserAccount.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TUserAccount.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TUserAccount.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TUserAccount.user_id <= items['user_id_end'])
        
        if 'balance' in items:
            q = q.where(TUserAccount.balance == items['balance'])
        if 'balance_start' in items:
            q = q.where(TUserAccount.balance >= items['balance_start'])
        if 'balance_end' in items:
            q = q.where(TUserAccount.balance <= items['balance_end'])
        
        if 'lock_balance' in items:
            q = q.where(TUserAccount.lock_balance == items['lock_balance'])
        if 'lock_balance_start' in items:
            q = q.where(TUserAccount.lock_balance >= items['lock_balance_start'])
        if 'lock_balance_end' in items:
            q = q.where(TUserAccount.lock_balance <= items['lock_balance_end'])
        
        if 'coin' in items:
            q = q.where(TUserAccount.coin == items['coin'])
        if 'coin_start' in items:
            q = q.where(TUserAccount.coin >= items['coin_start'])
        if 'coin_end' in items:
            q = q.where(TUserAccount.coin <= items['coin_end'])
        
        if 'description' in items:
            q = q.where(TUserAccount.description == items['description'])
        if 'description_start' in items:
            q = q.where(TUserAccount.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TUserAccount.description <= items['description_end'])
        
        if 'create_time' in items:
            q = q.where(TUserAccount.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TUserAccount.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TUserAccount.create_time <= items['create_time_end'])
        
        if 'freeze_balance' in items:
            q = q.where(TUserAccount.freeze_balance == items['freeze_balance'])
        if 'freeze_balance_start' in items:
            q = q.where(TUserAccount.freeze_balance >= items['freeze_balance_start'])
        if 'freeze_balance_end' in items:
            q = q.where(TUserAccount.freeze_balance <= items['freeze_balance_end'])
        
        if 'update_time' in items:
            q = q.where(TUserAccount.update_time == items['update_time'])
        if 'update_time_start' in items:
            q = q.where(TUserAccount.update_time >= items['update_time_start'])
        if 'update_time_end' in items:
            q = q.where(TUserAccount.update_time <= items['update_time_end'])
        

        if 'id' in set_items:
            q = q.where(TUserAccount.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TUserAccount.user_id.in_(set_items['user_id']))
        
        if 'balance' in set_items:
            q = q.where(TUserAccount.balance.in_(set_items['balance']))
        
        if 'lock_balance' in set_items:
            q = q.where(TUserAccount.lock_balance.in_(set_items['lock_balance']))
        
        if 'coin' in set_items:
            q = q.where(TUserAccount.coin.in_(set_items['coin']))
        
        if 'description' in set_items:
            q = q.where(TUserAccount.description.in_(set_items['description']))
        
        if 'create_time' in set_items:
            q = q.where(TUserAccount.create_time.in_(set_items['create_time']))
        
        if 'freeze_balance' in set_items:
            q = q.where(TUserAccount.freeze_balance.in_(set_items['freeze_balance']))
        
        if 'update_time' in set_items:
            q = q.where(TUserAccount.update_time.in_(set_items['update_time']))
        

        if 'description' in search_items:
            q = q.where(TUserAccount.description.like(search_items['description']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TUserAccount.update_time.asc())
                orders.append(TUserAccount.id.asc())
            elif val == 'desc':
                #orders.append(TUserAccount.update_time.desc())
                orders.append(TUserAccount.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_user_account_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SUserAccount.parse_obj(t.__dict__) for t in t_user_account_list]


def filter_count_user_account(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TUserAccount)


        if 'id' in items:
            q = q.where(TUserAccount.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUserAccount.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUserAccount.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TUserAccount.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TUserAccount.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TUserAccount.user_id <= items['user_id_end'])
        
        if 'balance' in items:
            q = q.where(TUserAccount.balance == items['balance'])
        if 'balance_start' in items:
            q = q.where(TUserAccount.balance >= items['balance_start'])
        if 'balance_end' in items:
            q = q.where(TUserAccount.balance <= items['balance_end'])
        
        if 'lock_balance' in items:
            q = q.where(TUserAccount.lock_balance == items['lock_balance'])
        if 'lock_balance_start' in items:
            q = q.where(TUserAccount.lock_balance >= items['lock_balance_start'])
        if 'lock_balance_end' in items:
            q = q.where(TUserAccount.lock_balance <= items['lock_balance_end'])
        
        if 'coin' in items:
            q = q.where(TUserAccount.coin == items['coin'])
        if 'coin_start' in items:
            q = q.where(TUserAccount.coin >= items['coin_start'])
        if 'coin_end' in items:
            q = q.where(TUserAccount.coin <= items['coin_end'])
        
        if 'description' in items:
            q = q.where(TUserAccount.description == items['description'])
        if 'description_start' in items:
            q = q.where(TUserAccount.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TUserAccount.description <= items['description_end'])
        
        if 'create_time' in items:
            q = q.where(TUserAccount.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TUserAccount.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TUserAccount.create_time <= items['create_time_end'])
        
        if 'freeze_balance' in items:
            q = q.where(TUserAccount.freeze_balance == items['freeze_balance'])
        if 'freeze_balance_start' in items:
            q = q.where(TUserAccount.freeze_balance >= items['freeze_balance_start'])
        if 'freeze_balance_end' in items:
            q = q.where(TUserAccount.freeze_balance <= items['freeze_balance_end'])
        
        if 'update_time' in items:
            q = q.where(TUserAccount.update_time == items['update_time'])
        if 'update_time_start' in items:
            q = q.where(TUserAccount.update_time >= items['update_time_start'])
        if 'update_time_end' in items:
            q = q.where(TUserAccount.update_time <= items['update_time_end'])
        

        if 'id' in set_items:
            q = q.where(TUserAccount.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TUserAccount.user_id.in_(set_items['user_id']))
        
        if 'balance' in set_items:
            q = q.where(TUserAccount.balance.in_(set_items['balance']))
        
        if 'lock_balance' in set_items:
            q = q.where(TUserAccount.lock_balance.in_(set_items['lock_balance']))
        
        if 'coin' in set_items:
            q = q.where(TUserAccount.coin.in_(set_items['coin']))
        
        if 'description' in set_items:
            q = q.where(TUserAccount.description.in_(set_items['description']))
        
        if 'create_time' in set_items:
            q = q.where(TUserAccount.create_time.in_(set_items['create_time']))
        
        if 'freeze_balance' in set_items:
            q = q.where(TUserAccount.freeze_balance.in_(set_items['freeze_balance']))
        
        if 'update_time' in set_items:
            q = q.where(TUserAccount.update_time.in_(set_items['update_time']))
        

        if 'description' in search_items:
            q = q.where(TUserAccount.description.like(search_items['description']))
        
    
        c = q.count()
        return c

    
def insert_user_bank(item: CreateUserBank, db: Optional[SessionLocal] = None) -> SUserBank:
    data = model2dict(item)
    t = TUserBank(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SUserBank.parse_obj(t.__dict__)

    
def delete_user_bank(user_bank_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TUserBank).where(TUserBank.id == user_bank_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUserBank).where(TUserBank.id == user_bank_id).delete()
        db.commit()

    
def update_user_bank(item: SUserBank, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TUserBank).where(TUserBank.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUserBank).where(TUserBank.id == item.id).update(data)
        db.commit()

    
def get_user_bank(user_bank_id: int) -> Optional[SUserBank]:
    with Dao() as db:
        t = db.query(TUserBank).where(TUserBank.id == user_bank_id).first()
        if t:
            return SUserBank.parse_obj(t.__dict__)
        else:
            return None


def filter_user_bank(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SUserBank]:
    with Dao() as db:
        q = db.query(TUserBank)


        if 'id' in items:
            q = q.where(TUserBank.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUserBank.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUserBank.id <= items['id_end'])
        
        if 'bank_name' in items:
            q = q.where(TUserBank.bank_name == items['bank_name'])
        if 'bank_name_start' in items:
            q = q.where(TUserBank.bank_name >= items['bank_name_start'])
        if 'bank_name_end' in items:
            q = q.where(TUserBank.bank_name <= items['bank_name_end'])
        
        if 'username' in items:
            q = q.where(TUserBank.username == items['username'])
        if 'username_start' in items:
            q = q.where(TUserBank.username >= items['username_start'])
        if 'username_end' in items:
            q = q.where(TUserBank.username <= items['username_end'])
        
        if 'id_card' in items:
            q = q.where(TUserBank.id_card == items['id_card'])
        if 'id_card_start' in items:
            q = q.where(TUserBank.id_card >= items['id_card_start'])
        if 'id_card_end' in items:
            q = q.where(TUserBank.id_card <= items['id_card_end'])
        
        if 'user_id' in items:
            q = q.where(TUserBank.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TUserBank.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TUserBank.user_id <= items['user_id_end'])
        
        if 'phone' in items:
            q = q.where(TUserBank.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TUserBank.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TUserBank.phone <= items['phone_end'])
        
        if 'bank_address' in items:
            q = q.where(TUserBank.bank_address == items['bank_address'])
        if 'bank_address_start' in items:
            q = q.where(TUserBank.bank_address >= items['bank_address_start'])
        if 'bank_address_end' in items:
            q = q.where(TUserBank.bank_address <= items['bank_address_end'])
        
        if 'is_default' in items:
            q = q.where(TUserBank.is_default == items['is_default'])
        if 'is_default_start' in items:
            q = q.where(TUserBank.is_default >= items['is_default_start'])
        if 'is_default_end' in items:
            q = q.where(TUserBank.is_default <= items['is_default_end'])
        

        if 'id' in set_items:
            q = q.where(TUserBank.id.in_(set_items['id']))
        
        if 'bank_name' in set_items:
            q = q.where(TUserBank.bank_name.in_(set_items['bank_name']))
        
        if 'username' in set_items:
            q = q.where(TUserBank.username.in_(set_items['username']))
        
        if 'id_card' in set_items:
            q = q.where(TUserBank.id_card.in_(set_items['id_card']))
        
        if 'user_id' in set_items:
            q = q.where(TUserBank.user_id.in_(set_items['user_id']))
        
        if 'phone' in set_items:
            q = q.where(TUserBank.phone.in_(set_items['phone']))
        
        if 'bank_address' in set_items:
            q = q.where(TUserBank.bank_address.in_(set_items['bank_address']))
        
        if 'is_default' in set_items:
            q = q.where(TUserBank.is_default.in_(set_items['is_default']))
        

        if 'bank_name' in search_items:
            q = q.where(TUserBank.bank_name.like(search_items['bank_name']))
        
        if 'username' in search_items:
            q = q.where(TUserBank.username.like(search_items['username']))
        
        if 'id_card' in search_items:
            q = q.where(TUserBank.id_card.like(search_items['id_card']))
        
        if 'phone' in search_items:
            q = q.where(TUserBank.phone.like(search_items['phone']))
        
        if 'bank_address' in search_items:
            q = q.where(TUserBank.bank_address.like(search_items['bank_address']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TUserBank.is_default.asc())
                orders.append(TUserBank.id.asc())
            elif val == 'desc':
                #orders.append(TUserBank.is_default.desc())
                orders.append(TUserBank.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_user_bank_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SUserBank.parse_obj(t.__dict__) for t in t_user_bank_list]


def filter_count_user_bank(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TUserBank)


        if 'id' in items:
            q = q.where(TUserBank.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUserBank.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUserBank.id <= items['id_end'])
        
        if 'bank_name' in items:
            q = q.where(TUserBank.bank_name == items['bank_name'])
        if 'bank_name_start' in items:
            q = q.where(TUserBank.bank_name >= items['bank_name_start'])
        if 'bank_name_end' in items:
            q = q.where(TUserBank.bank_name <= items['bank_name_end'])
        
        if 'username' in items:
            q = q.where(TUserBank.username == items['username'])
        if 'username_start' in items:
            q = q.where(TUserBank.username >= items['username_start'])
        if 'username_end' in items:
            q = q.where(TUserBank.username <= items['username_end'])
        
        if 'id_card' in items:
            q = q.where(TUserBank.id_card == items['id_card'])
        if 'id_card_start' in items:
            q = q.where(TUserBank.id_card >= items['id_card_start'])
        if 'id_card_end' in items:
            q = q.where(TUserBank.id_card <= items['id_card_end'])
        
        if 'user_id' in items:
            q = q.where(TUserBank.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TUserBank.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TUserBank.user_id <= items['user_id_end'])
        
        if 'phone' in items:
            q = q.where(TUserBank.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TUserBank.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TUserBank.phone <= items['phone_end'])
        
        if 'bank_address' in items:
            q = q.where(TUserBank.bank_address == items['bank_address'])
        if 'bank_address_start' in items:
            q = q.where(TUserBank.bank_address >= items['bank_address_start'])
        if 'bank_address_end' in items:
            q = q.where(TUserBank.bank_address <= items['bank_address_end'])
        
        if 'is_default' in items:
            q = q.where(TUserBank.is_default == items['is_default'])
        if 'is_default_start' in items:
            q = q.where(TUserBank.is_default >= items['is_default_start'])
        if 'is_default_end' in items:
            q = q.where(TUserBank.is_default <= items['is_default_end'])
        

        if 'id' in set_items:
            q = q.where(TUserBank.id.in_(set_items['id']))
        
        if 'bank_name' in set_items:
            q = q.where(TUserBank.bank_name.in_(set_items['bank_name']))
        
        if 'username' in set_items:
            q = q.where(TUserBank.username.in_(set_items['username']))
        
        if 'id_card' in set_items:
            q = q.where(TUserBank.id_card.in_(set_items['id_card']))
        
        if 'user_id' in set_items:
            q = q.where(TUserBank.user_id.in_(set_items['user_id']))
        
        if 'phone' in set_items:
            q = q.where(TUserBank.phone.in_(set_items['phone']))
        
        if 'bank_address' in set_items:
            q = q.where(TUserBank.bank_address.in_(set_items['bank_address']))
        
        if 'is_default' in set_items:
            q = q.where(TUserBank.is_default.in_(set_items['is_default']))
        

        if 'bank_name' in search_items:
            q = q.where(TUserBank.bank_name.like(search_items['bank_name']))
        
        if 'username' in search_items:
            q = q.where(TUserBank.username.like(search_items['username']))
        
        if 'id_card' in search_items:
            q = q.where(TUserBank.id_card.like(search_items['id_card']))
        
        if 'phone' in search_items:
            q = q.where(TUserBank.phone.like(search_items['phone']))
        
        if 'bank_address' in search_items:
            q = q.where(TUserBank.bank_address.like(search_items['bank_address']))
        
    
        c = q.count()
        return c

    
def insert_user_fav(item: CreateUserFav, db: Optional[SessionLocal] = None) -> SUserFav:
    data = model2dict(item)
    t = TUserFav(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SUserFav.parse_obj(t.__dict__)

    
def delete_user_fav(user_fav_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TUserFav).where(TUserFav.id == user_fav_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUserFav).where(TUserFav.id == user_fav_id).delete()
        db.commit()

    
def update_user_fav(item: SUserFav, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TUserFav).where(TUserFav.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUserFav).where(TUserFav.id == item.id).update(data)
        db.commit()

    
def get_user_fav(user_fav_id: int) -> Optional[SUserFav]:
    with Dao() as db:
        t = db.query(TUserFav).where(TUserFav.id == user_fav_id).first()
        if t:
            return SUserFav.parse_obj(t.__dict__)
        else:
            return None


def filter_user_fav(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SUserFav]:
    with Dao() as db:
        q = db.query(TUserFav)


        if 'id' in items:
            q = q.where(TUserFav.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUserFav.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUserFav.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TUserFav.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TUserFav.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TUserFav.user_id <= items['user_id_end'])
        
        if 'good_id' in items:
            q = q.where(TUserFav.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TUserFav.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TUserFav.good_id <= items['good_id_end'])
        
        if 'create_time' in items:
            q = q.where(TUserFav.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TUserFav.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TUserFav.create_time <= items['create_time_end'])
        
        if 'spec_id' in items:
            q = q.where(TUserFav.spec_id == items['spec_id'])
        if 'spec_id_start' in items:
            q = q.where(TUserFav.spec_id >= items['spec_id_start'])
        if 'spec_id_end' in items:
            q = q.where(TUserFav.spec_id <= items['spec_id_end'])
        

        if 'id' in set_items:
            q = q.where(TUserFav.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TUserFav.user_id.in_(set_items['user_id']))
        
        if 'good_id' in set_items:
            q = q.where(TUserFav.good_id.in_(set_items['good_id']))
        
        if 'create_time' in set_items:
            q = q.where(TUserFav.create_time.in_(set_items['create_time']))
        
        if 'spec_id' in set_items:
            q = q.where(TUserFav.spec_id.in_(set_items['spec_id']))
        

    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TUserFav.spec_id.asc())
                orders.append(TUserFav.id.asc())
            elif val == 'desc':
                #orders.append(TUserFav.spec_id.desc())
                orders.append(TUserFav.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_user_fav_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SUserFav.parse_obj(t.__dict__) for t in t_user_fav_list]


def filter_count_user_fav(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TUserFav)


        if 'id' in items:
            q = q.where(TUserFav.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUserFav.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUserFav.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TUserFav.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TUserFav.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TUserFav.user_id <= items['user_id_end'])
        
        if 'good_id' in items:
            q = q.where(TUserFav.good_id == items['good_id'])
        if 'good_id_start' in items:
            q = q.where(TUserFav.good_id >= items['good_id_start'])
        if 'good_id_end' in items:
            q = q.where(TUserFav.good_id <= items['good_id_end'])
        
        if 'create_time' in items:
            q = q.where(TUserFav.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TUserFav.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TUserFav.create_time <= items['create_time_end'])
        
        if 'spec_id' in items:
            q = q.where(TUserFav.spec_id == items['spec_id'])
        if 'spec_id_start' in items:
            q = q.where(TUserFav.spec_id >= items['spec_id_start'])
        if 'spec_id_end' in items:
            q = q.where(TUserFav.spec_id <= items['spec_id_end'])
        

        if 'id' in set_items:
            q = q.where(TUserFav.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TUserFav.user_id.in_(set_items['user_id']))
        
        if 'good_id' in set_items:
            q = q.where(TUserFav.good_id.in_(set_items['good_id']))
        
        if 'create_time' in set_items:
            q = q.where(TUserFav.create_time.in_(set_items['create_time']))
        
        if 'spec_id' in set_items:
            q = q.where(TUserFav.spec_id.in_(set_items['spec_id']))
        

    
        c = q.count()
        return c

    
def insert_user_level(item: CreateUserLevel, db: Optional[SessionLocal] = None) -> SUserLevel:
    data = model2dict(item)
    t = TUserLevel(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SUserLevel.parse_obj(t.__dict__)

    
def delete_user_level(user_level_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TUserLevel).where(TUserLevel.id == user_level_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUserLevel).where(TUserLevel.id == user_level_id).delete()
        db.commit()

    
def update_user_level(item: SUserLevel, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TUserLevel).where(TUserLevel.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUserLevel).where(TUserLevel.id == item.id).update(data)
        db.commit()

    
def get_user_level(user_level_id: int) -> Optional[SUserLevel]:
    with Dao() as db:
        t = db.query(TUserLevel).where(TUserLevel.id == user_level_id).first()
        if t:
            return SUserLevel.parse_obj(t.__dict__)
        else:
            return None


def filter_user_level(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SUserLevel]:
    with Dao() as db:
        q = db.query(TUserLevel)


        if 'id' in items:
            q = q.where(TUserLevel.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUserLevel.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUserLevel.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TUserLevel.title == items['title'])
        if 'title_start' in items:
            q = q.where(TUserLevel.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TUserLevel.title <= items['title_end'])
        

        if 'id' in set_items:
            q = q.where(TUserLevel.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TUserLevel.title.in_(set_items['title']))
        

        if 'title' in search_items:
            q = q.where(TUserLevel.title.like(search_items['title']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TUserLevel.title.asc())
                orders.append(TUserLevel.id.asc())
            elif val == 'desc':
                #orders.append(TUserLevel.title.desc())
                orders.append(TUserLevel.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_user_level_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SUserLevel.parse_obj(t.__dict__) for t in t_user_level_list]


def filter_count_user_level(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TUserLevel)


        if 'id' in items:
            q = q.where(TUserLevel.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUserLevel.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUserLevel.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TUserLevel.title == items['title'])
        if 'title_start' in items:
            q = q.where(TUserLevel.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TUserLevel.title <= items['title_end'])
        

        if 'id' in set_items:
            q = q.where(TUserLevel.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TUserLevel.title.in_(set_items['title']))
        

        if 'title' in search_items:
            q = q.where(TUserLevel.title.like(search_items['title']))
        
    
        c = q.count()
        return c

    
def insert_user_payment_history(item: CreateUserPaymentHistory, db: Optional[SessionLocal] = None) -> SUserPaymentHistory:
    data = model2dict(item)
    t = TUserPaymentHistory(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SUserPaymentHistory.parse_obj(t.__dict__)

    
def delete_user_payment_history(user_payment_history_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TUserPaymentHistory).where(TUserPaymentHistory.id == user_payment_history_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUserPaymentHistory).where(TUserPaymentHistory.id == user_payment_history_id).delete()
        db.commit()

    
def update_user_payment_history(item: SUserPaymentHistory, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TUserPaymentHistory).where(TUserPaymentHistory.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUserPaymentHistory).where(TUserPaymentHistory.id == item.id).update(data)
        db.commit()

    
def get_user_payment_history(user_payment_history_id: int) -> Optional[SUserPaymentHistory]:
    with Dao() as db:
        t = db.query(TUserPaymentHistory).where(TUserPaymentHistory.id == user_payment_history_id).first()
        if t:
            return SUserPaymentHistory.parse_obj(t.__dict__)
        else:
            return None


def filter_user_payment_history(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SUserPaymentHistory]:
    with Dao() as db:
        q = db.query(TUserPaymentHistory)


        if 'id' in items:
            q = q.where(TUserPaymentHistory.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUserPaymentHistory.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUserPaymentHistory.id <= items['id_end'])
        
        if 'fee' in items:
            q = q.where(TUserPaymentHistory.fee == items['fee'])
        if 'fee_start' in items:
            q = q.where(TUserPaymentHistory.fee >= items['fee_start'])
        if 'fee_end' in items:
            q = q.where(TUserPaymentHistory.fee <= items['fee_end'])
        
        if 'create_time' in items:
            q = q.where(TUserPaymentHistory.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TUserPaymentHistory.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TUserPaymentHistory.create_time <= items['create_time_end'])
        
        if 'description' in items:
            q = q.where(TUserPaymentHistory.description == items['description'])
        if 'description_start' in items:
            q = q.where(TUserPaymentHistory.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TUserPaymentHistory.description <= items['description_end'])
        

        if 'id' in set_items:
            q = q.where(TUserPaymentHistory.id.in_(set_items['id']))
        
        if 'fee' in set_items:
            q = q.where(TUserPaymentHistory.fee.in_(set_items['fee']))
        
        if 'create_time' in set_items:
            q = q.where(TUserPaymentHistory.create_time.in_(set_items['create_time']))
        
        if 'description' in set_items:
            q = q.where(TUserPaymentHistory.description.in_(set_items['description']))
        

        if 'description' in search_items:
            q = q.where(TUserPaymentHistory.description.like(search_items['description']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TUserPaymentHistory.description.asc())
                orders.append(TUserPaymentHistory.id.asc())
            elif val == 'desc':
                #orders.append(TUserPaymentHistory.description.desc())
                orders.append(TUserPaymentHistory.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_user_payment_history_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SUserPaymentHistory.parse_obj(t.__dict__) for t in t_user_payment_history_list]


def filter_count_user_payment_history(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TUserPaymentHistory)


        if 'id' in items:
            q = q.where(TUserPaymentHistory.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUserPaymentHistory.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUserPaymentHistory.id <= items['id_end'])
        
        if 'fee' in items:
            q = q.where(TUserPaymentHistory.fee == items['fee'])
        if 'fee_start' in items:
            q = q.where(TUserPaymentHistory.fee >= items['fee_start'])
        if 'fee_end' in items:
            q = q.where(TUserPaymentHistory.fee <= items['fee_end'])
        
        if 'create_time' in items:
            q = q.where(TUserPaymentHistory.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TUserPaymentHistory.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TUserPaymentHistory.create_time <= items['create_time_end'])
        
        if 'description' in items:
            q = q.where(TUserPaymentHistory.description == items['description'])
        if 'description_start' in items:
            q = q.where(TUserPaymentHistory.description >= items['description_start'])
        if 'description_end' in items:
            q = q.where(TUserPaymentHistory.description <= items['description_end'])
        

        if 'id' in set_items:
            q = q.where(TUserPaymentHistory.id.in_(set_items['id']))
        
        if 'fee' in set_items:
            q = q.where(TUserPaymentHistory.fee.in_(set_items['fee']))
        
        if 'create_time' in set_items:
            q = q.where(TUserPaymentHistory.create_time.in_(set_items['create_time']))
        
        if 'description' in set_items:
            q = q.where(TUserPaymentHistory.description.in_(set_items['description']))
        

        if 'description' in search_items:
            q = q.where(TUserPaymentHistory.description.like(search_items['description']))
        
    
        c = q.count()
        return c

    
def insert_user_phone_code(item: CreateUserPhoneCode, db: Optional[SessionLocal] = None) -> SUserPhoneCode:
    data = model2dict(item)
    t = TUserPhoneCode(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SUserPhoneCode.parse_obj(t.__dict__)

    
def delete_user_phone_code(user_phone_code_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TUserPhoneCode).where(TUserPhoneCode.id == user_phone_code_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUserPhoneCode).where(TUserPhoneCode.id == user_phone_code_id).delete()
        db.commit()

    
def update_user_phone_code(item: SUserPhoneCode, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TUserPhoneCode).where(TUserPhoneCode.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUserPhoneCode).where(TUserPhoneCode.id == item.id).update(data)
        db.commit()

    
def get_user_phone_code(user_phone_code_id: int) -> Optional[SUserPhoneCode]:
    with Dao() as db:
        t = db.query(TUserPhoneCode).where(TUserPhoneCode.id == user_phone_code_id).first()
        if t:
            return SUserPhoneCode.parse_obj(t.__dict__)
        else:
            return None


def filter_user_phone_code(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SUserPhoneCode]:
    with Dao() as db:
        q = db.query(TUserPhoneCode)


        if 'id' in items:
            q = q.where(TUserPhoneCode.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUserPhoneCode.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUserPhoneCode.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TUserPhoneCode.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TUserPhoneCode.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TUserPhoneCode.user_id <= items['user_id_end'])
        
        if 'code' in items:
            q = q.where(TUserPhoneCode.code == items['code'])
        if 'code_start' in items:
            q = q.where(TUserPhoneCode.code >= items['code_start'])
        if 'code_end' in items:
            q = q.where(TUserPhoneCode.code <= items['code_end'])
        
        if 'expired_time' in items:
            q = q.where(TUserPhoneCode.expired_time == items['expired_time'])
        if 'expired_time_start' in items:
            q = q.where(TUserPhoneCode.expired_time >= items['expired_time_start'])
        if 'expired_time_end' in items:
            q = q.where(TUserPhoneCode.expired_time <= items['expired_time_end'])
        
        if 'send_time' in items:
            q = q.where(TUserPhoneCode.send_time == items['send_time'])
        if 'send_time_start' in items:
            q = q.where(TUserPhoneCode.send_time >= items['send_time_start'])
        if 'send_time_end' in items:
            q = q.where(TUserPhoneCode.send_time <= items['send_time_end'])
        
        if 'employee_id' in items:
            q = q.where(TUserPhoneCode.employee_id == items['employee_id'])
        if 'employee_id_start' in items:
            q = q.where(TUserPhoneCode.employee_id >= items['employee_id_start'])
        if 'employee_id_end' in items:
            q = q.where(TUserPhoneCode.employee_id <= items['employee_id_end'])
        
        if 'store_owner_id' in items:
            q = q.where(TUserPhoneCode.store_owner_id == items['store_owner_id'])
        if 'store_owner_id_start' in items:
            q = q.where(TUserPhoneCode.store_owner_id >= items['store_owner_id_start'])
        if 'store_owner_id_end' in items:
            q = q.where(TUserPhoneCode.store_owner_id <= items['store_owner_id_end'])
        
        if 'worker_id' in items:
            q = q.where(TUserPhoneCode.worker_id == items['worker_id'])
        if 'worker_id_start' in items:
            q = q.where(TUserPhoneCode.worker_id >= items['worker_id_start'])
        if 'worker_id_end' in items:
            q = q.where(TUserPhoneCode.worker_id <= items['worker_id_end'])
        
        if 'phone' in items:
            q = q.where(TUserPhoneCode.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TUserPhoneCode.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TUserPhoneCode.phone <= items['phone_end'])
        

        if 'id' in set_items:
            q = q.where(TUserPhoneCode.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TUserPhoneCode.user_id.in_(set_items['user_id']))
        
        if 'code' in set_items:
            q = q.where(TUserPhoneCode.code.in_(set_items['code']))
        
        if 'expired_time' in set_items:
            q = q.where(TUserPhoneCode.expired_time.in_(set_items['expired_time']))
        
        if 'send_time' in set_items:
            q = q.where(TUserPhoneCode.send_time.in_(set_items['send_time']))
        
        if 'employee_id' in set_items:
            q = q.where(TUserPhoneCode.employee_id.in_(set_items['employee_id']))
        
        if 'store_owner_id' in set_items:
            q = q.where(TUserPhoneCode.store_owner_id.in_(set_items['store_owner_id']))
        
        if 'worker_id' in set_items:
            q = q.where(TUserPhoneCode.worker_id.in_(set_items['worker_id']))
        
        if 'phone' in set_items:
            q = q.where(TUserPhoneCode.phone.in_(set_items['phone']))
        

        if 'code' in search_items:
            q = q.where(TUserPhoneCode.code.like(search_items['code']))
        
        if 'phone' in search_items:
            q = q.where(TUserPhoneCode.phone.like(search_items['phone']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TUserPhoneCode.phone.asc())
                orders.append(TUserPhoneCode.id.asc())
            elif val == 'desc':
                #orders.append(TUserPhoneCode.phone.desc())
                orders.append(TUserPhoneCode.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_user_phone_code_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SUserPhoneCode.parse_obj(t.__dict__) for t in t_user_phone_code_list]


def filter_count_user_phone_code(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TUserPhoneCode)


        if 'id' in items:
            q = q.where(TUserPhoneCode.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUserPhoneCode.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUserPhoneCode.id <= items['id_end'])
        
        if 'user_id' in items:
            q = q.where(TUserPhoneCode.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TUserPhoneCode.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TUserPhoneCode.user_id <= items['user_id_end'])
        
        if 'code' in items:
            q = q.where(TUserPhoneCode.code == items['code'])
        if 'code_start' in items:
            q = q.where(TUserPhoneCode.code >= items['code_start'])
        if 'code_end' in items:
            q = q.where(TUserPhoneCode.code <= items['code_end'])
        
        if 'expired_time' in items:
            q = q.where(TUserPhoneCode.expired_time == items['expired_time'])
        if 'expired_time_start' in items:
            q = q.where(TUserPhoneCode.expired_time >= items['expired_time_start'])
        if 'expired_time_end' in items:
            q = q.where(TUserPhoneCode.expired_time <= items['expired_time_end'])
        
        if 'send_time' in items:
            q = q.where(TUserPhoneCode.send_time == items['send_time'])
        if 'send_time_start' in items:
            q = q.where(TUserPhoneCode.send_time >= items['send_time_start'])
        if 'send_time_end' in items:
            q = q.where(TUserPhoneCode.send_time <= items['send_time_end'])
        
        if 'employee_id' in items:
            q = q.where(TUserPhoneCode.employee_id == items['employee_id'])
        if 'employee_id_start' in items:
            q = q.where(TUserPhoneCode.employee_id >= items['employee_id_start'])
        if 'employee_id_end' in items:
            q = q.where(TUserPhoneCode.employee_id <= items['employee_id_end'])
        
        if 'store_owner_id' in items:
            q = q.where(TUserPhoneCode.store_owner_id == items['store_owner_id'])
        if 'store_owner_id_start' in items:
            q = q.where(TUserPhoneCode.store_owner_id >= items['store_owner_id_start'])
        if 'store_owner_id_end' in items:
            q = q.where(TUserPhoneCode.store_owner_id <= items['store_owner_id_end'])
        
        if 'worker_id' in items:
            q = q.where(TUserPhoneCode.worker_id == items['worker_id'])
        if 'worker_id_start' in items:
            q = q.where(TUserPhoneCode.worker_id >= items['worker_id_start'])
        if 'worker_id_end' in items:
            q = q.where(TUserPhoneCode.worker_id <= items['worker_id_end'])
        
        if 'phone' in items:
            q = q.where(TUserPhoneCode.phone == items['phone'])
        if 'phone_start' in items:
            q = q.where(TUserPhoneCode.phone >= items['phone_start'])
        if 'phone_end' in items:
            q = q.where(TUserPhoneCode.phone <= items['phone_end'])
        

        if 'id' in set_items:
            q = q.where(TUserPhoneCode.id.in_(set_items['id']))
        
        if 'user_id' in set_items:
            q = q.where(TUserPhoneCode.user_id.in_(set_items['user_id']))
        
        if 'code' in set_items:
            q = q.where(TUserPhoneCode.code.in_(set_items['code']))
        
        if 'expired_time' in set_items:
            q = q.where(TUserPhoneCode.expired_time.in_(set_items['expired_time']))
        
        if 'send_time' in set_items:
            q = q.where(TUserPhoneCode.send_time.in_(set_items['send_time']))
        
        if 'employee_id' in set_items:
            q = q.where(TUserPhoneCode.employee_id.in_(set_items['employee_id']))
        
        if 'store_owner_id' in set_items:
            q = q.where(TUserPhoneCode.store_owner_id.in_(set_items['store_owner_id']))
        
        if 'worker_id' in set_items:
            q = q.where(TUserPhoneCode.worker_id.in_(set_items['worker_id']))
        
        if 'phone' in set_items:
            q = q.where(TUserPhoneCode.phone.in_(set_items['phone']))
        

        if 'code' in search_items:
            q = q.where(TUserPhoneCode.code.like(search_items['code']))
        
        if 'phone' in search_items:
            q = q.where(TUserPhoneCode.phone.like(search_items['phone']))
        
    
        c = q.count()
        return c

    
def insert_user_withdraw(item: CreateUserWithdraw, db: Optional[SessionLocal] = None) -> SUserWithdraw:
    data = model2dict(item)
    t = TUserWithdraw(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SUserWithdraw.parse_obj(t.__dict__)

    
def delete_user_withdraw(user_withdraw_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TUserWithdraw).where(TUserWithdraw.id == user_withdraw_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUserWithdraw).where(TUserWithdraw.id == user_withdraw_id).delete()
        db.commit()

    
def update_user_withdraw(item: SUserWithdraw, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TUserWithdraw).where(TUserWithdraw.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUserWithdraw).where(TUserWithdraw.id == item.id).update(data)
        db.commit()

    
def get_user_withdraw(user_withdraw_id: int) -> Optional[SUserWithdraw]:
    with Dao() as db:
        t = db.query(TUserWithdraw).where(TUserWithdraw.id == user_withdraw_id).first()
        if t:
            return SUserWithdraw.parse_obj(t.__dict__)
        else:
            return None


def filter_user_withdraw(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SUserWithdraw]:
    with Dao() as db:
        q = db.query(TUserWithdraw)


        if 'id' in items:
            q = q.where(TUserWithdraw.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUserWithdraw.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUserWithdraw.id <= items['id_end'])
        
        if 'amount' in items:
            q = q.where(TUserWithdraw.amount == items['amount'])
        if 'amount_start' in items:
            q = q.where(TUserWithdraw.amount >= items['amount_start'])
        if 'amount_end' in items:
            q = q.where(TUserWithdraw.amount <= items['amount_end'])
        
        if 'user_withdraw_status_id' in items:
            q = q.where(TUserWithdraw.user_withdraw_status_id == items['user_withdraw_status_id'])
        if 'user_withdraw_status_id_start' in items:
            q = q.where(TUserWithdraw.user_withdraw_status_id >= items['user_withdraw_status_id_start'])
        if 'user_withdraw_status_id_end' in items:
            q = q.where(TUserWithdraw.user_withdraw_status_id <= items['user_withdraw_status_id_end'])
        
        if 'create_time' in items:
            q = q.where(TUserWithdraw.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TUserWithdraw.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TUserWithdraw.create_time <= items['create_time_end'])
        
        if 'update_time' in items:
            q = q.where(TUserWithdraw.update_time == items['update_time'])
        if 'update_time_start' in items:
            q = q.where(TUserWithdraw.update_time >= items['update_time_start'])
        if 'update_time_end' in items:
            q = q.where(TUserWithdraw.update_time <= items['update_time_end'])
        
        if 'user_id' in items:
            q = q.where(TUserWithdraw.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TUserWithdraw.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TUserWithdraw.user_id <= items['user_id_end'])
        
        if 'type_id' in items:
            q = q.where(TUserWithdraw.type_id == items['type_id'])
        if 'type_id_start' in items:
            q = q.where(TUserWithdraw.type_id >= items['type_id_start'])
        if 'type_id_end' in items:
            q = q.where(TUserWithdraw.type_id <= items['type_id_end'])
        
        if 'user_bank_id' in items:
            q = q.where(TUserWithdraw.user_bank_id == items['user_bank_id'])
        if 'user_bank_id_start' in items:
            q = q.where(TUserWithdraw.user_bank_id >= items['user_bank_id_start'])
        if 'user_bank_id_end' in items:
            q = q.where(TUserWithdraw.user_bank_id <= items['user_bank_id_end'])
        
        if 'operator_id' in items:
            q = q.where(TUserWithdraw.operator_id == items['operator_id'])
        if 'operator_id_start' in items:
            q = q.where(TUserWithdraw.operator_id >= items['operator_id_start'])
        if 'operator_id_end' in items:
            q = q.where(TUserWithdraw.operator_id <= items['operator_id_end'])
        
        if 'fee_type' in items:
            q = q.where(TUserWithdraw.fee_type == items['fee_type'])
        if 'fee_type_start' in items:
            q = q.where(TUserWithdraw.fee_type >= items['fee_type_start'])
        if 'fee_type_end' in items:
            q = q.where(TUserWithdraw.fee_type <= items['fee_type_end'])
        
        if 'fee_pro' in items:
            q = q.where(TUserWithdraw.fee_pro == items['fee_pro'])
        if 'fee_pro_start' in items:
            q = q.where(TUserWithdraw.fee_pro >= items['fee_pro_start'])
        if 'fee_pro_end' in items:
            q = q.where(TUserWithdraw.fee_pro <= items['fee_pro_end'])
        
        if 'out_batch_no' in items:
            q = q.where(TUserWithdraw.out_batch_no == items['out_batch_no'])
        if 'out_batch_no_start' in items:
            q = q.where(TUserWithdraw.out_batch_no >= items['out_batch_no_start'])
        if 'out_batch_no_end' in items:
            q = q.where(TUserWithdraw.out_batch_no <= items['out_batch_no_end'])
        
        if 'batch_name' in items:
            q = q.where(TUserWithdraw.batch_name == items['batch_name'])
        if 'batch_name_start' in items:
            q = q.where(TUserWithdraw.batch_name >= items['batch_name_start'])
        if 'batch_name_end' in items:
            q = q.where(TUserWithdraw.batch_name <= items['batch_name_end'])
        
        if 'batch_remark' in items:
            q = q.where(TUserWithdraw.batch_remark == items['batch_remark'])
        if 'batch_remark_start' in items:
            q = q.where(TUserWithdraw.batch_remark >= items['batch_remark_start'])
        if 'batch_remark_end' in items:
            q = q.where(TUserWithdraw.batch_remark <= items['batch_remark_end'])
        
        if 'out_detail_no' in items:
            q = q.where(TUserWithdraw.out_detail_no == items['out_detail_no'])
        if 'out_detail_no_start' in items:
            q = q.where(TUserWithdraw.out_detail_no >= items['out_detail_no_start'])
        if 'out_detail_no_end' in items:
            q = q.where(TUserWithdraw.out_detail_no <= items['out_detail_no_end'])
        
        if 'user_name' in items:
            q = q.where(TUserWithdraw.user_name == items['user_name'])
        if 'user_name_start' in items:
            q = q.where(TUserWithdraw.user_name >= items['user_name_start'])
        if 'user_name_end' in items:
            q = q.where(TUserWithdraw.user_name <= items['user_name_end'])
        
        if 'user_phone' in items:
            q = q.where(TUserWithdraw.user_phone == items['user_phone'])
        if 'user_phone_start' in items:
            q = q.where(TUserWithdraw.user_phone >= items['user_phone_start'])
        if 'user_phone_end' in items:
            q = q.where(TUserWithdraw.user_phone <= items['user_phone_end'])
        
        if 'fee_balance' in items:
            q = q.where(TUserWithdraw.fee_balance == items['fee_balance'])
        if 'fee_balance_start' in items:
            q = q.where(TUserWithdraw.fee_balance >= items['fee_balance_start'])
        if 'fee_balance_end' in items:
            q = q.where(TUserWithdraw.fee_balance <= items['fee_balance_end'])
        
        if 'deduct_balance' in items:
            q = q.where(TUserWithdraw.deduct_balance == items['deduct_balance'])
        if 'deduct_balance_start' in items:
            q = q.where(TUserWithdraw.deduct_balance >= items['deduct_balance_start'])
        if 'deduct_balance_end' in items:
            q = q.where(TUserWithdraw.deduct_balance <= items['deduct_balance_end'])
        

        if 'id' in set_items:
            q = q.where(TUserWithdraw.id.in_(set_items['id']))
        
        if 'amount' in set_items:
            q = q.where(TUserWithdraw.amount.in_(set_items['amount']))
        
        if 'user_withdraw_status_id' in set_items:
            q = q.where(TUserWithdraw.user_withdraw_status_id.in_(set_items['user_withdraw_status_id']))
        
        if 'create_time' in set_items:
            q = q.where(TUserWithdraw.create_time.in_(set_items['create_time']))
        
        if 'update_time' in set_items:
            q = q.where(TUserWithdraw.update_time.in_(set_items['update_time']))
        
        if 'user_id' in set_items:
            q = q.where(TUserWithdraw.user_id.in_(set_items['user_id']))
        
        if 'type_id' in set_items:
            q = q.where(TUserWithdraw.type_id.in_(set_items['type_id']))
        
        if 'user_bank_id' in set_items:
            q = q.where(TUserWithdraw.user_bank_id.in_(set_items['user_bank_id']))
        
        if 'operator_id' in set_items:
            q = q.where(TUserWithdraw.operator_id.in_(set_items['operator_id']))
        
        if 'fee_type' in set_items:
            q = q.where(TUserWithdraw.fee_type.in_(set_items['fee_type']))
        
        if 'fee_pro' in set_items:
            q = q.where(TUserWithdraw.fee_pro.in_(set_items['fee_pro']))
        
        if 'out_batch_no' in set_items:
            q = q.where(TUserWithdraw.out_batch_no.in_(set_items['out_batch_no']))
        
        if 'batch_name' in set_items:
            q = q.where(TUserWithdraw.batch_name.in_(set_items['batch_name']))
        
        if 'batch_remark' in set_items:
            q = q.where(TUserWithdraw.batch_remark.in_(set_items['batch_remark']))
        
        if 'out_detail_no' in set_items:
            q = q.where(TUserWithdraw.out_detail_no.in_(set_items['out_detail_no']))
        
        if 'user_name' in set_items:
            q = q.where(TUserWithdraw.user_name.in_(set_items['user_name']))
        
        if 'user_phone' in set_items:
            q = q.where(TUserWithdraw.user_phone.in_(set_items['user_phone']))
        
        if 'fee_balance' in set_items:
            q = q.where(TUserWithdraw.fee_balance.in_(set_items['fee_balance']))
        
        if 'deduct_balance' in set_items:
            q = q.where(TUserWithdraw.deduct_balance.in_(set_items['deduct_balance']))
        

        if 'out_batch_no' in search_items:
            q = q.where(TUserWithdraw.out_batch_no.like(search_items['out_batch_no']))
        
        if 'batch_name' in search_items:
            q = q.where(TUserWithdraw.batch_name.like(search_items['batch_name']))
        
        if 'batch_remark' in search_items:
            q = q.where(TUserWithdraw.batch_remark.like(search_items['batch_remark']))
        
        if 'out_detail_no' in search_items:
            q = q.where(TUserWithdraw.out_detail_no.like(search_items['out_detail_no']))
        
        if 'user_name' in search_items:
            q = q.where(TUserWithdraw.user_name.like(search_items['user_name']))
        
        if 'user_phone' in search_items:
            q = q.where(TUserWithdraw.user_phone.like(search_items['user_phone']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TUserWithdraw.deduct_balance.asc())
                orders.append(TUserWithdraw.id.asc())
            elif val == 'desc':
                #orders.append(TUserWithdraw.deduct_balance.desc())
                orders.append(TUserWithdraw.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_user_withdraw_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SUserWithdraw.parse_obj(t.__dict__) for t in t_user_withdraw_list]


def filter_count_user_withdraw(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TUserWithdraw)


        if 'id' in items:
            q = q.where(TUserWithdraw.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUserWithdraw.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUserWithdraw.id <= items['id_end'])
        
        if 'amount' in items:
            q = q.where(TUserWithdraw.amount == items['amount'])
        if 'amount_start' in items:
            q = q.where(TUserWithdraw.amount >= items['amount_start'])
        if 'amount_end' in items:
            q = q.where(TUserWithdraw.amount <= items['amount_end'])
        
        if 'user_withdraw_status_id' in items:
            q = q.where(TUserWithdraw.user_withdraw_status_id == items['user_withdraw_status_id'])
        if 'user_withdraw_status_id_start' in items:
            q = q.where(TUserWithdraw.user_withdraw_status_id >= items['user_withdraw_status_id_start'])
        if 'user_withdraw_status_id_end' in items:
            q = q.where(TUserWithdraw.user_withdraw_status_id <= items['user_withdraw_status_id_end'])
        
        if 'create_time' in items:
            q = q.where(TUserWithdraw.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TUserWithdraw.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TUserWithdraw.create_time <= items['create_time_end'])
        
        if 'update_time' in items:
            q = q.where(TUserWithdraw.update_time == items['update_time'])
        if 'update_time_start' in items:
            q = q.where(TUserWithdraw.update_time >= items['update_time_start'])
        if 'update_time_end' in items:
            q = q.where(TUserWithdraw.update_time <= items['update_time_end'])
        
        if 'user_id' in items:
            q = q.where(TUserWithdraw.user_id == items['user_id'])
        if 'user_id_start' in items:
            q = q.where(TUserWithdraw.user_id >= items['user_id_start'])
        if 'user_id_end' in items:
            q = q.where(TUserWithdraw.user_id <= items['user_id_end'])
        
        if 'type_id' in items:
            q = q.where(TUserWithdraw.type_id == items['type_id'])
        if 'type_id_start' in items:
            q = q.where(TUserWithdraw.type_id >= items['type_id_start'])
        if 'type_id_end' in items:
            q = q.where(TUserWithdraw.type_id <= items['type_id_end'])
        
        if 'user_bank_id' in items:
            q = q.where(TUserWithdraw.user_bank_id == items['user_bank_id'])
        if 'user_bank_id_start' in items:
            q = q.where(TUserWithdraw.user_bank_id >= items['user_bank_id_start'])
        if 'user_bank_id_end' in items:
            q = q.where(TUserWithdraw.user_bank_id <= items['user_bank_id_end'])
        
        if 'operator_id' in items:
            q = q.where(TUserWithdraw.operator_id == items['operator_id'])
        if 'operator_id_start' in items:
            q = q.where(TUserWithdraw.operator_id >= items['operator_id_start'])
        if 'operator_id_end' in items:
            q = q.where(TUserWithdraw.operator_id <= items['operator_id_end'])
        
        if 'fee_type' in items:
            q = q.where(TUserWithdraw.fee_type == items['fee_type'])
        if 'fee_type_start' in items:
            q = q.where(TUserWithdraw.fee_type >= items['fee_type_start'])
        if 'fee_type_end' in items:
            q = q.where(TUserWithdraw.fee_type <= items['fee_type_end'])
        
        if 'fee_pro' in items:
            q = q.where(TUserWithdraw.fee_pro == items['fee_pro'])
        if 'fee_pro_start' in items:
            q = q.where(TUserWithdraw.fee_pro >= items['fee_pro_start'])
        if 'fee_pro_end' in items:
            q = q.where(TUserWithdraw.fee_pro <= items['fee_pro_end'])
        
        if 'out_batch_no' in items:
            q = q.where(TUserWithdraw.out_batch_no == items['out_batch_no'])
        if 'out_batch_no_start' in items:
            q = q.where(TUserWithdraw.out_batch_no >= items['out_batch_no_start'])
        if 'out_batch_no_end' in items:
            q = q.where(TUserWithdraw.out_batch_no <= items['out_batch_no_end'])
        
        if 'batch_name' in items:
            q = q.where(TUserWithdraw.batch_name == items['batch_name'])
        if 'batch_name_start' in items:
            q = q.where(TUserWithdraw.batch_name >= items['batch_name_start'])
        if 'batch_name_end' in items:
            q = q.where(TUserWithdraw.batch_name <= items['batch_name_end'])
        
        if 'batch_remark' in items:
            q = q.where(TUserWithdraw.batch_remark == items['batch_remark'])
        if 'batch_remark_start' in items:
            q = q.where(TUserWithdraw.batch_remark >= items['batch_remark_start'])
        if 'batch_remark_end' in items:
            q = q.where(TUserWithdraw.batch_remark <= items['batch_remark_end'])
        
        if 'out_detail_no' in items:
            q = q.where(TUserWithdraw.out_detail_no == items['out_detail_no'])
        if 'out_detail_no_start' in items:
            q = q.where(TUserWithdraw.out_detail_no >= items['out_detail_no_start'])
        if 'out_detail_no_end' in items:
            q = q.where(TUserWithdraw.out_detail_no <= items['out_detail_no_end'])
        
        if 'user_name' in items:
            q = q.where(TUserWithdraw.user_name == items['user_name'])
        if 'user_name_start' in items:
            q = q.where(TUserWithdraw.user_name >= items['user_name_start'])
        if 'user_name_end' in items:
            q = q.where(TUserWithdraw.user_name <= items['user_name_end'])
        
        if 'user_phone' in items:
            q = q.where(TUserWithdraw.user_phone == items['user_phone'])
        if 'user_phone_start' in items:
            q = q.where(TUserWithdraw.user_phone >= items['user_phone_start'])
        if 'user_phone_end' in items:
            q = q.where(TUserWithdraw.user_phone <= items['user_phone_end'])
        
        if 'fee_balance' in items:
            q = q.where(TUserWithdraw.fee_balance == items['fee_balance'])
        if 'fee_balance_start' in items:
            q = q.where(TUserWithdraw.fee_balance >= items['fee_balance_start'])
        if 'fee_balance_end' in items:
            q = q.where(TUserWithdraw.fee_balance <= items['fee_balance_end'])
        
        if 'deduct_balance' in items:
            q = q.where(TUserWithdraw.deduct_balance == items['deduct_balance'])
        if 'deduct_balance_start' in items:
            q = q.where(TUserWithdraw.deduct_balance >= items['deduct_balance_start'])
        if 'deduct_balance_end' in items:
            q = q.where(TUserWithdraw.deduct_balance <= items['deduct_balance_end'])
        

        if 'id' in set_items:
            q = q.where(TUserWithdraw.id.in_(set_items['id']))
        
        if 'amount' in set_items:
            q = q.where(TUserWithdraw.amount.in_(set_items['amount']))
        
        if 'user_withdraw_status_id' in set_items:
            q = q.where(TUserWithdraw.user_withdraw_status_id.in_(set_items['user_withdraw_status_id']))
        
        if 'create_time' in set_items:
            q = q.where(TUserWithdraw.create_time.in_(set_items['create_time']))
        
        if 'update_time' in set_items:
            q = q.where(TUserWithdraw.update_time.in_(set_items['update_time']))
        
        if 'user_id' in set_items:
            q = q.where(TUserWithdraw.user_id.in_(set_items['user_id']))
        
        if 'type_id' in set_items:
            q = q.where(TUserWithdraw.type_id.in_(set_items['type_id']))
        
        if 'user_bank_id' in set_items:
            q = q.where(TUserWithdraw.user_bank_id.in_(set_items['user_bank_id']))
        
        if 'operator_id' in set_items:
            q = q.where(TUserWithdraw.operator_id.in_(set_items['operator_id']))
        
        if 'fee_type' in set_items:
            q = q.where(TUserWithdraw.fee_type.in_(set_items['fee_type']))
        
        if 'fee_pro' in set_items:
            q = q.where(TUserWithdraw.fee_pro.in_(set_items['fee_pro']))
        
        if 'out_batch_no' in set_items:
            q = q.where(TUserWithdraw.out_batch_no.in_(set_items['out_batch_no']))
        
        if 'batch_name' in set_items:
            q = q.where(TUserWithdraw.batch_name.in_(set_items['batch_name']))
        
        if 'batch_remark' in set_items:
            q = q.where(TUserWithdraw.batch_remark.in_(set_items['batch_remark']))
        
        if 'out_detail_no' in set_items:
            q = q.where(TUserWithdraw.out_detail_no.in_(set_items['out_detail_no']))
        
        if 'user_name' in set_items:
            q = q.where(TUserWithdraw.user_name.in_(set_items['user_name']))
        
        if 'user_phone' in set_items:
            q = q.where(TUserWithdraw.user_phone.in_(set_items['user_phone']))
        
        if 'fee_balance' in set_items:
            q = q.where(TUserWithdraw.fee_balance.in_(set_items['fee_balance']))
        
        if 'deduct_balance' in set_items:
            q = q.where(TUserWithdraw.deduct_balance.in_(set_items['deduct_balance']))
        

        if 'out_batch_no' in search_items:
            q = q.where(TUserWithdraw.out_batch_no.like(search_items['out_batch_no']))
        
        if 'batch_name' in search_items:
            q = q.where(TUserWithdraw.batch_name.like(search_items['batch_name']))
        
        if 'batch_remark' in search_items:
            q = q.where(TUserWithdraw.batch_remark.like(search_items['batch_remark']))
        
        if 'out_detail_no' in search_items:
            q = q.where(TUserWithdraw.out_detail_no.like(search_items['out_detail_no']))
        
        if 'user_name' in search_items:
            q = q.where(TUserWithdraw.user_name.like(search_items['user_name']))
        
        if 'user_phone' in search_items:
            q = q.where(TUserWithdraw.user_phone.like(search_items['user_phone']))
        
    
        c = q.count()
        return c

    
def insert_user_withdraw_status(item: CreateUserWithdrawStatus, db: Optional[SessionLocal] = None) -> SUserWithdrawStatus:
    data = model2dict(item)
    t = TUserWithdrawStatus(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SUserWithdrawStatus.parse_obj(t.__dict__)

    
def delete_user_withdraw_status(user_withdraw_status_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TUserWithdrawStatus).where(TUserWithdrawStatus.id == user_withdraw_status_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUserWithdrawStatus).where(TUserWithdrawStatus.id == user_withdraw_status_id).delete()
        db.commit()

    
def update_user_withdraw_status(item: SUserWithdrawStatus, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TUserWithdrawStatus).where(TUserWithdrawStatus.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUserWithdrawStatus).where(TUserWithdrawStatus.id == item.id).update(data)
        db.commit()

    
def get_user_withdraw_status(user_withdraw_status_id: int) -> Optional[SUserWithdrawStatus]:
    with Dao() as db:
        t = db.query(TUserWithdrawStatus).where(TUserWithdrawStatus.id == user_withdraw_status_id).first()
        if t:
            return SUserWithdrawStatus.parse_obj(t.__dict__)
        else:
            return None


def filter_user_withdraw_status(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SUserWithdrawStatus]:
    with Dao() as db:
        q = db.query(TUserWithdrawStatus)


        if 'id' in items:
            q = q.where(TUserWithdrawStatus.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUserWithdrawStatus.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUserWithdrawStatus.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TUserWithdrawStatus.title == items['title'])
        if 'title_start' in items:
            q = q.where(TUserWithdrawStatus.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TUserWithdrawStatus.title <= items['title_end'])
        

        if 'id' in set_items:
            q = q.where(TUserWithdrawStatus.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TUserWithdrawStatus.title.in_(set_items['title']))
        

        if 'title' in search_items:
            q = q.where(TUserWithdrawStatus.title.like(search_items['title']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TUserWithdrawStatus.title.asc())
                orders.append(TUserWithdrawStatus.id.asc())
            elif val == 'desc':
                #orders.append(TUserWithdrawStatus.title.desc())
                orders.append(TUserWithdrawStatus.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_user_withdraw_status_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SUserWithdrawStatus.parse_obj(t.__dict__) for t in t_user_withdraw_status_list]


def filter_count_user_withdraw_status(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TUserWithdrawStatus)


        if 'id' in items:
            q = q.where(TUserWithdrawStatus.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUserWithdrawStatus.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUserWithdrawStatus.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TUserWithdrawStatus.title == items['title'])
        if 'title_start' in items:
            q = q.where(TUserWithdrawStatus.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TUserWithdrawStatus.title <= items['title_end'])
        

        if 'id' in set_items:
            q = q.where(TUserWithdrawStatus.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TUserWithdrawStatus.title.in_(set_items['title']))
        

        if 'title' in search_items:
            q = q.where(TUserWithdrawStatus.title.like(search_items['title']))
        
    
        c = q.count()
        return c

    
def insert_user_withdraw_type(item: CreateUserWithdrawType, db: Optional[SessionLocal] = None) -> SUserWithdrawType:
    data = model2dict(item)
    t = TUserWithdrawType(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SUserWithdrawType.parse_obj(t.__dict__)

    
def delete_user_withdraw_type(user_withdraw_type_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TUserWithdrawType).where(TUserWithdrawType.id == user_withdraw_type_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUserWithdrawType).where(TUserWithdrawType.id == user_withdraw_type_id).delete()
        db.commit()

    
def update_user_withdraw_type(item: SUserWithdrawType, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TUserWithdrawType).where(TUserWithdrawType.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TUserWithdrawType).where(TUserWithdrawType.id == item.id).update(data)
        db.commit()

    
def get_user_withdraw_type(user_withdraw_type_id: int) -> Optional[SUserWithdrawType]:
    with Dao() as db:
        t = db.query(TUserWithdrawType).where(TUserWithdrawType.id == user_withdraw_type_id).first()
        if t:
            return SUserWithdrawType.parse_obj(t.__dict__)
        else:
            return None


def filter_user_withdraw_type(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SUserWithdrawType]:
    with Dao() as db:
        q = db.query(TUserWithdrawType)


        if 'id' in items:
            q = q.where(TUserWithdrawType.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUserWithdrawType.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUserWithdrawType.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TUserWithdrawType.title == items['title'])
        if 'title_start' in items:
            q = q.where(TUserWithdrawType.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TUserWithdrawType.title <= items['title_end'])
        

        if 'id' in set_items:
            q = q.where(TUserWithdrawType.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TUserWithdrawType.title.in_(set_items['title']))
        

        if 'title' in search_items:
            q = q.where(TUserWithdrawType.title.like(search_items['title']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TUserWithdrawType.title.asc())
                orders.append(TUserWithdrawType.id.asc())
            elif val == 'desc':
                #orders.append(TUserWithdrawType.title.desc())
                orders.append(TUserWithdrawType.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_user_withdraw_type_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SUserWithdrawType.parse_obj(t.__dict__) for t in t_user_withdraw_type_list]


def filter_count_user_withdraw_type(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TUserWithdrawType)


        if 'id' in items:
            q = q.where(TUserWithdrawType.id == items['id'])
        if 'id_start' in items:
            q = q.where(TUserWithdrawType.id >= items['id_start'])
        if 'id_end' in items:
            q = q.where(TUserWithdrawType.id <= items['id_end'])
        
        if 'title' in items:
            q = q.where(TUserWithdrawType.title == items['title'])
        if 'title_start' in items:
            q = q.where(TUserWithdrawType.title >= items['title_start'])
        if 'title_end' in items:
            q = q.where(TUserWithdrawType.title <= items['title_end'])
        

        if 'id' in set_items:
            q = q.where(TUserWithdrawType.id.in_(set_items['id']))
        
        if 'title' in set_items:
            q = q.where(TUserWithdrawType.title.in_(set_items['title']))
        

        if 'title' in search_items:
            q = q.where(TUserWithdrawType.title.like(search_items['title']))
        
    
        c = q.count()
        return c
