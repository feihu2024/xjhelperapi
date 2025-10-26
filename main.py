import logging
from setup.log import init_log
init_log()


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from urls import include_routers
from fastapi import Request
from fastapi import Response
import time
from fastapi import status
from fastapi import Depends
from fastapi import Header
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from dao import d_admin
from common import global_function, global_define
import re


app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

include_routers(app)

@app.on_event("startup")
async def startup():
    logging.info('Test log')
    pass


@app.on_event("shutdown")
async def shutdown():
    pass


@app.exception_handler(Exception)
async def value_error_handler(request, exc):
    error_detail = str(exc)  # 将detail转换为字符串形式
    return {"error": error_detail}

#@app.middleware("http")
#async def validate_users(request: Request, call_next):
#    start_time = time.time()
#    url_path = request.url.path
#    get_search = re.search(r'\'', str(request.query_params), flags=0)
#    get_search2 = re.search(r'%27', str(request.query_params), flags=0)
#    if get_search or get_search2:
#        response = JSONResponse(content={"status": 404, "message": "Bad way!!!"})
#        return response
#
#    if request.headers.get('kemaikemaisession') or url_path.lower().startswith('/mall/admin') or url_path.lower().startswith('/admin'):
#        if url_path.lower().startswith('/mall/admin/login') or url_path.lower().startswith('/mall/admin/login_out'):
#            response: Response = await call_next(request)
#            return response
#        else:
#            # print('------------------------------------------------')
#            # print(request.cookies)
#            if request.headers.get('kemaikemaisession'):
#                cookie_val = request.headers.get('kemaikemaisession')
#                new_cookie_val = d_admin.is_login(cookie_val)
#                if new_cookie_val:
#                    response: Response = await call_next(request)
#                    response.headers["kemaikemaisession"] = f"{new_cookie_val}"
#                    #response.set_cookie(key="kemaikemaisession", value=f"{new_cookie_val}")
#                    return response
#            response = JSONResponse(content={"status":404, "message": "please login"})
#            response.headers["access-control-allow-headers"] = "content-type,kemaikemaisession"
#            response.headers["Content-Type"] = "text/plain; charset=utf-8"
#            response.headers["access-control-allow-origin"] = "*"
#            response.headers["access-control-allow-methods"] = "DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT"
#            response.headers["Connection"] = "keep-alive"
#            return response
#    elif request.headers.get('Kmdeveloperssession'):
#        cookie_val = request.headers.get('Kmdeveloperssession')
#        valid_token = global_function.get_headtoken(cookie_val)
#        mychar = global_define.valid_char
#        for i in mychar:
#            valid_token = valid_token.replace(i,'')
#        if len(valid_token) == 0:
#            get_token = global_function.explain_headtoken(cookie_val)
#            pattern = re.compile(r'(\d+),(\d+)')
#            get_val = pattern.match(get_token)
#            if get_val:
#                response: Response = await call_next(request)
#                return response
#        else:
#            logging.info(f"Len>0：{cookie_val}，{valid_token}")
#
#        response = JSONResponse(content={"status": 404, "message": "Critical error!"})
#        response.headers["Content-Type"] = "text/plain; charset=utf-8"
#        return response
#    elif url_path.startswith('/assets/file') or url_path.startswith('/assets/image') or url_path.startswith('/wx/notify'):
#        response: Response = await call_next(request)
#        return response
#    else:
#        response = JSONResponse(content={"status": 404, "message": "Bad way!"})
#        response.headers["access-control-allow-headers"] = "content-type,kemaikemaisession"
#        response.headers["Content-Type"] = "text/plain; charset=utf-8"
#        response.headers["access-control-allow-origin"] = "*"
#        response.headers["access-control-allow-methods"] = "DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT"
#        response.headers["Connection"] = "keep-alive"
#
#    return response
#
    # 问题：await request.json() 之后的  await call_next(request)  无法执行
    # try:
    #     json_obj = await request.json()
    # except:
    #     json_obj = None
    # if json_obj:
    #     for k, v in json_obj.items():
    #         kv = str(k) + str(v)
    #         kv = kv.replace(" ", "")
    #         kv = kv.replace("\r\n", "\n")
    #         kv = kv.replace("\r", "\n")
    #         get_search = re.search(r'\'', kv, flags=0)
    #         get_search2 = re.search(r'%27', kv, flags=0)
    #         get_search3 = re.search(r'unionselect', kv, flags=0)
    #         if get_search or get_search2 or get_search3:
    #             response = JSONResponse(content={"status": 404, "message": "Bad way!!!!!"})
    #             return response

    #
    # start_time = time.time()
    # url_path = request.url.path
    # if url_path.lower().startswith('/mall/admin') or url_path.lower().startswith('/admin'):
    #     if url_path.lower().startswith('/mall/admin/login') or url_path.lower().startswith('/mall/admin/login_out'):
    #         response: Response = await call_next(request)
    #         return response
    #     else:
    #         # print('------------------------------------------------')
    #         # print(request.cookies)
    #         if request.headers.get('kemaikemaisession'):
    #             cookie_val = request.headers.get('kemaikemaisession')
    #             new_cookie_val = d_admin.is_login(cookie_val)
    #             if new_cookie_val:
    #                 response: Response = await call_next(request)
    #                 response.headers["kemaikemaisession"] = f"{new_cookie_val}"
    #                 #response.set_cookie(key="kemaikemaisession", value=f"{new_cookie_val}")
    #                 return response
    #         response = JSONResponse(content={"status":404, "message": "please login"})
    #         response.headers["access-control-allow-headers"] = "content-type,kemaikemaisession"
    #         response.headers["Content-Type"] = "text/plain; charset=utf-8"
    #         response.headers["access-control-allow-origin"] = "*"
    #         response.headers["access-control-allow-methods"] = "DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT"
    #         response.headers["Connection"] = "keep-alive"
    #         return response
    # else:
    #     response: Response = await call_next(request)
    #     # process_time = time.time() - start_time
    #     # response.headers["X-Process-Time"] = str(process_time)
    #     # response.status_code = status.HTTP_201_CREATED
    #     return response


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

