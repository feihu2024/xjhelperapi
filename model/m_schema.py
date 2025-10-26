from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from fastapi.exceptions import HTTPException


class CreateAddress(BaseModel):
    user_id: Optional[int] = Field(title='外键')
    province: Optional[str] = Field(title='省')
    city: Optional[str] = Field(title='市')
    area: Optional[str] = Field(title='区')
    street: Optional[str] = Field(title='街道')
    description: Optional[str] = Field(title='详细地址')
    default_: Optional[int] = Field(title='1:默认  0:非默认')
    consignee: Optional[str] = Field(title='收货人姓名')
    phone: Optional[str] = Field(title='收货人电话')

        
class SAddress(CreateAddress):
    id: int

    class Config:
        orm_mode = True

class Address(CreateAddress):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResAddress(BaseModel):
    data: List[SAddress]
    total: int
    
class CreateAdmin(BaseModel):
    username: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    level_id: Optional[int]
    password: Optional[str]
    id_card: Optional[str]
    gender: Optional[str]
    register_time: Optional[datetime]
    last_active_time: Optional[datetime]
    status: Optional[str]

        
class SAdmin(CreateAdmin):
    id: int

    class Config:
        orm_mode = True

class Admin(CreateAdmin):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResAdmin(BaseModel):
    data: List[SAdmin]
    total: int
    
class CreateBalance(BaseModel):
    user_id: Optional[int] = Field(title='外键')
    change: Optional[int] = Field(title='变动金额')
    balance: Optional[int] = Field(title='余额')
    type: Optional[str] = Field(title='类型')
    description: Optional[str] = Field(title='详细描述')
    create_time: Optional[datetime] = Field(title='创建时间')
    user_withdraw_id: Optional[int]
    operator_id: Optional[int] = Field(title='操作员ID')
    out_trade_no: Optional[str]
    good_id: Optional[str] = Field(title='收益商品id')
    good_title: Optional[str] = Field(title='收益商品标题名称')
    good_num: Optional[str] = Field(title='收益商品数量')

        
class SBalance(CreateBalance):
    id: int

    class Config:
        orm_mode = True

class Balance(CreateBalance):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResBalance(BaseModel):
    data: List[SBalance]
    total: int
    
class CreateBanner(BaseModel):
    image: Optional[str] = Field(title='图片url')
    title: Optional[str] = Field(title='主标题')
    subtitle: Optional[str] = Field(title='副标题')
    width: Optional[int] = Field(title='图片宽度')
    height: Optional[int] = Field(title='图片高度')
    create_time: Optional[datetime] = Field(title='创建时间')
    description: Optional[str] = Field(title='详情')
    good_id: Optional[int] = Field(title='商品id')
    ban_label: Optional[str] = Field(title='标签')
    type_id: Optional[int] = Field(title='0:banner   1:直通车')
    good_spec_id: Optional[int]

        
class SBanner(CreateBanner):
    id: int

    class Config:
        orm_mode = True

class Banner(CreateBanner):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResBanner(BaseModel):
    data: List[SBanner]
    total: int
    
class CreateCart(BaseModel):
    user_id: Optional[int] = Field(title='用户编号')
    good_id: Optional[int] = Field(title='商品编号')
    amount: Optional[int] = Field(title='购买数量')
    creat_time: Optional[datetime] = Field(title='创建时间')
    good_spec_id: Optional[int]

        
class SCart(CreateCart):
    id: int

    class Config:
        orm_mode = True

class Cart(CreateCart):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResCart(BaseModel):
    data: List[SCart]
    total: int
    
class CreateCategory(BaseModel):
    cname: Optional[str] = Field(title='分类名称')
    parent_category_id: Optional[int] = Field(title='上级分类id，默认0为顶级分类')

        
class SCategory(CreateCategory):
    id: int

    class Config:
        orm_mode = True

class Category(CreateCategory):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResCategory(BaseModel):
    data: List[SCategory]
    total: int
    
class CreateCity(BaseModel):
    cname: Optional[str]
    parid: Optional[int] = Field(title='上级地区id，默认0为顶级地区')
    status: Optional[int] = Field(title='地区状态')

        
class SCity(CreateCity):
    id: int

    class Config:
        orm_mode = True

class City(CreateCity):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResCity(BaseModel):
    data: List[SCity]
    total: int
    
class CreateCoin(BaseModel):
    user_id: Optional[int] = Field(title='外键')
    change: Optional[int] = Field(title='变动')
    coin: Optional[int] = Field(title='积分')
    type: Optional[str] = Field(title='类型')
    description: Optional[str] = Field(title='详细')
    create_time: Optional[datetime] = Field(title='创建时间')
    out_trade_no: Optional[str]

        
class SCoin(CreateCoin):
    id: int

    class Config:
        orm_mode = True

class Coin(CreateCoin):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResCoin(BaseModel):
    data: List[SCoin]
    total: int
    
class CreateCombo(BaseModel):
    good_id: Optional[int]
    title: Optional[str]
    amount: Optional[int]
    price: Optional[int]

        
class SCombo(CreateCombo):
    id: int

    class Config:
        orm_mode = True

class Combo(CreateCombo):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResCombo(BaseModel):
    data: List[SCombo]
    total: int
    
class CreateDeliveryRule(BaseModel):
    good_id: Optional[int] = Field(title='商品id')
    spec_id: Optional[int] = Field(title='规格id')
    province: Optional[str] = Field(title='省')
    city: Optional[str] = Field(title='市')
    area: Optional[str] = Field(title='区')
    is_reachable: Optional[int] = Field(title='是否可抵达    0：不可抵达     1：可抵达')
    delivery_fee: Optional[int] = Field(title='邮寄费用')

        
class SDeliveryRule(CreateDeliveryRule):
    id: int

    class Config:
        orm_mode = True

class DeliveryRule(CreateDeliveryRule):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResDeliveryRule(BaseModel):
    data: List[SDeliveryRule]
    total: int
    
class CreateExportFile(BaseModel):
    user_id: Optional[int] = Field(title='用户id')
    export_url: Optional[str] = Field(title='文件生成地址')
    type: Optional[str] = Field(title='类型')
    description: Optional[str] = Field(title='详细描述')
    create_time: Optional[datetime] = Field(title='创建时间')

        
class SExportFile(CreateExportFile):
    id: int

    class Config:
        orm_mode = True

class ExportFile(CreateExportFile):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResExportFile(BaseModel):
    data: List[SExportFile]
    total: int
    
class CreateFlashOrder(BaseModel):
    package_id: Optional[int] = Field(title='包id')
    status: Optional[int] = Field(title='状态   0：未付款    1：已付款    2：未发货    3：已发货    4：已签收     5：退货申请    6：退货中    7：已退货    8：取消交易')
    create_time: Optional[datetime] = Field(title='下单时间')
    paid_time: Optional[datetime] = Field(title='付款时间')
    user_id: Optional[int] = Field(title='用户id')
    number: Optional[int] = Field(title='商品数量')
    flash_price: Optional[int] = Field(title='秒杀单价')
    flash_cost: Optional[int] = Field(title='秒杀成本')
    out_trade_no: Optional[str]
    paid_amount: Optional[int] = Field(title='支付金额')
    paid_balance: Optional[int] = Field(title='余额支付金额')
    single_status: Optional[int] = Field(title='是否单份代卖')
    sold: Optional[int] = Field(title='已售出商品数量')
    whole_status: Optional[int] = Field(title='是否整份代码,暂时废弃,统一启用single_status字段判断')
    spec_id: Optional[int] = Field(title='规格id')
    put_on_time: Optional[datetime] = Field(title='上架时间,计算收益时使用')
    detail: Optional[str] = Field(title='订单备注,+=更新')
    is_assign_income: Optional[int] = Field(title='是否分配收益')
    complete_time: Optional[datetime] = Field(title='订单完结时间')
    return_sold: Optional[int] = Field(title='已提货数量')

        
