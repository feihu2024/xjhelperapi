import os


class MYSQL:
    host: str = os.getenv('DB_HOST')
    port: str = os.getenv('DB_PORT')
    username: str = os.getenv('DB_USERNAME')
    password: str = os.getenv('DB_PASSWORD')
    db: str = os.getenv('DB')


class LOG:
    log_dir: str = './log/'


class SECRET:
    SECRET_KEY: str = '5ae4af4a62cf33a9e14924aaba6be405e5912accd1c393466f56f01f85d33c89'
    ALGORITHM: str = "HS256"
    VALID_TIME = 3600 * 6  #2个小时

class WX:
    appId: str = os.getenv('WX_APP_ID')
    secret: str = os.getenv('WX_SECRET')

class WXPAY:
    # 微信支付商户号，服务商模式下为服务商户号，即官方文档中的sp_mchid。
    MCHID = os.getenv('WX_MCH_ID')

    # 商户证书私钥，此文件不要放置在下面设置的CERT_DIR目录里。
    if os.getenv('WX_PRIVATE_KEY'):
        with open(os.getenv('WX_PRIVATE_KEY'), 'r') as f:
            PRIVATE_KEY = f.read()
    else:
        PRIVATE_KEY = None

    # 商户证书序列号
    CERT_SERIAL_NO = os.getenv('WX_CERT_SERIAL_NO')

    # API v3密钥， https://pay.weixin.qq.com/wiki/doc/apiv3/wechatpay/wechatpay3_2.shtml
    APIV3_KEY = os.getenv('WX_APIV3_KEY')

    # 回调地址，也可以在调用接口的时候覆盖。
    NOTIFY_URL = os.getenv('WX_NOTIFY_URL')

    # 微信支付平台证书缓存目录，初始调试的时候可以设为None，首次使用确保此目录为空目录。
    CERT_DIR = os.getenv('WX_CERT_DIR')


class DigitalChain:
    app_key: str = os.getenv('DC_KEY')
    app_secret: str = os.getenv('DC_SECRET')

class WL:
    app_code: str = os.getenv('WL_APP_CODE')


class DIRS:
    assets_dir: str = './assets'


class BaseURL:
    assets_url: str


class SUPPLIER:
    appId: str = os.getenv('SUPPLIER_APP_ID')
    secret: str = os.getenv('SUPPLIER_SECRET')


DOMAIN=os.getenv('DOMAIN', None)
