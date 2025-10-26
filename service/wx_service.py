import logging
import requests
from fastapi import HTTPException
from pydantic import error_wrappers
from wechatpayv3 import WeChatPay, WeChatPayType
from config import WX, WXPAY, SUPPLIER
from model.third_part import ResWxLogin
import time

from pydantic import BaseModel

class WXBaseRes(BaseModel):
    errcode: int
    errmsg: str

class WXAccessToken(WXBaseRes):
    access_token: str
    expires_in: int
    refresh_token: str
    openid: str
    scope: str

class PhoneInfo(BaseModel):
    phoneNumber: str
    purePhoneNumber: str
    countryCode: str
    watermark: dict

class WXPhoneInfo(WXBaseRes):
    phone_info: PhoneInfo


def wx_login(code: str) -> ResWxLogin:
    """
    Login for openId and unionId
    param code: from client
    :return: model.third_part.ResWxLogin
    """
    wx_url = f'https://api.weixin.qq.com/sns/jscode2session?' \
             f'appid={WX.appId}&secret={WX.secret}&js_code={code}&grant_type=authorization_code'
    res = requests.get(wx_url)
    assert res.status_code == 200
    try:
        res = ResWxLogin.parse_obj(res.json())
    except error_wrappers.ValidationError:
        logging.error(f'wx_login error: {res.json()}')
        raise HTTPException(status_code=404, detail='登录失败，请检查code是否有效')
    return res


def supplier_login(code: str) -> ResWxLogin:
    """
    Login for openId and unionId
    param code: from client
    :return: model.third_part.ResWxLogin
    """
    wx_url = f'https://api.weixin.qq.com/sns/jscode2session?' \
             f'appid={SUPPLIER.appId}&secret={SUPPLIER.secret}&js_code={code}&grant_type=authorization_code'
    res = requests.get(wx_url)
    assert res.status_code == 200
    try:
        res = ResWxLogin.parse_obj(res.json())
    except error_wrappers.ValidationError:
        raise HTTPException(status_code=404, detail='登录失败，请检查code是否有效')
    return res


# 日志记录器，记录web请求和回调细节，便于调试排错。
# logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger("wxpay")

# wxpay = WeChatPay(
#    wechatpay_type=WeChatPayType.NATIVE,
#    mchid=WXPAY.MCHID,
#    private_key=WXPAY.PRIVATE_KEY,
#    cert_serial_no=WXPAY.CERT_SERIAL_NO,
#    apiv3_key=WXPAY.APIV3_KEY,
#    appid=WX.appId,
#    notify_url=WXPAY.NOTIFY_URL,
#    cert_dir=WXPAY.CERT_DIR,
#    logger=LOGGER,
#    partner_mode=False,
#    proxy=None)



wxpay = None

class WX_SDK:
    def __init__(self, appid, secret):
        self.appid = appid
        self.secret = secret
        self.access_token = None
        self.expires_time = None

    def get_access_token(self):
        if self.access_token is None or self.expires_time is None or self.expires_time < time.time():
            url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.appid}&secret={self.secret}'
            res = requests.get(url)
            assert res.status_code == 200
            res = res.json()
            self.access_token = res['access_token']
            #self.expires_time = time.time() + res['expires_in'] - 10
            self.expires_time = time.time() + 300
        return self.access_token

    def login(self, code):
        url = f'https://api.weixin.qq.com/sns/jscode2session?appid={self.appid}&secret={self.secret}&js_code={code}&grant_type=authorization_code'
        res = requests.get(url)
        assert res.status_code == 200
        res = res.json()
        return res

    def get_phone_number(self, code: str) -> WXPhoneInfo:
        url = f'https://api.weixin.qq.com/wxa/business/getuserphonenumber?access_token={self.get_access_token()}'
        res = requests.post(url, json={"code": code})
        assert res.status_code == 200
        return WXPhoneInfo.parse_obj(res.json())

    def get_getwxacode(self, width, path):
        post_url = f'https://api.weixin.qq.com/wxa/getwxacode?access_token={self.get_access_token()}'
        #pic_json = {"path": path, "width": width, "is_hyaline": True, "env_version": "trial"}
        pic_json = {"path": path, "width": width, "is_hyaline": True, "env_version": "release"}
        res = requests.post(post_url, json=pic_json)
        assert res.status_code == 200
        return res.content

    def get_getwxshorturl(self, page_url, page_title, is_permanent=False):
        post_url = f'https://api.weixin.qq.com/wxa/genwxashortlink?access_token={self.get_access_token()}'
        pic_json = {"page_url": page_url, "page_title": page_title, "is_permanent": is_permanent}
        res = requests.post(post_url, json=pic_json)
        assert res.status_code == 200
        return res.content

mall_wx_sdk = WX_SDK(WX.appId, WX.secret)
supplier_wx_sdk = WX_SDK(SUPPLIER.appId, SUPPLIER.secret)