class SFlashOrder(CreateFlashOrder):
    id: int

    class Config:
        orm_mode = True

class FlashOrder(CreateFlashOrder):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResFlashOrder(BaseModel):
    data: List[SFlashOrder]
    total: int
    
class CreateFlashOrderReturn(BaseModel):
    user_id: Optional[int] = Field(title='用户id')
    income_days: Optional[int] = Field(title='剩余秒杀退货收益天数')
    latest_time: Optional[datetime] = Field(title='最近一次退货时间')
    latest_income_user: Optional[int] = Field(title='最近一次退货收益')
    latest_income_layer: Optional[int] = Field(title='最近一次退货层级收益')
    latest_income_toper: Optional[int] = Field(title='最近一次退货见点收益')
    latest_income_groupsir: Optional[int] = Field(title='最近一次退货团长收益')

        
class SFlashOrderReturn(CreateFlashOrderReturn):
    id: int = Field(title='主键id')

    class Config:
        orm_mode = True

class FlashOrderReturn(CreateFlashOrderReturn):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResFlashOrderReturn(BaseModel):
    data: List[SFlashOrderReturn]
    total: int
    
class CreatePackageOrderStatus(BaseModel):
    title: Optional[str]

        
class SPackageOrderStatus(CreatePackageOrderStatus):
    id: int

    class Config:
        orm_mode = True

class PackageOrderStatus(CreatePackageOrderStatus):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResPackageOrderStatus(BaseModel):
    data: List[SPackageOrderStatus]
    total: int
    
class CreateGood(BaseModel):
    name: Optional[str] = Field(title='产品名称')
    is_flash_sale: Optional[int] = Field(title='是否参加秒杀')
    category_id: Optional[int] = Field(title='大类别ID   关联t_category表')
    type: Optional[int] = Field(title='0:虚拟(卡券） 1:实体')
    num_sale: Optional[int] = Field(title='销量')
    image_url: Optional[str] = Field(title='主图片url')
    priority: Optional[int] = Field(title='优先级  越小越好')
    add_coin: Optional[int] = Field(title='购买后给予多少积分')
    model_id: Optional[int] = Field(title='模型id  如海底捞卡券属于火锅模型')
    expired_time: Optional[datetime] = Field(title='过期时间')
    parent_good_id: Optional[int] = Field(title='如果是套餐产品，这个是父商品id')
    title: Optional[str] = Field(title='主标题        如糖醋鱼的标题是美食')
    subtitle: Optional[str] = Field(title='副标题')
    stock_cordon: Optional[int] = Field(title='库存警戒线')
    status: Optional[int] = Field(title='0: 下架   1: 上架 ')
    details: Optional[str] = Field(title='商品详情描述')
    supplier_id: Optional[int] = Field(title='供应商id')
    share_ratio: Optional[int] = Field(title='分成比例')
    create_time: Optional[datetime] = Field(title='添加时间')
    last_update_time: Optional[datetime] = Field(title='最后修改时间')
    saleable: Optional[int] = Field(title='0：下架  1：上架')
    click_count: Optional[int] = Field(title='点击量')
    transmit_count: Optional[int] = Field(title='转发量')
    coinable: Optional[int] = Field(title='0:不可以使用积分      1:可使用积分')
    price_line: Optional[int] = Field(title='商品划价线')
    introducer_id: Optional[int] = Field(title='介绍人id')
    sell_high: Optional[int] = Field(title='最高售价')
    sell_low: Optional[int] = Field(title='最低售价')
    cost_high: Optional[int] = Field(title='最高成本')
    cost_low: Optional[int] = Field(title='最低成本')
    display: Optional[int] = Field(title='显示位置          1:顶部       0:底部')
    coinable_number: Optional[int] = Field(title='积分可用数')
    is_package: Optional[int]
    fake_owner_name: Optional[str] = Field(title='临时数据   负责人名称')
    fake_owner_phone: Optional[str] = Field(title='临时数据   负责人电话')
    unavailable_date: Optional[str] = Field(title='不可用时间')
    available_time: Optional[str]
    usage_rule: Optional[str]
    refund_rule: Optional[str]
    order_expired_time: Optional[datetime] = Field(title='订单过期时间，用户下单后这个日期会被复制code_expired_time，后期修改不影响已下单过期时间')
    cover_url: Optional[str] = Field(title='封面图片url')
    video_url: Optional[str] = Field(title='视频url')

        
class SGood(CreateGood):
    id: int

    class Config:
        orm_mode = True

class Good(CreateGood):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResGood(BaseModel):
    data: List[SGood]
    total: int
    
class CreateGoodCategory(BaseModel):
    title: Optional[str] = Field(title='小类别名称   比如火锅、烧烤')
    general_id: Optional[int] = Field(title='大类id     关联t_category表')

        
class SGoodCategory(CreateGoodCategory):
    id: int

    class Config:
        orm_mode = True

class GoodCategory(CreateGoodCategory):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResGoodCategory(BaseModel):
    data: List[SGoodCategory]
    total: int
    
class CreateGoodImage(BaseModel):
    image: Optional[str] = Field(title='商品图片url')
    good_id: Optional[int] = Field(title='商品id')

        
class SGoodImage(CreateGoodImage):
    id: int

    class Config:
        orm_mode = True

class GoodImage(CreateGoodImage):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResGoodImage(BaseModel):
    data: List[SGoodImage]
    total: int
    
class CreateGoodIntroducer(BaseModel):
    name: Optional[str] = Field(title='介绍人名称')
    phone: Optional[str] = Field(title='介绍人电话')
    address: Optional[str] = Field(title='介绍人住址')
    id_card: Optional[str] = Field(title='介绍人身份证')

        
class SGoodIntroducer(CreateGoodIntroducer):
    id: int

    class Config:
        orm_mode = True

class GoodIntroducer(CreateGoodIntroducer):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResGoodIntroducer(BaseModel):
    data: List[SGoodIntroducer]
    total: int
    
class CreateGoodModel(BaseModel):
    model: Optional[str]

        
class SGoodModel(CreateGoodModel):
    id: int

    class Config:
        orm_mode = True

class GoodModel(CreateGoodModel):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResGoodModel(BaseModel):
    data: List[SGoodModel]
    total: int
    
class CreateGoodPackage(BaseModel):
    number: Optional[str] = Field(title='商品份数')
    price: Optional[str] = Field(title='单价')
    title: Optional[str] = Field(title='商品标题')
    create_time: Optional[datetime] = Field(title='创建时间')
    good_id: Optional[int] = Field(title='商品id')

        
