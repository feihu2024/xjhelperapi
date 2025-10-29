from fastapi import APIRouter
from typing import List
from dao import d_db
from model.m_schema import *
from fastapi.exceptions import HTTPException
import re

router = APIRouter()

    
@router.post(f'/balance/create', response_model=SBalance)
async def create_balance(item: CreateBalance) -> SBalance:
    dict_item = dict(item)
    for k,v in dict_item.items():
        if v is not None:
            v = str(v)
            v = v.replace(" ", "")
            get_search = re.search(r"'", v, flags=0)
            get_search2 = re.search(r'%27', v, flags=0)
            get_search3 = re.search(r'unionselect', v, flags=0)
            if get_search or get_search2 or get_search3:
               raise HTTPException(status_code=404, detail='bad way~~~~~~')

    return d_db.insert_balance(item)
        
    
@router.post(f'/balance/update', response_model=str)
async def update_balance(item: SBalance) -> str:
    d_db.update_balance(item)
    return "success"

    
@router.get(f'/balance/get', response_model=SBalance)
async def get_balance(balance_id: int) -> SBalance:
    return d_db.get_balance(balance_id)


@router.get(f'/balance/filter', response_model=FilterResBalance)
async def filter_balance(
        id: Optional[str] = None, 
        user_id: Optional[str] = None, 
        change: Optional[str] = None, 
        balance: Optional[str] = None, 
        type: Optional[str] = None, 
        description: Optional[str] = None, 
        create_time: Optional[str] = None, 
        user_withdraw_id: Optional[str] = None, 
        operator_id: Optional[str] = None, 
        out_trade_no: Optional[str] = None, 
        good_id: Optional[str] = None, 
        good_title: Optional[str] = None, 
        good_num: Optional[str] = None, 
        l_id: Optional[str] = None, 
        l_user_id: Optional[str] = None, 
        l_change: Optional[str] = None, 
        l_balance: Optional[str] = None, 
        l_type: Optional[str] = None, 
        l_description: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_user_withdraw_id: Optional[str] = None, 
        l_operator_id: Optional[str] = None, 
        l_out_trade_no: Optional[str] = None, 
        l_good_id: Optional[str] = None, 
        l_good_title: Optional[str] = None, 
        l_good_num: Optional[str] = None, 
        s_type: Optional[str] = None, 
        s_description: Optional[str] = None, 
        s_out_trade_no: Optional[str] = None, 
        s_good_id: Optional[str] = None, 
        s_good_title: Optional[str] = None, 
        s_good_num: Optional[str] = None,
        order_by: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResBalance:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if id is not None:
        values = id.split(',')
        if len(values) == 1:
            val = values[0]
            items['id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['id_end'] = int(val)
        
    if user_id is not None:
        values = user_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['user_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['user_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['user_id_end'] = int(val)
        
    if change is not None:
        values = change.split(',')
        if len(values) == 1:
            val = values[0]
            items['change'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['change_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['change_end'] = int(val)
        
    if balance is not None:
        values = balance.split(',')
        if len(values) == 1:
            val = values[0]
            items['balance'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['balance_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['balance_end'] = int(val)
        
    if type is not None:
        values = type.split(',')
        if len(values) == 1:
            val = values[0]
            items['type'] = val
        else:
            val = values[0]
            if val != '':
                items['type_start'] = val
            
            val = values[1]
            if val != '':
                items['type_end'] = val
        
    if description is not None:
        values = description.split(',')
        if len(values) == 1:
            val = values[0]
            items['description'] = val
        else:
            val = values[0]
            if val != '':
                items['description_start'] = val
            
            val = values[1]
            if val != '':
                items['description_end'] = val
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if user_withdraw_id is not None:
        values = user_withdraw_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['user_withdraw_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['user_withdraw_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['user_withdraw_id_end'] = int(val)
        
    if operator_id is not None:
        values = operator_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['operator_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['operator_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['operator_id_end'] = int(val)
        
    if out_trade_no is not None:
        values = out_trade_no.split(',')
        if len(values) == 1:
            val = values[0]
            items['out_trade_no'] = val
        else:
            val = values[0]
            if val != '':
                items['out_trade_no_start'] = val
            
            val = values[1]
            if val != '':
                items['out_trade_no_end'] = val
        
    if good_id is not None:
        values = good_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['good_id'] = val
        else:
            val = values[0]
            if val != '':
                items['good_id_start'] = val
            
            val = values[1]
            if val != '':
                items['good_id_end'] = val
        
    if good_title is not None:
        values = good_title.split(',')
        if len(values) == 1:
            val = values[0]
            items['good_title'] = val
        else:
            val = values[0]
            if val != '':
                items['good_title_start'] = val
            
            val = values[1]
            if val != '':
                items['good_title_end'] = val
        
    if good_num is not None:
        values = good_num.split(',')
        if len(values) == 1:
            val = values[0]
            items['good_num'] = val
        else:
            val = values[0]
            if val != '':
                items['good_num_start'] = val
            
            val = values[1]
            if val != '':
                items['good_num_end'] = val
        

    if s_type is not None:
        search_items['type'] = '%' + s_type + '%'
        
    if s_description is not None:
        search_items['description'] = '%' + s_description + '%'
        
    if s_out_trade_no is not None:
        search_items['out_trade_no'] = '%' + s_out_trade_no + '%'
        
    if s_good_id is not None:
        search_items['good_id'] = '%' + s_good_id + '%'
        
    if s_good_title is not None:
        search_items['good_title'] = '%' + s_good_title + '%'
        
    if s_good_num is not None:
        search_items['good_num'] = '%' + s_good_num + '%'
        

    if l_id is not None:
        values = l_id.split(',')
        values = [int(val) for val in values]
        set_items['id'] = values
        
    if l_user_id is not None:
        values = l_user_id.split(',')
        values = [int(val) for val in values]
        set_items['user_id'] = values
        
    if l_change is not None:
        values = l_change.split(',')
        values = [int(val) for val in values]
        set_items['change'] = values
        
    if l_balance is not None:
        values = l_balance.split(',')
        values = [int(val) for val in values]
        set_items['balance'] = values
        
    if l_type is not None:
        values = l_type.split(',')
        values = [val for val in values]
        set_items['type'] = values
        
    if l_description is not None:
        values = l_description.split(',')
        values = [val for val in values]
        set_items['description'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_user_withdraw_id is not None:
        values = l_user_withdraw_id.split(',')
        values = [int(val) for val in values]
        set_items['user_withdraw_id'] = values
        
    if l_operator_id is not None:
        values = l_operator_id.split(',')
        values = [int(val) for val in values]
        set_items['operator_id'] = values
        
    if l_out_trade_no is not None:
        values = l_out_trade_no.split(',')
        values = [val for val in values]
        set_items['out_trade_no'] = values
        
    if l_good_id is not None:
        values = l_good_id.split(',')
        values = [val for val in values]
        set_items['good_id'] = values
        
    if l_good_title is not None:
        values = l_good_title.split(',')
        values = [val for val in values]
        set_items['good_title'] = values
        
    if l_good_num is not None:
        values = l_good_num.split(',')
        values = [val for val in values]
        set_items['good_num'] = values
            
    
    
    order_items = dict()
    if order_by is not None:
        orders = order_by.split(',')
        for order in orders:
            if order.startswith('-'):
                order_items[order[1:]] = 'desc'
            else:
                order_items[order] = 'asc'
    data = d_db.filter_balance(items, search_items, set_items, order_items, page, page_size)
    c = d_db.filter_count_balance(items, search_items, set_items)
    
    return FilterResBalance(data=data, total=c)


@router.get(f'/balance/fast_filter', response_model=FilterResBalance)
async def fast_filter_balance(
        id: Optional[str] = None, 
        user_id: Optional[str] = None, 
        change: Optional[str] = None, 
        balance: Optional[str] = None, 
        type: Optional[str] = None, 
        description: Optional[str] = None, 
        create_time: Optional[str] = None, 
        user_withdraw_id: Optional[str] = None, 
        operator_id: Optional[str] = None, 
        out_trade_no: Optional[str] = None, 
        good_id: Optional[str] = None, 
        good_title: Optional[str] = None, 
        good_num: Optional[str] = None, 
        l_id: Optional[str] = None, 
        l_user_id: Optional[str] = None, 
        l_change: Optional[str] = None, 
        l_balance: Optional[str] = None, 
        l_type: Optional[str] = None, 
        l_description: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_user_withdraw_id: Optional[str] = None, 
        l_operator_id: Optional[str] = None, 
        l_out_trade_no: Optional[str] = None, 
        l_good_id: Optional[str] = None, 
        l_good_title: Optional[str] = None, 
        l_good_num: Optional[str] = None, 
        s_type: Optional[str] = None, 
        s_description: Optional[str] = None, 
        s_out_trade_no: Optional[str] = None, 
        s_good_id: Optional[str] = None, 
        s_good_title: Optional[str] = None, 
        s_good_num: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResBalance:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if id is not None:
        values = id.split(',')
        if len(values) == 1:
            val = values[0]
            items['id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['id_end'] = int(val)
        
    if user_id is not None:
        values = user_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['user_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['user_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['user_id_end'] = int(val)
        
    if change is not None:
        values = change.split(',')
        if len(values) == 1:
            val = values[0]
            items['change'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['change_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['change_end'] = int(val)
        
    if balance is not None:
        values = balance.split(',')
        if len(values) == 1:
            val = values[0]
            items['balance'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['balance_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['balance_end'] = int(val)
        
    if type is not None:
        values = type.split(',')
        if len(values) == 1:
            val = values[0]
            items['type'] = val
        else:
            val = values[0]
            if val != '':
                items['type_start'] = val
            
            val = values[1]
            if val != '':
                items['type_end'] = val
        
    if description is not None:
        values = description.split(',')
        if len(values) == 1:
            val = values[0]
            items['description'] = val
        else:
            val = values[0]
            if val != '':
                items['description_start'] = val
            
            val = values[1]
            if val != '':
                items['description_end'] = val
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if user_withdraw_id is not None:
        values = user_withdraw_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['user_withdraw_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['user_withdraw_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['user_withdraw_id_end'] = int(val)
        
    if operator_id is not None:
        values = operator_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['operator_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['operator_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['operator_id_end'] = int(val)
        
    if out_trade_no is not None:
        values = out_trade_no.split(',')
        if len(values) == 1:
            val = values[0]
            items['out_trade_no'] = val
        else:
            val = values[0]
            if val != '':
                items['out_trade_no_start'] = val
            
            val = values[1]
            if val != '':
                items['out_trade_no_end'] = val
        
    if good_id is not None:
        values = good_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['good_id'] = val
        else:
            val = values[0]
            if val != '':
                items['good_id_start'] = val
            
            val = values[1]
            if val != '':
                items['good_id_end'] = val
        
    if good_title is not None:
        values = good_title.split(',')
        if len(values) == 1:
            val = values[0]
            items['good_title'] = val
        else:
            val = values[0]
            if val != '':
                items['good_title_start'] = val
            
            val = values[1]
            if val != '':
                items['good_title_end'] = val
        
    if good_num is not None:
        values = good_num.split(',')
        if len(values) == 1:
            val = values[0]
            items['good_num'] = val
        else:
            val = values[0]
            if val != '':
                items['good_num_start'] = val
            
            val = values[1]
            if val != '':
                items['good_num_end'] = val
        

    if s_type is not None:
        search_items['type'] = '%' + s_type + '%'
        
    if s_description is not None:
        search_items['description'] = '%' + s_description + '%'
        
    if s_out_trade_no is not None:
        search_items['out_trade_no'] = '%' + s_out_trade_no + '%'
        
    if s_good_id is not None:
        search_items['good_id'] = '%' + s_good_id + '%'
        
    if s_good_title is not None:
        search_items['good_title'] = '%' + s_good_title + '%'
        
    if s_good_num is not None:
        search_items['good_num'] = '%' + s_good_num + '%'
        

    if l_id is not None:
        values = l_id.split(',')
        values = [int(val) for val in values]
        set_items['id'] = values
        
    if l_user_id is not None:
        values = l_user_id.split(',')
        values = [int(val) for val in values]
        set_items['user_id'] = values
        
    if l_change is not None:
        values = l_change.split(',')
        values = [int(val) for val in values]
        set_items['change'] = values
        
    if l_balance is not None:
        values = l_balance.split(',')
        values = [int(val) for val in values]
        set_items['balance'] = values
        
    if l_type is not None:
        values = l_type.split(',')
        values = [val for val in values]
        set_items['type'] = values
        
    if l_description is not None:
        values = l_description.split(',')
        values = [val for val in values]
        set_items['description'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_user_withdraw_id is not None:
        values = l_user_withdraw_id.split(',')
        values = [int(val) for val in values]
        set_items['user_withdraw_id'] = values
        
    if l_operator_id is not None:
        values = l_operator_id.split(',')
        values = [int(val) for val in values]
        set_items['operator_id'] = values
        
    if l_out_trade_no is not None:
        values = l_out_trade_no.split(',')
        values = [val for val in values]
        set_items['out_trade_no'] = values
        
    if l_good_id is not None:
        values = l_good_id.split(',')
        values = [val for val in values]
        set_items['good_id'] = values
        
    if l_good_title is not None:
        values = l_good_title.split(',')
        values = [val for val in values]
        set_items['good_title'] = values
        
    if l_good_num is not None:
        values = l_good_num.split(',')
        values = [val for val in values]
        set_items['good_num'] = values
            
    
    data = d_db.filter_balance(items, search_items, set_items, page, page_size)
    return FilterResBalance(data=data, total=-1)

    
@router.post(f'/chinese_point_subject/create', response_model=SChinesePointSubject)
async def create_chinese_point_subject(item: CreateChinesePointSubject) -> SChinesePointSubject:
    dict_item = dict(item)
    for k,v in dict_item.items():
        if v is not None:
            v = str(v)
            v = v.replace(" ", "")
            get_search = re.search(r"'", v, flags=0)
            get_search2 = re.search(r'%27', v, flags=0)
            get_search3 = re.search(r'unionselect', v, flags=0)
            if get_search or get_search2 or get_search3:
               raise HTTPException(status_code=404, detail='bad way~~~~~~')

    return d_db.insert_chinese_point_subject(item)
        
    
@router.post(f'/chinese_point_subject/update', response_model=str)
async def update_chinese_point_subject(item: SChinesePointSubject) -> str:
    d_db.update_chinese_point_subject(item)
    return "success"

    
@router.get(f'/chinese_point_subject/get', response_model=SChinesePointSubject)
async def get_chinese_point_subject(chinese_point_subject_id: int) -> SChinesePointSubject:
    return d_db.get_chinese_point_subject(chinese_point_subject_id)


@router.get(f'/chinese_point_subject/filter', response_model=FilterResChinesePointSubject)
async def filter_chinese_point_subject(
        cps_id: Optional[str] = None, 
        create_time: Optional[str] = None, 
        cps_content: Optional[str] = None, 
        cps_create_name: Optional[str] = None, 
        class_id: Optional[str] = None, 
        subject_id: Optional[str] = None, 
        knowledge_id: Optional[str] = None, 
        answer_txt: Optional[str] = None, 
        answer_pic_path: Optional[str] = None, 
        answer_audio_path: Optional[str] = None, 
        knowledge_list: Optional[str] = None, 
        l_cps_id: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_cps_content: Optional[str] = None, 
        l_cps_create_name: Optional[str] = None, 
        l_class_id: Optional[str] = None, 
        l_subject_id: Optional[str] = None, 
        l_knowledge_id: Optional[str] = None, 
        l_answer_txt: Optional[str] = None, 
        l_answer_pic_path: Optional[str] = None, 
        l_answer_audio_path: Optional[str] = None, 
        l_knowledge_list: Optional[str] = None, 
        s_cps_content: Optional[str] = None, 
        s_cps_create_name: Optional[str] = None, 
        s_answer_txt: Optional[str] = None, 
        s_answer_pic_path: Optional[str] = None, 
        s_answer_audio_path: Optional[str] = None, 
        s_knowledge_list: Optional[str] = None,
        order_by: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResChinesePointSubject:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if cps_id is not None:
        values = cps_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['cps_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['cps_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['cps_id_end'] = int(val)
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if cps_content is not None:
        values = cps_content.split(',')
        if len(values) == 1:
            val = values[0]
            items['cps_content'] = val
        else:
            val = values[0]
            if val != '':
                items['cps_content_start'] = val
            
            val = values[1]
            if val != '':
                items['cps_content_end'] = val
        
    if cps_create_name is not None:
        values = cps_create_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['cps_create_name'] = val
        else:
            val = values[0]
            if val != '':
                items['cps_create_name_start'] = val
            
            val = values[1]
            if val != '':
                items['cps_create_name_end'] = val
        
    if class_id is not None:
        values = class_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['class_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['class_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['class_id_end'] = int(val)
        
    if subject_id is not None:
        values = subject_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['subject_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['subject_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['subject_id_end'] = int(val)
        
    if knowledge_id is not None:
        values = knowledge_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['knowledge_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['knowledge_id_end'] = int(val)
        
    if answer_txt is not None:
        values = answer_txt.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_txt'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_txt_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_txt_end'] = val
        
    if answer_pic_path is not None:
        values = answer_pic_path.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_pic_path'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_pic_path_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_pic_path_end'] = val
        
    if answer_audio_path is not None:
        values = answer_audio_path.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_audio_path'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_audio_path_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_audio_path_end'] = val
        
    if knowledge_list is not None:
        values = knowledge_list.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_list'] = val
        else:
            val = values[0]
            if val != '':
                items['knowledge_list_start'] = val
            
            val = values[1]
            if val != '':
                items['knowledge_list_end'] = val
        

    if s_cps_content is not None:
        search_items['cps_content'] = '%' + s_cps_content + '%'
        
    if s_cps_create_name is not None:
        search_items['cps_create_name'] = '%' + s_cps_create_name + '%'
        
    if s_answer_txt is not None:
        search_items['answer_txt'] = '%' + s_answer_txt + '%'
        
    if s_answer_pic_path is not None:
        search_items['answer_pic_path'] = '%' + s_answer_pic_path + '%'
        
    if s_answer_audio_path is not None:
        search_items['answer_audio_path'] = '%' + s_answer_audio_path + '%'
        
    if s_knowledge_list is not None:
        search_items['knowledge_list'] = '%' + s_knowledge_list + '%'
        

    if l_cps_id is not None:
        values = l_cps_id.split(',')
        values = [int(val) for val in values]
        set_items['cps_id'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_cps_content is not None:
        values = l_cps_content.split(',')
        values = [val for val in values]
        set_items['cps_content'] = values
        
    if l_cps_create_name is not None:
        values = l_cps_create_name.split(',')
        values = [val for val in values]
        set_items['cps_create_name'] = values
        
    if l_class_id is not None:
        values = l_class_id.split(',')
        values = [int(val) for val in values]
        set_items['class_id'] = values
        
    if l_subject_id is not None:
        values = l_subject_id.split(',')
        values = [int(val) for val in values]
        set_items['subject_id'] = values
        
    if l_knowledge_id is not None:
        values = l_knowledge_id.split(',')
        values = [int(val) for val in values]
        set_items['knowledge_id'] = values
        
    if l_answer_txt is not None:
        values = l_answer_txt.split(',')
        values = [val for val in values]
        set_items['answer_txt'] = values
        
    if l_answer_pic_path is not None:
        values = l_answer_pic_path.split(',')
        values = [val for val in values]
        set_items['answer_pic_path'] = values
        
    if l_answer_audio_path is not None:
        values = l_answer_audio_path.split(',')
        values = [val for val in values]
        set_items['answer_audio_path'] = values
        
    if l_knowledge_list is not None:
        values = l_knowledge_list.split(',')
        values = [val for val in values]
        set_items['knowledge_list'] = values
            
    
    
    order_items = dict()
    if order_by is not None:
        orders = order_by.split(',')
        for order in orders:
            if order.startswith('-'):
                order_items[order[1:]] = 'desc'
            else:
                order_items[order] = 'asc'
    data = d_db.filter_chinese_point_subject(items, search_items, set_items, order_items, page, page_size)
    c = d_db.filter_count_chinese_point_subject(items, search_items, set_items)
    
    return FilterResChinesePointSubject(data=data, total=c)


@router.get(f'/chinese_point_subject/fast_filter', response_model=FilterResChinesePointSubject)
async def fast_filter_chinese_point_subject(
        cps_id: Optional[str] = None, 
        create_time: Optional[str] = None, 
        cps_content: Optional[str] = None, 
        cps_create_name: Optional[str] = None, 
        class_id: Optional[str] = None, 
        subject_id: Optional[str] = None, 
        knowledge_id: Optional[str] = None, 
        answer_txt: Optional[str] = None, 
        answer_pic_path: Optional[str] = None, 
        answer_audio_path: Optional[str] = None, 
        knowledge_list: Optional[str] = None, 
        l_cps_id: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_cps_content: Optional[str] = None, 
        l_cps_create_name: Optional[str] = None, 
        l_class_id: Optional[str] = None, 
        l_subject_id: Optional[str] = None, 
        l_knowledge_id: Optional[str] = None, 
        l_answer_txt: Optional[str] = None, 
        l_answer_pic_path: Optional[str] = None, 
        l_answer_audio_path: Optional[str] = None, 
        l_knowledge_list: Optional[str] = None, 
        s_cps_content: Optional[str] = None, 
        s_cps_create_name: Optional[str] = None, 
        s_answer_txt: Optional[str] = None, 
        s_answer_pic_path: Optional[str] = None, 
        s_answer_audio_path: Optional[str] = None, 
        s_knowledge_list: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResChinesePointSubject:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if cps_id is not None:
        values = cps_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['cps_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['cps_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['cps_id_end'] = int(val)
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if cps_content is not None:
        values = cps_content.split(',')
        if len(values) == 1:
            val = values[0]
            items['cps_content'] = val
        else:
            val = values[0]
            if val != '':
                items['cps_content_start'] = val
            
            val = values[1]
            if val != '':
                items['cps_content_end'] = val
        
    if cps_create_name is not None:
        values = cps_create_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['cps_create_name'] = val
        else:
            val = values[0]
            if val != '':
                items['cps_create_name_start'] = val
            
            val = values[1]
            if val != '':
                items['cps_create_name_end'] = val
        
    if class_id is not None:
        values = class_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['class_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['class_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['class_id_end'] = int(val)
        
    if subject_id is not None:
        values = subject_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['subject_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['subject_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['subject_id_end'] = int(val)
        
    if knowledge_id is not None:
        values = knowledge_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['knowledge_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['knowledge_id_end'] = int(val)
        
    if answer_txt is not None:
        values = answer_txt.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_txt'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_txt_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_txt_end'] = val
        
    if answer_pic_path is not None:
        values = answer_pic_path.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_pic_path'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_pic_path_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_pic_path_end'] = val
        
    if answer_audio_path is not None:
        values = answer_audio_path.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_audio_path'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_audio_path_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_audio_path_end'] = val
        
    if knowledge_list is not None:
        values = knowledge_list.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_list'] = val
        else:
            val = values[0]
            if val != '':
                items['knowledge_list_start'] = val
            
            val = values[1]
            if val != '':
                items['knowledge_list_end'] = val
        

    if s_cps_content is not None:
        search_items['cps_content'] = '%' + s_cps_content + '%'
        
    if s_cps_create_name is not None:
        search_items['cps_create_name'] = '%' + s_cps_create_name + '%'
        
    if s_answer_txt is not None:
        search_items['answer_txt'] = '%' + s_answer_txt + '%'
        
    if s_answer_pic_path is not None:
        search_items['answer_pic_path'] = '%' + s_answer_pic_path + '%'
        
    if s_answer_audio_path is not None:
        search_items['answer_audio_path'] = '%' + s_answer_audio_path + '%'
        
    if s_knowledge_list is not None:
        search_items['knowledge_list'] = '%' + s_knowledge_list + '%'
        

    if l_cps_id is not None:
        values = l_cps_id.split(',')
        values = [int(val) for val in values]
        set_items['cps_id'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_cps_content is not None:
        values = l_cps_content.split(',')
        values = [val for val in values]
        set_items['cps_content'] = values
        
    if l_cps_create_name is not None:
        values = l_cps_create_name.split(',')
        values = [val for val in values]
        set_items['cps_create_name'] = values
        
    if l_class_id is not None:
        values = l_class_id.split(',')
        values = [int(val) for val in values]
        set_items['class_id'] = values
        
    if l_subject_id is not None:
        values = l_subject_id.split(',')
        values = [int(val) for val in values]
        set_items['subject_id'] = values
        
    if l_knowledge_id is not None:
        values = l_knowledge_id.split(',')
        values = [int(val) for val in values]
        set_items['knowledge_id'] = values
        
    if l_answer_txt is not None:
        values = l_answer_txt.split(',')
        values = [val for val in values]
        set_items['answer_txt'] = values
        
    if l_answer_pic_path is not None:
        values = l_answer_pic_path.split(',')
        values = [val for val in values]
        set_items['answer_pic_path'] = values
        
    if l_answer_audio_path is not None:
        values = l_answer_audio_path.split(',')
        values = [val for val in values]
        set_items['answer_audio_path'] = values
        
    if l_knowledge_list is not None:
        values = l_knowledge_list.split(',')
        values = [val for val in values]
        set_items['knowledge_list'] = values
            
    
    data = d_db.filter_chinese_point_subject(items, search_items, set_items, page, page_size)
    return FilterResChinesePointSubject(data=data, total=-1)

    
@router.post(f'/city/create', response_model=SCity)
async def create_city(item: CreateCity) -> SCity:
    dict_item = dict(item)
    for k,v in dict_item.items():
        if v is not None:
            v = str(v)
            v = v.replace(" ", "")
            get_search = re.search(r"'", v, flags=0)
            get_search2 = re.search(r'%27', v, flags=0)
            get_search3 = re.search(r'unionselect', v, flags=0)
            if get_search or get_search2 or get_search3:
               raise HTTPException(status_code=404, detail='bad way~~~~~~')

    return d_db.insert_city(item)
        
    
@router.post(f'/city/update', response_model=str)
async def update_city(item: SCity) -> str:
    d_db.update_city(item)
    return "success"

    
@router.get(f'/city/get', response_model=SCity)
async def get_city(city_id: int) -> SCity:
    return d_db.get_city(city_id)


@router.get(f'/city/filter', response_model=FilterResCity)
async def filter_city(
        id: Optional[str] = None, 
        cname: Optional[str] = None, 
        parid: Optional[str] = None, 
        status: Optional[str] = None, 
        l_id: Optional[str] = None, 
        l_cname: Optional[str] = None, 
        l_parid: Optional[str] = None, 
        l_status: Optional[str] = None, 
        s_cname: Optional[str] = None,
        order_by: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResCity:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if id is not None:
        values = id.split(',')
        if len(values) == 1:
            val = values[0]
            items['id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['id_end'] = int(val)
        
    if cname is not None:
        values = cname.split(',')
        if len(values) == 1:
            val = values[0]
            items['cname'] = val
        else:
            val = values[0]
            if val != '':
                items['cname_start'] = val
            
            val = values[1]
            if val != '':
                items['cname_end'] = val
        
    if parid is not None:
        values = parid.split(',')
        if len(values) == 1:
            val = values[0]
            items['parid'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['parid_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['parid_end'] = int(val)
        
    if status is not None:
        values = status.split(',')
        if len(values) == 1:
            val = values[0]
            items['status'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['status_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['status_end'] = int(val)
        

    if s_cname is not None:
        search_items['cname'] = '%' + s_cname + '%'
        

    if l_id is not None:
        values = l_id.split(',')
        values = [int(val) for val in values]
        set_items['id'] = values
        
    if l_cname is not None:
        values = l_cname.split(',')
        values = [val for val in values]
        set_items['cname'] = values
        
    if l_parid is not None:
        values = l_parid.split(',')
        values = [int(val) for val in values]
        set_items['parid'] = values
        
    if l_status is not None:
        values = l_status.split(',')
        values = [int(val) for val in values]
        set_items['status'] = values
            
    
    
    order_items = dict()
    if order_by is not None:
        orders = order_by.split(',')
        for order in orders:
            if order.startswith('-'):
                order_items[order[1:]] = 'desc'
            else:
                order_items[order] = 'asc'
    data = d_db.filter_city(items, search_items, set_items, order_items, page, page_size)
    c = d_db.filter_count_city(items, search_items, set_items)
    
    return FilterResCity(data=data, total=c)


@router.get(f'/city/fast_filter', response_model=FilterResCity)
async def fast_filter_city(
        id: Optional[str] = None, 
        cname: Optional[str] = None, 
        parid: Optional[str] = None, 
        status: Optional[str] = None, 
        l_id: Optional[str] = None, 
        l_cname: Optional[str] = None, 
        l_parid: Optional[str] = None, 
        l_status: Optional[str] = None, 
        s_cname: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResCity:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if id is not None:
        values = id.split(',')
        if len(values) == 1:
            val = values[0]
            items['id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['id_end'] = int(val)
        
    if cname is not None:
        values = cname.split(',')
        if len(values) == 1:
            val = values[0]
            items['cname'] = val
        else:
            val = values[0]
            if val != '':
                items['cname_start'] = val
            
            val = values[1]
            if val != '':
                items['cname_end'] = val
        
    if parid is not None:
        values = parid.split(',')
        if len(values) == 1:
            val = values[0]
            items['parid'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['parid_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['parid_end'] = int(val)
        
    if status is not None:
        values = status.split(',')
        if len(values) == 1:
            val = values[0]
            items['status'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['status_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['status_end'] = int(val)
        

    if s_cname is not None:
        search_items['cname'] = '%' + s_cname + '%'
        

    if l_id is not None:
        values = l_id.split(',')
        values = [int(val) for val in values]
        set_items['id'] = values
        
    if l_cname is not None:
        values = l_cname.split(',')
        values = [val for val in values]
        set_items['cname'] = values
        
    if l_parid is not None:
        values = l_parid.split(',')
        values = [int(val) for val in values]
        set_items['parid'] = values
        
    if l_status is not None:
        values = l_status.split(',')
        values = [int(val) for val in values]
        set_items['status'] = values
            
    
    data = d_db.filter_city(items, search_items, set_items, page, page_size)
    return FilterResCity(data=data, total=-1)

    
@router.post(f'/coin/create', response_model=SCoin)
async def create_coin(item: CreateCoin) -> SCoin:
    dict_item = dict(item)
    for k,v in dict_item.items():
        if v is not None:
            v = str(v)
            v = v.replace(" ", "")
            get_search = re.search(r"'", v, flags=0)
            get_search2 = re.search(r'%27', v, flags=0)
            get_search3 = re.search(r'unionselect', v, flags=0)
            if get_search or get_search2 or get_search3:
               raise HTTPException(status_code=404, detail='bad way~~~~~~')

    return d_db.insert_coin(item)
        
    
@router.post(f'/coin/update', response_model=str)
async def update_coin(item: SCoin) -> str:
    d_db.update_coin(item)
    return "success"

    
@router.get(f'/coin/get', response_model=SCoin)
async def get_coin(coin_id: int) -> SCoin:
    return d_db.get_coin(coin_id)


@router.get(f'/coin/filter', response_model=FilterResCoin)
async def filter_coin(
        id: Optional[str] = None, 
        user_id: Optional[str] = None, 
        change: Optional[str] = None, 
        coin: Optional[str] = None, 
        type: Optional[str] = None, 
        description: Optional[str] = None, 
        create_time: Optional[str] = None, 
        out_trade_no: Optional[str] = None, 
        l_id: Optional[str] = None, 
        l_user_id: Optional[str] = None, 
        l_change: Optional[str] = None, 
        l_coin: Optional[str] = None, 
        l_type: Optional[str] = None, 
        l_description: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_out_trade_no: Optional[str] = None, 
        s_type: Optional[str] = None, 
        s_description: Optional[str] = None, 
        s_out_trade_no: Optional[str] = None,
        order_by: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResCoin:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if id is not None:
        values = id.split(',')
        if len(values) == 1:
            val = values[0]
            items['id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['id_end'] = int(val)
        
    if user_id is not None:
        values = user_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['user_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['user_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['user_id_end'] = int(val)
        
    if change is not None:
        values = change.split(',')
        if len(values) == 1:
            val = values[0]
            items['change'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['change_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['change_end'] = int(val)
        
    if coin is not None:
        values = coin.split(',')
        if len(values) == 1:
            val = values[0]
            items['coin'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['coin_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['coin_end'] = int(val)
        
    if type is not None:
        values = type.split(',')
        if len(values) == 1:
            val = values[0]
            items['type'] = val
        else:
            val = values[0]
            if val != '':
                items['type_start'] = val
            
            val = values[1]
            if val != '':
                items['type_end'] = val
        
    if description is not None:
        values = description.split(',')
        if len(values) == 1:
            val = values[0]
            items['description'] = val
        else:
            val = values[0]
            if val != '':
                items['description_start'] = val
            
            val = values[1]
            if val != '':
                items['description_end'] = val
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if out_trade_no is not None:
        values = out_trade_no.split(',')
        if len(values) == 1:
            val = values[0]
            items['out_trade_no'] = val
        else:
            val = values[0]
            if val != '':
                items['out_trade_no_start'] = val
            
            val = values[1]
            if val != '':
                items['out_trade_no_end'] = val
        

    if s_type is not None:
        search_items['type'] = '%' + s_type + '%'
        
    if s_description is not None:
        search_items['description'] = '%' + s_description + '%'
        
    if s_out_trade_no is not None:
        search_items['out_trade_no'] = '%' + s_out_trade_no + '%'
        

    if l_id is not None:
        values = l_id.split(',')
        values = [int(val) for val in values]
        set_items['id'] = values
        
    if l_user_id is not None:
        values = l_user_id.split(',')
        values = [int(val) for val in values]
        set_items['user_id'] = values
        
    if l_change is not None:
        values = l_change.split(',')
        values = [int(val) for val in values]
        set_items['change'] = values
        
    if l_coin is not None:
        values = l_coin.split(',')
        values = [int(val) for val in values]
        set_items['coin'] = values
        
    if l_type is not None:
        values = l_type.split(',')
        values = [val for val in values]
        set_items['type'] = values
        
    if l_description is not None:
        values = l_description.split(',')
        values = [val for val in values]
        set_items['description'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_out_trade_no is not None:
        values = l_out_trade_no.split(',')
        values = [val for val in values]
        set_items['out_trade_no'] = values
            
    
    
    order_items = dict()
    if order_by is not None:
        orders = order_by.split(',')
        for order in orders:
            if order.startswith('-'):
                order_items[order[1:]] = 'desc'
            else:
                order_items[order] = 'asc'
    data = d_db.filter_coin(items, search_items, set_items, order_items, page, page_size)
    c = d_db.filter_count_coin(items, search_items, set_items)
    
    return FilterResCoin(data=data, total=c)


@router.get(f'/coin/fast_filter', response_model=FilterResCoin)
async def fast_filter_coin(
        id: Optional[str] = None, 
        user_id: Optional[str] = None, 
        change: Optional[str] = None, 
        coin: Optional[str] = None, 
        type: Optional[str] = None, 
        description: Optional[str] = None, 
        create_time: Optional[str] = None, 
        out_trade_no: Optional[str] = None, 
        l_id: Optional[str] = None, 
        l_user_id: Optional[str] = None, 
        l_change: Optional[str] = None, 
        l_coin: Optional[str] = None, 
        l_type: Optional[str] = None, 
        l_description: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_out_trade_no: Optional[str] = None, 
        s_type: Optional[str] = None, 
        s_description: Optional[str] = None, 
        s_out_trade_no: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResCoin:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if id is not None:
        values = id.split(',')
        if len(values) == 1:
            val = values[0]
            items['id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['id_end'] = int(val)
        
    if user_id is not None:
        values = user_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['user_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['user_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['user_id_end'] = int(val)
        
    if change is not None:
        values = change.split(',')
        if len(values) == 1:
            val = values[0]
            items['change'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['change_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['change_end'] = int(val)
        
    if coin is not None:
        values = coin.split(',')
        if len(values) == 1:
            val = values[0]
            items['coin'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['coin_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['coin_end'] = int(val)
        
    if type is not None:
        values = type.split(',')
        if len(values) == 1:
            val = values[0]
            items['type'] = val
        else:
            val = values[0]
            if val != '':
                items['type_start'] = val
            
            val = values[1]
            if val != '':
                items['type_end'] = val
        
    if description is not None:
        values = description.split(',')
        if len(values) == 1:
            val = values[0]
            items['description'] = val
        else:
            val = values[0]
            if val != '':
                items['description_start'] = val
            
            val = values[1]
            if val != '':
                items['description_end'] = val
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if out_trade_no is not None:
        values = out_trade_no.split(',')
        if len(values) == 1:
            val = values[0]
            items['out_trade_no'] = val
        else:
            val = values[0]
            if val != '':
                items['out_trade_no_start'] = val
            
            val = values[1]
            if val != '':
                items['out_trade_no_end'] = val
        

    if s_type is not None:
        search_items['type'] = '%' + s_type + '%'
        
    if s_description is not None:
        search_items['description'] = '%' + s_description + '%'
        
    if s_out_trade_no is not None:
        search_items['out_trade_no'] = '%' + s_out_trade_no + '%'
        

    if l_id is not None:
        values = l_id.split(',')
        values = [int(val) for val in values]
        set_items['id'] = values
        
    if l_user_id is not None:
        values = l_user_id.split(',')
        values = [int(val) for val in values]
        set_items['user_id'] = values
        
    if l_change is not None:
        values = l_change.split(',')
        values = [int(val) for val in values]
        set_items['change'] = values
        
    if l_coin is not None:
        values = l_coin.split(',')
        values = [int(val) for val in values]
        set_items['coin'] = values
        
    if l_type is not None:
        values = l_type.split(',')
        values = [val for val in values]
        set_items['type'] = values
        
    if l_description is not None:
        values = l_description.split(',')
        values = [val for val in values]
        set_items['description'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_out_trade_no is not None:
        values = l_out_trade_no.split(',')
        values = [val for val in values]
        set_items['out_trade_no'] = values
            
    
    data = d_db.filter_coin(items, search_items, set_items, page, page_size)
    return FilterResCoin(data=data, total=-1)

    
@router.post(f'/english_point_subject/create', response_model=SEnglishPointSubject)
async def create_english_point_subject(item: CreateEnglishPointSubject) -> SEnglishPointSubject:
    dict_item = dict(item)
    for k,v in dict_item.items():
        if v is not None:
            v = str(v)
            v = v.replace(" ", "")
            get_search = re.search(r"'", v, flags=0)
            get_search2 = re.search(r'%27', v, flags=0)
            get_search3 = re.search(r'unionselect', v, flags=0)
            if get_search or get_search2 or get_search3:
               raise HTTPException(status_code=404, detail='bad way~~~~~~')

    return d_db.insert_english_point_subject(item)
        
    
@router.post(f'/english_point_subject/update', response_model=str)
async def update_english_point_subject(item: SEnglishPointSubject) -> str:
    d_db.update_english_point_subject(item)
    return "success"

    
@router.get(f'/english_point_subject/get', response_model=SEnglishPointSubject)
async def get_english_point_subject(english_point_subject_id: int) -> SEnglishPointSubject:
    return d_db.get_english_point_subject(english_point_subject_id)


@router.get(f'/english_point_subject/filter', response_model=FilterResEnglishPointSubject)
async def filter_english_point_subject(
        eps_id: Optional[str] = None, 
        create_time: Optional[str] = None, 
        eps_content: Optional[str] = None, 
        eps_create_name: Optional[str] = None, 
        class_id: Optional[str] = None, 
        subject_id: Optional[str] = None, 
        knowledge_id: Optional[str] = None, 
        answer_txt: Optional[str] = None, 
        answer_pic_path: Optional[str] = None, 
        answer_audio_path: Optional[str] = None, 
        knowledge_list: Optional[str] = None, 
        l_eps_id: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_eps_content: Optional[str] = None, 
        l_eps_create_name: Optional[str] = None, 
        l_class_id: Optional[str] = None, 
        l_subject_id: Optional[str] = None, 
        l_knowledge_id: Optional[str] = None, 
        l_answer_txt: Optional[str] = None, 
        l_answer_pic_path: Optional[str] = None, 
        l_answer_audio_path: Optional[str] = None, 
        l_knowledge_list: Optional[str] = None, 
        s_eps_content: Optional[str] = None, 
        s_eps_create_name: Optional[str] = None, 
        s_answer_txt: Optional[str] = None, 
        s_answer_pic_path: Optional[str] = None, 
        s_answer_audio_path: Optional[str] = None, 
        s_knowledge_list: Optional[str] = None,
        order_by: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResEnglishPointSubject:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if eps_id is not None:
        values = eps_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['eps_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['eps_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['eps_id_end'] = int(val)
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if eps_content is not None:
        values = eps_content.split(',')
        if len(values) == 1:
            val = values[0]
            items['eps_content'] = val
        else:
            val = values[0]
            if val != '':
                items['eps_content_start'] = val
            
            val = values[1]
            if val != '':
                items['eps_content_end'] = val
        
    if eps_create_name is not None:
        values = eps_create_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['eps_create_name'] = val
        else:
            val = values[0]
            if val != '':
                items['eps_create_name_start'] = val
            
            val = values[1]
            if val != '':
                items['eps_create_name_end'] = val
        
    if class_id is not None:
        values = class_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['class_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['class_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['class_id_end'] = int(val)
        
    if subject_id is not None:
        values = subject_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['subject_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['subject_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['subject_id_end'] = int(val)
        
    if knowledge_id is not None:
        values = knowledge_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['knowledge_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['knowledge_id_end'] = int(val)
        
    if answer_txt is not None:
        values = answer_txt.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_txt'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_txt_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_txt_end'] = val
        
    if answer_pic_path is not None:
        values = answer_pic_path.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_pic_path'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_pic_path_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_pic_path_end'] = val
        
    if answer_audio_path is not None:
        values = answer_audio_path.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_audio_path'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_audio_path_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_audio_path_end'] = val
        
    if knowledge_list is not None:
        values = knowledge_list.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_list'] = val
        else:
            val = values[0]
            if val != '':
                items['knowledge_list_start'] = val
            
            val = values[1]
            if val != '':
                items['knowledge_list_end'] = val
        

    if s_eps_content is not None:
        search_items['eps_content'] = '%' + s_eps_content + '%'
        
    if s_eps_create_name is not None:
        search_items['eps_create_name'] = '%' + s_eps_create_name + '%'
        
    if s_answer_txt is not None:
        search_items['answer_txt'] = '%' + s_answer_txt + '%'
        
    if s_answer_pic_path is not None:
        search_items['answer_pic_path'] = '%' + s_answer_pic_path + '%'
        
    if s_answer_audio_path is not None:
        search_items['answer_audio_path'] = '%' + s_answer_audio_path + '%'
        
    if s_knowledge_list is not None:
        search_items['knowledge_list'] = '%' + s_knowledge_list + '%'
        

    if l_eps_id is not None:
        values = l_eps_id.split(',')
        values = [int(val) for val in values]
        set_items['eps_id'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_eps_content is not None:
        values = l_eps_content.split(',')
        values = [val for val in values]
        set_items['eps_content'] = values
        
    if l_eps_create_name is not None:
        values = l_eps_create_name.split(',')
        values = [val for val in values]
        set_items['eps_create_name'] = values
        
    if l_class_id is not None:
        values = l_class_id.split(',')
        values = [int(val) for val in values]
        set_items['class_id'] = values
        
    if l_subject_id is not None:
        values = l_subject_id.split(',')
        values = [int(val) for val in values]
        set_items['subject_id'] = values
        
    if l_knowledge_id is not None:
        values = l_knowledge_id.split(',')
        values = [int(val) for val in values]
        set_items['knowledge_id'] = values
        
    if l_answer_txt is not None:
        values = l_answer_txt.split(',')
        values = [val for val in values]
        set_items['answer_txt'] = values
        
    if l_answer_pic_path is not None:
        values = l_answer_pic_path.split(',')
        values = [val for val in values]
        set_items['answer_pic_path'] = values
        
    if l_answer_audio_path is not None:
        values = l_answer_audio_path.split(',')
        values = [val for val in values]
        set_items['answer_audio_path'] = values
        
    if l_knowledge_list is not None:
        values = l_knowledge_list.split(',')
        values = [val for val in values]
        set_items['knowledge_list'] = values
            
    
    
    order_items = dict()
    if order_by is not None:
        orders = order_by.split(',')
        for order in orders:
            if order.startswith('-'):
                order_items[order[1:]] = 'desc'
            else:
                order_items[order] = 'asc'
    data = d_db.filter_english_point_subject(items, search_items, set_items, order_items, page, page_size)
    c = d_db.filter_count_english_point_subject(items, search_items, set_items)
    
    return FilterResEnglishPointSubject(data=data, total=c)


@router.get(f'/english_point_subject/fast_filter', response_model=FilterResEnglishPointSubject)
async def fast_filter_english_point_subject(
        eps_id: Optional[str] = None, 
        create_time: Optional[str] = None, 
        eps_content: Optional[str] = None, 
        eps_create_name: Optional[str] = None, 
        class_id: Optional[str] = None, 
        subject_id: Optional[str] = None, 
        knowledge_id: Optional[str] = None, 
        answer_txt: Optional[str] = None, 
        answer_pic_path: Optional[str] = None, 
        answer_audio_path: Optional[str] = None, 
        knowledge_list: Optional[str] = None, 
        l_eps_id: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_eps_content: Optional[str] = None, 
        l_eps_create_name: Optional[str] = None, 
        l_class_id: Optional[str] = None, 
        l_subject_id: Optional[str] = None, 
        l_knowledge_id: Optional[str] = None, 
        l_answer_txt: Optional[str] = None, 
        l_answer_pic_path: Optional[str] = None, 
        l_answer_audio_path: Optional[str] = None, 
        l_knowledge_list: Optional[str] = None, 
        s_eps_content: Optional[str] = None, 
        s_eps_create_name: Optional[str] = None, 
        s_answer_txt: Optional[str] = None, 
        s_answer_pic_path: Optional[str] = None, 
        s_answer_audio_path: Optional[str] = None, 
        s_knowledge_list: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResEnglishPointSubject:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if eps_id is not None:
        values = eps_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['eps_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['eps_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['eps_id_end'] = int(val)
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if eps_content is not None:
        values = eps_content.split(',')
        if len(values) == 1:
            val = values[0]
            items['eps_content'] = val
        else:
            val = values[0]
            if val != '':
                items['eps_content_start'] = val
            
            val = values[1]
            if val != '':
                items['eps_content_end'] = val
        
    if eps_create_name is not None:
        values = eps_create_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['eps_create_name'] = val
        else:
            val = values[0]
            if val != '':
                items['eps_create_name_start'] = val
            
            val = values[1]
            if val != '':
                items['eps_create_name_end'] = val
        
    if class_id is not None:
        values = class_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['class_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['class_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['class_id_end'] = int(val)
        
    if subject_id is not None:
        values = subject_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['subject_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['subject_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['subject_id_end'] = int(val)
        
    if knowledge_id is not None:
        values = knowledge_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['knowledge_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['knowledge_id_end'] = int(val)
        
    if answer_txt is not None:
        values = answer_txt.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_txt'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_txt_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_txt_end'] = val
        
    if answer_pic_path is not None:
        values = answer_pic_path.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_pic_path'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_pic_path_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_pic_path_end'] = val
        
    if answer_audio_path is not None:
        values = answer_audio_path.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_audio_path'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_audio_path_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_audio_path_end'] = val
        
    if knowledge_list is not None:
        values = knowledge_list.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_list'] = val
        else:
            val = values[0]
            if val != '':
                items['knowledge_list_start'] = val
            
            val = values[1]
            if val != '':
                items['knowledge_list_end'] = val
        

    if s_eps_content is not None:
        search_items['eps_content'] = '%' + s_eps_content + '%'
        
    if s_eps_create_name is not None:
        search_items['eps_create_name'] = '%' + s_eps_create_name + '%'
        
    if s_answer_txt is not None:
        search_items['answer_txt'] = '%' + s_answer_txt + '%'
        
    if s_answer_pic_path is not None:
        search_items['answer_pic_path'] = '%' + s_answer_pic_path + '%'
        
    if s_answer_audio_path is not None:
        search_items['answer_audio_path'] = '%' + s_answer_audio_path + '%'
        
    if s_knowledge_list is not None:
        search_items['knowledge_list'] = '%' + s_knowledge_list + '%'
        

    if l_eps_id is not None:
        values = l_eps_id.split(',')
        values = [int(val) for val in values]
        set_items['eps_id'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_eps_content is not None:
        values = l_eps_content.split(',')
        values = [val for val in values]
        set_items['eps_content'] = values
        
    if l_eps_create_name is not None:
        values = l_eps_create_name.split(',')
        values = [val for val in values]
        set_items['eps_create_name'] = values
        
    if l_class_id is not None:
        values = l_class_id.split(',')
        values = [int(val) for val in values]
        set_items['class_id'] = values
        
    if l_subject_id is not None:
        values = l_subject_id.split(',')
        values = [int(val) for val in values]
        set_items['subject_id'] = values
        
    if l_knowledge_id is not None:
        values = l_knowledge_id.split(',')
        values = [int(val) for val in values]
        set_items['knowledge_id'] = values
        
    if l_answer_txt is not None:
        values = l_answer_txt.split(',')
        values = [val for val in values]
        set_items['answer_txt'] = values
        
    if l_answer_pic_path is not None:
        values = l_answer_pic_path.split(',')
        values = [val for val in values]
        set_items['answer_pic_path'] = values
        
    if l_answer_audio_path is not None:
        values = l_answer_audio_path.split(',')
        values = [val for val in values]
        set_items['answer_audio_path'] = values
        
    if l_knowledge_list is not None:
        values = l_knowledge_list.split(',')
        values = [val for val in values]
        set_items['knowledge_list'] = values
            
    
    data = d_db.filter_english_point_subject(items, search_items, set_items, page, page_size)
    return FilterResEnglishPointSubject(data=data, total=-1)

    
@router.post(f'/knowledge_point/create', response_model=SKnowledgePoint)
async def create_knowledge_point(item: CreateKnowledgePoint) -> SKnowledgePoint:
    dict_item = dict(item)
    for k,v in dict_item.items():
        if v is not None:
            v = str(v)
            v = v.replace(" ", "")
            get_search = re.search(r"'", v, flags=0)
            get_search2 = re.search(r'%27', v, flags=0)
            get_search3 = re.search(r'unionselect', v, flags=0)
            if get_search or get_search2 or get_search3:
               raise HTTPException(status_code=404, detail='bad way~~~~~~')

    return d_db.insert_knowledge_point(item)
        
    
@router.post(f'/knowledge_point/update', response_model=str)
async def update_knowledge_point(item: SKnowledgePoint) -> str:
    d_db.update_knowledge_point(item)
    return "success"

    
@router.get(f'/knowledge_point/get', response_model=SKnowledgePoint)
async def get_knowledge_point(knowledge_point_id: int) -> SKnowledgePoint:
    return d_db.get_knowledge_point(knowledge_point_id)


@router.get(f'/knowledge_point/filter', response_model=FilterResKnowledgePoint)
async def filter_knowledge_point(
        kn_id: Optional[str] = None, 
        create_time: Optional[str] = None, 
        kn_name: Optional[str] = None, 
        kn_create_name: Optional[str] = None, 
        class_id: Optional[str] = None, 
        subject_id: Optional[str] = None, 
        l_kn_id: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_kn_name: Optional[str] = None, 
        l_kn_create_name: Optional[str] = None, 
        l_class_id: Optional[str] = None, 
        l_subject_id: Optional[str] = None, 
        s_kn_name: Optional[str] = None, 
        s_kn_create_name: Optional[str] = None,
        order_by: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResKnowledgePoint:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if kn_id is not None:
        values = kn_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['kn_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['kn_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['kn_id_end'] = int(val)
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if kn_name is not None:
        values = kn_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['kn_name'] = val
        else:
            val = values[0]
            if val != '':
                items['kn_name_start'] = val
            
            val = values[1]
            if val != '':
                items['kn_name_end'] = val
        
    if kn_create_name is not None:
        values = kn_create_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['kn_create_name'] = val
        else:
            val = values[0]
            if val != '':
                items['kn_create_name_start'] = val
            
            val = values[1]
            if val != '':
                items['kn_create_name_end'] = val
        
    if class_id is not None:
        values = class_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['class_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['class_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['class_id_end'] = int(val)
        
    if subject_id is not None:
        values = subject_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['subject_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['subject_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['subject_id_end'] = int(val)
        

    if s_kn_name is not None:
        search_items['kn_name'] = '%' + s_kn_name + '%'
        
    if s_kn_create_name is not None:
        search_items['kn_create_name'] = '%' + s_kn_create_name + '%'
        

    if l_kn_id is not None:
        values = l_kn_id.split(',')
        values = [int(val) for val in values]
        set_items['kn_id'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_kn_name is not None:
        values = l_kn_name.split(',')
        values = [val for val in values]
        set_items['kn_name'] = values
        
    if l_kn_create_name is not None:
        values = l_kn_create_name.split(',')
        values = [val for val in values]
        set_items['kn_create_name'] = values
        
    if l_class_id is not None:
        values = l_class_id.split(',')
        values = [int(val) for val in values]
        set_items['class_id'] = values
        
    if l_subject_id is not None:
        values = l_subject_id.split(',')
        values = [int(val) for val in values]
        set_items['subject_id'] = values
            
    
    
    order_items = dict()
    if order_by is not None:
        orders = order_by.split(',')
        for order in orders:
            if order.startswith('-'):
                order_items[order[1:]] = 'desc'
            else:
                order_items[order] = 'asc'
    data = d_db.filter_knowledge_point(items, search_items, set_items, order_items, page, page_size)
    c = d_db.filter_count_knowledge_point(items, search_items, set_items)
    
    return FilterResKnowledgePoint(data=data, total=c)


@router.get(f'/knowledge_point/fast_filter', response_model=FilterResKnowledgePoint)
async def fast_filter_knowledge_point(
        kn_id: Optional[str] = None, 
        create_time: Optional[str] = None, 
        kn_name: Optional[str] = None, 
        kn_create_name: Optional[str] = None, 
        class_id: Optional[str] = None, 
        subject_id: Optional[str] = None, 
        l_kn_id: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_kn_name: Optional[str] = None, 
        l_kn_create_name: Optional[str] = None, 
        l_class_id: Optional[str] = None, 
        l_subject_id: Optional[str] = None, 
        s_kn_name: Optional[str] = None, 
        s_kn_create_name: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResKnowledgePoint:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if kn_id is not None:
        values = kn_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['kn_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['kn_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['kn_id_end'] = int(val)
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if kn_name is not None:
        values = kn_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['kn_name'] = val
        else:
            val = values[0]
            if val != '':
                items['kn_name_start'] = val
            
            val = values[1]
            if val != '':
                items['kn_name_end'] = val
        
    if kn_create_name is not None:
        values = kn_create_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['kn_create_name'] = val
        else:
            val = values[0]
            if val != '':
                items['kn_create_name_start'] = val
            
            val = values[1]
            if val != '':
                items['kn_create_name_end'] = val
        
    if class_id is not None:
        values = class_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['class_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['class_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['class_id_end'] = int(val)
        
    if subject_id is not None:
        values = subject_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['subject_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['subject_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['subject_id_end'] = int(val)
        

    if s_kn_name is not None:
        search_items['kn_name'] = '%' + s_kn_name + '%'
        
    if s_kn_create_name is not None:
        search_items['kn_create_name'] = '%' + s_kn_create_name + '%'
        

    if l_kn_id is not None:
        values = l_kn_id.split(',')
        values = [int(val) for val in values]
        set_items['kn_id'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_kn_name is not None:
        values = l_kn_name.split(',')
        values = [val for val in values]
        set_items['kn_name'] = values
        
    if l_kn_create_name is not None:
        values = l_kn_create_name.split(',')
        values = [val for val in values]
        set_items['kn_create_name'] = values
        
    if l_class_id is not None:
        values = l_class_id.split(',')
        values = [int(val) for val in values]
        set_items['class_id'] = values
        
    if l_subject_id is not None:
        values = l_subject_id.split(',')
        values = [int(val) for val in values]
        set_items['subject_id'] = values
            
    
    data = d_db.filter_knowledge_point(items, search_items, set_items, page, page_size)
    return FilterResKnowledgePoint(data=data, total=-1)

    
@router.post(f'/math_point_subject/create', response_model=SMathPointSubject)
async def create_math_point_subject(item: CreateMathPointSubject) -> SMathPointSubject:
    dict_item = dict(item)
    for k,v in dict_item.items():
        if v is not None:
            v = str(v)
            v = v.replace(" ", "")
            get_search = re.search(r"'", v, flags=0)
            get_search2 = re.search(r'%27', v, flags=0)
            get_search3 = re.search(r'unionselect', v, flags=0)
            if get_search or get_search2 or get_search3:
               raise HTTPException(status_code=404, detail='bad way~~~~~~')

    return d_db.insert_math_point_subject(item)
        
    
@router.post(f'/math_point_subject/update', response_model=str)
async def update_math_point_subject(item: SMathPointSubject) -> str:
    d_db.update_math_point_subject(item)
    return "success"

    
@router.get(f'/math_point_subject/get', response_model=SMathPointSubject)
async def get_math_point_subject(math_point_subject_id: int) -> SMathPointSubject:
    return d_db.get_math_point_subject(math_point_subject_id)


@router.get(f'/math_point_subject/filter', response_model=FilterResMathPointSubject)
async def filter_math_point_subject(
        mps_id: Optional[str] = None, 
        create_time: Optional[str] = None, 
        mps_content: Optional[str] = None, 
        mps_create_name: Optional[str] = None, 
        class_id: Optional[str] = None, 
        subject_id: Optional[str] = None, 
        knowledge_id: Optional[str] = None, 
        answer_txt: Optional[str] = None, 
        answer_pic_path: Optional[str] = None, 
        answer_audio_path: Optional[str] = None, 
        knowledge_list: Optional[str] = None, 
        l_mps_id: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_mps_content: Optional[str] = None, 
        l_mps_create_name: Optional[str] = None, 
        l_class_id: Optional[str] = None, 
        l_subject_id: Optional[str] = None, 
        l_knowledge_id: Optional[str] = None, 
        l_answer_txt: Optional[str] = None, 
        l_answer_pic_path: Optional[str] = None, 
        l_answer_audio_path: Optional[str] = None, 
        l_knowledge_list: Optional[str] = None, 
        s_mps_content: Optional[str] = None, 
        s_mps_create_name: Optional[str] = None, 
        s_answer_txt: Optional[str] = None, 
        s_answer_pic_path: Optional[str] = None, 
        s_answer_audio_path: Optional[str] = None, 
        s_knowledge_list: Optional[str] = None,
        order_by: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResMathPointSubject:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if mps_id is not None:
        values = mps_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['mps_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['mps_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['mps_id_end'] = int(val)
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if mps_content is not None:
        values = mps_content.split(',')
        if len(values) == 1:
            val = values[0]
            items['mps_content'] = val
        else:
            val = values[0]
            if val != '':
                items['mps_content_start'] = val
            
            val = values[1]
            if val != '':
                items['mps_content_end'] = val
        
    if mps_create_name is not None:
        values = mps_create_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['mps_create_name'] = val
        else:
            val = values[0]
            if val != '':
                items['mps_create_name_start'] = val
            
            val = values[1]
            if val != '':
                items['mps_create_name_end'] = val
        
    if class_id is not None:
        values = class_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['class_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['class_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['class_id_end'] = int(val)
        
    if subject_id is not None:
        values = subject_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['subject_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['subject_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['subject_id_end'] = int(val)
        
    if knowledge_id is not None:
        values = knowledge_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['knowledge_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['knowledge_id_end'] = int(val)
        
    if answer_txt is not None:
        values = answer_txt.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_txt'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_txt_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_txt_end'] = val
        
    if answer_pic_path is not None:
        values = answer_pic_path.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_pic_path'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_pic_path_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_pic_path_end'] = val
        
    if answer_audio_path is not None:
        values = answer_audio_path.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_audio_path'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_audio_path_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_audio_path_end'] = val
        
    if knowledge_list is not None:
        values = knowledge_list.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_list'] = val
        else:
            val = values[0]
            if val != '':
                items['knowledge_list_start'] = val
            
            val = values[1]
            if val != '':
                items['knowledge_list_end'] = val
        

    if s_mps_content is not None:
        search_items['mps_content'] = '%' + s_mps_content + '%'
        
    if s_mps_create_name is not None:
        search_items['mps_create_name'] = '%' + s_mps_create_name + '%'
        
    if s_answer_txt is not None:
        search_items['answer_txt'] = '%' + s_answer_txt + '%'
        
    if s_answer_pic_path is not None:
        search_items['answer_pic_path'] = '%' + s_answer_pic_path + '%'
        
    if s_answer_audio_path is not None:
        search_items['answer_audio_path'] = '%' + s_answer_audio_path + '%'
        
    if s_knowledge_list is not None:
        search_items['knowledge_list'] = '%' + s_knowledge_list + '%'
        

    if l_mps_id is not None:
        values = l_mps_id.split(',')
        values = [int(val) for val in values]
        set_items['mps_id'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_mps_content is not None:
        values = l_mps_content.split(',')
        values = [val for val in values]
        set_items['mps_content'] = values
        
    if l_mps_create_name is not None:
        values = l_mps_create_name.split(',')
        values = [val for val in values]
        set_items['mps_create_name'] = values
        
    if l_class_id is not None:
        values = l_class_id.split(',')
        values = [int(val) for val in values]
        set_items['class_id'] = values
        
    if l_subject_id is not None:
        values = l_subject_id.split(',')
        values = [int(val) for val in values]
        set_items['subject_id'] = values
        
    if l_knowledge_id is not None:
        values = l_knowledge_id.split(',')
        values = [int(val) for val in values]
        set_items['knowledge_id'] = values
        
    if l_answer_txt is not None:
        values = l_answer_txt.split(',')
        values = [val for val in values]
        set_items['answer_txt'] = values
        
    if l_answer_pic_path is not None:
        values = l_answer_pic_path.split(',')
        values = [val for val in values]
        set_items['answer_pic_path'] = values
        
    if l_answer_audio_path is not None:
        values = l_answer_audio_path.split(',')
        values = [val for val in values]
        set_items['answer_audio_path'] = values
        
    if l_knowledge_list is not None:
        values = l_knowledge_list.split(',')
        values = [val for val in values]
        set_items['knowledge_list'] = values
            
    
    
    order_items = dict()
    if order_by is not None:
        orders = order_by.split(',')
        for order in orders:
            if order.startswith('-'):
                order_items[order[1:]] = 'desc'
            else:
                order_items[order] = 'asc'
    data = d_db.filter_math_point_subject(items, search_items, set_items, order_items, page, page_size)
    c = d_db.filter_count_math_point_subject(items, search_items, set_items)
    
    return FilterResMathPointSubject(data=data, total=c)


@router.get(f'/math_point_subject/fast_filter', response_model=FilterResMathPointSubject)
async def fast_filter_math_point_subject(
        mps_id: Optional[str] = None, 
        create_time: Optional[str] = None, 
        mps_content: Optional[str] = None, 
        mps_create_name: Optional[str] = None, 
        class_id: Optional[str] = None, 
        subject_id: Optional[str] = None, 
        knowledge_id: Optional[str] = None, 
        answer_txt: Optional[str] = None, 
        answer_pic_path: Optional[str] = None, 
        answer_audio_path: Optional[str] = None, 
        knowledge_list: Optional[str] = None, 
        l_mps_id: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_mps_content: Optional[str] = None, 
        l_mps_create_name: Optional[str] = None, 
        l_class_id: Optional[str] = None, 
        l_subject_id: Optional[str] = None, 
        l_knowledge_id: Optional[str] = None, 
        l_answer_txt: Optional[str] = None, 
        l_answer_pic_path: Optional[str] = None, 
        l_answer_audio_path: Optional[str] = None, 
        l_knowledge_list: Optional[str] = None, 
        s_mps_content: Optional[str] = None, 
        s_mps_create_name: Optional[str] = None, 
        s_answer_txt: Optional[str] = None, 
        s_answer_pic_path: Optional[str] = None, 
        s_answer_audio_path: Optional[str] = None, 
        s_knowledge_list: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResMathPointSubject:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if mps_id is not None:
        values = mps_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['mps_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['mps_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['mps_id_end'] = int(val)
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if mps_content is not None:
        values = mps_content.split(',')
        if len(values) == 1:
            val = values[0]
            items['mps_content'] = val
        else:
            val = values[0]
            if val != '':
                items['mps_content_start'] = val
            
            val = values[1]
            if val != '':
                items['mps_content_end'] = val
        
    if mps_create_name is not None:
        values = mps_create_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['mps_create_name'] = val
        else:
            val = values[0]
            if val != '':
                items['mps_create_name_start'] = val
            
            val = values[1]
            if val != '':
                items['mps_create_name_end'] = val
        
    if class_id is not None:
        values = class_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['class_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['class_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['class_id_end'] = int(val)
        
    if subject_id is not None:
        values = subject_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['subject_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['subject_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['subject_id_end'] = int(val)
        
    if knowledge_id is not None:
        values = knowledge_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['knowledge_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['knowledge_id_end'] = int(val)
        
    if answer_txt is not None:
        values = answer_txt.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_txt'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_txt_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_txt_end'] = val
        
    if answer_pic_path is not None:
        values = answer_pic_path.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_pic_path'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_pic_path_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_pic_path_end'] = val
        
    if answer_audio_path is not None:
        values = answer_audio_path.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_audio_path'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_audio_path_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_audio_path_end'] = val
        
    if knowledge_list is not None:
        values = knowledge_list.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_list'] = val
        else:
            val = values[0]
            if val != '':
                items['knowledge_list_start'] = val
            
            val = values[1]
            if val != '':
                items['knowledge_list_end'] = val
        

    if s_mps_content is not None:
        search_items['mps_content'] = '%' + s_mps_content + '%'
        
    if s_mps_create_name is not None:
        search_items['mps_create_name'] = '%' + s_mps_create_name + '%'
        
    if s_answer_txt is not None:
        search_items['answer_txt'] = '%' + s_answer_txt + '%'
        
    if s_answer_pic_path is not None:
        search_items['answer_pic_path'] = '%' + s_answer_pic_path + '%'
        
    if s_answer_audio_path is not None:
        search_items['answer_audio_path'] = '%' + s_answer_audio_path + '%'
        
    if s_knowledge_list is not None:
        search_items['knowledge_list'] = '%' + s_knowledge_list + '%'
        

    if l_mps_id is not None:
        values = l_mps_id.split(',')
        values = [int(val) for val in values]
        set_items['mps_id'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_mps_content is not None:
        values = l_mps_content.split(',')
        values = [val for val in values]
        set_items['mps_content'] = values
        
    if l_mps_create_name is not None:
        values = l_mps_create_name.split(',')
        values = [val for val in values]
        set_items['mps_create_name'] = values
        
    if l_class_id is not None:
        values = l_class_id.split(',')
        values = [int(val) for val in values]
        set_items['class_id'] = values
        
    if l_subject_id is not None:
        values = l_subject_id.split(',')
        values = [int(val) for val in values]
        set_items['subject_id'] = values
        
    if l_knowledge_id is not None:
        values = l_knowledge_id.split(',')
        values = [int(val) for val in values]
        set_items['knowledge_id'] = values
        
    if l_answer_txt is not None:
        values = l_answer_txt.split(',')
        values = [val for val in values]
        set_items['answer_txt'] = values
        
    if l_answer_pic_path is not None:
        values = l_answer_pic_path.split(',')
        values = [val for val in values]
        set_items['answer_pic_path'] = values
        
    if l_answer_audio_path is not None:
        values = l_answer_audio_path.split(',')
        values = [val for val in values]
        set_items['answer_audio_path'] = values
        
    if l_knowledge_list is not None:
        values = l_knowledge_list.split(',')
        values = [val for val in values]
        set_items['knowledge_list'] = values
            
    
    data = d_db.filter_math_point_subject(items, search_items, set_items, page, page_size)
    return FilterResMathPointSubject(data=data, total=-1)

    
@router.post(f'/question_type/create', response_model=SQuestionType)
async def create_question_type(item: CreateQuestionType) -> SQuestionType:
    dict_item = dict(item)
    for k,v in dict_item.items():
        if v is not None:
            v = str(v)
            v = v.replace(" ", "")
            get_search = re.search(r"'", v, flags=0)
            get_search2 = re.search(r'%27', v, flags=0)
            get_search3 = re.search(r'unionselect', v, flags=0)
            if get_search or get_search2 or get_search3:
               raise HTTPException(status_code=404, detail='bad way~~~~~~')

    return d_db.insert_question_type(item)
        
    
@router.post(f'/question_type/update', response_model=str)
async def update_question_type(item: SQuestionType) -> str:
    d_db.update_question_type(item)
    return "success"

    
@router.get(f'/question_type/get', response_model=SQuestionType)
async def get_question_type(question_type_id: int) -> SQuestionType:
    return d_db.get_question_type(question_type_id)


@router.get(f'/question_type/filter', response_model=FilterResQuestionType)
async def filter_question_type(
        qu_id: Optional[str] = None, 
        create_time: Optional[str] = None, 
        qu_name: Optional[str] = None, 
        qu_create_name: Optional[str] = None, 
        class_id: Optional[str] = None, 
        subject_id: Optional[str] = None, 
        knowledge_id: Optional[str] = None, 
        knowledge_list: Optional[str] = None, 
        l_qu_id: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_qu_name: Optional[str] = None, 
        l_qu_create_name: Optional[str] = None, 
        l_class_id: Optional[str] = None, 
        l_subject_id: Optional[str] = None, 
        l_knowledge_id: Optional[str] = None, 
        l_knowledge_list: Optional[str] = None, 
        s_qu_name: Optional[str] = None, 
        s_qu_create_name: Optional[str] = None, 
        s_knowledge_list: Optional[str] = None,
        order_by: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResQuestionType:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if qu_id is not None:
        values = qu_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['qu_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['qu_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['qu_id_end'] = int(val)
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if qu_name is not None:
        values = qu_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['qu_name'] = val
        else:
            val = values[0]
            if val != '':
                items['qu_name_start'] = val
            
            val = values[1]
            if val != '':
                items['qu_name_end'] = val
        
    if qu_create_name is not None:
        values = qu_create_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['qu_create_name'] = val
        else:
            val = values[0]
            if val != '':
                items['qu_create_name_start'] = val
            
            val = values[1]
            if val != '':
                items['qu_create_name_end'] = val
        
    if class_id is not None:
        values = class_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['class_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['class_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['class_id_end'] = int(val)
        
    if subject_id is not None:
        values = subject_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['subject_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['subject_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['subject_id_end'] = int(val)
        
    if knowledge_id is not None:
        values = knowledge_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['knowledge_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['knowledge_id_end'] = int(val)
        
    if knowledge_list is not None:
        values = knowledge_list.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_list'] = val
        else:
            val = values[0]
            if val != '':
                items['knowledge_list_start'] = val
            
            val = values[1]
            if val != '':
                items['knowledge_list_end'] = val
        

    if s_qu_name is not None:
        search_items['qu_name'] = '%' + s_qu_name + '%'
        
    if s_qu_create_name is not None:
        search_items['qu_create_name'] = '%' + s_qu_create_name + '%'
        
    if s_knowledge_list is not None:
        search_items['knowledge_list'] = '%' + s_knowledge_list + '%'
        

    if l_qu_id is not None:
        values = l_qu_id.split(',')
        values = [int(val) for val in values]
        set_items['qu_id'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_qu_name is not None:
        values = l_qu_name.split(',')
        values = [val for val in values]
        set_items['qu_name'] = values
        
    if l_qu_create_name is not None:
        values = l_qu_create_name.split(',')
        values = [val for val in values]
        set_items['qu_create_name'] = values
        
    if l_class_id is not None:
        values = l_class_id.split(',')
        values = [int(val) for val in values]
        set_items['class_id'] = values
        
    if l_subject_id is not None:
        values = l_subject_id.split(',')
        values = [int(val) for val in values]
        set_items['subject_id'] = values
        
    if l_knowledge_id is not None:
        values = l_knowledge_id.split(',')
        values = [int(val) for val in values]
        set_items['knowledge_id'] = values
        
    if l_knowledge_list is not None:
        values = l_knowledge_list.split(',')
        values = [val for val in values]
        set_items['knowledge_list'] = values
            
    
    
    order_items = dict()
    if order_by is not None:
        orders = order_by.split(',')
        for order in orders:
            if order.startswith('-'):
                order_items[order[1:]] = 'desc'
            else:
                order_items[order] = 'asc'
    data = d_db.filter_question_type(items, search_items, set_items, order_items, page, page_size)
    c = d_db.filter_count_question_type(items, search_items, set_items)
    
    return FilterResQuestionType(data=data, total=c)


@router.get(f'/question_type/fast_filter', response_model=FilterResQuestionType)
async def fast_filter_question_type(
        qu_id: Optional[str] = None, 
        create_time: Optional[str] = None, 
        qu_name: Optional[str] = None, 
        qu_create_name: Optional[str] = None, 
        class_id: Optional[str] = None, 
        subject_id: Optional[str] = None, 
        knowledge_id: Optional[str] = None, 
        knowledge_list: Optional[str] = None, 
        l_qu_id: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_qu_name: Optional[str] = None, 
        l_qu_create_name: Optional[str] = None, 
        l_class_id: Optional[str] = None, 
        l_subject_id: Optional[str] = None, 
        l_knowledge_id: Optional[str] = None, 
        l_knowledge_list: Optional[str] = None, 
        s_qu_name: Optional[str] = None, 
        s_qu_create_name: Optional[str] = None, 
        s_knowledge_list: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResQuestionType:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if qu_id is not None:
        values = qu_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['qu_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['qu_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['qu_id_end'] = int(val)
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if qu_name is not None:
        values = qu_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['qu_name'] = val
        else:
            val = values[0]
            if val != '':
                items['qu_name_start'] = val
            
            val = values[1]
            if val != '':
                items['qu_name_end'] = val
        
    if qu_create_name is not None:
        values = qu_create_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['qu_create_name'] = val
        else:
            val = values[0]
            if val != '':
                items['qu_create_name_start'] = val
            
            val = values[1]
            if val != '':
                items['qu_create_name_end'] = val
        
    if class_id is not None:
        values = class_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['class_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['class_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['class_id_end'] = int(val)
        
    if subject_id is not None:
        values = subject_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['subject_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['subject_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['subject_id_end'] = int(val)
        
    if knowledge_id is not None:
        values = knowledge_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['knowledge_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['knowledge_id_end'] = int(val)
        
    if knowledge_list is not None:
        values = knowledge_list.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_list'] = val
        else:
            val = values[0]
            if val != '':
                items['knowledge_list_start'] = val
            
            val = values[1]
            if val != '':
                items['knowledge_list_end'] = val
        

    if s_qu_name is not None:
        search_items['qu_name'] = '%' + s_qu_name + '%'
        
    if s_qu_create_name is not None:
        search_items['qu_create_name'] = '%' + s_qu_create_name + '%'
        
    if s_knowledge_list is not None:
        search_items['knowledge_list'] = '%' + s_knowledge_list + '%'
        

    if l_qu_id is not None:
        values = l_qu_id.split(',')
        values = [int(val) for val in values]
        set_items['qu_id'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_qu_name is not None:
        values = l_qu_name.split(',')
        values = [val for val in values]
        set_items['qu_name'] = values
        
    if l_qu_create_name is not None:
        values = l_qu_create_name.split(',')
        values = [val for val in values]
        set_items['qu_create_name'] = values
        
    if l_class_id is not None:
        values = l_class_id.split(',')
        values = [int(val) for val in values]
        set_items['class_id'] = values
        
    if l_subject_id is not None:
        values = l_subject_id.split(',')
        values = [int(val) for val in values]
        set_items['subject_id'] = values
        
    if l_knowledge_id is not None:
        values = l_knowledge_id.split(',')
        values = [int(val) for val in values]
        set_items['knowledge_id'] = values
        
    if l_knowledge_list is not None:
        values = l_knowledge_list.split(',')
        values = [val for val in values]
        set_items['knowledge_list'] = values
            
    
    data = d_db.filter_question_type(items, search_items, set_items, page, page_size)
    return FilterResQuestionType(data=data, total=-1)

    
@router.post(f'/remain_point_subject/create', response_model=SRemainPointSubject)
async def create_remain_point_subject(item: CreateRemainPointSubject) -> SRemainPointSubject:
    dict_item = dict(item)
    for k,v in dict_item.items():
        if v is not None:
            v = str(v)
            v = v.replace(" ", "")
            get_search = re.search(r"'", v, flags=0)
            get_search2 = re.search(r'%27', v, flags=0)
            get_search3 = re.search(r'unionselect', v, flags=0)
            if get_search or get_search2 or get_search3:
               raise HTTPException(status_code=404, detail='bad way~~~~~~')

    return d_db.insert_remain_point_subject(item)
        
    
@router.post(f'/remain_point_subject/update', response_model=str)
async def update_remain_point_subject(item: SRemainPointSubject) -> str:
    d_db.update_remain_point_subject(item)
    return "success"

    
@router.get(f'/remain_point_subject/get', response_model=SRemainPointSubject)
async def get_remain_point_subject(remain_point_subject_id: int) -> SRemainPointSubject:
    return d_db.get_remain_point_subject(remain_point_subject_id)


@router.get(f'/remain_point_subject/filter', response_model=FilterResRemainPointSubject)
async def filter_remain_point_subject(
        rps_id: Optional[str] = None, 
        create_time: Optional[str] = None, 
        rps_content: Optional[str] = None, 
        rps_create_name: Optional[str] = None, 
        class_id: Optional[str] = None, 
        subject_id: Optional[str] = None, 
        knowledge_id: Optional[str] = None, 
        answer_txt: Optional[str] = None, 
        answer_pic_path: Optional[str] = None, 
        answer_audio_path: Optional[str] = None, 
        knowledge_list: Optional[str] = None, 
        l_rps_id: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_rps_content: Optional[str] = None, 
        l_rps_create_name: Optional[str] = None, 
        l_class_id: Optional[str] = None, 
        l_subject_id: Optional[str] = None, 
        l_knowledge_id: Optional[str] = None, 
        l_answer_txt: Optional[str] = None, 
        l_answer_pic_path: Optional[str] = None, 
        l_answer_audio_path: Optional[str] = None, 
        l_knowledge_list: Optional[str] = None, 
        s_rps_content: Optional[str] = None, 
        s_rps_create_name: Optional[str] = None, 
        s_answer_txt: Optional[str] = None, 
        s_answer_pic_path: Optional[str] = None, 
        s_answer_audio_path: Optional[str] = None, 
        s_knowledge_list: Optional[str] = None,
        order_by: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResRemainPointSubject:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if rps_id is not None:
        values = rps_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['rps_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['rps_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['rps_id_end'] = int(val)
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if rps_content is not None:
        values = rps_content.split(',')
        if len(values) == 1:
            val = values[0]
            items['rps_content'] = val
        else:
            val = values[0]
            if val != '':
                items['rps_content_start'] = val
            
            val = values[1]
            if val != '':
                items['rps_content_end'] = val
        
    if rps_create_name is not None:
        values = rps_create_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['rps_create_name'] = val
        else:
            val = values[0]
            if val != '':
                items['rps_create_name_start'] = val
            
            val = values[1]
            if val != '':
                items['rps_create_name_end'] = val
        
    if class_id is not None:
        values = class_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['class_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['class_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['class_id_end'] = int(val)
        
    if subject_id is not None:
        values = subject_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['subject_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['subject_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['subject_id_end'] = int(val)
        
    if knowledge_id is not None:
        values = knowledge_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['knowledge_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['knowledge_id_end'] = int(val)
        
    if answer_txt is not None:
        values = answer_txt.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_txt'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_txt_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_txt_end'] = val
        
    if answer_pic_path is not None:
        values = answer_pic_path.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_pic_path'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_pic_path_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_pic_path_end'] = val
        
    if answer_audio_path is not None:
        values = answer_audio_path.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_audio_path'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_audio_path_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_audio_path_end'] = val
        
    if knowledge_list is not None:
        values = knowledge_list.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_list'] = val
        else:
            val = values[0]
            if val != '':
                items['knowledge_list_start'] = val
            
            val = values[1]
            if val != '':
                items['knowledge_list_end'] = val
        

    if s_rps_content is not None:
        search_items['rps_content'] = '%' + s_rps_content + '%'
        
    if s_rps_create_name is not None:
        search_items['rps_create_name'] = '%' + s_rps_create_name + '%'
        
    if s_answer_txt is not None:
        search_items['answer_txt'] = '%' + s_answer_txt + '%'
        
    if s_answer_pic_path is not None:
        search_items['answer_pic_path'] = '%' + s_answer_pic_path + '%'
        
    if s_answer_audio_path is not None:
        search_items['answer_audio_path'] = '%' + s_answer_audio_path + '%'
        
    if s_knowledge_list is not None:
        search_items['knowledge_list'] = '%' + s_knowledge_list + '%'
        

    if l_rps_id is not None:
        values = l_rps_id.split(',')
        values = [int(val) for val in values]
        set_items['rps_id'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_rps_content is not None:
        values = l_rps_content.split(',')
        values = [val for val in values]
        set_items['rps_content'] = values
        
    if l_rps_create_name is not None:
        values = l_rps_create_name.split(',')
        values = [val for val in values]
        set_items['rps_create_name'] = values
        
    if l_class_id is not None:
        values = l_class_id.split(',')
        values = [int(val) for val in values]
        set_items['class_id'] = values
        
    if l_subject_id is not None:
        values = l_subject_id.split(',')
        values = [int(val) for val in values]
        set_items['subject_id'] = values
        
    if l_knowledge_id is not None:
        values = l_knowledge_id.split(',')
        values = [int(val) for val in values]
        set_items['knowledge_id'] = values
        
    if l_answer_txt is not None:
        values = l_answer_txt.split(',')
        values = [val for val in values]
        set_items['answer_txt'] = values
        
    if l_answer_pic_path is not None:
        values = l_answer_pic_path.split(',')
        values = [val for val in values]
        set_items['answer_pic_path'] = values
        
    if l_answer_audio_path is not None:
        values = l_answer_audio_path.split(',')
        values = [val for val in values]
        set_items['answer_audio_path'] = values
        
    if l_knowledge_list is not None:
        values = l_knowledge_list.split(',')
        values = [val for val in values]
        set_items['knowledge_list'] = values
            
    
    
    order_items = dict()
    if order_by is not None:
        orders = order_by.split(',')
        for order in orders:
            if order.startswith('-'):
                order_items[order[1:]] = 'desc'
            else:
                order_items[order] = 'asc'
    data = d_db.filter_remain_point_subject(items, search_items, set_items, order_items, page, page_size)
    c = d_db.filter_count_remain_point_subject(items, search_items, set_items)
    
    return FilterResRemainPointSubject(data=data, total=c)


@router.get(f'/remain_point_subject/fast_filter', response_model=FilterResRemainPointSubject)
async def fast_filter_remain_point_subject(
        rps_id: Optional[str] = None, 
        create_time: Optional[str] = None, 
        rps_content: Optional[str] = None, 
        rps_create_name: Optional[str] = None, 
        class_id: Optional[str] = None, 
        subject_id: Optional[str] = None, 
        knowledge_id: Optional[str] = None, 
        answer_txt: Optional[str] = None, 
        answer_pic_path: Optional[str] = None, 
        answer_audio_path: Optional[str] = None, 
        knowledge_list: Optional[str] = None, 
        l_rps_id: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_rps_content: Optional[str] = None, 
        l_rps_create_name: Optional[str] = None, 
        l_class_id: Optional[str] = None, 
        l_subject_id: Optional[str] = None, 
        l_knowledge_id: Optional[str] = None, 
        l_answer_txt: Optional[str] = None, 
        l_answer_pic_path: Optional[str] = None, 
        l_answer_audio_path: Optional[str] = None, 
        l_knowledge_list: Optional[str] = None, 
        s_rps_content: Optional[str] = None, 
        s_rps_create_name: Optional[str] = None, 
        s_answer_txt: Optional[str] = None, 
        s_answer_pic_path: Optional[str] = None, 
        s_answer_audio_path: Optional[str] = None, 
        s_knowledge_list: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResRemainPointSubject:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if rps_id is not None:
        values = rps_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['rps_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['rps_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['rps_id_end'] = int(val)
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if rps_content is not None:
        values = rps_content.split(',')
        if len(values) == 1:
            val = values[0]
            items['rps_content'] = val
        else:
            val = values[0]
            if val != '':
                items['rps_content_start'] = val
            
            val = values[1]
            if val != '':
                items['rps_content_end'] = val
        
    if rps_create_name is not None:
        values = rps_create_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['rps_create_name'] = val
        else:
            val = values[0]
            if val != '':
                items['rps_create_name_start'] = val
            
            val = values[1]
            if val != '':
                items['rps_create_name_end'] = val
        
    if class_id is not None:
        values = class_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['class_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['class_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['class_id_end'] = int(val)
        
    if subject_id is not None:
        values = subject_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['subject_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['subject_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['subject_id_end'] = int(val)
        
    if knowledge_id is not None:
        values = knowledge_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['knowledge_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['knowledge_id_end'] = int(val)
        
    if answer_txt is not None:
        values = answer_txt.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_txt'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_txt_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_txt_end'] = val
        
    if answer_pic_path is not None:
        values = answer_pic_path.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_pic_path'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_pic_path_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_pic_path_end'] = val
        
    if answer_audio_path is not None:
        values = answer_audio_path.split(',')
        if len(values) == 1:
            val = values[0]
            items['answer_audio_path'] = val
        else:
            val = values[0]
            if val != '':
                items['answer_audio_path_start'] = val
            
            val = values[1]
            if val != '':
                items['answer_audio_path_end'] = val
        
    if knowledge_list is not None:
        values = knowledge_list.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_list'] = val
        else:
            val = values[0]
            if val != '':
                items['knowledge_list_start'] = val
            
            val = values[1]
            if val != '':
                items['knowledge_list_end'] = val
        

    if s_rps_content is not None:
        search_items['rps_content'] = '%' + s_rps_content + '%'
        
    if s_rps_create_name is not None:
        search_items['rps_create_name'] = '%' + s_rps_create_name + '%'
        
    if s_answer_txt is not None:
        search_items['answer_txt'] = '%' + s_answer_txt + '%'
        
    if s_answer_pic_path is not None:
        search_items['answer_pic_path'] = '%' + s_answer_pic_path + '%'
        
    if s_answer_audio_path is not None:
        search_items['answer_audio_path'] = '%' + s_answer_audio_path + '%'
        
    if s_knowledge_list is not None:
        search_items['knowledge_list'] = '%' + s_knowledge_list + '%'
        

    if l_rps_id is not None:
        values = l_rps_id.split(',')
        values = [int(val) for val in values]
        set_items['rps_id'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_rps_content is not None:
        values = l_rps_content.split(',')
        values = [val for val in values]
        set_items['rps_content'] = values
        
    if l_rps_create_name is not None:
        values = l_rps_create_name.split(',')
        values = [val for val in values]
        set_items['rps_create_name'] = values
        
    if l_class_id is not None:
        values = l_class_id.split(',')
        values = [int(val) for val in values]
        set_items['class_id'] = values
        
    if l_subject_id is not None:
        values = l_subject_id.split(',')
        values = [int(val) for val in values]
        set_items['subject_id'] = values
        
    if l_knowledge_id is not None:
        values = l_knowledge_id.split(',')
        values = [int(val) for val in values]
        set_items['knowledge_id'] = values
        
    if l_answer_txt is not None:
        values = l_answer_txt.split(',')
        values = [val for val in values]
        set_items['answer_txt'] = values
        
    if l_answer_pic_path is not None:
        values = l_answer_pic_path.split(',')
        values = [val for val in values]
        set_items['answer_pic_path'] = values
        
    if l_answer_audio_path is not None:
        values = l_answer_audio_path.split(',')
        values = [val for val in values]
        set_items['answer_audio_path'] = values
        
    if l_knowledge_list is not None:
        values = l_knowledge_list.split(',')
        values = [val for val in values]
        set_items['knowledge_list'] = values
            
    
    data = d_db.filter_remain_point_subject(items, search_items, set_items, page, page_size)
    return FilterResRemainPointSubject(data=data, total=-1)

    
@router.post(f'/sh_clas/create', response_model=SShClas)
async def create_sh_clas(item: CreateShClas) -> SShClas:
    dict_item = dict(item)
    for k,v in dict_item.items():
        if v is not None:
            v = str(v)
            v = v.replace(" ", "")
            get_search = re.search(r"'", v, flags=0)
            get_search2 = re.search(r'%27', v, flags=0)
            get_search3 = re.search(r'unionselect', v, flags=0)
            if get_search or get_search2 or get_search3:
               raise HTTPException(status_code=404, detail='bad way~~~~~~')

    return d_db.insert_sh_clas(item)
        
    
@router.post(f'/sh_clas/update', response_model=str)
async def update_sh_clas(item: SShClas) -> str:
    d_db.update_sh_clas(item)
    return "success"

    
@router.get(f'/sh_clas/get', response_model=SShClas)
async def get_sh_clas(sh_clas_id: int) -> SShClas:
    return d_db.get_sh_clas(sh_clas_id)


@router.get(f'/sh_clas/filter', response_model=FilterResShClas)
async def filter_sh_clas(
        cl_id: Optional[str] = None, 
        create_time: Optional[str] = None, 
        cl_name: Optional[str] = None, 
        cl_create_name: Optional[str] = None, 
        l_cl_id: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_cl_name: Optional[str] = None, 
        l_cl_create_name: Optional[str] = None, 
        s_cl_name: Optional[str] = None, 
        s_cl_create_name: Optional[str] = None,
        order_by: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResShClas:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if cl_id is not None:
        values = cl_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['cl_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['cl_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['cl_id_end'] = int(val)
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if cl_name is not None:
        values = cl_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['cl_name'] = val
        else:
            val = values[0]
            if val != '':
                items['cl_name_start'] = val
            
            val = values[1]
            if val != '':
                items['cl_name_end'] = val
        
    if cl_create_name is not None:
        values = cl_create_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['cl_create_name'] = val
        else:
            val = values[0]
            if val != '':
                items['cl_create_name_start'] = val
            
            val = values[1]
            if val != '':
                items['cl_create_name_end'] = val
        

    if s_cl_name is not None:
        search_items['cl_name'] = '%' + s_cl_name + '%'
        
    if s_cl_create_name is not None:
        search_items['cl_create_name'] = '%' + s_cl_create_name + '%'
        

    if l_cl_id is not None:
        values = l_cl_id.split(',')
        values = [int(val) for val in values]
        set_items['cl_id'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_cl_name is not None:
        values = l_cl_name.split(',')
        values = [val for val in values]
        set_items['cl_name'] = values
        
    if l_cl_create_name is not None:
        values = l_cl_create_name.split(',')
        values = [val for val in values]
        set_items['cl_create_name'] = values
            
    
    
    order_items = dict()
    if order_by is not None:
        orders = order_by.split(',')
        for order in orders:
            if order.startswith('-'):
                order_items[order[1:]] = 'desc'
            else:
                order_items[order] = 'asc'
    data = d_db.filter_sh_clas(items, search_items, set_items, order_items, page, page_size)
    c = d_db.filter_count_sh_clas(items, search_items, set_items)
    
    return FilterResShClas(data=data, total=c)


@router.get(f'/sh_clas/fast_filter', response_model=FilterResShClas)
async def fast_filter_sh_clas(
        cl_id: Optional[str] = None, 
        create_time: Optional[str] = None, 
        cl_name: Optional[str] = None, 
        cl_create_name: Optional[str] = None, 
        l_cl_id: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_cl_name: Optional[str] = None, 
        l_cl_create_name: Optional[str] = None, 
        s_cl_name: Optional[str] = None, 
        s_cl_create_name: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResShClas:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if cl_id is not None:
        values = cl_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['cl_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['cl_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['cl_id_end'] = int(val)
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if cl_name is not None:
        values = cl_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['cl_name'] = val
        else:
            val = values[0]
            if val != '':
                items['cl_name_start'] = val
            
            val = values[1]
            if val != '':
                items['cl_name_end'] = val
        
    if cl_create_name is not None:
        values = cl_create_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['cl_create_name'] = val
        else:
            val = values[0]
            if val != '':
                items['cl_create_name_start'] = val
            
            val = values[1]
            if val != '':
                items['cl_create_name_end'] = val
        

    if s_cl_name is not None:
        search_items['cl_name'] = '%' + s_cl_name + '%'
        
    if s_cl_create_name is not None:
        search_items['cl_create_name'] = '%' + s_cl_create_name + '%'
        

    if l_cl_id is not None:
        values = l_cl_id.split(',')
        values = [int(val) for val in values]
        set_items['cl_id'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_cl_name is not None:
        values = l_cl_name.split(',')
        values = [val for val in values]
        set_items['cl_name'] = values
        
    if l_cl_create_name is not None:
        values = l_cl_create_name.split(',')
        values = [val for val in values]
        set_items['cl_create_name'] = values
            
    
    data = d_db.filter_sh_clas(items, search_items, set_items, page, page_size)
    return FilterResShClas(data=data, total=-1)

    
@router.post(f'/sh_subject/create', response_model=SShSubject)
async def create_sh_subject(item: CreateShSubject) -> SShSubject:
    dict_item = dict(item)
    for k,v in dict_item.items():
        if v is not None:
            v = str(v)
            v = v.replace(" ", "")
            get_search = re.search(r"'", v, flags=0)
            get_search2 = re.search(r'%27', v, flags=0)
            get_search3 = re.search(r'unionselect', v, flags=0)
            if get_search or get_search2 or get_search3:
               raise HTTPException(status_code=404, detail='bad way~~~~~~')

    return d_db.insert_sh_subject(item)
        
    
@router.post(f'/sh_subject/update', response_model=str)
async def update_sh_subject(item: SShSubject) -> str:
    d_db.update_sh_subject(item)
    return "success"

    
@router.get(f'/sh_subject/get', response_model=SShSubject)
async def get_sh_subject(sh_subject_id: int) -> SShSubject:
    return d_db.get_sh_subject(sh_subject_id)


@router.get(f'/sh_subject/filter', response_model=FilterResShSubject)
async def filter_sh_subject(
        su_id: Optional[str] = None, 
        create_time: Optional[str] = None, 
        su_name: Optional[str] = None, 
        su_create_name: Optional[str] = None, 
        class_id: Optional[str] = None, 
        knowledge_list: Optional[str] = None, 
        l_su_id: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_su_name: Optional[str] = None, 
        l_su_create_name: Optional[str] = None, 
        l_class_id: Optional[str] = None, 
        l_knowledge_list: Optional[str] = None, 
        s_su_name: Optional[str] = None, 
        s_su_create_name: Optional[str] = None, 
        s_knowledge_list: Optional[str] = None,
        order_by: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResShSubject:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if su_id is not None:
        values = su_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['su_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['su_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['su_id_end'] = int(val)
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if su_name is not None:
        values = su_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['su_name'] = val
        else:
            val = values[0]
            if val != '':
                items['su_name_start'] = val
            
            val = values[1]
            if val != '':
                items['su_name_end'] = val
        
    if su_create_name is not None:
        values = su_create_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['su_create_name'] = val
        else:
            val = values[0]
            if val != '':
                items['su_create_name_start'] = val
            
            val = values[1]
            if val != '':
                items['su_create_name_end'] = val
        
    if class_id is not None:
        values = class_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['class_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['class_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['class_id_end'] = int(val)
        
    if knowledge_list is not None:
        values = knowledge_list.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_list'] = val
        else:
            val = values[0]
            if val != '':
                items['knowledge_list_start'] = val
            
            val = values[1]
            if val != '':
                items['knowledge_list_end'] = val
        

    if s_su_name is not None:
        search_items['su_name'] = '%' + s_su_name + '%'
        
    if s_su_create_name is not None:
        search_items['su_create_name'] = '%' + s_su_create_name + '%'
        
    if s_knowledge_list is not None:
        search_items['knowledge_list'] = '%' + s_knowledge_list + '%'
        

    if l_su_id is not None:
        values = l_su_id.split(',')
        values = [int(val) for val in values]
        set_items['su_id'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_su_name is not None:
        values = l_su_name.split(',')
        values = [val for val in values]
        set_items['su_name'] = values
        
    if l_su_create_name is not None:
        values = l_su_create_name.split(',')
        values = [val for val in values]
        set_items['su_create_name'] = values
        
    if l_class_id is not None:
        values = l_class_id.split(',')
        values = [int(val) for val in values]
        set_items['class_id'] = values
        
    if l_knowledge_list is not None:
        values = l_knowledge_list.split(',')
        values = [val for val in values]
        set_items['knowledge_list'] = values
            
    
    
    order_items = dict()
    if order_by is not None:
        orders = order_by.split(',')
        for order in orders:
            if order.startswith('-'):
                order_items[order[1:]] = 'desc'
            else:
                order_items[order] = 'asc'
    data = d_db.filter_sh_subject(items, search_items, set_items, order_items, page, page_size)
    c = d_db.filter_count_sh_subject(items, search_items, set_items)
    
    return FilterResShSubject(data=data, total=c)


@router.get(f'/sh_subject/fast_filter', response_model=FilterResShSubject)
async def fast_filter_sh_subject(
        su_id: Optional[str] = None, 
        create_time: Optional[str] = None, 
        su_name: Optional[str] = None, 
        su_create_name: Optional[str] = None, 
        class_id: Optional[str] = None, 
        knowledge_list: Optional[str] = None, 
        l_su_id: Optional[str] = None, 
        l_create_time: Optional[str] = None, 
        l_su_name: Optional[str] = None, 
        l_su_create_name: Optional[str] = None, 
        l_class_id: Optional[str] = None, 
        l_knowledge_list: Optional[str] = None, 
        s_su_name: Optional[str] = None, 
        s_su_create_name: Optional[str] = None, 
        s_knowledge_list: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResShSubject:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if su_id is not None:
        values = su_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['su_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['su_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['su_id_end'] = int(val)
        
    if create_time is not None:
        values = create_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['create_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['create_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['create_time_end'] = datetime.fromtimestamp(int(val))
        
    if su_name is not None:
        values = su_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['su_name'] = val
        else:
            val = values[0]
            if val != '':
                items['su_name_start'] = val
            
            val = values[1]
            if val != '':
                items['su_name_end'] = val
        
    if su_create_name is not None:
        values = su_create_name.split(',')
        if len(values) == 1:
            val = values[0]
            items['su_create_name'] = val
        else:
            val = values[0]
            if val != '':
                items['su_create_name_start'] = val
            
            val = values[1]
            if val != '':
                items['su_create_name_end'] = val
        
    if class_id is not None:
        values = class_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['class_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['class_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['class_id_end'] = int(val)
        
    if knowledge_list is not None:
        values = knowledge_list.split(',')
        if len(values) == 1:
            val = values[0]
            items['knowledge_list'] = val
        else:
            val = values[0]
            if val != '':
                items['knowledge_list_start'] = val
            
            val = values[1]
            if val != '':
                items['knowledge_list_end'] = val
        

    if s_su_name is not None:
        search_items['su_name'] = '%' + s_su_name + '%'
        
    if s_su_create_name is not None:
        search_items['su_create_name'] = '%' + s_su_create_name + '%'
        
    if s_knowledge_list is not None:
        search_items['knowledge_list'] = '%' + s_knowledge_list + '%'
        

    if l_su_id is not None:
        values = l_su_id.split(',')
        values = [int(val) for val in values]
        set_items['su_id'] = values
        
    if l_create_time is not None:
        values = l_create_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['create_time'] = values
        
    if l_su_name is not None:
        values = l_su_name.split(',')
        values = [val for val in values]
        set_items['su_name'] = values
        
    if l_su_create_name is not None:
        values = l_su_create_name.split(',')
        values = [val for val in values]
        set_items['su_create_name'] = values
        
    if l_class_id is not None:
        values = l_class_id.split(',')
        values = [int(val) for val in values]
        set_items['class_id'] = values
        
    if l_knowledge_list is not None:
        values = l_knowledge_list.split(',')
        values = [val for val in values]
        set_items['knowledge_list'] = values
            
    
    data = d_db.filter_sh_subject(items, search_items, set_items, page, page_size)
    return FilterResShSubject(data=data, total=-1)

    
@router.post(f'/user/create', response_model=SUser)
async def create_user(item: CreateUser) -> SUser:
    dict_item = dict(item)
    for k,v in dict_item.items():
        if v is not None:
            v = str(v)
            v = v.replace(" ", "")
            get_search = re.search(r"'", v, flags=0)
            get_search2 = re.search(r'%27', v, flags=0)
            get_search3 = re.search(r'unionselect', v, flags=0)
            if get_search or get_search2 or get_search3:
               raise HTTPException(status_code=404, detail='bad way~~~~~~')

    return d_db.insert_user(item)
        
    
@router.post(f'/user/update', response_model=str)
async def update_user(item: SUser) -> str:
    d_db.update_user(item)
    return "success"

    
@router.get(f'/user/get', response_model=SUser)
async def get_user(user_id: int) -> SUser:
    return d_db.get_user(user_id)


@router.get(f'/user/filter', response_model=FilterResUser)
async def filter_user(
        id: Optional[str] = None, 
        username: Optional[str] = None, 
        email: Optional[str] = None, 
        open_id: Optional[str] = None, 
        union_id: Optional[str] = None, 
        password: Optional[str] = None, 
        nickname: Optional[str] = None, 
        phone: Optional[str] = None, 
        id_card: Optional[str] = None, 
        level_id: Optional[str] = None, 
        status: Optional[str] = None, 
        register_time: Optional[str] = None, 
        avatar: Optional[str] = None, 
        invited_user_id: Optional[str] = None, 
        coin: Optional[str] = None, 
        gender: Optional[str] = None, 
        last_active_time: Optional[str] = None, 
        name: Optional[str] = None, 
        is_agree: Optional[str] = None, 
        parent_id: Optional[str] = None, 
        parent_id_history: Optional[str] = None, 
        level_one_time: Optional[str] = None, 
        level_two_time: Optional[str] = None, 
        level_three_time: Optional[str] = None, 
        level_top_time: Optional[str] = None, 
        manage_id: Optional[str] = None, 
        l_id: Optional[str] = None, 
        l_username: Optional[str] = None, 
        l_email: Optional[str] = None, 
        l_open_id: Optional[str] = None, 
        l_union_id: Optional[str] = None, 
        l_password: Optional[str] = None, 
        l_nickname: Optional[str] = None, 
        l_phone: Optional[str] = None, 
        l_id_card: Optional[str] = None, 
        l_level_id: Optional[str] = None, 
        l_status: Optional[str] = None, 
        l_register_time: Optional[str] = None, 
        l_avatar: Optional[str] = None, 
        l_invited_user_id: Optional[str] = None, 
        l_coin: Optional[str] = None, 
        l_gender: Optional[str] = None, 
        l_last_active_time: Optional[str] = None, 
        l_name: Optional[str] = None, 
        l_is_agree: Optional[str] = None, 
        l_parent_id: Optional[str] = None, 
        l_parent_id_history: Optional[str] = None, 
        l_level_one_time: Optional[str] = None, 
        l_level_two_time: Optional[str] = None, 
        l_level_three_time: Optional[str] = None, 
        l_level_top_time: Optional[str] = None, 
        l_manage_id: Optional[str] = None, 
        s_username: Optional[str] = None, 
        s_email: Optional[str] = None, 
        s_open_id: Optional[str] = None, 
        s_union_id: Optional[str] = None, 
        s_password: Optional[str] = None, 
        s_nickname: Optional[str] = None, 
        s_phone: Optional[str] = None, 
        s_id_card: Optional[str] = None, 
        s_avatar: Optional[str] = None, 
        s_name: Optional[str] = None, 
        s_parent_id_history: Optional[str] = None,
        order_by: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResUser:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if id is not None:
        values = id.split(',')
        if len(values) == 1:
            val = values[0]
            items['id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['id_end'] = int(val)
        
    if username is not None:
        values = username.split(',')
        if len(values) == 1:
            val = values[0]
            items['username'] = val
        else:
            val = values[0]
            if val != '':
                items['username_start'] = val
            
            val = values[1]
            if val != '':
                items['username_end'] = val
        
    if email is not None:
        values = email.split(',')
        if len(values) == 1:
            val = values[0]
            items['email'] = val
        else:
            val = values[0]
            if val != '':
                items['email_start'] = val
            
            val = values[1]
            if val != '':
                items['email_end'] = val
        
    if open_id is not None:
        values = open_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['open_id'] = val
        else:
            val = values[0]
            if val != '':
                items['open_id_start'] = val
            
            val = values[1]
            if val != '':
                items['open_id_end'] = val
        
    if union_id is not None:
        values = union_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['union_id'] = val
        else:
            val = values[0]
            if val != '':
                items['union_id_start'] = val
            
            val = values[1]
            if val != '':
                items['union_id_end'] = val
        
    if password is not None:
        values = password.split(',')
        if len(values) == 1:
            val = values[0]
            items['password'] = val
        else:
            val = values[0]
            if val != '':
                items['password_start'] = val
            
            val = values[1]
            if val != '':
                items['password_end'] = val
        
    if nickname is not None:
        values = nickname.split(',')
        if len(values) == 1:
            val = values[0]
            items['nickname'] = val
        else:
            val = values[0]
            if val != '':
                items['nickname_start'] = val
            
            val = values[1]
            if val != '':
                items['nickname_end'] = val
        
    if phone is not None:
        values = phone.split(',')
        if len(values) == 1:
            val = values[0]
            items['phone'] = val
        else:
            val = values[0]
            if val != '':
                items['phone_start'] = val
            
            val = values[1]
            if val != '':
                items['phone_end'] = val
        
    if id_card is not None:
        values = id_card.split(',')
        if len(values) == 1:
            val = values[0]
            items['id_card'] = val
        else:
            val = values[0]
            if val != '':
                items['id_card_start'] = val
            
            val = values[1]
            if val != '':
                items['id_card_end'] = val
        
    if level_id is not None:
        values = level_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['level_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['level_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['level_id_end'] = int(val)
        
    if status is not None:
        values = status.split(',')
        if len(values) == 1:
            val = values[0]
            items['status'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['status_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['status_end'] = int(val)
        
    if register_time is not None:
        values = register_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['register_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['register_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['register_time_end'] = datetime.fromtimestamp(int(val))
        
    if avatar is not None:
        values = avatar.split(',')
        if len(values) == 1:
            val = values[0]
            items['avatar'] = val
        else:
            val = values[0]
            if val != '':
                items['avatar_start'] = val
            
            val = values[1]
            if val != '':
                items['avatar_end'] = val
        
    if invited_user_id is not None:
        values = invited_user_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['invited_user_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['invited_user_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['invited_user_id_end'] = int(val)
        
    if coin is not None:
        values = coin.split(',')
        if len(values) == 1:
            val = values[0]
            items['coin'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['coin_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['coin_end'] = int(val)
        
    if gender is not None:
        values = gender.split(',')
        if len(values) == 1:
            val = values[0]
            items['gender'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['gender_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['gender_end'] = int(val)
        
    if last_active_time is not None:
        values = last_active_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['last_active_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['last_active_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['last_active_time_end'] = datetime.fromtimestamp(int(val))
        
    if name is not None:
        values = name.split(',')
        if len(values) == 1:
            val = values[0]
            items['name'] = val
        else:
            val = values[0]
            if val != '':
                items['name_start'] = val
            
            val = values[1]
            if val != '':
                items['name_end'] = val
        
    if is_agree is not None:
        values = is_agree.split(',')
        if len(values) == 1:
            val = values[0]
            items['is_agree'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['is_agree_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['is_agree_end'] = int(val)
        
    if parent_id is not None:
        values = parent_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['parent_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['parent_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['parent_id_end'] = int(val)
        
    if parent_id_history is not None:
        values = parent_id_history.split(',')
        if len(values) == 1:
            val = values[0]
            items['parent_id_history'] = val
        else:
            val = values[0]
            if val != '':
                items['parent_id_history_start'] = val
            
            val = values[1]
            if val != '':
                items['parent_id_history_end'] = val
        
    if level_one_time is not None:
        values = level_one_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['level_one_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['level_one_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['level_one_time_end'] = datetime.fromtimestamp(int(val))
        
    if level_two_time is not None:
        values = level_two_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['level_two_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['level_two_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['level_two_time_end'] = datetime.fromtimestamp(int(val))
        
    if level_three_time is not None:
        values = level_three_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['level_three_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['level_three_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['level_three_time_end'] = datetime.fromtimestamp(int(val))
        
    if level_top_time is not None:
        values = level_top_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['level_top_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['level_top_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['level_top_time_end'] = datetime.fromtimestamp(int(val))
        
    if manage_id is not None:
        values = manage_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['manage_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['manage_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['manage_id_end'] = int(val)
        

    if s_username is not None:
        search_items['username'] = '%' + s_username + '%'
        
    if s_email is not None:
        search_items['email'] = '%' + s_email + '%'
        
    if s_open_id is not None:
        search_items['open_id'] = '%' + s_open_id + '%'
        
    if s_union_id is not None:
        search_items['union_id'] = '%' + s_union_id + '%'
        
    if s_password is not None:
        search_items['password'] = '%' + s_password + '%'
        
    if s_nickname is not None:
        search_items['nickname'] = '%' + s_nickname + '%'
        
    if s_phone is not None:
        search_items['phone'] = '%' + s_phone + '%'
        
    if s_id_card is not None:
        search_items['id_card'] = '%' + s_id_card + '%'
        
    if s_avatar is not None:
        search_items['avatar'] = '%' + s_avatar + '%'
        
    if s_name is not None:
        search_items['name'] = '%' + s_name + '%'
        
    if s_parent_id_history is not None:
        search_items['parent_id_history'] = '%' + s_parent_id_history + '%'
        

    if l_id is not None:
        values = l_id.split(',')
        values = [int(val) for val in values]
        set_items['id'] = values
        
    if l_username is not None:
        values = l_username.split(',')
        values = [val for val in values]
        set_items['username'] = values
        
    if l_email is not None:
        values = l_email.split(',')
        values = [val for val in values]
        set_items['email'] = values
        
    if l_open_id is not None:
        values = l_open_id.split(',')
        values = [val for val in values]
        set_items['open_id'] = values
        
    if l_union_id is not None:
        values = l_union_id.split(',')
        values = [val for val in values]
        set_items['union_id'] = values
        
    if l_password is not None:
        values = l_password.split(',')
        values = [val for val in values]
        set_items['password'] = values
        
    if l_nickname is not None:
        values = l_nickname.split(',')
        values = [val for val in values]
        set_items['nickname'] = values
        
    if l_phone is not None:
        values = l_phone.split(',')
        values = [val for val in values]
        set_items['phone'] = values
        
    if l_id_card is not None:
        values = l_id_card.split(',')
        values = [val for val in values]
        set_items['id_card'] = values
        
    if l_level_id is not None:
        values = l_level_id.split(',')
        values = [int(val) for val in values]
        set_items['level_id'] = values
        
    if l_status is not None:
        values = l_status.split(',')
        values = [int(val) for val in values]
        set_items['status'] = values
        
    if l_register_time is not None:
        values = l_register_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['register_time'] = values
        
    if l_avatar is not None:
        values = l_avatar.split(',')
        values = [val for val in values]
        set_items['avatar'] = values
        
    if l_invited_user_id is not None:
        values = l_invited_user_id.split(',')
        values = [int(val) for val in values]
        set_items['invited_user_id'] = values
        
    if l_coin is not None:
        values = l_coin.split(',')
        values = [int(val) for val in values]
        set_items['coin'] = values
        
    if l_gender is not None:
        values = l_gender.split(',')
        values = [int(val) for val in values]
        set_items['gender'] = values
        
    if l_last_active_time is not None:
        values = l_last_active_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['last_active_time'] = values
        
    if l_name is not None:
        values = l_name.split(',')
        values = [val for val in values]
        set_items['name'] = values
        
    if l_is_agree is not None:
        values = l_is_agree.split(',')
        values = [int(val) for val in values]
        set_items['is_agree'] = values
        
    if l_parent_id is not None:
        values = l_parent_id.split(',')
        values = [int(val) for val in values]
        set_items['parent_id'] = values
        
    if l_parent_id_history is not None:
        values = l_parent_id_history.split(',')
        values = [val for val in values]
        set_items['parent_id_history'] = values
        
    if l_level_one_time is not None:
        values = l_level_one_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['level_one_time'] = values
        
    if l_level_two_time is not None:
        values = l_level_two_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['level_two_time'] = values
        
    if l_level_three_time is not None:
        values = l_level_three_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['level_three_time'] = values
        
    if l_level_top_time is not None:
        values = l_level_top_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['level_top_time'] = values
        
    if l_manage_id is not None:
        values = l_manage_id.split(',')
        values = [int(val) for val in values]
        set_items['manage_id'] = values
            
    
    
    order_items = dict()
    if order_by is not None:
        orders = order_by.split(',')
        for order in orders:
            if order.startswith('-'):
                order_items[order[1:]] = 'desc'
            else:
                order_items[order] = 'asc'
    data = d_db.filter_user(items, search_items, set_items, order_items, page, page_size)
    c = d_db.filter_count_user(items, search_items, set_items)
    
    return FilterResUser(data=data, total=c)


@router.get(f'/user/fast_filter', response_model=FilterResUser)
async def fast_filter_user(
        id: Optional[str] = None, 
        username: Optional[str] = None, 
        email: Optional[str] = None, 
        open_id: Optional[str] = None, 
        union_id: Optional[str] = None, 
        password: Optional[str] = None, 
        nickname: Optional[str] = None, 
        phone: Optional[str] = None, 
        id_card: Optional[str] = None, 
        level_id: Optional[str] = None, 
        status: Optional[str] = None, 
        register_time: Optional[str] = None, 
        avatar: Optional[str] = None, 
        invited_user_id: Optional[str] = None, 
        coin: Optional[str] = None, 
        gender: Optional[str] = None, 
        last_active_time: Optional[str] = None, 
        name: Optional[str] = None, 
        is_agree: Optional[str] = None, 
        parent_id: Optional[str] = None, 
        parent_id_history: Optional[str] = None, 
        level_one_time: Optional[str] = None, 
        level_two_time: Optional[str] = None, 
        level_three_time: Optional[str] = None, 
        level_top_time: Optional[str] = None, 
        manage_id: Optional[str] = None, 
        l_id: Optional[str] = None, 
        l_username: Optional[str] = None, 
        l_email: Optional[str] = None, 
        l_open_id: Optional[str] = None, 
        l_union_id: Optional[str] = None, 
        l_password: Optional[str] = None, 
        l_nickname: Optional[str] = None, 
        l_phone: Optional[str] = None, 
        l_id_card: Optional[str] = None, 
        l_level_id: Optional[str] = None, 
        l_status: Optional[str] = None, 
        l_register_time: Optional[str] = None, 
        l_avatar: Optional[str] = None, 
        l_invited_user_id: Optional[str] = None, 
        l_coin: Optional[str] = None, 
        l_gender: Optional[str] = None, 
        l_last_active_time: Optional[str] = None, 
        l_name: Optional[str] = None, 
        l_is_agree: Optional[str] = None, 
        l_parent_id: Optional[str] = None, 
        l_parent_id_history: Optional[str] = None, 
        l_level_one_time: Optional[str] = None, 
        l_level_two_time: Optional[str] = None, 
        l_level_three_time: Optional[str] = None, 
        l_level_top_time: Optional[str] = None, 
        l_manage_id: Optional[str] = None, 
        s_username: Optional[str] = None, 
        s_email: Optional[str] = None, 
        s_open_id: Optional[str] = None, 
        s_union_id: Optional[str] = None, 
        s_password: Optional[str] = None, 
        s_nickname: Optional[str] = None, 
        s_phone: Optional[str] = None, 
        s_id_card: Optional[str] = None, 
        s_avatar: Optional[str] = None, 
        s_name: Optional[str] = None, 
        s_parent_id_history: Optional[str] = None,
        page: int = 1, 
        page_size: int = 20) -> FilterResUser:

    """
    1. 按照字段查询`?field1=value1&field2=value2`
    2. 按照范围查询，大于某个值`?field=value,`, 表示filed大于value
    3. 按照范围查询，小于某个值`?field=,value`， 表示field小于value
    4. 按照范围查询，范围值`?field=value1,value2`，表示搜索field大于等于value1，小于等于value2
    5. page是页数，第一页为1
    6. page_size为每一页大小， 默认20
    7. 如果是日期，请使用时间戳，十位的时间戳，单位：秒
    8. 所有字符串字段均可搜索，需要在字段前加个前缀`s_`,例如搜索`username`包含`zhang`， 则可以这样`s_username=zhang`写,这里只是一个假设
    9. 字段的多选择（in关系），需要在字段前加前缀`l_`,并且以逗号`,`隔开,例如要找出`id=2`或者`id=3`的样本，可以这样写`?l_id=2,3`
    """
    

    items = dict()
    search_items = dict()
    set_items = dict()

    if id is not None:
        values = id.split(',')
        if len(values) == 1:
            val = values[0]
            items['id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['id_end'] = int(val)
        
    if username is not None:
        values = username.split(',')
        if len(values) == 1:
            val = values[0]
            items['username'] = val
        else:
            val = values[0]
            if val != '':
                items['username_start'] = val
            
            val = values[1]
            if val != '':
                items['username_end'] = val
        
    if email is not None:
        values = email.split(',')
        if len(values) == 1:
            val = values[0]
            items['email'] = val
        else:
            val = values[0]
            if val != '':
                items['email_start'] = val
            
            val = values[1]
            if val != '':
                items['email_end'] = val
        
    if open_id is not None:
        values = open_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['open_id'] = val
        else:
            val = values[0]
            if val != '':
                items['open_id_start'] = val
            
            val = values[1]
            if val != '':
                items['open_id_end'] = val
        
    if union_id is not None:
        values = union_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['union_id'] = val
        else:
            val = values[0]
            if val != '':
                items['union_id_start'] = val
            
            val = values[1]
            if val != '':
                items['union_id_end'] = val
        
    if password is not None:
        values = password.split(',')
        if len(values) == 1:
            val = values[0]
            items['password'] = val
        else:
            val = values[0]
            if val != '':
                items['password_start'] = val
            
            val = values[1]
            if val != '':
                items['password_end'] = val
        
    if nickname is not None:
        values = nickname.split(',')
        if len(values) == 1:
            val = values[0]
            items['nickname'] = val
        else:
            val = values[0]
            if val != '':
                items['nickname_start'] = val
            
            val = values[1]
            if val != '':
                items['nickname_end'] = val
        
    if phone is not None:
        values = phone.split(',')
        if len(values) == 1:
            val = values[0]
            items['phone'] = val
        else:
            val = values[0]
            if val != '':
                items['phone_start'] = val
            
            val = values[1]
            if val != '':
                items['phone_end'] = val
        
    if id_card is not None:
        values = id_card.split(',')
        if len(values) == 1:
            val = values[0]
            items['id_card'] = val
        else:
            val = values[0]
            if val != '':
                items['id_card_start'] = val
            
            val = values[1]
            if val != '':
                items['id_card_end'] = val
        
    if level_id is not None:
        values = level_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['level_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['level_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['level_id_end'] = int(val)
        
    if status is not None:
        values = status.split(',')
        if len(values) == 1:
            val = values[0]
            items['status'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['status_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['status_end'] = int(val)
        
    if register_time is not None:
        values = register_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['register_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['register_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['register_time_end'] = datetime.fromtimestamp(int(val))
        
    if avatar is not None:
        values = avatar.split(',')
        if len(values) == 1:
            val = values[0]
            items['avatar'] = val
        else:
            val = values[0]
            if val != '':
                items['avatar_start'] = val
            
            val = values[1]
            if val != '':
                items['avatar_end'] = val
        
    if invited_user_id is not None:
        values = invited_user_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['invited_user_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['invited_user_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['invited_user_id_end'] = int(val)
        
    if coin is not None:
        values = coin.split(',')
        if len(values) == 1:
            val = values[0]
            items['coin'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['coin_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['coin_end'] = int(val)
        
    if gender is not None:
        values = gender.split(',')
        if len(values) == 1:
            val = values[0]
            items['gender'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['gender_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['gender_end'] = int(val)
        
    if last_active_time is not None:
        values = last_active_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['last_active_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['last_active_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['last_active_time_end'] = datetime.fromtimestamp(int(val))
        
    if name is not None:
        values = name.split(',')
        if len(values) == 1:
            val = values[0]
            items['name'] = val
        else:
            val = values[0]
            if val != '':
                items['name_start'] = val
            
            val = values[1]
            if val != '':
                items['name_end'] = val
        
    if is_agree is not None:
        values = is_agree.split(',')
        if len(values) == 1:
            val = values[0]
            items['is_agree'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['is_agree_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['is_agree_end'] = int(val)
        
    if parent_id is not None:
        values = parent_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['parent_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['parent_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['parent_id_end'] = int(val)
        
    if parent_id_history is not None:
        values = parent_id_history.split(',')
        if len(values) == 1:
            val = values[0]
            items['parent_id_history'] = val
        else:
            val = values[0]
            if val != '':
                items['parent_id_history_start'] = val
            
            val = values[1]
            if val != '':
                items['parent_id_history_end'] = val
        
    if level_one_time is not None:
        values = level_one_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['level_one_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['level_one_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['level_one_time_end'] = datetime.fromtimestamp(int(val))
        
    if level_two_time is not None:
        values = level_two_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['level_two_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['level_two_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['level_two_time_end'] = datetime.fromtimestamp(int(val))
        
    if level_three_time is not None:
        values = level_three_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['level_three_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['level_three_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['level_three_time_end'] = datetime.fromtimestamp(int(val))
        
    if level_top_time is not None:
        values = level_top_time.split(',')
        if len(values) == 1:
            val = values[0]
            items['level_top_time'] = datetime.fromtimestamp(int(val))
        else:
            val = values[0]
            if val != '':
                items['level_top_time_start'] = datetime.fromtimestamp(int(val))
            
            val = values[1]
            if val != '':
                items['level_top_time_end'] = datetime.fromtimestamp(int(val))
        
    if manage_id is not None:
        values = manage_id.split(',')
        if len(values) == 1:
            val = values[0]
            items['manage_id'] = int(val)
        else:
            val = values[0]
            if val != '':
                items['manage_id_start'] = int(val)
            
            val = values[1]
            if val != '':
                items['manage_id_end'] = int(val)
        

    if s_username is not None:
        search_items['username'] = '%' + s_username + '%'
        
    if s_email is not None:
        search_items['email'] = '%' + s_email + '%'
        
    if s_open_id is not None:
        search_items['open_id'] = '%' + s_open_id + '%'
        
    if s_union_id is not None:
        search_items['union_id'] = '%' + s_union_id + '%'
        
    if s_password is not None:
        search_items['password'] = '%' + s_password + '%'
        
    if s_nickname is not None:
        search_items['nickname'] = '%' + s_nickname + '%'
        
    if s_phone is not None:
        search_items['phone'] = '%' + s_phone + '%'
        
    if s_id_card is not None:
        search_items['id_card'] = '%' + s_id_card + '%'
        
    if s_avatar is not None:
        search_items['avatar'] = '%' + s_avatar + '%'
        
    if s_name is not None:
        search_items['name'] = '%' + s_name + '%'
        
    if s_parent_id_history is not None:
        search_items['parent_id_history'] = '%' + s_parent_id_history + '%'
        

    if l_id is not None:
        values = l_id.split(',')
        values = [int(val) for val in values]
        set_items['id'] = values
        
    if l_username is not None:
        values = l_username.split(',')
        values = [val for val in values]
        set_items['username'] = values
        
    if l_email is not None:
        values = l_email.split(',')
        values = [val for val in values]
        set_items['email'] = values
        
    if l_open_id is not None:
        values = l_open_id.split(',')
        values = [val for val in values]
        set_items['open_id'] = values
        
    if l_union_id is not None:
        values = l_union_id.split(',')
        values = [val for val in values]
        set_items['union_id'] = values
        
    if l_password is not None:
        values = l_password.split(',')
        values = [val for val in values]
        set_items['password'] = values
        
    if l_nickname is not None:
        values = l_nickname.split(',')
        values = [val for val in values]
        set_items['nickname'] = values
        
    if l_phone is not None:
        values = l_phone.split(',')
        values = [val for val in values]
        set_items['phone'] = values
        
    if l_id_card is not None:
        values = l_id_card.split(',')
        values = [val for val in values]
        set_items['id_card'] = values
        
    if l_level_id is not None:
        values = l_level_id.split(',')
        values = [int(val) for val in values]
        set_items['level_id'] = values
        
    if l_status is not None:
        values = l_status.split(',')
        values = [int(val) for val in values]
        set_items['status'] = values
        
    if l_register_time is not None:
        values = l_register_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['register_time'] = values
        
    if l_avatar is not None:
        values = l_avatar.split(',')
        values = [val for val in values]
        set_items['avatar'] = values
        
    if l_invited_user_id is not None:
        values = l_invited_user_id.split(',')
        values = [int(val) for val in values]
        set_items['invited_user_id'] = values
        
    if l_coin is not None:
        values = l_coin.split(',')
        values = [int(val) for val in values]
        set_items['coin'] = values
        
    if l_gender is not None:
        values = l_gender.split(',')
        values = [int(val) for val in values]
        set_items['gender'] = values
        
    if l_last_active_time is not None:
        values = l_last_active_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['last_active_time'] = values
        
    if l_name is not None:
        values = l_name.split(',')
        values = [val for val in values]
        set_items['name'] = values
        
    if l_is_agree is not None:
        values = l_is_agree.split(',')
        values = [int(val) for val in values]
        set_items['is_agree'] = values
        
    if l_parent_id is not None:
        values = l_parent_id.split(',')
        values = [int(val) for val in values]
        set_items['parent_id'] = values
        
    if l_parent_id_history is not None:
        values = l_parent_id_history.split(',')
        values = [val for val in values]
        set_items['parent_id_history'] = values
        
    if l_level_one_time is not None:
        values = l_level_one_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['level_one_time'] = values
        
    if l_level_two_time is not None:
        values = l_level_two_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['level_two_time'] = values
        
    if l_level_three_time is not None:
        values = l_level_three_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['level_three_time'] = values
        
    if l_level_top_time is not None:
        values = l_level_top_time.split(',')
        values = [datetime.fromtimestamp(int(val)) for val in values]
        set_items['level_top_time'] = values
        
    if l_manage_id is not None:
        values = l_manage_id.split(',')
        values = [int(val) for val in values]
        set_items['manage_id'] = values
            
    
    data = d_db.filter_user(items, search_items, set_items, page, page_size)
    return FilterResUser(data=data, total=-1)
