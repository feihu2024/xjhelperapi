from fastapi import Depends, FastAPI, Header, HTTPException, Request
from typing import List, Optional
import random
import string
from common import global_define

async def verify_token(request: Request,call_next, accept_encoding:Optional[str] = Header(None)):
    print('--------------------------header--------------------------')
    print(accept_encoding)
    print(request.headers)
    print(request.url)
    print(request.url.path)
    raise HTTPException(status_code=400, detail="x_token 未定义！")


#reversed dict
def reversed_dict(data:dict):
    re_data = {}
    for d in list(reversed(data.keys())):
        re_data[d] = data[d]
    return re_data

def get_randoms(num:int):
    token = string.ascii_letters + string.digits
    token = random.sample(token,num)
    token = ''.join(token)
    return token

def explain_headtoken(timeuser):
    mychar = global_define.valid_char
    token =  timeuser[int(len(timeuser)/2):] + timeuser[0:int(len(timeuser)/2)]
    for i, val in enumerate(mychar):
        if i==10:
            token = token.replace(val, ',')
        else:
            token = token.replace(val, str(i))
    return token

def get_headtoken(timeuser):
    token =  timeuser[int(len(timeuser)/2):] + timeuser[0:int(len(timeuser)/2)]
    return token