class SGoodPackage(CreateGoodPackage):
    id: int

    class Config:
        orm_mode = True

class GoodPackage(CreateGoodPackage):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResGoodPackage(BaseModel):
    data: List[SGoodPackage]
    total: int
    
class CreateGoodPerson(BaseModel):
    good_id: Optional[int] = Field(title='商品编号')
    person_id: Optional[int] = Field(title='人数id')

        
class SGoodPerson(CreateGoodPerson):
    id: int

    class Config:
        orm_mode = True

class GoodPerson(CreateGoodPerson):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResGoodPerson(BaseModel):
    data: List[SGoodPerson]
    total: int
    
class CreateGoodPersonState(BaseModel):
    title: Optional[str] = Field(title='使用人数')

        
class SGoodPersonState(CreateGoodPersonState):
    id: int

    class Config:
        orm_mode = True

class GoodPersonState(CreateGoodPersonState):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResGoodPersonState(BaseModel):
    data: List[SGoodPersonState]
    total: int
    
class CreateGoodPriority(BaseModel):
    title: Optional[str]

        
class SGoodPriority(CreateGoodPriority):
    id: int

    class Config:
        orm_mode = True

class GoodPriority(CreateGoodPriority):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResGoodPriority(BaseModel):
    data: List[SGoodPriority]
    total: int
    
class CreateGoodRule(BaseModel):
    good_id: Optional[int] = Field(title='商品id')
    create_time: Optional[datetime] = Field(title='创建时间')
    validate_day: Optional[str] = Field(title='有效期    例如： 2023.04.19   至  2024.04.19')
    unuseful_day: Optional[str] = Field(title='不可用日期     例如： 2023.05.01 至 2024.05.07')
    useful_time: Optional[str] = Field(title='可用时间      例如：24小时可用       14:00-20:00可用等')
    use_rule: Optional[str] = Field(title='使用规则')
    return_rule: Optional[str] = Field(title='退货规则')
    room: Optional[int] = Field(title='0:不可使用包间     1：可使用包间')
    title: Optional[str]
    value: Optional[str]

        
class SGoodRule(CreateGoodRule):
    id: int

    class Config:
        orm_mode = True

class GoodRule(CreateGoodRule):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResGoodRule(BaseModel):
    data: List[SGoodRule]
    total: int
    
class CreateGoodSpec(BaseModel):
    good_id: Optional[int] = Field(title='商品id')
    price: Optional[int] = Field(title='售价')
    cost: Optional[int] = Field(title='成本')
    value: Optional[str] = Field(title='规格的值    例如：糖醋里脊的甜口、酸口')
    stock: Optional[int] = Field(title='库存')
    price_line: Optional[int] = Field(title='划价线')
    image: Optional[str] = Field(title='图片url')
    is_sub_good: Optional[int]
    num_sale: Optional[int] = Field(title='销量')
    parent_fee: Optional[int] = Field(title='分层奖，上一级的奖励')
    top_fee: Optional[int] = Field(title='见点奖，第一高级会员分成')
    recommender_fee: Optional[int] = Field(title='售出奖，推荐人的奖励')
    supplier_fee: Optional[int] = Field(title='供货收益')
    lower_num_people: Optional[int] = Field(title='人数下限')
    upper_num_people: Optional[int] = Field(title='人数上限')
    room: Optional[str] = Field(title='包间')
    post: Optional[str]
    status: Optional[int] = Field(title='0: 下架   1: 上架 ')
    share_fee: Optional[int] = Field(title='分享商品收益')
    is_default: Optional[int] = Field(title='是否默认规格')
    spec_num: Optional[str] = Field(title='商品规格编号')
    profit: Optional[int] = Field(title='产品利润')
    eqlevel_fee: Optional[int] = Field(title='平级奖 直推关系下见点收益的推荐人收益')

        
class SGoodSpec(CreateGoodSpec):
    id: int

    class Config:
        orm_mode = True

class GoodSpec(CreateGoodSpec):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResGoodSpec(BaseModel):
    data: List[SGoodSpec]
    total: int
    
class CreateGoodSpecCombo(BaseModel):
    good_spec_id: Optional[int]
    value: Optional[str]
    price: Optional[int]
    amount: Optional[str] = Field(title='数量')

        
class SGoodSpecCombo(CreateGoodSpecCombo):
    id: int

    class Config:
        orm_mode = True

class GoodSpecCombo(CreateGoodSpecCombo):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResGoodSpecCombo(BaseModel):
    data: List[SGoodSpecCombo]
    total: int
    
class CreateGoodSpecDetail(BaseModel):
    good_spec_id: Optional[int]
    detail: Optional[str]

        
class SGoodSpecDetail(CreateGoodSpecDetail):
    id: int

    class Config:
        orm_mode = True

class GoodSpecDetail(CreateGoodSpecDetail):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResGoodSpecDetail(BaseModel):
    data: List[SGoodSpecDetail]
    total: int
    
class CreateGoodSpecImage(BaseModel):
    spec_id: Optional[int] = Field(title='规格id')
    image: Optional[str] = Field(title='图片url')

        
class SGoodSpecImage(CreateGoodSpecImage):
    id: int

    class Config:
        orm_mode = True

class GoodSpecImage(CreateGoodSpecImage):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResGoodSpecImage(BaseModel):
    data: List[SGoodSpecImage]
    total: int
    
class CreateGoodStore(BaseModel):
    good_id: Optional[int]
    store_id: Optional[int]

        
class SGoodStore(CreateGoodStore):
    id: int

    class Config:
        orm_mode = True

class GoodStore(CreateGoodStore):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResGoodStore(BaseModel):
    data: List[SGoodStore]
    total: int
    
class CreateGoodText(BaseModel):
    good_id: Optional[int] = Field(title='商品id')
    description: Optional[str] = Field(title='图文详情   图片和文字放在一起')
    create_time: Optional[datetime] = Field(title='创建时间')

        
class SGoodText(CreateGoodText):
    id: int

    class Config:
        orm_mode = True

class GoodText(CreateGoodText):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResGoodText(BaseModel):
    data: List[SGoodText]
    total: int
    
class CreateGoodType(BaseModel):
    type: Optional[str]

        
class SGoodType(CreateGoodType):
    id: int

    class Config:
        orm_mode = True

class GoodType(CreateGoodType):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResGoodType(BaseModel):
    data: List[SGoodType]
    total: int
    
class CreateGroupsir(BaseModel):
    user_id: Optional[int] = Field(title='关联t_user表id')
    parent_id: Optional[int] = Field(title='0:表示团长，非0表示下级成员')
    register_time: Optional[datetime] = Field(title='成团时间和入团')
    status: Optional[int] = Field(title='0: 启用   1: 暂停  -1：出团或解散')
    is_empower: Optional[int] = Field(title='0: 未授权   1:已授权（可以使用所有商品秒杀包）')
    notes: Optional[str] = Field(title='团员备注')

        
class SGroupsir(CreateGroupsir):
    id: int = Field(title='团长id')

    class Config:
        orm_mode = True

class Groupsir(CreateGroupsir):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResGroupsir(BaseModel):
    data: List[SGroupsir]
    total: int
    
