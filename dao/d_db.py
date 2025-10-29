from common import Dao
from common.db import SessionLocal
from typing import List
from model.m_schema import *
from model.schema import *
from fastapi.exceptions import HTTPException

def model2dict(item) -> dict:
    return {key: val for key, val in item.dict().items() if val is not None}

    
def insert_chinese_point_subject(item: CreateChinesePointSubject, db: Optional[SessionLocal] = None) -> SChinesePointSubject:
    data = model2dict(item)
    t = TChinesePointSubject(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SChinesePointSubject.parse_obj(t.__dict__)

    
def delete_chinese_point_subject(chinese_point_subject_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TChinesePointSubject).where(TChinesePointSubject.id == chinese_point_subject_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TChinesePointSubject).where(TChinesePointSubject.id == chinese_point_subject_id).delete()
        db.commit()

    
def update_chinese_point_subject(item: SChinesePointSubject, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TChinesePointSubject).where(TChinesePointSubject.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TChinesePointSubject).where(TChinesePointSubject.id == item.id).update(data)
        db.commit()

    
def get_chinese_point_subject(chinese_point_subject_id: int) -> Optional[SChinesePointSubject]:
    with Dao() as db:
        t = db.query(TChinesePointSubject).where(TChinesePointSubject.id == chinese_point_subject_id).first()
        if t:
            return SChinesePointSubject.parse_obj(t.__dict__)
        else:
            return None


def filter_chinese_point_subject(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SChinesePointSubject]:
    with Dao() as db:
        q = db.query(TChinesePointSubject)


        if 'cps_id' in items:
            q = q.where(TChinesePointSubject.cps_id == items['cps_id'])
        if 'cps_id_start' in items:
            q = q.where(TChinesePointSubject.cps_id >= items['cps_id_start'])
        if 'cps_id_end' in items:
            q = q.where(TChinesePointSubject.cps_id <= items['cps_id_end'])
        
        if 'create_time' in items:
            q = q.where(TChinesePointSubject.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TChinesePointSubject.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TChinesePointSubject.create_time <= items['create_time_end'])
        
        if 'cps_content' in items:
            q = q.where(TChinesePointSubject.cps_content == items['cps_content'])
        if 'cps_content_start' in items:
            q = q.where(TChinesePointSubject.cps_content >= items['cps_content_start'])
        if 'cps_content_end' in items:
            q = q.where(TChinesePointSubject.cps_content <= items['cps_content_end'])
        
        if 'cps_create_name' in items:
            q = q.where(TChinesePointSubject.cps_create_name == items['cps_create_name'])
        if 'cps_create_name_start' in items:
            q = q.where(TChinesePointSubject.cps_create_name >= items['cps_create_name_start'])
        if 'cps_create_name_end' in items:
            q = q.where(TChinesePointSubject.cps_create_name <= items['cps_create_name_end'])
        
        if 'class_id' in items:
            q = q.where(TChinesePointSubject.class_id == items['class_id'])
        if 'class_id_start' in items:
            q = q.where(TChinesePointSubject.class_id >= items['class_id_start'])
        if 'class_id_end' in items:
            q = q.where(TChinesePointSubject.class_id <= items['class_id_end'])
        
        if 'subject_id' in items:
            q = q.where(TChinesePointSubject.subject_id == items['subject_id'])
        if 'subject_id_start' in items:
            q = q.where(TChinesePointSubject.subject_id >= items['subject_id_start'])
        if 'subject_id_end' in items:
            q = q.where(TChinesePointSubject.subject_id <= items['subject_id_end'])
        
        if 'knowledge_id' in items:
            q = q.where(TChinesePointSubject.knowledge_id == items['knowledge_id'])
        if 'knowledge_id_start' in items:
            q = q.where(TChinesePointSubject.knowledge_id >= items['knowledge_id_start'])
        if 'knowledge_id_end' in items:
            q = q.where(TChinesePointSubject.knowledge_id <= items['knowledge_id_end'])
        
        if 'answer_txt' in items:
            q = q.where(TChinesePointSubject.answer_txt == items['answer_txt'])
        if 'answer_txt_start' in items:
            q = q.where(TChinesePointSubject.answer_txt >= items['answer_txt_start'])
        if 'answer_txt_end' in items:
            q = q.where(TChinesePointSubject.answer_txt <= items['answer_txt_end'])
        
        if 'answer_pic_path' in items:
            q = q.where(TChinesePointSubject.answer_pic_path == items['answer_pic_path'])
        if 'answer_pic_path_start' in items:
            q = q.where(TChinesePointSubject.answer_pic_path >= items['answer_pic_path_start'])
        if 'answer_pic_path_end' in items:
            q = q.where(TChinesePointSubject.answer_pic_path <= items['answer_pic_path_end'])
        
        if 'answer_audio_path' in items:
            q = q.where(TChinesePointSubject.answer_audio_path == items['answer_audio_path'])
        if 'answer_audio_path_start' in items:
            q = q.where(TChinesePointSubject.answer_audio_path >= items['answer_audio_path_start'])
        if 'answer_audio_path_end' in items:
            q = q.where(TChinesePointSubject.answer_audio_path <= items['answer_audio_path_end'])
        
        if 'knowledge_list' in items:
            q = q.where(TChinesePointSubject.knowledge_list == items['knowledge_list'])
        if 'knowledge_list_start' in items:
            q = q.where(TChinesePointSubject.knowledge_list >= items['knowledge_list_start'])
        if 'knowledge_list_end' in items:
            q = q.where(TChinesePointSubject.knowledge_list <= items['knowledge_list_end'])
        

        if 'cps_id' in set_items:
            q = q.where(TChinesePointSubject.cps_id.in_(set_items['cps_id']))
        
        if 'create_time' in set_items:
            q = q.where(TChinesePointSubject.create_time.in_(set_items['create_time']))
        
        if 'cps_content' in set_items:
            q = q.where(TChinesePointSubject.cps_content.in_(set_items['cps_content']))
        
        if 'cps_create_name' in set_items:
            q = q.where(TChinesePointSubject.cps_create_name.in_(set_items['cps_create_name']))
        
        if 'class_id' in set_items:
            q = q.where(TChinesePointSubject.class_id.in_(set_items['class_id']))
        
        if 'subject_id' in set_items:
            q = q.where(TChinesePointSubject.subject_id.in_(set_items['subject_id']))
        
        if 'knowledge_id' in set_items:
            q = q.where(TChinesePointSubject.knowledge_id.in_(set_items['knowledge_id']))
        
        if 'answer_txt' in set_items:
            q = q.where(TChinesePointSubject.answer_txt.in_(set_items['answer_txt']))
        
        if 'answer_pic_path' in set_items:
            q = q.where(TChinesePointSubject.answer_pic_path.in_(set_items['answer_pic_path']))
        
        if 'answer_audio_path' in set_items:
            q = q.where(TChinesePointSubject.answer_audio_path.in_(set_items['answer_audio_path']))
        
        if 'knowledge_list' in set_items:
            q = q.where(TChinesePointSubject.knowledge_list.in_(set_items['knowledge_list']))
        

        if 'cps_content' in search_items:
            q = q.where(TChinesePointSubject.cps_content.like(search_items['cps_content']))
        
        if 'cps_create_name' in search_items:
            q = q.where(TChinesePointSubject.cps_create_name.like(search_items['cps_create_name']))
        
        if 'answer_txt' in search_items:
            q = q.where(TChinesePointSubject.answer_txt.like(search_items['answer_txt']))
        
        if 'answer_pic_path' in search_items:
            q = q.where(TChinesePointSubject.answer_pic_path.like(search_items['answer_pic_path']))
        
        if 'answer_audio_path' in search_items:
            q = q.where(TChinesePointSubject.answer_audio_path.like(search_items['answer_audio_path']))
        
        if 'knowledge_list' in search_items:
            q = q.where(TChinesePointSubject.knowledge_list.like(search_items['knowledge_list']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TChinesePointSubject.knowledge_list.asc())
                orders.append(TChinesePointSubject.id.asc())
            elif val == 'desc':
                #orders.append(TChinesePointSubject.knowledge_list.desc())
                orders.append(TChinesePointSubject.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_chinese_point_subject_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SChinesePointSubject.parse_obj(t.__dict__) for t in t_chinese_point_subject_list]


def filter_count_chinese_point_subject(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TChinesePointSubject)


        if 'cps_id' in items:
            q = q.where(TChinesePointSubject.cps_id == items['cps_id'])
        if 'cps_id_start' in items:
            q = q.where(TChinesePointSubject.cps_id >= items['cps_id_start'])
        if 'cps_id_end' in items:
            q = q.where(TChinesePointSubject.cps_id <= items['cps_id_end'])
        
        if 'create_time' in items:
            q = q.where(TChinesePointSubject.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TChinesePointSubject.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TChinesePointSubject.create_time <= items['create_time_end'])
        
        if 'cps_content' in items:
            q = q.where(TChinesePointSubject.cps_content == items['cps_content'])
        if 'cps_content_start' in items:
            q = q.where(TChinesePointSubject.cps_content >= items['cps_content_start'])
        if 'cps_content_end' in items:
            q = q.where(TChinesePointSubject.cps_content <= items['cps_content_end'])
        
        if 'cps_create_name' in items:
            q = q.where(TChinesePointSubject.cps_create_name == items['cps_create_name'])
        if 'cps_create_name_start' in items:
            q = q.where(TChinesePointSubject.cps_create_name >= items['cps_create_name_start'])
        if 'cps_create_name_end' in items:
            q = q.where(TChinesePointSubject.cps_create_name <= items['cps_create_name_end'])
        
        if 'class_id' in items:
            q = q.where(TChinesePointSubject.class_id == items['class_id'])
        if 'class_id_start' in items:
            q = q.where(TChinesePointSubject.class_id >= items['class_id_start'])
        if 'class_id_end' in items:
            q = q.where(TChinesePointSubject.class_id <= items['class_id_end'])
        
        if 'subject_id' in items:
            q = q.where(TChinesePointSubject.subject_id == items['subject_id'])
        if 'subject_id_start' in items:
            q = q.where(TChinesePointSubject.subject_id >= items['subject_id_start'])
        if 'subject_id_end' in items:
            q = q.where(TChinesePointSubject.subject_id <= items['subject_id_end'])
        
        if 'knowledge_id' in items:
            q = q.where(TChinesePointSubject.knowledge_id == items['knowledge_id'])
        if 'knowledge_id_start' in items:
            q = q.where(TChinesePointSubject.knowledge_id >= items['knowledge_id_start'])
        if 'knowledge_id_end' in items:
            q = q.where(TChinesePointSubject.knowledge_id <= items['knowledge_id_end'])
        
        if 'answer_txt' in items:
            q = q.where(TChinesePointSubject.answer_txt == items['answer_txt'])
        if 'answer_txt_start' in items:
            q = q.where(TChinesePointSubject.answer_txt >= items['answer_txt_start'])
        if 'answer_txt_end' in items:
            q = q.where(TChinesePointSubject.answer_txt <= items['answer_txt_end'])
        
        if 'answer_pic_path' in items:
            q = q.where(TChinesePointSubject.answer_pic_path == items['answer_pic_path'])
        if 'answer_pic_path_start' in items:
            q = q.where(TChinesePointSubject.answer_pic_path >= items['answer_pic_path_start'])
        if 'answer_pic_path_end' in items:
            q = q.where(TChinesePointSubject.answer_pic_path <= items['answer_pic_path_end'])
        
        if 'answer_audio_path' in items:
            q = q.where(TChinesePointSubject.answer_audio_path == items['answer_audio_path'])
        if 'answer_audio_path_start' in items:
            q = q.where(TChinesePointSubject.answer_audio_path >= items['answer_audio_path_start'])
        if 'answer_audio_path_end' in items:
            q = q.where(TChinesePointSubject.answer_audio_path <= items['answer_audio_path_end'])
        
        if 'knowledge_list' in items:
            q = q.where(TChinesePointSubject.knowledge_list == items['knowledge_list'])
        if 'knowledge_list_start' in items:
            q = q.where(TChinesePointSubject.knowledge_list >= items['knowledge_list_start'])
        if 'knowledge_list_end' in items:
            q = q.where(TChinesePointSubject.knowledge_list <= items['knowledge_list_end'])
        

        if 'cps_id' in set_items:
            q = q.where(TChinesePointSubject.cps_id.in_(set_items['cps_id']))
        
        if 'create_time' in set_items:
            q = q.where(TChinesePointSubject.create_time.in_(set_items['create_time']))
        
        if 'cps_content' in set_items:
            q = q.where(TChinesePointSubject.cps_content.in_(set_items['cps_content']))
        
        if 'cps_create_name' in set_items:
            q = q.where(TChinesePointSubject.cps_create_name.in_(set_items['cps_create_name']))
        
        if 'class_id' in set_items:
            q = q.where(TChinesePointSubject.class_id.in_(set_items['class_id']))
        
        if 'subject_id' in set_items:
            q = q.where(TChinesePointSubject.subject_id.in_(set_items['subject_id']))
        
        if 'knowledge_id' in set_items:
            q = q.where(TChinesePointSubject.knowledge_id.in_(set_items['knowledge_id']))
        
        if 'answer_txt' in set_items:
            q = q.where(TChinesePointSubject.answer_txt.in_(set_items['answer_txt']))
        
        if 'answer_pic_path' in set_items:
            q = q.where(TChinesePointSubject.answer_pic_path.in_(set_items['answer_pic_path']))
        
        if 'answer_audio_path' in set_items:
            q = q.where(TChinesePointSubject.answer_audio_path.in_(set_items['answer_audio_path']))
        
        if 'knowledge_list' in set_items:
            q = q.where(TChinesePointSubject.knowledge_list.in_(set_items['knowledge_list']))
        

        if 'cps_content' in search_items:
            q = q.where(TChinesePointSubject.cps_content.like(search_items['cps_content']))
        
        if 'cps_create_name' in search_items:
            q = q.where(TChinesePointSubject.cps_create_name.like(search_items['cps_create_name']))
        
        if 'answer_txt' in search_items:
            q = q.where(TChinesePointSubject.answer_txt.like(search_items['answer_txt']))
        
        if 'answer_pic_path' in search_items:
            q = q.where(TChinesePointSubject.answer_pic_path.like(search_items['answer_pic_path']))
        
        if 'answer_audio_path' in search_items:
            q = q.where(TChinesePointSubject.answer_audio_path.like(search_items['answer_audio_path']))
        
        if 'knowledge_list' in search_items:
            q = q.where(TChinesePointSubject.knowledge_list.like(search_items['knowledge_list']))
        
    
        c = q.count()
        return c

    
def insert_english_point_subject(item: CreateEnglishPointSubject, db: Optional[SessionLocal] = None) -> SEnglishPointSubject:
    data = model2dict(item)
    t = TEnglishPointSubject(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SEnglishPointSubject.parse_obj(t.__dict__)

    
def delete_english_point_subject(english_point_subject_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TEnglishPointSubject).where(TEnglishPointSubject.id == english_point_subject_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TEnglishPointSubject).where(TEnglishPointSubject.id == english_point_subject_id).delete()
        db.commit()

    
def update_english_point_subject(item: SEnglishPointSubject, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TEnglishPointSubject).where(TEnglishPointSubject.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TEnglishPointSubject).where(TEnglishPointSubject.id == item.id).update(data)
        db.commit()

    
def get_english_point_subject(english_point_subject_id: int) -> Optional[SEnglishPointSubject]:
    with Dao() as db:
        t = db.query(TEnglishPointSubject).where(TEnglishPointSubject.id == english_point_subject_id).first()
        if t:
            return SEnglishPointSubject.parse_obj(t.__dict__)
        else:
            return None


def filter_english_point_subject(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SEnglishPointSubject]:
    with Dao() as db:
        q = db.query(TEnglishPointSubject)


        if 'eps_id' in items:
            q = q.where(TEnglishPointSubject.eps_id == items['eps_id'])
        if 'eps_id_start' in items:
            q = q.where(TEnglishPointSubject.eps_id >= items['eps_id_start'])
        if 'eps_id_end' in items:
            q = q.where(TEnglishPointSubject.eps_id <= items['eps_id_end'])
        
        if 'create_time' in items:
            q = q.where(TEnglishPointSubject.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TEnglishPointSubject.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TEnglishPointSubject.create_time <= items['create_time_end'])
        
        if 'eps_content' in items:
            q = q.where(TEnglishPointSubject.eps_content == items['eps_content'])
        if 'eps_content_start' in items:
            q = q.where(TEnglishPointSubject.eps_content >= items['eps_content_start'])
        if 'eps_content_end' in items:
            q = q.where(TEnglishPointSubject.eps_content <= items['eps_content_end'])
        
        if 'eps_create_name' in items:
            q = q.where(TEnglishPointSubject.eps_create_name == items['eps_create_name'])
        if 'eps_create_name_start' in items:
            q = q.where(TEnglishPointSubject.eps_create_name >= items['eps_create_name_start'])
        if 'eps_create_name_end' in items:
            q = q.where(TEnglishPointSubject.eps_create_name <= items['eps_create_name_end'])
        
        if 'class_id' in items:
            q = q.where(TEnglishPointSubject.class_id == items['class_id'])
        if 'class_id_start' in items:
            q = q.where(TEnglishPointSubject.class_id >= items['class_id_start'])
        if 'class_id_end' in items:
            q = q.where(TEnglishPointSubject.class_id <= items['class_id_end'])
        
        if 'subject_id' in items:
            q = q.where(TEnglishPointSubject.subject_id == items['subject_id'])
        if 'subject_id_start' in items:
            q = q.where(TEnglishPointSubject.subject_id >= items['subject_id_start'])
        if 'subject_id_end' in items:
            q = q.where(TEnglishPointSubject.subject_id <= items['subject_id_end'])
        
        if 'knowledge_id' in items:
            q = q.where(TEnglishPointSubject.knowledge_id == items['knowledge_id'])
        if 'knowledge_id_start' in items:
            q = q.where(TEnglishPointSubject.knowledge_id >= items['knowledge_id_start'])
        if 'knowledge_id_end' in items:
            q = q.where(TEnglishPointSubject.knowledge_id <= items['knowledge_id_end'])
        
        if 'answer_txt' in items:
            q = q.where(TEnglishPointSubject.answer_txt == items['answer_txt'])
        if 'answer_txt_start' in items:
            q = q.where(TEnglishPointSubject.answer_txt >= items['answer_txt_start'])
        if 'answer_txt_end' in items:
            q = q.where(TEnglishPointSubject.answer_txt <= items['answer_txt_end'])
        
        if 'answer_pic_path' in items:
            q = q.where(TEnglishPointSubject.answer_pic_path == items['answer_pic_path'])
        if 'answer_pic_path_start' in items:
            q = q.where(TEnglishPointSubject.answer_pic_path >= items['answer_pic_path_start'])
        if 'answer_pic_path_end' in items:
            q = q.where(TEnglishPointSubject.answer_pic_path <= items['answer_pic_path_end'])
        
        if 'answer_audio_path' in items:
            q = q.where(TEnglishPointSubject.answer_audio_path == items['answer_audio_path'])
        if 'answer_audio_path_start' in items:
            q = q.where(TEnglishPointSubject.answer_audio_path >= items['answer_audio_path_start'])
        if 'answer_audio_path_end' in items:
            q = q.where(TEnglishPointSubject.answer_audio_path <= items['answer_audio_path_end'])
        
        if 'knowledge_list' in items:
            q = q.where(TEnglishPointSubject.knowledge_list == items['knowledge_list'])
        if 'knowledge_list_start' in items:
            q = q.where(TEnglishPointSubject.knowledge_list >= items['knowledge_list_start'])
        if 'knowledge_list_end' in items:
            q = q.where(TEnglishPointSubject.knowledge_list <= items['knowledge_list_end'])
        

        if 'eps_id' in set_items:
            q = q.where(TEnglishPointSubject.eps_id.in_(set_items['eps_id']))
        
        if 'create_time' in set_items:
            q = q.where(TEnglishPointSubject.create_time.in_(set_items['create_time']))
        
        if 'eps_content' in set_items:
            q = q.where(TEnglishPointSubject.eps_content.in_(set_items['eps_content']))
        
        if 'eps_create_name' in set_items:
            q = q.where(TEnglishPointSubject.eps_create_name.in_(set_items['eps_create_name']))
        
        if 'class_id' in set_items:
            q = q.where(TEnglishPointSubject.class_id.in_(set_items['class_id']))
        
        if 'subject_id' in set_items:
            q = q.where(TEnglishPointSubject.subject_id.in_(set_items['subject_id']))
        
        if 'knowledge_id' in set_items:
            q = q.where(TEnglishPointSubject.knowledge_id.in_(set_items['knowledge_id']))
        
        if 'answer_txt' in set_items:
            q = q.where(TEnglishPointSubject.answer_txt.in_(set_items['answer_txt']))
        
        if 'answer_pic_path' in set_items:
            q = q.where(TEnglishPointSubject.answer_pic_path.in_(set_items['answer_pic_path']))
        
        if 'answer_audio_path' in set_items:
            q = q.where(TEnglishPointSubject.answer_audio_path.in_(set_items['answer_audio_path']))
        
        if 'knowledge_list' in set_items:
            q = q.where(TEnglishPointSubject.knowledge_list.in_(set_items['knowledge_list']))
        

        if 'eps_content' in search_items:
            q = q.where(TEnglishPointSubject.eps_content.like(search_items['eps_content']))
        
        if 'eps_create_name' in search_items:
            q = q.where(TEnglishPointSubject.eps_create_name.like(search_items['eps_create_name']))
        
        if 'answer_txt' in search_items:
            q = q.where(TEnglishPointSubject.answer_txt.like(search_items['answer_txt']))
        
        if 'answer_pic_path' in search_items:
            q = q.where(TEnglishPointSubject.answer_pic_path.like(search_items['answer_pic_path']))
        
        if 'answer_audio_path' in search_items:
            q = q.where(TEnglishPointSubject.answer_audio_path.like(search_items['answer_audio_path']))
        
        if 'knowledge_list' in search_items:
            q = q.where(TEnglishPointSubject.knowledge_list.like(search_items['knowledge_list']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TEnglishPointSubject.knowledge_list.asc())
                orders.append(TEnglishPointSubject.id.asc())
            elif val == 'desc':
                #orders.append(TEnglishPointSubject.knowledge_list.desc())
                orders.append(TEnglishPointSubject.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_english_point_subject_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SEnglishPointSubject.parse_obj(t.__dict__) for t in t_english_point_subject_list]


def filter_count_english_point_subject(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TEnglishPointSubject)


        if 'eps_id' in items:
            q = q.where(TEnglishPointSubject.eps_id == items['eps_id'])
        if 'eps_id_start' in items:
            q = q.where(TEnglishPointSubject.eps_id >= items['eps_id_start'])
        if 'eps_id_end' in items:
            q = q.where(TEnglishPointSubject.eps_id <= items['eps_id_end'])
        
        if 'create_time' in items:
            q = q.where(TEnglishPointSubject.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TEnglishPointSubject.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TEnglishPointSubject.create_time <= items['create_time_end'])
        
        if 'eps_content' in items:
            q = q.where(TEnglishPointSubject.eps_content == items['eps_content'])
        if 'eps_content_start' in items:
            q = q.where(TEnglishPointSubject.eps_content >= items['eps_content_start'])
        if 'eps_content_end' in items:
            q = q.where(TEnglishPointSubject.eps_content <= items['eps_content_end'])
        
        if 'eps_create_name' in items:
            q = q.where(TEnglishPointSubject.eps_create_name == items['eps_create_name'])
        if 'eps_create_name_start' in items:
            q = q.where(TEnglishPointSubject.eps_create_name >= items['eps_create_name_start'])
        if 'eps_create_name_end' in items:
            q = q.where(TEnglishPointSubject.eps_create_name <= items['eps_create_name_end'])
        
        if 'class_id' in items:
            q = q.where(TEnglishPointSubject.class_id == items['class_id'])
        if 'class_id_start' in items:
            q = q.where(TEnglishPointSubject.class_id >= items['class_id_start'])
        if 'class_id_end' in items:
            q = q.where(TEnglishPointSubject.class_id <= items['class_id_end'])
        
        if 'subject_id' in items:
            q = q.where(TEnglishPointSubject.subject_id == items['subject_id'])
        if 'subject_id_start' in items:
            q = q.where(TEnglishPointSubject.subject_id >= items['subject_id_start'])
        if 'subject_id_end' in items:
            q = q.where(TEnglishPointSubject.subject_id <= items['subject_id_end'])
        
        if 'knowledge_id' in items:
            q = q.where(TEnglishPointSubject.knowledge_id == items['knowledge_id'])
        if 'knowledge_id_start' in items:
            q = q.where(TEnglishPointSubject.knowledge_id >= items['knowledge_id_start'])
        if 'knowledge_id_end' in items:
            q = q.where(TEnglishPointSubject.knowledge_id <= items['knowledge_id_end'])
        
        if 'answer_txt' in items:
            q = q.where(TEnglishPointSubject.answer_txt == items['answer_txt'])
        if 'answer_txt_start' in items:
            q = q.where(TEnglishPointSubject.answer_txt >= items['answer_txt_start'])
        if 'answer_txt_end' in items:
            q = q.where(TEnglishPointSubject.answer_txt <= items['answer_txt_end'])
        
        if 'answer_pic_path' in items:
            q = q.where(TEnglishPointSubject.answer_pic_path == items['answer_pic_path'])
        if 'answer_pic_path_start' in items:
            q = q.where(TEnglishPointSubject.answer_pic_path >= items['answer_pic_path_start'])
        if 'answer_pic_path_end' in items:
            q = q.where(TEnglishPointSubject.answer_pic_path <= items['answer_pic_path_end'])
        
        if 'answer_audio_path' in items:
            q = q.where(TEnglishPointSubject.answer_audio_path == items['answer_audio_path'])
        if 'answer_audio_path_start' in items:
            q = q.where(TEnglishPointSubject.answer_audio_path >= items['answer_audio_path_start'])
        if 'answer_audio_path_end' in items:
            q = q.where(TEnglishPointSubject.answer_audio_path <= items['answer_audio_path_end'])
        
        if 'knowledge_list' in items:
            q = q.where(TEnglishPointSubject.knowledge_list == items['knowledge_list'])
        if 'knowledge_list_start' in items:
            q = q.where(TEnglishPointSubject.knowledge_list >= items['knowledge_list_start'])
        if 'knowledge_list_end' in items:
            q = q.where(TEnglishPointSubject.knowledge_list <= items['knowledge_list_end'])
        

        if 'eps_id' in set_items:
            q = q.where(TEnglishPointSubject.eps_id.in_(set_items['eps_id']))
        
        if 'create_time' in set_items:
            q = q.where(TEnglishPointSubject.create_time.in_(set_items['create_time']))
        
        if 'eps_content' in set_items:
            q = q.where(TEnglishPointSubject.eps_content.in_(set_items['eps_content']))
        
        if 'eps_create_name' in set_items:
            q = q.where(TEnglishPointSubject.eps_create_name.in_(set_items['eps_create_name']))
        
        if 'class_id' in set_items:
            q = q.where(TEnglishPointSubject.class_id.in_(set_items['class_id']))
        
        if 'subject_id' in set_items:
            q = q.where(TEnglishPointSubject.subject_id.in_(set_items['subject_id']))
        
        if 'knowledge_id' in set_items:
            q = q.where(TEnglishPointSubject.knowledge_id.in_(set_items['knowledge_id']))
        
        if 'answer_txt' in set_items:
            q = q.where(TEnglishPointSubject.answer_txt.in_(set_items['answer_txt']))
        
        if 'answer_pic_path' in set_items:
            q = q.where(TEnglishPointSubject.answer_pic_path.in_(set_items['answer_pic_path']))
        
        if 'answer_audio_path' in set_items:
            q = q.where(TEnglishPointSubject.answer_audio_path.in_(set_items['answer_audio_path']))
        
        if 'knowledge_list' in set_items:
            q = q.where(TEnglishPointSubject.knowledge_list.in_(set_items['knowledge_list']))
        

        if 'eps_content' in search_items:
            q = q.where(TEnglishPointSubject.eps_content.like(search_items['eps_content']))
        
        if 'eps_create_name' in search_items:
            q = q.where(TEnglishPointSubject.eps_create_name.like(search_items['eps_create_name']))
        
        if 'answer_txt' in search_items:
            q = q.where(TEnglishPointSubject.answer_txt.like(search_items['answer_txt']))
        
        if 'answer_pic_path' in search_items:
            q = q.where(TEnglishPointSubject.answer_pic_path.like(search_items['answer_pic_path']))
        
        if 'answer_audio_path' in search_items:
            q = q.where(TEnglishPointSubject.answer_audio_path.like(search_items['answer_audio_path']))
        
        if 'knowledge_list' in search_items:
            q = q.where(TEnglishPointSubject.knowledge_list.like(search_items['knowledge_list']))
        
    
        c = q.count()
        return c

    
def insert_knowledge_point(item: CreateKnowledgePoint, db: Optional[SessionLocal] = None) -> SKnowledgePoint:
    data = model2dict(item)
    t = TKnowledgePoint(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SKnowledgePoint.parse_obj(t.__dict__)

    
def delete_knowledge_point(knowledge_point_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TKnowledgePoint).where(TKnowledgePoint.id == knowledge_point_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TKnowledgePoint).where(TKnowledgePoint.id == knowledge_point_id).delete()
        db.commit()

    
def update_knowledge_point(item: SKnowledgePoint, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TKnowledgePoint).where(TKnowledgePoint.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TKnowledgePoint).where(TKnowledgePoint.id == item.id).update(data)
        db.commit()

    
def get_knowledge_point(knowledge_point_id: int) -> Optional[SKnowledgePoint]:
    with Dao() as db:
        t = db.query(TKnowledgePoint).where(TKnowledgePoint.id == knowledge_point_id).first()
        if t:
            return SKnowledgePoint.parse_obj(t.__dict__)
        else:
            return None


def filter_knowledge_point(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SKnowledgePoint]:
    with Dao() as db:
        q = db.query(TKnowledgePoint)


        if 'kn_id' in items:
            q = q.where(TKnowledgePoint.kn_id == items['kn_id'])
        if 'kn_id_start' in items:
            q = q.where(TKnowledgePoint.kn_id >= items['kn_id_start'])
        if 'kn_id_end' in items:
            q = q.where(TKnowledgePoint.kn_id <= items['kn_id_end'])
        
        if 'create_time' in items:
            q = q.where(TKnowledgePoint.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TKnowledgePoint.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TKnowledgePoint.create_time <= items['create_time_end'])
        
        if 'kn_name' in items:
            q = q.where(TKnowledgePoint.kn_name == items['kn_name'])
        if 'kn_name_start' in items:
            q = q.where(TKnowledgePoint.kn_name >= items['kn_name_start'])
        if 'kn_name_end' in items:
            q = q.where(TKnowledgePoint.kn_name <= items['kn_name_end'])
        
        if 'kn_create_name' in items:
            q = q.where(TKnowledgePoint.kn_create_name == items['kn_create_name'])
        if 'kn_create_name_start' in items:
            q = q.where(TKnowledgePoint.kn_create_name >= items['kn_create_name_start'])
        if 'kn_create_name_end' in items:
            q = q.where(TKnowledgePoint.kn_create_name <= items['kn_create_name_end'])
        
        if 'class_id' in items:
            q = q.where(TKnowledgePoint.class_id == items['class_id'])
        if 'class_id_start' in items:
            q = q.where(TKnowledgePoint.class_id >= items['class_id_start'])
        if 'class_id_end' in items:
            q = q.where(TKnowledgePoint.class_id <= items['class_id_end'])
        
        if 'subject_id' in items:
            q = q.where(TKnowledgePoint.subject_id == items['subject_id'])
        if 'subject_id_start' in items:
            q = q.where(TKnowledgePoint.subject_id >= items['subject_id_start'])
        if 'subject_id_end' in items:
            q = q.where(TKnowledgePoint.subject_id <= items['subject_id_end'])
        

        if 'kn_id' in set_items:
            q = q.where(TKnowledgePoint.kn_id.in_(set_items['kn_id']))
        
        if 'create_time' in set_items:
            q = q.where(TKnowledgePoint.create_time.in_(set_items['create_time']))
        
        if 'kn_name' in set_items:
            q = q.where(TKnowledgePoint.kn_name.in_(set_items['kn_name']))
        
        if 'kn_create_name' in set_items:
            q = q.where(TKnowledgePoint.kn_create_name.in_(set_items['kn_create_name']))
        
        if 'class_id' in set_items:
            q = q.where(TKnowledgePoint.class_id.in_(set_items['class_id']))
        
        if 'subject_id' in set_items:
            q = q.where(TKnowledgePoint.subject_id.in_(set_items['subject_id']))
        

        if 'kn_name' in search_items:
            q = q.where(TKnowledgePoint.kn_name.like(search_items['kn_name']))
        
        if 'kn_create_name' in search_items:
            q = q.where(TKnowledgePoint.kn_create_name.like(search_items['kn_create_name']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TKnowledgePoint.subject_id.asc())
                orders.append(TKnowledgePoint.id.asc())
            elif val == 'desc':
                #orders.append(TKnowledgePoint.subject_id.desc())
                orders.append(TKnowledgePoint.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_knowledge_point_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SKnowledgePoint.parse_obj(t.__dict__) for t in t_knowledge_point_list]


def filter_count_knowledge_point(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TKnowledgePoint)


        if 'kn_id' in items:
            q = q.where(TKnowledgePoint.kn_id == items['kn_id'])
        if 'kn_id_start' in items:
            q = q.where(TKnowledgePoint.kn_id >= items['kn_id_start'])
        if 'kn_id_end' in items:
            q = q.where(TKnowledgePoint.kn_id <= items['kn_id_end'])
        
        if 'create_time' in items:
            q = q.where(TKnowledgePoint.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TKnowledgePoint.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TKnowledgePoint.create_time <= items['create_time_end'])
        
        if 'kn_name' in items:
            q = q.where(TKnowledgePoint.kn_name == items['kn_name'])
        if 'kn_name_start' in items:
            q = q.where(TKnowledgePoint.kn_name >= items['kn_name_start'])
        if 'kn_name_end' in items:
            q = q.where(TKnowledgePoint.kn_name <= items['kn_name_end'])
        
        if 'kn_create_name' in items:
            q = q.where(TKnowledgePoint.kn_create_name == items['kn_create_name'])
        if 'kn_create_name_start' in items:
            q = q.where(TKnowledgePoint.kn_create_name >= items['kn_create_name_start'])
        if 'kn_create_name_end' in items:
            q = q.where(TKnowledgePoint.kn_create_name <= items['kn_create_name_end'])
        
        if 'class_id' in items:
            q = q.where(TKnowledgePoint.class_id == items['class_id'])
        if 'class_id_start' in items:
            q = q.where(TKnowledgePoint.class_id >= items['class_id_start'])
        if 'class_id_end' in items:
            q = q.where(TKnowledgePoint.class_id <= items['class_id_end'])
        
        if 'subject_id' in items:
            q = q.where(TKnowledgePoint.subject_id == items['subject_id'])
        if 'subject_id_start' in items:
            q = q.where(TKnowledgePoint.subject_id >= items['subject_id_start'])
        if 'subject_id_end' in items:
            q = q.where(TKnowledgePoint.subject_id <= items['subject_id_end'])
        

        if 'kn_id' in set_items:
            q = q.where(TKnowledgePoint.kn_id.in_(set_items['kn_id']))
        
        if 'create_time' in set_items:
            q = q.where(TKnowledgePoint.create_time.in_(set_items['create_time']))
        
        if 'kn_name' in set_items:
            q = q.where(TKnowledgePoint.kn_name.in_(set_items['kn_name']))
        
        if 'kn_create_name' in set_items:
            q = q.where(TKnowledgePoint.kn_create_name.in_(set_items['kn_create_name']))
        
        if 'class_id' in set_items:
            q = q.where(TKnowledgePoint.class_id.in_(set_items['class_id']))
        
        if 'subject_id' in set_items:
            q = q.where(TKnowledgePoint.subject_id.in_(set_items['subject_id']))
        

        if 'kn_name' in search_items:
            q = q.where(TKnowledgePoint.kn_name.like(search_items['kn_name']))
        
        if 'kn_create_name' in search_items:
            q = q.where(TKnowledgePoint.kn_create_name.like(search_items['kn_create_name']))
        
    
        c = q.count()
        return c

    
def insert_math_point_subject(item: CreateMathPointSubject, db: Optional[SessionLocal] = None) -> SMathPointSubject:
    data = model2dict(item)
    t = TMathPointSubject(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SMathPointSubject.parse_obj(t.__dict__)

    
def delete_math_point_subject(math_point_subject_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TMathPointSubject).where(TMathPointSubject.id == math_point_subject_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TMathPointSubject).where(TMathPointSubject.id == math_point_subject_id).delete()
        db.commit()

    
def update_math_point_subject(item: SMathPointSubject, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TMathPointSubject).where(TMathPointSubject.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TMathPointSubject).where(TMathPointSubject.id == item.id).update(data)
        db.commit()

    
def get_math_point_subject(math_point_subject_id: int) -> Optional[SMathPointSubject]:
    with Dao() as db:
        t = db.query(TMathPointSubject).where(TMathPointSubject.id == math_point_subject_id).first()
        if t:
            return SMathPointSubject.parse_obj(t.__dict__)
        else:
            return None


def filter_math_point_subject(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SMathPointSubject]:
    with Dao() as db:
        q = db.query(TMathPointSubject)


        if 'mps_id' in items:
            q = q.where(TMathPointSubject.mps_id == items['mps_id'])
        if 'mps_id_start' in items:
            q = q.where(TMathPointSubject.mps_id >= items['mps_id_start'])
        if 'mps_id_end' in items:
            q = q.where(TMathPointSubject.mps_id <= items['mps_id_end'])
        
        if 'create_time' in items:
            q = q.where(TMathPointSubject.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TMathPointSubject.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TMathPointSubject.create_time <= items['create_time_end'])
        
        if 'mps_content' in items:
            q = q.where(TMathPointSubject.mps_content == items['mps_content'])
        if 'mps_content_start' in items:
            q = q.where(TMathPointSubject.mps_content >= items['mps_content_start'])
        if 'mps_content_end' in items:
            q = q.where(TMathPointSubject.mps_content <= items['mps_content_end'])
        
        if 'mps_create_name' in items:
            q = q.where(TMathPointSubject.mps_create_name == items['mps_create_name'])
        if 'mps_create_name_start' in items:
            q = q.where(TMathPointSubject.mps_create_name >= items['mps_create_name_start'])
        if 'mps_create_name_end' in items:
            q = q.where(TMathPointSubject.mps_create_name <= items['mps_create_name_end'])
        
        if 'class_id' in items:
            q = q.where(TMathPointSubject.class_id == items['class_id'])
        if 'class_id_start' in items:
            q = q.where(TMathPointSubject.class_id >= items['class_id_start'])
        if 'class_id_end' in items:
            q = q.where(TMathPointSubject.class_id <= items['class_id_end'])
        
        if 'subject_id' in items:
            q = q.where(TMathPointSubject.subject_id == items['subject_id'])
        if 'subject_id_start' in items:
            q = q.where(TMathPointSubject.subject_id >= items['subject_id_start'])
        if 'subject_id_end' in items:
            q = q.where(TMathPointSubject.subject_id <= items['subject_id_end'])
        
        if 'knowledge_id' in items:
            q = q.where(TMathPointSubject.knowledge_id == items['knowledge_id'])
        if 'knowledge_id_start' in items:
            q = q.where(TMathPointSubject.knowledge_id >= items['knowledge_id_start'])
        if 'knowledge_id_end' in items:
            q = q.where(TMathPointSubject.knowledge_id <= items['knowledge_id_end'])
        
        if 'answer_txt' in items:
            q = q.where(TMathPointSubject.answer_txt == items['answer_txt'])
        if 'answer_txt_start' in items:
            q = q.where(TMathPointSubject.answer_txt >= items['answer_txt_start'])
        if 'answer_txt_end' in items:
            q = q.where(TMathPointSubject.answer_txt <= items['answer_txt_end'])
        
        if 'answer_pic_path' in items:
            q = q.where(TMathPointSubject.answer_pic_path == items['answer_pic_path'])
        if 'answer_pic_path_start' in items:
            q = q.where(TMathPointSubject.answer_pic_path >= items['answer_pic_path_start'])
        if 'answer_pic_path_end' in items:
            q = q.where(TMathPointSubject.answer_pic_path <= items['answer_pic_path_end'])
        
        if 'answer_audio_path' in items:
            q = q.where(TMathPointSubject.answer_audio_path == items['answer_audio_path'])
        if 'answer_audio_path_start' in items:
            q = q.where(TMathPointSubject.answer_audio_path >= items['answer_audio_path_start'])
        if 'answer_audio_path_end' in items:
            q = q.where(TMathPointSubject.answer_audio_path <= items['answer_audio_path_end'])
        
        if 'knowledge_list' in items:
            q = q.where(TMathPointSubject.knowledge_list == items['knowledge_list'])
        if 'knowledge_list_start' in items:
            q = q.where(TMathPointSubject.knowledge_list >= items['knowledge_list_start'])
        if 'knowledge_list_end' in items:
            q = q.where(TMathPointSubject.knowledge_list <= items['knowledge_list_end'])
        

        if 'mps_id' in set_items:
            q = q.where(TMathPointSubject.mps_id.in_(set_items['mps_id']))
        
        if 'create_time' in set_items:
            q = q.where(TMathPointSubject.create_time.in_(set_items['create_time']))
        
        if 'mps_content' in set_items:
            q = q.where(TMathPointSubject.mps_content.in_(set_items['mps_content']))
        
        if 'mps_create_name' in set_items:
            q = q.where(TMathPointSubject.mps_create_name.in_(set_items['mps_create_name']))
        
        if 'class_id' in set_items:
            q = q.where(TMathPointSubject.class_id.in_(set_items['class_id']))
        
        if 'subject_id' in set_items:
            q = q.where(TMathPointSubject.subject_id.in_(set_items['subject_id']))
        
        if 'knowledge_id' in set_items:
            q = q.where(TMathPointSubject.knowledge_id.in_(set_items['knowledge_id']))
        
        if 'answer_txt' in set_items:
            q = q.where(TMathPointSubject.answer_txt.in_(set_items['answer_txt']))
        
        if 'answer_pic_path' in set_items:
            q = q.where(TMathPointSubject.answer_pic_path.in_(set_items['answer_pic_path']))
        
        if 'answer_audio_path' in set_items:
            q = q.where(TMathPointSubject.answer_audio_path.in_(set_items['answer_audio_path']))
        
        if 'knowledge_list' in set_items:
            q = q.where(TMathPointSubject.knowledge_list.in_(set_items['knowledge_list']))
        

        if 'mps_content' in search_items:
            q = q.where(TMathPointSubject.mps_content.like(search_items['mps_content']))
        
        if 'mps_create_name' in search_items:
            q = q.where(TMathPointSubject.mps_create_name.like(search_items['mps_create_name']))
        
        if 'answer_txt' in search_items:
            q = q.where(TMathPointSubject.answer_txt.like(search_items['answer_txt']))
        
        if 'answer_pic_path' in search_items:
            q = q.where(TMathPointSubject.answer_pic_path.like(search_items['answer_pic_path']))
        
        if 'answer_audio_path' in search_items:
            q = q.where(TMathPointSubject.answer_audio_path.like(search_items['answer_audio_path']))
        
        if 'knowledge_list' in search_items:
            q = q.where(TMathPointSubject.knowledge_list.like(search_items['knowledge_list']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TMathPointSubject.knowledge_list.asc())
                orders.append(TMathPointSubject.id.asc())
            elif val == 'desc':
                #orders.append(TMathPointSubject.knowledge_list.desc())
                orders.append(TMathPointSubject.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_math_point_subject_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SMathPointSubject.parse_obj(t.__dict__) for t in t_math_point_subject_list]


def filter_count_math_point_subject(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TMathPointSubject)


        if 'mps_id' in items:
            q = q.where(TMathPointSubject.mps_id == items['mps_id'])
        if 'mps_id_start' in items:
            q = q.where(TMathPointSubject.mps_id >= items['mps_id_start'])
        if 'mps_id_end' in items:
            q = q.where(TMathPointSubject.mps_id <= items['mps_id_end'])
        
        if 'create_time' in items:
            q = q.where(TMathPointSubject.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TMathPointSubject.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TMathPointSubject.create_time <= items['create_time_end'])
        
        if 'mps_content' in items:
            q = q.where(TMathPointSubject.mps_content == items['mps_content'])
        if 'mps_content_start' in items:
            q = q.where(TMathPointSubject.mps_content >= items['mps_content_start'])
        if 'mps_content_end' in items:
            q = q.where(TMathPointSubject.mps_content <= items['mps_content_end'])
        
        if 'mps_create_name' in items:
            q = q.where(TMathPointSubject.mps_create_name == items['mps_create_name'])
        if 'mps_create_name_start' in items:
            q = q.where(TMathPointSubject.mps_create_name >= items['mps_create_name_start'])
        if 'mps_create_name_end' in items:
            q = q.where(TMathPointSubject.mps_create_name <= items['mps_create_name_end'])
        
        if 'class_id' in items:
            q = q.where(TMathPointSubject.class_id == items['class_id'])
        if 'class_id_start' in items:
            q = q.where(TMathPointSubject.class_id >= items['class_id_start'])
        if 'class_id_end' in items:
            q = q.where(TMathPointSubject.class_id <= items['class_id_end'])
        
        if 'subject_id' in items:
            q = q.where(TMathPointSubject.subject_id == items['subject_id'])
        if 'subject_id_start' in items:
            q = q.where(TMathPointSubject.subject_id >= items['subject_id_start'])
        if 'subject_id_end' in items:
            q = q.where(TMathPointSubject.subject_id <= items['subject_id_end'])
        
        if 'knowledge_id' in items:
            q = q.where(TMathPointSubject.knowledge_id == items['knowledge_id'])
        if 'knowledge_id_start' in items:
            q = q.where(TMathPointSubject.knowledge_id >= items['knowledge_id_start'])
        if 'knowledge_id_end' in items:
            q = q.where(TMathPointSubject.knowledge_id <= items['knowledge_id_end'])
        
        if 'answer_txt' in items:
            q = q.where(TMathPointSubject.answer_txt == items['answer_txt'])
        if 'answer_txt_start' in items:
            q = q.where(TMathPointSubject.answer_txt >= items['answer_txt_start'])
        if 'answer_txt_end' in items:
            q = q.where(TMathPointSubject.answer_txt <= items['answer_txt_end'])
        
        if 'answer_pic_path' in items:
            q = q.where(TMathPointSubject.answer_pic_path == items['answer_pic_path'])
        if 'answer_pic_path_start' in items:
            q = q.where(TMathPointSubject.answer_pic_path >= items['answer_pic_path_start'])
        if 'answer_pic_path_end' in items:
            q = q.where(TMathPointSubject.answer_pic_path <= items['answer_pic_path_end'])
        
        if 'answer_audio_path' in items:
            q = q.where(TMathPointSubject.answer_audio_path == items['answer_audio_path'])
        if 'answer_audio_path_start' in items:
            q = q.where(TMathPointSubject.answer_audio_path >= items['answer_audio_path_start'])
        if 'answer_audio_path_end' in items:
            q = q.where(TMathPointSubject.answer_audio_path <= items['answer_audio_path_end'])
        
        if 'knowledge_list' in items:
            q = q.where(TMathPointSubject.knowledge_list == items['knowledge_list'])
        if 'knowledge_list_start' in items:
            q = q.where(TMathPointSubject.knowledge_list >= items['knowledge_list_start'])
        if 'knowledge_list_end' in items:
            q = q.where(TMathPointSubject.knowledge_list <= items['knowledge_list_end'])
        

        if 'mps_id' in set_items:
            q = q.where(TMathPointSubject.mps_id.in_(set_items['mps_id']))
        
        if 'create_time' in set_items:
            q = q.where(TMathPointSubject.create_time.in_(set_items['create_time']))
        
        if 'mps_content' in set_items:
            q = q.where(TMathPointSubject.mps_content.in_(set_items['mps_content']))
        
        if 'mps_create_name' in set_items:
            q = q.where(TMathPointSubject.mps_create_name.in_(set_items['mps_create_name']))
        
        if 'class_id' in set_items:
            q = q.where(TMathPointSubject.class_id.in_(set_items['class_id']))
        
        if 'subject_id' in set_items:
            q = q.where(TMathPointSubject.subject_id.in_(set_items['subject_id']))
        
        if 'knowledge_id' in set_items:
            q = q.where(TMathPointSubject.knowledge_id.in_(set_items['knowledge_id']))
        
        if 'answer_txt' in set_items:
            q = q.where(TMathPointSubject.answer_txt.in_(set_items['answer_txt']))
        
        if 'answer_pic_path' in set_items:
            q = q.where(TMathPointSubject.answer_pic_path.in_(set_items['answer_pic_path']))
        
        if 'answer_audio_path' in set_items:
            q = q.where(TMathPointSubject.answer_audio_path.in_(set_items['answer_audio_path']))
        
        if 'knowledge_list' in set_items:
            q = q.where(TMathPointSubject.knowledge_list.in_(set_items['knowledge_list']))
        

        if 'mps_content' in search_items:
            q = q.where(TMathPointSubject.mps_content.like(search_items['mps_content']))
        
        if 'mps_create_name' in search_items:
            q = q.where(TMathPointSubject.mps_create_name.like(search_items['mps_create_name']))
        
        if 'answer_txt' in search_items:
            q = q.where(TMathPointSubject.answer_txt.like(search_items['answer_txt']))
        
        if 'answer_pic_path' in search_items:
            q = q.where(TMathPointSubject.answer_pic_path.like(search_items['answer_pic_path']))
        
        if 'answer_audio_path' in search_items:
            q = q.where(TMathPointSubject.answer_audio_path.like(search_items['answer_audio_path']))
        
        if 'knowledge_list' in search_items:
            q = q.where(TMathPointSubject.knowledge_list.like(search_items['knowledge_list']))
        
    
        c = q.count()
        return c

    
def insert_question_type(item: CreateQuestionType, db: Optional[SessionLocal] = None) -> SQuestionType:
    data = model2dict(item)
    t = TQuestionType(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SQuestionType.parse_obj(t.__dict__)

    
def delete_question_type(question_type_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TQuestionType).where(TQuestionType.id == question_type_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TQuestionType).where(TQuestionType.id == question_type_id).delete()
        db.commit()

    
def update_question_type(item: SQuestionType, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TQuestionType).where(TQuestionType.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TQuestionType).where(TQuestionType.id == item.id).update(data)
        db.commit()

    
def get_question_type(question_type_id: int) -> Optional[SQuestionType]:
    with Dao() as db:
        t = db.query(TQuestionType).where(TQuestionType.id == question_type_id).first()
        if t:
            return SQuestionType.parse_obj(t.__dict__)
        else:
            return None


def filter_question_type(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SQuestionType]:
    with Dao() as db:
        q = db.query(TQuestionType)


        if 'qu_id' in items:
            q = q.where(TQuestionType.qu_id == items['qu_id'])
        if 'qu_id_start' in items:
            q = q.where(TQuestionType.qu_id >= items['qu_id_start'])
        if 'qu_id_end' in items:
            q = q.where(TQuestionType.qu_id <= items['qu_id_end'])
        
        if 'create_time' in items:
            q = q.where(TQuestionType.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TQuestionType.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TQuestionType.create_time <= items['create_time_end'])
        
        if 'qu_name' in items:
            q = q.where(TQuestionType.qu_name == items['qu_name'])
        if 'qu_name_start' in items:
            q = q.where(TQuestionType.qu_name >= items['qu_name_start'])
        if 'qu_name_end' in items:
            q = q.where(TQuestionType.qu_name <= items['qu_name_end'])
        
        if 'qu_create_name' in items:
            q = q.where(TQuestionType.qu_create_name == items['qu_create_name'])
        if 'qu_create_name_start' in items:
            q = q.where(TQuestionType.qu_create_name >= items['qu_create_name_start'])
        if 'qu_create_name_end' in items:
            q = q.where(TQuestionType.qu_create_name <= items['qu_create_name_end'])
        
        if 'class_id' in items:
            q = q.where(TQuestionType.class_id == items['class_id'])
        if 'class_id_start' in items:
            q = q.where(TQuestionType.class_id >= items['class_id_start'])
        if 'class_id_end' in items:
            q = q.where(TQuestionType.class_id <= items['class_id_end'])
        
        if 'subject_id' in items:
            q = q.where(TQuestionType.subject_id == items['subject_id'])
        if 'subject_id_start' in items:
            q = q.where(TQuestionType.subject_id >= items['subject_id_start'])
        if 'subject_id_end' in items:
            q = q.where(TQuestionType.subject_id <= items['subject_id_end'])
        
        if 'knowledge_id' in items:
            q = q.where(TQuestionType.knowledge_id == items['knowledge_id'])
        if 'knowledge_id_start' in items:
            q = q.where(TQuestionType.knowledge_id >= items['knowledge_id_start'])
        if 'knowledge_id_end' in items:
            q = q.where(TQuestionType.knowledge_id <= items['knowledge_id_end'])
        
        if 'knowledge_list' in items:
            q = q.where(TQuestionType.knowledge_list == items['knowledge_list'])
        if 'knowledge_list_start' in items:
            q = q.where(TQuestionType.knowledge_list >= items['knowledge_list_start'])
        if 'knowledge_list_end' in items:
            q = q.where(TQuestionType.knowledge_list <= items['knowledge_list_end'])
        

        if 'qu_id' in set_items:
            q = q.where(TQuestionType.qu_id.in_(set_items['qu_id']))
        
        if 'create_time' in set_items:
            q = q.where(TQuestionType.create_time.in_(set_items['create_time']))
        
        if 'qu_name' in set_items:
            q = q.where(TQuestionType.qu_name.in_(set_items['qu_name']))
        
        if 'qu_create_name' in set_items:
            q = q.where(TQuestionType.qu_create_name.in_(set_items['qu_create_name']))
        
        if 'class_id' in set_items:
            q = q.where(TQuestionType.class_id.in_(set_items['class_id']))
        
        if 'subject_id' in set_items:
            q = q.where(TQuestionType.subject_id.in_(set_items['subject_id']))
        
        if 'knowledge_id' in set_items:
            q = q.where(TQuestionType.knowledge_id.in_(set_items['knowledge_id']))
        
        if 'knowledge_list' in set_items:
            q = q.where(TQuestionType.knowledge_list.in_(set_items['knowledge_list']))
        

        if 'qu_name' in search_items:
            q = q.where(TQuestionType.qu_name.like(search_items['qu_name']))
        
        if 'qu_create_name' in search_items:
            q = q.where(TQuestionType.qu_create_name.like(search_items['qu_create_name']))
        
        if 'knowledge_list' in search_items:
            q = q.where(TQuestionType.knowledge_list.like(search_items['knowledge_list']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TQuestionType.knowledge_list.asc())
                orders.append(TQuestionType.id.asc())
            elif val == 'desc':
                #orders.append(TQuestionType.knowledge_list.desc())
                orders.append(TQuestionType.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_question_type_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SQuestionType.parse_obj(t.__dict__) for t in t_question_type_list]


def filter_count_question_type(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TQuestionType)


        if 'qu_id' in items:
            q = q.where(TQuestionType.qu_id == items['qu_id'])
        if 'qu_id_start' in items:
            q = q.where(TQuestionType.qu_id >= items['qu_id_start'])
        if 'qu_id_end' in items:
            q = q.where(TQuestionType.qu_id <= items['qu_id_end'])
        
        if 'create_time' in items:
            q = q.where(TQuestionType.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TQuestionType.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TQuestionType.create_time <= items['create_time_end'])
        
        if 'qu_name' in items:
            q = q.where(TQuestionType.qu_name == items['qu_name'])
        if 'qu_name_start' in items:
            q = q.where(TQuestionType.qu_name >= items['qu_name_start'])
        if 'qu_name_end' in items:
            q = q.where(TQuestionType.qu_name <= items['qu_name_end'])
        
        if 'qu_create_name' in items:
            q = q.where(TQuestionType.qu_create_name == items['qu_create_name'])
        if 'qu_create_name_start' in items:
            q = q.where(TQuestionType.qu_create_name >= items['qu_create_name_start'])
        if 'qu_create_name_end' in items:
            q = q.where(TQuestionType.qu_create_name <= items['qu_create_name_end'])
        
        if 'class_id' in items:
            q = q.where(TQuestionType.class_id == items['class_id'])
        if 'class_id_start' in items:
            q = q.where(TQuestionType.class_id >= items['class_id_start'])
        if 'class_id_end' in items:
            q = q.where(TQuestionType.class_id <= items['class_id_end'])
        
        if 'subject_id' in items:
            q = q.where(TQuestionType.subject_id == items['subject_id'])
        if 'subject_id_start' in items:
            q = q.where(TQuestionType.subject_id >= items['subject_id_start'])
        if 'subject_id_end' in items:
            q = q.where(TQuestionType.subject_id <= items['subject_id_end'])
        
        if 'knowledge_id' in items:
            q = q.where(TQuestionType.knowledge_id == items['knowledge_id'])
        if 'knowledge_id_start' in items:
            q = q.where(TQuestionType.knowledge_id >= items['knowledge_id_start'])
        if 'knowledge_id_end' in items:
            q = q.where(TQuestionType.knowledge_id <= items['knowledge_id_end'])
        
        if 'knowledge_list' in items:
            q = q.where(TQuestionType.knowledge_list == items['knowledge_list'])
        if 'knowledge_list_start' in items:
            q = q.where(TQuestionType.knowledge_list >= items['knowledge_list_start'])
        if 'knowledge_list_end' in items:
            q = q.where(TQuestionType.knowledge_list <= items['knowledge_list_end'])
        

        if 'qu_id' in set_items:
            q = q.where(TQuestionType.qu_id.in_(set_items['qu_id']))
        
        if 'create_time' in set_items:
            q = q.where(TQuestionType.create_time.in_(set_items['create_time']))
        
        if 'qu_name' in set_items:
            q = q.where(TQuestionType.qu_name.in_(set_items['qu_name']))
        
        if 'qu_create_name' in set_items:
            q = q.where(TQuestionType.qu_create_name.in_(set_items['qu_create_name']))
        
        if 'class_id' in set_items:
            q = q.where(TQuestionType.class_id.in_(set_items['class_id']))
        
        if 'subject_id' in set_items:
            q = q.where(TQuestionType.subject_id.in_(set_items['subject_id']))
        
        if 'knowledge_id' in set_items:
            q = q.where(TQuestionType.knowledge_id.in_(set_items['knowledge_id']))
        
        if 'knowledge_list' in set_items:
            q = q.where(TQuestionType.knowledge_list.in_(set_items['knowledge_list']))
        

        if 'qu_name' in search_items:
            q = q.where(TQuestionType.qu_name.like(search_items['qu_name']))
        
        if 'qu_create_name' in search_items:
            q = q.where(TQuestionType.qu_create_name.like(search_items['qu_create_name']))
        
        if 'knowledge_list' in search_items:
            q = q.where(TQuestionType.knowledge_list.like(search_items['knowledge_list']))
        
    
        c = q.count()
        return c

    
def insert_remain_point_subject(item: CreateRemainPointSubject, db: Optional[SessionLocal] = None) -> SRemainPointSubject:
    data = model2dict(item)
    t = TRemainPointSubject(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SRemainPointSubject.parse_obj(t.__dict__)

    
def delete_remain_point_subject(remain_point_subject_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TRemainPointSubject).where(TRemainPointSubject.id == remain_point_subject_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TRemainPointSubject).where(TRemainPointSubject.id == remain_point_subject_id).delete()
        db.commit()

    
def update_remain_point_subject(item: SRemainPointSubject, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TRemainPointSubject).where(TRemainPointSubject.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TRemainPointSubject).where(TRemainPointSubject.id == item.id).update(data)
        db.commit()

    
def get_remain_point_subject(remain_point_subject_id: int) -> Optional[SRemainPointSubject]:
    with Dao() as db:
        t = db.query(TRemainPointSubject).where(TRemainPointSubject.id == remain_point_subject_id).first()
        if t:
            return SRemainPointSubject.parse_obj(t.__dict__)
        else:
            return None


def filter_remain_point_subject(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SRemainPointSubject]:
    with Dao() as db:
        q = db.query(TRemainPointSubject)


        if 'rps_id' in items:
            q = q.where(TRemainPointSubject.rps_id == items['rps_id'])
        if 'rps_id_start' in items:
            q = q.where(TRemainPointSubject.rps_id >= items['rps_id_start'])
        if 'rps_id_end' in items:
            q = q.where(TRemainPointSubject.rps_id <= items['rps_id_end'])
        
        if 'create_time' in items:
            q = q.where(TRemainPointSubject.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TRemainPointSubject.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TRemainPointSubject.create_time <= items['create_time_end'])
        
        if 'rps_content' in items:
            q = q.where(TRemainPointSubject.rps_content == items['rps_content'])
        if 'rps_content_start' in items:
            q = q.where(TRemainPointSubject.rps_content >= items['rps_content_start'])
        if 'rps_content_end' in items:
            q = q.where(TRemainPointSubject.rps_content <= items['rps_content_end'])
        
        if 'rps_create_name' in items:
            q = q.where(TRemainPointSubject.rps_create_name == items['rps_create_name'])
        if 'rps_create_name_start' in items:
            q = q.where(TRemainPointSubject.rps_create_name >= items['rps_create_name_start'])
        if 'rps_create_name_end' in items:
            q = q.where(TRemainPointSubject.rps_create_name <= items['rps_create_name_end'])
        
        if 'class_id' in items:
            q = q.where(TRemainPointSubject.class_id == items['class_id'])
        if 'class_id_start' in items:
            q = q.where(TRemainPointSubject.class_id >= items['class_id_start'])
        if 'class_id_end' in items:
            q = q.where(TRemainPointSubject.class_id <= items['class_id_end'])
        
        if 'subject_id' in items:
            q = q.where(TRemainPointSubject.subject_id == items['subject_id'])
        if 'subject_id_start' in items:
            q = q.where(TRemainPointSubject.subject_id >= items['subject_id_start'])
        if 'subject_id_end' in items:
            q = q.where(TRemainPointSubject.subject_id <= items['subject_id_end'])
        
        if 'knowledge_id' in items:
            q = q.where(TRemainPointSubject.knowledge_id == items['knowledge_id'])
        if 'knowledge_id_start' in items:
            q = q.where(TRemainPointSubject.knowledge_id >= items['knowledge_id_start'])
        if 'knowledge_id_end' in items:
            q = q.where(TRemainPointSubject.knowledge_id <= items['knowledge_id_end'])
        
        if 'answer_txt' in items:
            q = q.where(TRemainPointSubject.answer_txt == items['answer_txt'])
        if 'answer_txt_start' in items:
            q = q.where(TRemainPointSubject.answer_txt >= items['answer_txt_start'])
        if 'answer_txt_end' in items:
            q = q.where(TRemainPointSubject.answer_txt <= items['answer_txt_end'])
        
        if 'answer_pic_path' in items:
            q = q.where(TRemainPointSubject.answer_pic_path == items['answer_pic_path'])
        if 'answer_pic_path_start' in items:
            q = q.where(TRemainPointSubject.answer_pic_path >= items['answer_pic_path_start'])
        if 'answer_pic_path_end' in items:
            q = q.where(TRemainPointSubject.answer_pic_path <= items['answer_pic_path_end'])
        
        if 'answer_audio_path' in items:
            q = q.where(TRemainPointSubject.answer_audio_path == items['answer_audio_path'])
        if 'answer_audio_path_start' in items:
            q = q.where(TRemainPointSubject.answer_audio_path >= items['answer_audio_path_start'])
        if 'answer_audio_path_end' in items:
            q = q.where(TRemainPointSubject.answer_audio_path <= items['answer_audio_path_end'])
        
        if 'knowledge_list' in items:
            q = q.where(TRemainPointSubject.knowledge_list == items['knowledge_list'])
        if 'knowledge_list_start' in items:
            q = q.where(TRemainPointSubject.knowledge_list >= items['knowledge_list_start'])
        if 'knowledge_list_end' in items:
            q = q.where(TRemainPointSubject.knowledge_list <= items['knowledge_list_end'])
        

        if 'rps_id' in set_items:
            q = q.where(TRemainPointSubject.rps_id.in_(set_items['rps_id']))
        
        if 'create_time' in set_items:
            q = q.where(TRemainPointSubject.create_time.in_(set_items['create_time']))
        
        if 'rps_content' in set_items:
            q = q.where(TRemainPointSubject.rps_content.in_(set_items['rps_content']))
        
        if 'rps_create_name' in set_items:
            q = q.where(TRemainPointSubject.rps_create_name.in_(set_items['rps_create_name']))
        
        if 'class_id' in set_items:
            q = q.where(TRemainPointSubject.class_id.in_(set_items['class_id']))
        
        if 'subject_id' in set_items:
            q = q.where(TRemainPointSubject.subject_id.in_(set_items['subject_id']))
        
        if 'knowledge_id' in set_items:
            q = q.where(TRemainPointSubject.knowledge_id.in_(set_items['knowledge_id']))
        
        if 'answer_txt' in set_items:
            q = q.where(TRemainPointSubject.answer_txt.in_(set_items['answer_txt']))
        
        if 'answer_pic_path' in set_items:
            q = q.where(TRemainPointSubject.answer_pic_path.in_(set_items['answer_pic_path']))
        
        if 'answer_audio_path' in set_items:
            q = q.where(TRemainPointSubject.answer_audio_path.in_(set_items['answer_audio_path']))
        
        if 'knowledge_list' in set_items:
            q = q.where(TRemainPointSubject.knowledge_list.in_(set_items['knowledge_list']))
        

        if 'rps_content' in search_items:
            q = q.where(TRemainPointSubject.rps_content.like(search_items['rps_content']))
        
        if 'rps_create_name' in search_items:
            q = q.where(TRemainPointSubject.rps_create_name.like(search_items['rps_create_name']))
        
        if 'answer_txt' in search_items:
            q = q.where(TRemainPointSubject.answer_txt.like(search_items['answer_txt']))
        
        if 'answer_pic_path' in search_items:
            q = q.where(TRemainPointSubject.answer_pic_path.like(search_items['answer_pic_path']))
        
        if 'answer_audio_path' in search_items:
            q = q.where(TRemainPointSubject.answer_audio_path.like(search_items['answer_audio_path']))
        
        if 'knowledge_list' in search_items:
            q = q.where(TRemainPointSubject.knowledge_list.like(search_items['knowledge_list']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TRemainPointSubject.knowledge_list.asc())
                orders.append(TRemainPointSubject.id.asc())
            elif val == 'desc':
                #orders.append(TRemainPointSubject.knowledge_list.desc())
                orders.append(TRemainPointSubject.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_remain_point_subject_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SRemainPointSubject.parse_obj(t.__dict__) for t in t_remain_point_subject_list]


def filter_count_remain_point_subject(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TRemainPointSubject)


        if 'rps_id' in items:
            q = q.where(TRemainPointSubject.rps_id == items['rps_id'])
        if 'rps_id_start' in items:
            q = q.where(TRemainPointSubject.rps_id >= items['rps_id_start'])
        if 'rps_id_end' in items:
            q = q.where(TRemainPointSubject.rps_id <= items['rps_id_end'])
        
        if 'create_time' in items:
            q = q.where(TRemainPointSubject.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TRemainPointSubject.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TRemainPointSubject.create_time <= items['create_time_end'])
        
        if 'rps_content' in items:
            q = q.where(TRemainPointSubject.rps_content == items['rps_content'])
        if 'rps_content_start' in items:
            q = q.where(TRemainPointSubject.rps_content >= items['rps_content_start'])
        if 'rps_content_end' in items:
            q = q.where(TRemainPointSubject.rps_content <= items['rps_content_end'])
        
        if 'rps_create_name' in items:
            q = q.where(TRemainPointSubject.rps_create_name == items['rps_create_name'])
        if 'rps_create_name_start' in items:
            q = q.where(TRemainPointSubject.rps_create_name >= items['rps_create_name_start'])
        if 'rps_create_name_end' in items:
            q = q.where(TRemainPointSubject.rps_create_name <= items['rps_create_name_end'])
        
        if 'class_id' in items:
            q = q.where(TRemainPointSubject.class_id == items['class_id'])
        if 'class_id_start' in items:
            q = q.where(TRemainPointSubject.class_id >= items['class_id_start'])
        if 'class_id_end' in items:
            q = q.where(TRemainPointSubject.class_id <= items['class_id_end'])
        
        if 'subject_id' in items:
            q = q.where(TRemainPointSubject.subject_id == items['subject_id'])
        if 'subject_id_start' in items:
            q = q.where(TRemainPointSubject.subject_id >= items['subject_id_start'])
        if 'subject_id_end' in items:
            q = q.where(TRemainPointSubject.subject_id <= items['subject_id_end'])
        
        if 'knowledge_id' in items:
            q = q.where(TRemainPointSubject.knowledge_id == items['knowledge_id'])
        if 'knowledge_id_start' in items:
            q = q.where(TRemainPointSubject.knowledge_id >= items['knowledge_id_start'])
        if 'knowledge_id_end' in items:
            q = q.where(TRemainPointSubject.knowledge_id <= items['knowledge_id_end'])
        
        if 'answer_txt' in items:
            q = q.where(TRemainPointSubject.answer_txt == items['answer_txt'])
        if 'answer_txt_start' in items:
            q = q.where(TRemainPointSubject.answer_txt >= items['answer_txt_start'])
        if 'answer_txt_end' in items:
            q = q.where(TRemainPointSubject.answer_txt <= items['answer_txt_end'])
        
        if 'answer_pic_path' in items:
            q = q.where(TRemainPointSubject.answer_pic_path == items['answer_pic_path'])
        if 'answer_pic_path_start' in items:
            q = q.where(TRemainPointSubject.answer_pic_path >= items['answer_pic_path_start'])
        if 'answer_pic_path_end' in items:
            q = q.where(TRemainPointSubject.answer_pic_path <= items['answer_pic_path_end'])
        
        if 'answer_audio_path' in items:
            q = q.where(TRemainPointSubject.answer_audio_path == items['answer_audio_path'])
        if 'answer_audio_path_start' in items:
            q = q.where(TRemainPointSubject.answer_audio_path >= items['answer_audio_path_start'])
        if 'answer_audio_path_end' in items:
            q = q.where(TRemainPointSubject.answer_audio_path <= items['answer_audio_path_end'])
        
        if 'knowledge_list' in items:
            q = q.where(TRemainPointSubject.knowledge_list == items['knowledge_list'])
        if 'knowledge_list_start' in items:
            q = q.where(TRemainPointSubject.knowledge_list >= items['knowledge_list_start'])
        if 'knowledge_list_end' in items:
            q = q.where(TRemainPointSubject.knowledge_list <= items['knowledge_list_end'])
        

        if 'rps_id' in set_items:
            q = q.where(TRemainPointSubject.rps_id.in_(set_items['rps_id']))
        
        if 'create_time' in set_items:
            q = q.where(TRemainPointSubject.create_time.in_(set_items['create_time']))
        
        if 'rps_content' in set_items:
            q = q.where(TRemainPointSubject.rps_content.in_(set_items['rps_content']))
        
        if 'rps_create_name' in set_items:
            q = q.where(TRemainPointSubject.rps_create_name.in_(set_items['rps_create_name']))
        
        if 'class_id' in set_items:
            q = q.where(TRemainPointSubject.class_id.in_(set_items['class_id']))
        
        if 'subject_id' in set_items:
            q = q.where(TRemainPointSubject.subject_id.in_(set_items['subject_id']))
        
        if 'knowledge_id' in set_items:
            q = q.where(TRemainPointSubject.knowledge_id.in_(set_items['knowledge_id']))
        
        if 'answer_txt' in set_items:
            q = q.where(TRemainPointSubject.answer_txt.in_(set_items['answer_txt']))
        
        if 'answer_pic_path' in set_items:
            q = q.where(TRemainPointSubject.answer_pic_path.in_(set_items['answer_pic_path']))
        
        if 'answer_audio_path' in set_items:
            q = q.where(TRemainPointSubject.answer_audio_path.in_(set_items['answer_audio_path']))
        
        if 'knowledge_list' in set_items:
            q = q.where(TRemainPointSubject.knowledge_list.in_(set_items['knowledge_list']))
        

        if 'rps_content' in search_items:
            q = q.where(TRemainPointSubject.rps_content.like(search_items['rps_content']))
        
        if 'rps_create_name' in search_items:
            q = q.where(TRemainPointSubject.rps_create_name.like(search_items['rps_create_name']))
        
        if 'answer_txt' in search_items:
            q = q.where(TRemainPointSubject.answer_txt.like(search_items['answer_txt']))
        
        if 'answer_pic_path' in search_items:
            q = q.where(TRemainPointSubject.answer_pic_path.like(search_items['answer_pic_path']))
        
        if 'answer_audio_path' in search_items:
            q = q.where(TRemainPointSubject.answer_audio_path.like(search_items['answer_audio_path']))
        
        if 'knowledge_list' in search_items:
            q = q.where(TRemainPointSubject.knowledge_list.like(search_items['knowledge_list']))
        
    
        c = q.count()
        return c

    
def insert_sh_clas(item: CreateShClas, db: Optional[SessionLocal] = None) -> SShClas:
    data = model2dict(item)
    t = TShClas(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SShClas.parse_obj(t.__dict__)

    
def delete_sh_clas(sh_clas_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TShClas).where(TShClas.id == sh_clas_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TShClas).where(TShClas.id == sh_clas_id).delete()
        db.commit()

    
def update_sh_clas(item: SShClas, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TShClas).where(TShClas.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TShClas).where(TShClas.id == item.id).update(data)
        db.commit()

    
def get_sh_clas(sh_clas_id: int) -> Optional[SShClas]:
    with Dao() as db:
        t = db.query(TShClas).where(TShClas.id == sh_clas_id).first()
        if t:
            return SShClas.parse_obj(t.__dict__)
        else:
            return None


def filter_sh_clas(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SShClas]:
    with Dao() as db:
        q = db.query(TShClas)


        if 'cl_id' in items:
            q = q.where(TShClas.cl_id == items['cl_id'])
        if 'cl_id_start' in items:
            q = q.where(TShClas.cl_id >= items['cl_id_start'])
        if 'cl_id_end' in items:
            q = q.where(TShClas.cl_id <= items['cl_id_end'])
        
        if 'create_time' in items:
            q = q.where(TShClas.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TShClas.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TShClas.create_time <= items['create_time_end'])
        
        if 'cl_name' in items:
            q = q.where(TShClas.cl_name == items['cl_name'])
        if 'cl_name_start' in items:
            q = q.where(TShClas.cl_name >= items['cl_name_start'])
        if 'cl_name_end' in items:
            q = q.where(TShClas.cl_name <= items['cl_name_end'])
        
        if 'cl_create_name' in items:
            q = q.where(TShClas.cl_create_name == items['cl_create_name'])
        if 'cl_create_name_start' in items:
            q = q.where(TShClas.cl_create_name >= items['cl_create_name_start'])
        if 'cl_create_name_end' in items:
            q = q.where(TShClas.cl_create_name <= items['cl_create_name_end'])
        

        if 'cl_id' in set_items:
            q = q.where(TShClas.cl_id.in_(set_items['cl_id']))
        
        if 'create_time' in set_items:
            q = q.where(TShClas.create_time.in_(set_items['create_time']))
        
        if 'cl_name' in set_items:
            q = q.where(TShClas.cl_name.in_(set_items['cl_name']))
        
        if 'cl_create_name' in set_items:
            q = q.where(TShClas.cl_create_name.in_(set_items['cl_create_name']))
        

        if 'cl_name' in search_items:
            q = q.where(TShClas.cl_name.like(search_items['cl_name']))
        
        if 'cl_create_name' in search_items:
            q = q.where(TShClas.cl_create_name.like(search_items['cl_create_name']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TShClas.cl_create_name.asc())
                orders.append(TShClas.id.asc())
            elif val == 'desc':
                #orders.append(TShClas.cl_create_name.desc())
                orders.append(TShClas.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_sh_clas_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SShClas.parse_obj(t.__dict__) for t in t_sh_clas_list]


def filter_count_sh_clas(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TShClas)


        if 'cl_id' in items:
            q = q.where(TShClas.cl_id == items['cl_id'])
        if 'cl_id_start' in items:
            q = q.where(TShClas.cl_id >= items['cl_id_start'])
        if 'cl_id_end' in items:
            q = q.where(TShClas.cl_id <= items['cl_id_end'])
        
        if 'create_time' in items:
            q = q.where(TShClas.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TShClas.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TShClas.create_time <= items['create_time_end'])
        
        if 'cl_name' in items:
            q = q.where(TShClas.cl_name == items['cl_name'])
        if 'cl_name_start' in items:
            q = q.where(TShClas.cl_name >= items['cl_name_start'])
        if 'cl_name_end' in items:
            q = q.where(TShClas.cl_name <= items['cl_name_end'])
        
        if 'cl_create_name' in items:
            q = q.where(TShClas.cl_create_name == items['cl_create_name'])
        if 'cl_create_name_start' in items:
            q = q.where(TShClas.cl_create_name >= items['cl_create_name_start'])
        if 'cl_create_name_end' in items:
            q = q.where(TShClas.cl_create_name <= items['cl_create_name_end'])
        

        if 'cl_id' in set_items:
            q = q.where(TShClas.cl_id.in_(set_items['cl_id']))
        
        if 'create_time' in set_items:
            q = q.where(TShClas.create_time.in_(set_items['create_time']))
        
        if 'cl_name' in set_items:
            q = q.where(TShClas.cl_name.in_(set_items['cl_name']))
        
        if 'cl_create_name' in set_items:
            q = q.where(TShClas.cl_create_name.in_(set_items['cl_create_name']))
        

        if 'cl_name' in search_items:
            q = q.where(TShClas.cl_name.like(search_items['cl_name']))
        
        if 'cl_create_name' in search_items:
            q = q.where(TShClas.cl_create_name.like(search_items['cl_create_name']))
        
    
        c = q.count()
        return c

    
def insert_sh_subject(item: CreateShSubject, db: Optional[SessionLocal] = None) -> SShSubject:
    data = model2dict(item)
    t = TShSubject(**data)
    if db:
        db.add(t)
        db.flush()
        db.refresh(t)
        return SAddress.parse_obj(t.__dict__)
    with Dao() as db:
        db.add(t)
        db.commit()
        db.refresh(t)
    return SShSubject.parse_obj(t.__dict__)

    
def delete_sh_subject(sh_subject_id: int, db: Optional[SessionLocal] = None):
    if db:
        db.query(TShSubject).where(TShSubject.id == sh_subject_id).delete()
        db.flush()
        return
    
    with Dao() as db:
        db.query(TShSubject).where(TShSubject.id == sh_subject_id).delete()
        db.commit()

    
def update_sh_subject(item: SShSubject, db: Optional[SessionLocal] = None):
    data = model2dict(item)
    data.pop('id')
    if db:
        db.query(TShSubject).where(TShSubject.id == item.id).update(data)
        db.flush()
        return
    
    with Dao() as db:
        db.query(TShSubject).where(TShSubject.id == item.id).update(data)
        db.commit()

    
def get_sh_subject(sh_subject_id: int) -> Optional[SShSubject]:
    with Dao() as db:
        t = db.query(TShSubject).where(TShSubject.id == sh_subject_id).first()
        if t:
            return SShSubject.parse_obj(t.__dict__)
        else:
            return None


def filter_sh_subject(
    items: dict, 
    search_items: dict={}, 
    set_items: dict={}, 
    order_items: dict={},
    page: int = 1,
    page_size: int = 20) -> List[SShSubject]:
    with Dao() as db:
        q = db.query(TShSubject)


        if 'su_id' in items:
            q = q.where(TShSubject.su_id == items['su_id'])
        if 'su_id_start' in items:
            q = q.where(TShSubject.su_id >= items['su_id_start'])
        if 'su_id_end' in items:
            q = q.where(TShSubject.su_id <= items['su_id_end'])
        
        if 'create_time' in items:
            q = q.where(TShSubject.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TShSubject.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TShSubject.create_time <= items['create_time_end'])
        
        if 'su_name' in items:
            q = q.where(TShSubject.su_name == items['su_name'])
        if 'su_name_start' in items:
            q = q.where(TShSubject.su_name >= items['su_name_start'])
        if 'su_name_end' in items:
            q = q.where(TShSubject.su_name <= items['su_name_end'])
        
        if 'su_create_name' in items:
            q = q.where(TShSubject.su_create_name == items['su_create_name'])
        if 'su_create_name_start' in items:
            q = q.where(TShSubject.su_create_name >= items['su_create_name_start'])
        if 'su_create_name_end' in items:
            q = q.where(TShSubject.su_create_name <= items['su_create_name_end'])
        
        if 'class_id' in items:
            q = q.where(TShSubject.class_id == items['class_id'])
        if 'class_id_start' in items:
            q = q.where(TShSubject.class_id >= items['class_id_start'])
        if 'class_id_end' in items:
            q = q.where(TShSubject.class_id <= items['class_id_end'])
        
        if 'knowledge_list' in items:
            q = q.where(TShSubject.knowledge_list == items['knowledge_list'])
        if 'knowledge_list_start' in items:
            q = q.where(TShSubject.knowledge_list >= items['knowledge_list_start'])
        if 'knowledge_list_end' in items:
            q = q.where(TShSubject.knowledge_list <= items['knowledge_list_end'])
        

        if 'su_id' in set_items:
            q = q.where(TShSubject.su_id.in_(set_items['su_id']))
        
        if 'create_time' in set_items:
            q = q.where(TShSubject.create_time.in_(set_items['create_time']))
        
        if 'su_name' in set_items:
            q = q.where(TShSubject.su_name.in_(set_items['su_name']))
        
        if 'su_create_name' in set_items:
            q = q.where(TShSubject.su_create_name.in_(set_items['su_create_name']))
        
        if 'class_id' in set_items:
            q = q.where(TShSubject.class_id.in_(set_items['class_id']))
        
        if 'knowledge_list' in set_items:
            q = q.where(TShSubject.knowledge_list.in_(set_items['knowledge_list']))
        

        if 'su_name' in search_items:
            q = q.where(TShSubject.su_name.like(search_items['su_name']))
        
        if 'su_create_name' in search_items:
            q = q.where(TShSubject.su_create_name.like(search_items['su_create_name']))
        
        if 'knowledge_list' in search_items:
            q = q.where(TShSubject.knowledge_list.like(search_items['knowledge_list']))
        
    

        orders = []
        for col, val in order_items.items():
            if val == 'asc':          
                #orders.append(TShSubject.knowledge_list.asc())
                orders.append(TShSubject.id.asc())
            elif val == 'desc':
                #orders.append(TShSubject.knowledge_list.desc())
                orders.append(TShSubject.id.desc())
            else:
                raise HTTPException(400, 'order value must be asc or desc')
        if len(order_items) > 0:
            q = q.order_by(*orders)
        
        t_sh_subject_list = q.offset(page*page_size-page_size).limit(page_size).all()
        return [SShSubject.parse_obj(t.__dict__) for t in t_sh_subject_list]


def filter_count_sh_subject(items: dict, search_items: dict={}, set_items: dict={}) -> int:
    with Dao() as db:
        q = db.query(TShSubject)


        if 'su_id' in items:
            q = q.where(TShSubject.su_id == items['su_id'])
        if 'su_id_start' in items:
            q = q.where(TShSubject.su_id >= items['su_id_start'])
        if 'su_id_end' in items:
            q = q.where(TShSubject.su_id <= items['su_id_end'])
        
        if 'create_time' in items:
            q = q.where(TShSubject.create_time == items['create_time'])
        if 'create_time_start' in items:
            q = q.where(TShSubject.create_time >= items['create_time_start'])
        if 'create_time_end' in items:
            q = q.where(TShSubject.create_time <= items['create_time_end'])
        
        if 'su_name' in items:
            q = q.where(TShSubject.su_name == items['su_name'])
        if 'su_name_start' in items:
            q = q.where(TShSubject.su_name >= items['su_name_start'])
        if 'su_name_end' in items:
            q = q.where(TShSubject.su_name <= items['su_name_end'])
        
        if 'su_create_name' in items:
            q = q.where(TShSubject.su_create_name == items['su_create_name'])
        if 'su_create_name_start' in items:
            q = q.where(TShSubject.su_create_name >= items['su_create_name_start'])
        if 'su_create_name_end' in items:
            q = q.where(TShSubject.su_create_name <= items['su_create_name_end'])
        
        if 'class_id' in items:
            q = q.where(TShSubject.class_id == items['class_id'])
        if 'class_id_start' in items:
            q = q.where(TShSubject.class_id >= items['class_id_start'])
        if 'class_id_end' in items:
            q = q.where(TShSubject.class_id <= items['class_id_end'])
        
        if 'knowledge_list' in items:
            q = q.where(TShSubject.knowledge_list == items['knowledge_list'])
        if 'knowledge_list_start' in items:
            q = q.where(TShSubject.knowledge_list >= items['knowledge_list_start'])
        if 'knowledge_list_end' in items:
            q = q.where(TShSubject.knowledge_list <= items['knowledge_list_end'])
        

        if 'su_id' in set_items:
            q = q.where(TShSubject.su_id.in_(set_items['su_id']))
        
        if 'create_time' in set_items:
            q = q.where(TShSubject.create_time.in_(set_items['create_time']))
        
        if 'su_name' in set_items:
            q = q.where(TShSubject.su_name.in_(set_items['su_name']))
        
        if 'su_create_name' in set_items:
            q = q.where(TShSubject.su_create_name.in_(set_items['su_create_name']))
        
        if 'class_id' in set_items:
            q = q.where(TShSubject.class_id.in_(set_items['class_id']))
        
        if 'knowledge_list' in set_items:
            q = q.where(TShSubject.knowledge_list.in_(set_items['knowledge_list']))
        

        if 'su_name' in search_items:
            q = q.where(TShSubject.su_name.like(search_items['su_name']))
        
        if 'su_create_name' in search_items:
            q = q.where(TShSubject.su_create_name.like(search_items['su_create_name']))
        
        if 'knowledge_list' in search_items:
            q = q.where(TShSubject.knowledge_list.like(search_items['knowledge_list']))
        
    
        c = q.count()
        return c