class CreateLevel(BaseModel):
    title: Optional[str]

        
class SLevel(CreateLevel):
    id: int

    class Config:
        orm_mode = True

class Level(CreateLevel):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResLevel(BaseModel):
    data: List[SLevel]
    total: int
    
class CreateLockBalance(BaseModel):
    user_id: Optional[int] = Field(title='外键')
    change: Optional[int] = Field(title='变动')
    lock_balance: Optional[int] = Field(title='锁定金额')
    type: Optional[str] = Field(title='类型')
    description: Optional[str] = Field(title='描述')
    create_time: Optional[datetime] = Field(title='创建时间')
    out_trade_no: Optional[str]

        
class SLockBalance(CreateLockBalance):
    id: int

    class Config:
        orm_mode = True

class LockBalance(CreateLockBalance):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResLockBalance(BaseModel):
    data: List[SLockBalance]
    total: int
    
class CreateModel(BaseModel):
    product_id: Optional[int]

        
class SModel(CreateModel):
    id: int

    class Config:
        orm_mode = True

class Model(CreateModel):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResModel(BaseModel):
    data: List[SModel]
    total: int
    
class CreateOrder(BaseModel):
    good_id: Optional[int] = Field(title='商品id')
    paider_id: Optional[int] = Field(title='付款人id')
    sale_price: Optional[int] = Field(title='售价      记录客户购买时的商品价格（因为价格可能变动）')
    cost_price: Optional[int] = Field(title='成本       记录客户购买时的商品成本（因为成本可能变动）')
    create_time: Optional[datetime] = Field(title='创建时间    与支付时间有本质区别')
    paid_time: Optional[datetime] = Field(title='支付时间')
    status_id: Optional[int] = Field(title='状态id        对应未发货、已发货、已完成')
    number: Optional[int] = Field(title='商品数量')
    consignee_address: Optional[str] = Field(title='收货人地址')
    consignee_phone: Optional[str] = Field(title='收货人联系电话')
    store_id: Optional[int] = Field(title='店铺id')
    paid_amount: Optional[int] = Field(title='实际第三方支付的金额     用于标记除客户账户以外支付的金额（比如微信、银行卡)')
    delivery_fee: Optional[int] = Field(title='运费金额')
    spec_id: Optional[int] = Field(title='规格编号')
    paid_coin: Optional[int] = Field(title='实际支付的积分      用于标记客户账户内支付的积分')
    delivery_track_code: Optional[str] = Field(title='第三方物流单号  比如顺丰的单号')
    paid_channel_id: Optional[int] = Field(title='第三方支付渠道    比如微信支付  银行卡支付等')
    consignee_name: Optional[str] = Field(title='收货人名称')
    delivery_time: Optional[datetime] = Field(title='发货时间')
    good_name: Optional[str] = Field(title='商品名称    记录客户购买时的商品名称（因为名称可能变动）')
    paid_track_code: Optional[str] = Field(title='第三方支付流水号    比如微信支付提供的支付编码')
    paider_name: Optional[str] = Field(title='付款人姓名')
    paider_phone: Optional[str] = Field(title='付款人电话')
    paider_address: Optional[str] = Field(title='付款人地址')
    supplier_id: Optional[int] = Field(title='商家id')
    paid_balance: Optional[int] = Field(title='实际支付的余额         用于标记客户账户内支付的余额')
    paid_lock_balance: Optional[int] = Field(title='实际支付的锁定额        用于标记客户账户内支付的锁定额')
    delivery_company: Optional[str] = Field(title='第三方物流公司   比如圆通、顺丰等')
    complete_time: Optional[datetime] = Field(title='订单完结时间')
    use_balance: Optional[int] = Field(title='是否使用余额')
    use_coin: Optional[int] = Field(title='是否使用积分')
    consignee_province: Optional[str]
    consignee_description: Optional[str]
    consignee_city: Optional[str]
    consignee_area: Optional[str]
    consignee_street: Optional[str]
    out_trade_no: Optional[str] = Field(title='商户单号')
    code: Optional[str] = Field(title='虚拟消费券的code')
    code_expired_time: Optional[datetime] = Field(title='虚拟消费券的过期时间')
    is_display: Optional[int] = Field(title='是否可以展示')
    recommender_id: Optional[int] = Field(title='推荐人Id')
    detail: Optional[str] = Field(title='订单备注,+=更新')
    is_assign_income: Optional[int] = Field(title='是否分配收益')
    parent_uid: Optional[int] = Field(title='层级收益人id')
    top_uid: Optional[int] = Field(title='顶级收益人id')
    invited_uid: Optional[int] = Field(title='直推收益人id')
    supplier_uid: Optional[int] = Field(title='供货介绍收益人id')
    eqlevel_uid: Optional[int] = Field(title='平级奖收益人id')

        
class SOrder(CreateOrder):
    id: int = Field(title='订单id')

    class Config:
        orm_mode = True

class Order(CreateOrder):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResOrder(BaseModel):
    data: List[SOrder]
    total: int
    
class CreateOrderBatch(BaseModel):
    create_time: Optional[datetime]

        
class SOrderBatch(CreateOrderBatch):
    id: int

    class Config:
        orm_mode = True

class OrderBatch(CreateOrderBatch):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResOrderBatch(BaseModel):
    data: List[SOrderBatch]
    total: int
    
class CreateOrderCheck(BaseModel):
    order_id: Optional[int] = Field(title='订单id')
    check_num: Optional[int] = Field(title='核销数量')
    check_time: Optional[datetime] = Field(title='核销时间')
    worker_id: Optional[int] = Field(title='核销人id，对应店铺的人员')
    check_amount: Optional[int] = Field(title='核销金额')

        
class SOrderCheck(CreateOrderCheck):
    id: int

    class Config:
        orm_mode = True

class OrderCheck(CreateOrderCheck):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResOrderCheck(BaseModel):
    data: List[SOrderCheck]
    total: int
    
class CreateOrderReturn(BaseModel):
    returner_name: Optional[str] = Field(title='退款人姓名   对应订单表的付款人')
    returner_phone: Optional[str] = Field(title='退款人电话   对应订单表的付款人')
    returner_address: Optional[str] = Field(title='退款人地址   对应订单表的付款人')
    delivery_fee: Optional[int] = Field(title='退货运费')
    return_amount: Optional[int] = Field(title='第三方支付退款额度    比如退还微信10元')
    return_submit_time: Optional[datetime] = Field(title='退货申请时间')
    return_reason: Optional[str] = Field(title='退货原因')
    order_id: Optional[int] = Field(title='订单编号     关联订单表')
    good_id: Optional[int] = Field(title='商品id')
    return_num: Optional[int] = Field(title='退货商品数量')
    store_id: Optional[int] = Field(title='店铺id')
    return_delivery_track_code: Optional[str] = Field(title='第三方退货物流单号')
    status_id: Optional[int] = Field(title='状态id     对应退款协商中、未处理、已退货')
    consignee_name: Optional[str] = Field(title='收货人姓名')
    consignee_phone: Optional[str] = Field(title='收货人电话')
    consignee_address: Optional[str] = Field(title='收货人地址')
    return_balance: Optional[int] = Field(title='客户账户余额退还额度')
    return_lock_balance: Optional[int] = Field(title='客户账户锁定额退还额度')
    return_coin: Optional[int] = Field(title='客户账户积分退还额度')
    return_delivery_company: Optional[str] = Field(title='第三方物流公司')
    return_paid_track_code: Optional[str] = Field(title='第三方退款流水号')

        
class SOrderReturn(CreateOrderReturn):
    id: int = Field(title='退货编号')

    class Config:
        orm_mode = True

class OrderReturn(CreateOrderReturn):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResOrderReturn(BaseModel):
    data: List[SOrderReturn]
    total: int
    
class CreateOrderReturnState(BaseModel):
    state: Optional[str] = Field(title='退换货状态')

        
class SOrderReturnState(CreateOrderReturnState):
    id: int

    class Config:
        orm_mode = True

class OrderReturnState(CreateOrderReturnState):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResOrderReturnState(BaseModel):
    data: List[SOrderReturnState]
    total: int
    
class CreateOrderReturnType(BaseModel):
    type: Optional[str] = Field(title='类型')

        
class SOrderReturnType(CreateOrderReturnType):
    id: int

    class Config:
        orm_mode = True

class OrderReturnType(CreateOrderReturnType):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResOrderReturnType(BaseModel):
    data: List[SOrderReturnType]
    total: int
    
class CreateOrderSource(BaseModel):
    order_id: Optional[int] = Field(title='订单id')
    source_id: Optional[int] = Field(title='订单来源，来再t_flash_order.id，如果是空或者-1表示平台')
    amount: Optional[int] = Field(title='商品数量')
    create_time: Optional[datetime] = Field(title='创建时间')
    order_user_id: Optional[int] = Field(title='订单购买用户id')
    package_user_id: Optional[int] = Field(title='秒杀包用户id')

        
class SOrderSource(CreateOrderSource):
    id: int

    class Config:
        orm_mode = True

class OrderSource(CreateOrderSource):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResOrderSource(BaseModel):
    data: List[SOrderSource]
    total: int
    
class CreateOrderState(BaseModel):
    state: Optional[str] = Field(title='订单状态')
    belong: Optional[str] = Field(title='所属订单类别   比如发货  退货')

        
class SOrderState(CreateOrderState):
    id: int

    class Config:
        orm_mode = True

class OrderState(CreateOrderState):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResOrderState(BaseModel):
    data: List[SOrderState]
    total: int
    
class CreatePackage(BaseModel):
    good_id: Optional[int] = Field(title='产品id')
    amount: Optional[int] = Field(title='份数;the number of good in one amount一个包包含的产品的数量')
    flash_sale_price: Optional[int] = Field(title='秒杀价格;in cent,秒杀价格')
    num: Optional[int] = Field(title='包个数;一共有多少个包')
    stock: Optional[int] = Field(title='剩余包数量')
    seller_id: Optional[int] = Field(title='发布商品的卖家，如果id为空或者0，则为官方卖家')
    spec_id: Optional[int] = Field(title='规格id')
    share_fee: Optional[int] = Field(title='让利金额')
    status: Optional[int] = Field(title='状态：-1删除, 默认0/null正常')

        
class SPackage(CreatePackage):
    id: int

    class Config:
        orm_mode = True

class Package(CreatePackage):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResPackage(BaseModel):
    data: List[SPackage]
    total: int
    
class CreatePackageExpress(BaseModel):
    flash_order_id: Optional[int]
    status: Optional[int] = Field(title='1: 申请中  2:  已发货  3: 拒绝发货退款  4：已签收  5:未使用  6:已使用')
    address_id: Optional[int] = Field(title='邮寄地址id')
    amount: Optional[int] = Field(title='邮寄数量')
    express_num: Optional[str] = Field(title='物流号')
    apply_time: Optional[datetime] = Field(title='申请发货时间')
    delivery_time: Optional[datetime] = Field(title='发货时间')
    complete_time: Optional[datetime] = Field(title='签收或完成时间')
    detail: Optional[str] = Field(title='订单备注,+=更新')

        
class SPackageExpress(CreatePackageExpress):
    id: int

    class Config:
        orm_mode = True

class PackageExpress(CreatePackageExpress):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResPackageExpress(BaseModel):
    data: List[SPackageExpress]
    total: int
    
class CreatePackageExpressStatus(BaseModel):
    title: Optional[str]

        
class SPackageExpressStatus(CreatePackageExpressStatus):
    id: int

    class Config:
        orm_mode = True

class PackageExpressStatus(CreatePackageExpressStatus):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResPackageExpressStatus(BaseModel):
    data: List[SPackageExpressStatus]
    total: int
    
class CreatePackageTime(BaseModel):
    start_time: Optional[int] = Field(title='开始时间;9*3600表示9:00')
    end_time: Optional[int] = Field(title='结束时间;以秒为单位')

        
class SPackageTime(CreatePackageTime):
    id: int

    class Config:
        orm_mode = True

class PackageTime(CreatePackageTime):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResPackageTime(BaseModel):
    data: List[SPackageTime]
    total: int
    
class CreatePackageTimePair(BaseModel):
    package_id: Optional[int]
    package_time_id: Optional[int]
    status: Optional[int] = Field(title='状态; 0: 未激活, 1: 激活')
    package_num: Optional[int] = Field(title='此时段秒杀包库存')

        
class SPackageTimePair(CreatePackageTimePair):
    id: int

    class Config:
        orm_mode = True

class PackageTimePair(CreatePackageTimePair):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResPackageTimePair(BaseModel):
    data: List[SPackageTimePair]
    total: int
    
class CreatePayChannel(BaseModel):
    type: Optional[str] = Field(title='支付方式')

        
class SPayChannel(CreatePayChannel):
    id: int

    class Config:
        orm_mode = True

class PayChannel(CreatePayChannel):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResPayChannel(BaseModel):
    data: List[SPayChannel]
    total: int
    
class CreatePlatformLaw(BaseModel):
    create_time: Optional[datetime] = Field(title='创建时间')
    admin_id: Optional[int] = Field(title='操作员id')
    law: Optional[str] = Field(title='法律文本 用户协议')
    privacy: Optional[str] = Field(title='隐私协议')
    purchase: Optional[str] = Field(title='购买协议')
    flash_law: Optional[str] = Field(title='批发协议')
    withdraw_law: Optional[str] = Field(title='提现规则')

        
class SPlatformLaw(CreatePlatformLaw):
    id: int

    class Config:
        orm_mode = True

class PlatformLaw(CreatePlatformLaw):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResPlatformLaw(BaseModel):
    data: List[SPlatformLaw]
    total: int
    
class CreatePlatformNotice(BaseModel):
    title: Optional[str] = Field(title='通知内容')
    create_time: Optional[datetime] = Field(title='创建时间')
    admin_id: Optional[int] = Field(title='添加人id    对应哪个管理员')

        
class SPlatformNotice(CreatePlatformNotice):
    id: int

    class Config:
        orm_mode = True

class PlatformNotice(CreatePlatformNotice):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResPlatformNotice(BaseModel):
    data: List[SPlatformNotice]
    total: int
    
class CreatePoster(BaseModel):
    user_id: Optional[int] = Field(title='用户id')
    poster_url: Optional[str] = Field(title='海报文件地址')
    status: Optional[str] = Field(title='状态')
    description: Optional[str] = Field(title='描述')
    create_time: Optional[datetime] = Field(title='创建时间')

        
class SPoster(CreatePoster):
    id: int

    class Config:
        orm_mode = True

class Poster(CreatePoster):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResPoster(BaseModel):
    data: List[SPoster]
    total: int
    
class CreateSetting(BaseModel):
    recommend_num: Optional[int] = Field(title='定义推荐系升级人数')
    flash_order_income: Optional[float] = Field(title='定义秒杀产品24小时停留收益比千分之')
    tuan_order_income: Optional[float] = Field(title='定义团长秒杀产品收益比（千分之）')
    flash_order_max: Optional[int] = Field(title='秒杀用户持单量限制(未完成出售订单)')
    flash_order_money_max: Optional[int] = Field(title='秒杀用户持单总金额限制(未完成出售订单)')
    flash_order_active_user: Optional[int] = Field(title='秒杀并支付多少单，普通会员晋升活跃会员')
    consume_money_active_user: Optional[int] = Field(title='完成商品订单达到指定额度，普通会员晋升活跃会员')
    many_high_user: Optional[int] = Field(title='直推多少个活跃会员，晋升高级会员')
    many_top_user: Optional[int] = Field(title='直推多少个高级会员，晋升顶级会员')
    flash_order_income_retio: Optional[float] = Field(title='秒杀人退货收益比（千分之）')
    flash_order_income_layer: Optional[float] = Field(title='秒杀人退货层级收益比（百分之）')
    flash_order_income_toper: Optional[float] = Field(title='秒杀人退货顶级收益比(百分比)')
    flash_order_income_groupsir: Optional[float] = Field(title='秒杀人退货团长收益比(百分比)')
    flash_order_owner_times: Optional[int] = Field(title='秒杀包持有人退货时间限制（小时）')
    parent_user_limit: Optional[int] = Field(title='推广人升级顶级时，留给原上级的人数')
    flash_order_income_subsidy: Optional[int] = Field(title='团队补贴,秒杀的退款收益， 给直接推荐人 的一份')

        
class SSetting(CreateSetting):
    id: int = Field(title='标识id，修改时从1开始对应recommend_num之后的字段')

    class Config:
        orm_mode = True

class Setting(CreateSetting):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResSetting(BaseModel):
    data: List[SSetting]
    total: int
    
class CreateStore(BaseModel):
    name: Optional[str] = Field(title='店铺名称')
    phone: Optional[str] = Field(title='电话')
    province: Optional[str] = Field(title='省份')
    city: Optional[str] = Field(title='城市')
    area: Optional[str] = Field(title='区域')
    street: Optional[str] = Field(title='街道')
    address: Optional[str] = Field(title='详细地址')
    status: Optional[int] = Field(title='店铺状态')
    owner: Optional[str] = Field(title='店铺负责人')
    recommender_id: Optional[int] = Field(title='推荐人id   对应某个用户')
    register_time: Optional[datetime] = Field(title='注册时间')
    type: Optional[int] = Field(title='商家类型    供应商或店铺等')
    expired_time: Optional[datetime] = Field(title='合同到期时间')
    open_time: Optional[int] = Field(title='开始营业时间   9*3600表示9:00')
    close_time: Optional[int] = Field(title='结束营业时间   9*3600表示9:00，以秒为单位')
    image: Optional[str] = Field(title='商家门头图片')
    owner_id: Optional[int] = Field(title='负责人id')
    supplier_id: Optional[int] = Field(title='商家id')
    company_name: Optional[str] = Field(title='公司名称')
    reject_reason: Optional[str] = Field(title='驳回原因')
    reject_time: Optional[datetime] = Field(title='驳回时间')
    reject_admin_id: Optional[int] = Field(title='管理员id   记录是谁驳回的')
    is_default: Optional[int] = Field(title='默认店铺')

        
class SStore(CreateStore):
    id: int

    class Config:
        orm_mode = True

class Store(CreateStore):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResStore(BaseModel):
    data: List[SStore]
    total: int
    
class CreateStoreAmount(BaseModel):
    type: Optional[int] = Field(title='变动类型')
    change: Optional[int] = Field(title='资金变动额      +10    -5')
    amount: Optional[int] = Field(title='资金总额')
    create_time: Optional[datetime] = Field(title='创建时间')
    store_id: Optional[int] = Field(title='店铺id')

        
class SStoreAmount(CreateStoreAmount):
    id: int

    class Config:
        orm_mode = True

class StoreAmount(CreateStoreAmount):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResStoreAmount(BaseModel):
    data: List[SStoreAmount]
    total: int
    
class CreateStoreChangeType(BaseModel):
    type: Optional[str] = Field(title='资金变动类型')

        
class SStoreChangeType(CreateStoreChangeType):
    id: int

    class Config:
        orm_mode = True

class StoreChangeType(CreateStoreChangeType):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResStoreChangeType(BaseModel):
    data: List[SStoreChangeType]
    total: int
    
class CreateStoreContract(BaseModel):
    contract: Optional[str] = Field(title='合同照片')
    store_id: Optional[int] = Field(title='商家编号')
    create_time: Optional[datetime] = Field(title='创建时间')
    expired_time: Optional[datetime] = Field(title='到期时间')

        
class SStoreContract(CreateStoreContract):
    id: int

    class Config:
        orm_mode = True

class StoreContract(CreateStoreContract):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResStoreContract(BaseModel):
    data: List[SStoreContract]
    total: int
    
class CreateStoreIncome(BaseModel):
    income_add: Optional[int] = Field(title='收入增加额')
    income_total: Optional[int] = Field(title='商家总收入')
    create_time: Optional[datetime] = Field(title='创建时间')
    store_id: Optional[int] = Field(title='商家id')

        
class SStoreIncome(CreateStoreIncome):
    id: int

    class Config:
        orm_mode = True

class StoreIncome(CreateStoreIncome):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResStoreIncome(BaseModel):
    data: List[SStoreIncome]
    total: int
    
class CreateStoreLicense(BaseModel):
    license: Optional[str] = Field(title='营业执照文本')
    store_id: Optional[int] = Field(title='商家id')
    create_time: Optional[datetime] = Field(title='更新时间')

        
class SStoreLicense(CreateStoreLicense):
    id: int

    class Config:
        orm_mode = True

class StoreLicense(CreateStoreLicense):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResStoreLicense(BaseModel):
    data: List[SStoreLicense]
    total: int
    
class CreateStoreMembership(BaseModel):
    store_id: Optional[int] = Field(title='商家id')
    user_id: Optional[int] = Field(title='用户id')
    status: Optional[str]
    create_time: Optional[datetime]
    expired_time: Optional[datetime] = Field(title='过期时间')

        
class SStoreMembership(CreateStoreMembership):
    id: int

    class Config:
        orm_mode = True

class StoreMembership(CreateStoreMembership):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResStoreMembership(BaseModel):
    data: List[SStoreMembership]
    total: int
    
class CreateStoreOwner(BaseModel):
    name: Optional[str] = Field(title='负责人姓名')
    phone: Optional[str] = Field(title='电话')
    password: Optional[str] = Field(title='密码（哈希值）')
    id_card: Optional[str] = Field(title='身份证号')
    front_image: Optional[str] = Field(title='身份证正面照')
    back_image: Optional[str] = Field(title='身份证背面照')

        
class SStoreOwner(CreateStoreOwner):
    id: int

    class Config:
        orm_mode = True

class StoreOwner(CreateStoreOwner):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResStoreOwner(BaseModel):
    data: List[SStoreOwner]
    total: int
    
class CreateStoreState(BaseModel):
    status: Optional[str] = Field(title='商家类型')

        
class SStoreState(CreateStoreState):
    id: int

    class Config:
        orm_mode = True

class StoreState(CreateStoreState):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResStoreState(BaseModel):
    data: List[SStoreState]
    total: int
    
class CreateSupplier(BaseModel):
    name: Optional[str] = Field(title='商家名称')
    phone: Optional[str] = Field(title='电话')
    province: Optional[str] = Field(title='省份')
    city: Optional[str] = Field(title='城市')
    area: Optional[str] = Field(title='区域')
    street: Optional[str] = Field(title='街道')
    address: Optional[str] = Field(title='详细地址')
    status: Optional[int] = Field(title='商家状态')
    owner: Optional[str] = Field(title='商家负责人')
    recommender_id: Optional[int] = Field(title='推荐人id   对应某个用户')
    register_time: Optional[datetime] = Field(title='注册时间')
    type: Optional[int] = Field(title='商家类型;   0: 商家  1:供应商')
    expired_time: Optional[datetime] = Field(title='合同到期时间')
    open_time: Optional[int] = Field(title='开始营业时间   9*3600表示9:00')
    close_time: Optional[int] = Field(title='结束营业时间   9*3600表示9:00，以秒为单位')
    image: Optional[str] = Field(title='商家门头图片')
    owner_id: Optional[int] = Field(title='负责人id')
    category: Optional[int] = Field(title='供应商类型  2：供应商   1：商家')
    balance: Optional[int] = Field(title='余额；以分为单位')
    reject_reason: Optional[str] = Field(title='驳回原因')
    reject_admin_id: Optional[int] = Field(title='管理员id   记录是谁审批的')
    reject_time: Optional[datetime] = Field(title='驳回时间')
    company_name: Optional[str] = Field(title='公司名称')

        
class SSupplier(CreateSupplier):
    id: int

    class Config:
        orm_mode = True

class Supplier(CreateSupplier):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResSupplier(BaseModel):
    data: List[SSupplier]
    total: int
    
class CreateSupplierAmount(BaseModel):
    type: Optional[int] = Field(title='变动类型')
    change: Optional[int] = Field(title='资金变动额      +10    -5')
    amount: Optional[int] = Field(title='资金总额')
    create_time: Optional[datetime] = Field(title='创建时间')
    supplier_id: Optional[int] = Field(title='商家id')
    order_id: Optional[int] = Field(title='订单id')
    description: Optional[str] = Field(title='描述')

        
class SSupplierAmount(CreateSupplierAmount):
    id: int

    class Config:
        orm_mode = True

class SupplierAmount(CreateSupplierAmount):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResSupplierAmount(BaseModel):
    data: List[SSupplierAmount]
    total: int
    
class CreateSupplierChangeType(BaseModel):
    type: Optional[str] = Field(title='资金变动类型')

        
class SSupplierChangeType(CreateSupplierChangeType):
    id: int

    class Config:
        orm_mode = True

class SupplierChangeType(CreateSupplierChangeType):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResSupplierChangeType(BaseModel):
    data: List[SSupplierChangeType]
    total: int
    
class CreateSupplierIncome(BaseModel):
    supplier_id: Optional[int] = Field(title='外键,供应商id')
    change: Optional[int] = Field(title='变动金额')
    balance: Optional[int] = Field(title='余额')
    type: Optional[str] = Field(title='类型')
    description: Optional[str] = Field(title='详细描述')
    create_time: Optional[datetime] = Field(title='创建时间')
    user_withdraw_id: Optional[int]
    operator_id: Optional[int] = Field(title='操作员ID')
    out_trade_no: Optional[str]

        
class SSupplierIncome(CreateSupplierIncome):
    id: int

    class Config:
        orm_mode = True

class SupplierIncome(CreateSupplierIncome):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResSupplierIncome(BaseModel):
    data: List[SSupplierIncome]
    total: int
    
class CreateSupplierLicense(BaseModel):
    license: Optional[str] = Field(title='营业执照文本')
    supplier_id: Optional[int] = Field(title='商家id')
    create_time: Optional[datetime] = Field(title='更新时间')

        
class SSupplierLicense(CreateSupplierLicense):
    id: int

    class Config:
        orm_mode = True

class SupplierLicense(CreateSupplierLicense):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResSupplierLicense(BaseModel):
    data: List[SSupplierLicense]
    total: int
    
class CreateSupplierMembership(BaseModel):
    supplier_id: Optional[int] = Field(title='商家id')
    user_id: Optional[int] = Field(title='用户id')
    status: Optional[str]
    create_time: Optional[datetime]
    expired_time: Optional[datetime] = Field(title='过期时间')

        
class SSupplierMembership(CreateSupplierMembership):
    id: int

    class Config:
        orm_mode = True

class SupplierMembership(CreateSupplierMembership):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResSupplierMembership(BaseModel):
    data: List[SSupplierMembership]
    total: int
    
class CreateSupplierOwner(BaseModel):
    name: Optional[str] = Field(title='负责人姓名')
    phone: Optional[str] = Field(title='电话')
    password: Optional[str] = Field(title='密码（哈希值）')
    id_card: Optional[str] = Field(title='身份证号')
    front_image: Optional[str] = Field(title='身份证正面照')
    back_image: Optional[str] = Field(title='身份证背面照')
    open_id: Optional[str]
    union_id: Optional[str]
    level_id: Optional[int] = Field(title='角色id    0：负责人     1：财务人员      2：核销人员')

        
class SSupplierOwner(CreateSupplierOwner):
    id: int

    class Config:
        orm_mode = True

class SupplierOwner(CreateSupplierOwner):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResSupplierOwner(BaseModel):
    data: List[SSupplierOwner]
    total: int
    
class CreateSupplierState(BaseModel):
    status: Optional[str] = Field(title='商家类型')

        
class SSupplierState(CreateSupplierState):
    id: int

    class Config:
        orm_mode = True

class SupplierState(CreateSupplierState):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResSupplierState(BaseModel):
    data: List[SSupplierState]
    total: int
    
class CreateSupplierType(BaseModel):
    type_: Optional[str] = Field(title='类型')

        
class SSupplierType(CreateSupplierType):
    id: int

    class Config:
        orm_mode = True

class SupplierType(CreateSupplierType):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResSupplierType(BaseModel):
    data: List[SSupplierType]
    total: int
    
class CreateUser(BaseModel):
    username: Optional[str] = Field(title='用户名')
    email: Optional[str] = Field(title='邮箱')
    open_id: Optional[str] = Field(title='openID from wechat channel')
    union_id: Optional[str] = Field(title='unionID from tecent')
    password: Optional[str] = Field(title='密码（哈希值）')
    nickname: Optional[str] = Field(title='昵称')
    phone: Optional[str] = Field(title='联系方式')
    id_card: Optional[str] = Field(title='身份证')
    level_id: Optional[int] = Field(title='用户等等级 默认是0')
    status: Optional[int] = Field(title='0: 已实名   1: 未实名,被is_agree替代')
    register_time: Optional[datetime] = Field(title='注册时间')
    avatar: Optional[str] = Field(title='头像url')
    invited_user_id: Optional[int] = Field(title='邀请人id')
    coin: Optional[int] = Field(title='积分')
    gender: Optional[int] = Field(title='0:  男  1:  女')
    last_active_time: Optional[datetime] = Field(title='最近登录时间')
    name: Optional[str] = Field(title='用户名')
    is_agree: Optional[int] = Field(title='是否已经校验')
    parent_id: Optional[int] = Field(title='父级用户')
    parent_id_history: Optional[str] = Field(title='曾经的上级(ID之间逗号分隔)')
    level_one_time: Optional[datetime] = Field(title='升级活跃会员时间')
    level_two_time: Optional[datetime] = Field(title='升级老板会员时间')
    level_three_time: Optional[datetime] = Field(title='升级大老板会员时间')
    level_top_time: Optional[datetime] = Field(title='升级推广顶级时间')

        
class SUser(CreateUser):
    id: int = Field(title='标识id')

    class Config:
        orm_mode = True

class User(CreateUser):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResUser(BaseModel):
    data: List[SUser]
    total: int
    
class CreateUserAccount(BaseModel):
    user_id: Optional[int] = Field(title='用户id')
    balance: Optional[int] = Field(title='余额')
    lock_balance: Optional[int] = Field(title='锁定额')
    coin: Optional[int] = Field(title='积分')
    description: Optional[str] = Field(title='详细描述')
    create_time: Optional[datetime] = Field(title='记录生成时间')
    freeze_balance: Optional[int] = Field(title='冻结额 单位：分')
    update_time: Optional[datetime]

        
class SUserAccount(CreateUserAccount):
    id: int = Field(title='账户id')

    class Config:
        orm_mode = True

class UserAccount(CreateUserAccount):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResUserAccount(BaseModel):
    data: List[SUserAccount]
    total: int
    
class CreateUserBank(BaseModel):
    bank_name: Optional[str] = Field(title='开户行')
    username: Optional[str] = Field(title='户主姓名')
    id_card: Optional[str] = Field(title='银行卡号')
    user_id: Optional[int] = Field(title='用户id')
    phone: Optional[str] = Field(title='户主电话')
    bank_address: Optional[str] = Field(title='开户行地址')
    is_default: Optional[int]

        
class SUserBank(CreateUserBank):
    id: int

    class Config:
        orm_mode = True

class UserBank(CreateUserBank):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResUserBank(BaseModel):
    data: List[SUserBank]
    total: int
    
class CreateUserFav(BaseModel):
    user_id: Optional[int]
    good_id: Optional[int]
    create_time: Optional[datetime]
    spec_id: Optional[int] = Field(title='规格id')

        
class SUserFav(CreateUserFav):
    id: int

    class Config:
        orm_mode = True

class UserFav(CreateUserFav):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResUserFav(BaseModel):
    data: List[SUserFav]
    total: int
    
class CreateUserLevel(BaseModel):
    title: Optional[str]

        
class SUserLevel(CreateUserLevel):
    id: int

    class Config:
        orm_mode = True

class UserLevel(CreateUserLevel):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResUserLevel(BaseModel):
    data: List[SUserLevel]
    total: int
    
class CreateUserPaymentHistory(BaseModel):
    fee: Optional[int]
    create_time: Optional[datetime]
    description: Optional[str]

        
class SUserPaymentHistory(CreateUserPaymentHistory):
    id: int

    class Config:
        orm_mode = True

class UserPaymentHistory(CreateUserPaymentHistory):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResUserPaymentHistory(BaseModel):
    data: List[SUserPaymentHistory]
    total: int
    
class CreateUserPhoneCode(BaseModel):
    user_id: Optional[int]
    code: Optional[str] = Field(title='6位验证码')
    expired_time: Optional[int] = Field(title='按秒计算')
    send_time: Optional[datetime] = Field(title='短信发送时间')
    employee_id: Optional[int]
    store_owner_id: Optional[int] = Field(title='店主管id')
    worker_id: Optional[int] = Field(title='普通员工id')
    phone: Optional[str] = Field(title='电话号码')

        
class SUserPhoneCode(CreateUserPhoneCode):
    id: int

    class Config:
        orm_mode = True

class UserPhoneCode(CreateUserPhoneCode):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResUserPhoneCode(BaseModel):
    data: List[SUserPhoneCode]
    total: int
    
class CreateUserWithdraw(BaseModel):
    amount: Optional[int] = Field(title='提现金额，单位分')
    user_withdraw_status_id: Optional[int] = Field(title='状态')
    create_time: Optional[datetime] = Field(title='申请时间')
    update_time: Optional[datetime] = Field(title='更新时间')
    user_id: Optional[int]
    type_id: Optional[int] = Field(title='提现类型')
    user_bank_id: Optional[int] = Field(title='当类型为银行卡时，该字段指向银行卡号')
    operator_id: Optional[int]
    fee_type: Optional[int] = Field(title='扣费类型')
    fee_pro: Optional[float] = Field(title='扣费比例')
    out_batch_no: Optional[str] = Field(title=' 商户系统内部的商家批次单号，要求此参数只能由数字、大小写字母组成，在商户系统内部唯一')
    batch_name: Optional[str] = Field(title='该笔批量转账的名称')
    batch_remark: Optional[str] = Field(title='转账说明，UTF8编码，最多允许32个字符')
    out_detail_no: Optional[str] = Field(title=' 商户系统内部区分转账批次单下不同转账明细单的唯一标识，要求此参数只能由数字、大小写字母组成')
    user_name: Optional[str] = Field(title=' 姓名')
    user_phone: Optional[str] = Field(title=' 电话')
    fee_balance: Optional[int] = Field(title='实际提现金额')
    deduct_balance: Optional[int] = Field(title='扣除或返锁定额金额')

        
class SUserWithdraw(CreateUserWithdraw):
    id: int

    class Config:
        orm_mode = True

class UserWithdraw(CreateUserWithdraw):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResUserWithdraw(BaseModel):
    data: List[SUserWithdraw]
    total: int
    
class CreateUserWithdrawStatus(BaseModel):
    title: Optional[str]

        
class SUserWithdrawStatus(CreateUserWithdrawStatus):
    id: int

    class Config:
        orm_mode = True

class UserWithdrawStatus(CreateUserWithdrawStatus):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResUserWithdrawStatus(BaseModel):
    data: List[SUserWithdrawStatus]
    total: int
    
class CreateUserWithdrawType(BaseModel):
    title: Optional[str] = Field(title='标注')

        
class SUserWithdrawType(CreateUserWithdrawType):
    id: int

    class Config:
        orm_mode = True

class UserWithdrawType(CreateUserWithdrawType):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class FilterResUserWithdrawType(BaseModel):
    data: List[SUserWithdrawType]
    total: int
    