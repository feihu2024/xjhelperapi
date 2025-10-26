# coding: utf-8
from sqlalchemy import Column, Float, Integer, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import LONGTEXT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TAddress(Base):
    __tablename__ = 't_address'
    __table_args__ = {'comment': '地址表，用于存放表的地址，一个用户可以有多个地址'}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, comment='外键')
    province = Column(VARCHAR(20), comment='省')
    city = Column(VARCHAR(20), comment='市')
    area = Column(VARCHAR(20), comment='区')
    street = Column(VARCHAR(20), comment='街道')
    description = Column(VARCHAR(250), comment='详细地址')
    default_ = Column(TINYINT, comment='1:默认  0:非默认')
    consignee = Column(String(25), comment='收货人姓名')
    phone = Column(String(25), comment='收货人电话')


class TAdmin(Base):
    __tablename__ = 't_admin'
    __table_args__ = {'comment': '管理员的表'}

    id = Column(Integer, primary_key=True)
    username = Column(String(45))
    phone = Column(String(45))
    email = Column(String(45))
    level_id = Column(Integer)
    password = Column(String(100))
    id_card = Column(String(45))
    gender = Column(String(20))
    register_time = Column(TIMESTAMP)
    last_active_time = Column(TIMESTAMP)
    status = Column(String(20))


class TBalance(Base):
    __tablename__ = 't_balance'
    __table_args__ = {'comment': '用户账户余额表，用户的余额历史记录，不可修改，只能增加'}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, comment='外键')
    change = Column(Integer, nullable=False, server_default=text("'0'"), comment='变动金额')
    balance = Column(Integer, nullable=False, comment='余额')
    type = Column(VARCHAR(20), comment='类型')
    description = Column(VARCHAR(100), comment='详细描述')
    create_time = Column(TIMESTAMP, comment='创建时间')
    user_withdraw_id = Column(Integer)
    operator_id = Column(Integer, comment='操作员ID')
    out_trade_no = Column(String(64))
    good_id = Column(VARCHAR(100), comment='收益商品id')
    good_title = Column(Text, comment='收益商品标题名称')
    good_num = Column(VARCHAR(100), comment='收益商品数量')


class TBanner(Base):
    __tablename__ = 't_banner'
    __table_args__ = {'comment': 'banner管理表，商城小程序里首页的头部的广告图'}

    id = Column(Integer, primary_key=True)
    image = Column(String(256), comment='图片url')
    title = Column(String(100), comment='主标题')
    subtitle = Column(String(100), comment='副标题')
    width = Column(Integer, comment='图片宽度')
    height = Column(Integer, comment='图片高度')
    create_time = Column(TIMESTAMP, comment='创建时间')
    description = Column(String(100), comment='详情')
    good_id = Column(Integer, comment='商品id')
    ban_label = Column(String(45), comment='标签')
    type_id = Column(TINYINT, comment='0:banner   1:直通车')
    good_spec_id = Column(Integer)


class TCart(Base):
    __tablename__ = 't_cart'
    __table_args__ = {'comment': '购物车表'}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, comment='用户编号')
    good_id = Column(Integer, comment='商品编号')
    amount = Column(Integer, comment='购买数量')
    creat_time = Column(TIMESTAMP, comment='创建时间')
    good_spec_id = Column(Integer)


class TCategory(Base):
    __tablename__ = 't_category'
    __table_args__ = {'comment': '此表使用中   对应商品的四大分类，商品种类'}

    id = Column(Integer, primary_key=True)
    cname = Column(String(128), comment='分类名称')
    parent_category_id = Column(Integer, server_default=text("'0'"), comment='上级分类id，默认0为顶级分类')


class TCity(Base):
    __tablename__ = 't_city'
    __table_args__ = {'comment': '地区表省，市，区'}

    id = Column(Integer, primary_key=True)
    cname = Column(String(128))
    parid = Column(Integer, server_default=text("'0'"), comment='上级地区id，默认0为顶级地区')
    status = Column(TINYINT(1), server_default=text("'0'"), comment='地区状态')


class TCoin(Base):
    __tablename__ = 't_coin'
    __table_args__ = {'comment': '用户的积分历史记录'}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, comment='外键')
    change = Column(Integer, nullable=False, server_default=text("'0'"), comment='变动')
    coin = Column(Integer, nullable=False, comment='积分')
    type = Column(VARCHAR(20), nullable=False, comment='类型')
    description = Column(VARCHAR(100), comment='详细')
    create_time = Column(TIMESTAMP, comment='创建时间')
    out_trade_no = Column(String(64))


class TCombo(Base):
    __tablename__ = 't_combo'

    id = Column(Integer, primary_key=True)
    good_id = Column(Integer)
    title = Column(String(45))
    amount = Column(Integer)
    price = Column(Integer)


class TDeliveryRule(Base):
    __tablename__ = 't_delivery_rule'
    __table_args__ = {'comment': '商品的邮寄规则，例如有的区域可以运送，有的不行，然后有的区域是免邮费，有的不能免邮费，这里记录这些规则'}

    id = Column(Integer, primary_key=True)
    good_id = Column(Integer, comment='商品id')
    spec_id = Column(Integer, comment='规格id')
    province = Column(VARCHAR(45), comment='省')
    city = Column(VARCHAR(45), comment='市')
    area = Column(VARCHAR(45), comment='区')
    is_reachable = Column(TINYINT(1), comment='是否可抵达    0：不可抵达     1：可抵达')
    delivery_fee = Column(Integer, server_default=text("'0'"), comment='邮寄费用')


class TExportFile(Base):
    __tablename__ = 't_export_files'
    __table_args__ = {'comment': '导出文件列表'}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, server_default=text("'0'"), comment='用户id')
    export_url = Column(VARCHAR(256), comment='文件生成地址')
    type = Column(VARCHAR(20), comment='类型')
    description = Column(VARCHAR(100), comment='详细描述')
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')


class TFlashOrder(Base):
    __tablename__ = 't_flash_order'
    __table_args__ = {'comment': '秒杀订单表'}

    id = Column(Integer, primary_key=True, unique=True)
    package_id = Column(Integer, comment='包id')
    status = Column(TINYINT, nullable=False, comment='状态   0：未付款    1：已付款    2：未发货    3：已发货    4：已签收     5：退货申请    6：退货中    7：已退货    8：取消交易')
    create_time = Column(TIMESTAMP, comment='下单时间')
    paid_time = Column(TIMESTAMP, comment='付款时间')
    user_id = Column(Integer, nullable=False, comment='用户id')
    number = Column(Integer, comment='商品数量')
    flash_price = Column(Integer, comment='秒杀单价')
    flash_cost = Column(Integer, comment='秒杀成本')
    out_trade_no = Column(String(64))
    paid_amount = Column(Integer, comment='支付金额')
    paid_balance = Column(Integer, comment='余额支付金额')
    single_status = Column(TINYINT(1), comment='是否单份代卖')
    sold = Column(Integer, comment='已售出商品数量')
    whole_status = Column(TINYINT(1), comment='是否整份代码,暂时废弃,统一启用single_status字段判断')
    spec_id = Column(Integer, comment='规格id')
    put_on_time = Column(TIMESTAMP, comment='上架时间,计算收益时使用')
    detail = Column(Text, comment='订单备注,+=更新')
    is_assign_income = Column(TINYINT(1), server_default=text("'0'"), comment='是否分配收益')
    complete_time = Column(TIMESTAMP, comment='订单完结时间')
    return_sold = Column(Integer, server_default=text("'0'"), comment='已提货数量')


class TFlashOrderReturn(Base):
    __tablename__ = 't_flash_order_return'
    __table_args__ = {'comment': '秒杀订单退货收益表'}

    id = Column(Integer, primary_key=True, unique=True, comment='主键id')
    user_id = Column(Integer, server_default=text("'0'"), comment='用户id')
    income_days = Column(Integer, server_default=text("'0'"), comment='剩余秒杀退货收益天数')
    latest_time = Column(TIMESTAMP, comment='最近一次退货时间')
    latest_income_user = Column(Integer, server_default=text("'0'"), comment='最近一次退货收益')
    latest_income_layer = Column(Integer, server_default=text("'0'"), comment='最近一次退货层级收益')
    latest_income_toper = Column(Integer, server_default=text("'0'"), comment='最近一次退货见点收益')
    latest_income_groupsir = Column(Integer, server_default=text("'0'"), comment='最近一次退货团长收益')


class TPackageOrderStatus(Base):
    __tablename__ = 't_flash_order_status'

    id = Column(Integer, primary_key=True)
    title = Column(String(45))


class TGood(Base):
    __tablename__ = 't_good'
    __table_args__ = {'comment': '商品表'}

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(VARCHAR(45), comment='产品名称')
    is_flash_sale = Column(Integer, comment='是否参加秒杀')
    category_id = Column(Integer, comment='大类别ID   关联t_category表')
    type = Column(TINYINT, server_default=text("'1'"), comment='0:虚拟(卡券） 1:实体')
    num_sale = Column(Integer, comment='销量')
    image_url = Column(VARCHAR(256), comment='主图片url')
    priority = Column(Integer, comment='优先级  越小越好')
    add_coin = Column(Integer, comment='购买后给予多少积分')
    model_id = Column(Integer, comment='模型id  如海底捞卡券属于火锅模型')
    expired_time = Column(TIMESTAMP, comment='过期时间')
    parent_good_id = Column(Integer, comment='如果是套餐产品，这个是父商品id')
    title = Column(VARCHAR(256), comment='主标题        如糖醋鱼的标题是美食')
    subtitle = Column(VARCHAR(256), comment='副标题')
    stock_cordon = Column(Integer, comment='库存警戒线')
    status = Column(TINYINT, server_default=text("'1'"), comment='0: 下架   1: 上架 ')
    details = Column(VARCHAR(256), comment='商品详情描述')
    supplier_id = Column(Integer, comment='供应商id')
    share_ratio = Column(Integer, comment='分成比例')
    create_time = Column(TIMESTAMP, comment='添加时间')
    last_update_time = Column(TIMESTAMP, comment='最后修改时间')
    saleable = Column(TINYINT(1), server_default=text("'1'"), comment='0：下架  1：上架')
    click_count = Column(Integer, comment='点击量')
    transmit_count = Column(Integer, comment='转发量')
    coinable = Column(TINYINT, server_default=text("'0'"), comment='0:不可以使用积分      1:可使用积分')
    price_line = Column(Integer, comment='商品划价线')
    introducer_id = Column(Integer, comment='介绍人id')
    sell_high = Column(Integer, comment='最高售价')
    sell_low = Column(Integer, comment='最低售价')
    cost_high = Column(Integer, comment='最高成本')
    cost_low = Column(Integer, comment='最低成本')
    display = Column(TINYINT, server_default=text("'1'"), comment='显示位置          1:顶部       0:底部')
    coinable_number = Column(Integer, comment='积分可用数')
    is_package = Column(TINYINT)
    fake_owner_name = Column(String(45), comment='临时数据   负责人名称')
    fake_owner_phone = Column(String(45), comment='临时数据   负责人电话')
    unavailable_date = Column(String(45), comment='不可用时间')
    available_time = Column(String(45))
    usage_rule = Column(String(45))
    refund_rule = Column(String(45))
    order_expired_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='订单过期时间，用户下单后这个日期会被复制code_expired_time，后期修改不影响已下单过期时间')
    cover_url = Column(VARCHAR(256), comment='封面图片url')
    video_url = Column(VARCHAR(256), comment='视频url')


class TGoodCategory(Base):
    __tablename__ = 't_good_category'
    __table_args__ = {'comment': '此表不用'}

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR(128), comment='小类别名称   比如火锅、烧烤')
    general_id = Column(Integer, comment='大类id     关联t_category表')


class TGoodImage(Base):
    __tablename__ = 't_good_image'
    __table_args__ = {'comment': '一个商品存在多张图片'}

    id = Column(Integer, primary_key=True)
    image = Column(VARCHAR(256), comment='商品图片url')
    good_id = Column(Integer, comment='商品id')


class TGoodIntroducer(Base):
    __tablename__ = 't_good_introducer'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45), comment='介绍人名称')
    phone = Column(VARCHAR(25), comment='介绍人电话')
    address = Column(VARCHAR(100), comment='介绍人住址')
    id_card = Column(String(25), comment='介绍人身份证')


class TGoodModel(Base):
    __tablename__ = 't_good_model'

    id = Column(Integer, primary_key=True, unique=True)
    model = Column(String(25))


class TGoodPackage(Base):
    __tablename__ = 't_good_package'
    __table_args__ = {'comment': '商品套餐表，包含套餐商品下的菜品等'}

    id = Column(Integer, primary_key=True)
    number = Column(String(20), comment='商品份数')
    price = Column(String(20), comment='单价')
    title = Column(VARCHAR(100), comment='商品标题')
    create_time = Column(TIMESTAMP, comment='创建时间')
    good_id = Column(Integer, comment='商品id')


class TGoodPerson(Base):
    __tablename__ = 't_good_person'

    id = Column(Integer, primary_key=True)
    good_id = Column(Integer, comment='商品编号')
    person_id = Column(Integer, comment='人数id')


class TGoodPersonState(Base):
    __tablename__ = 't_good_person_state'
    __table_args__ = {'comment': '套餐商品人数'}

    id = Column(Integer, primary_key=True)
    title = Column(String(100), comment='使用人数')


class TGoodPriority(Base):
    __tablename__ = 't_good_priority'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))


class TGoodRule(Base):
    __tablename__ = 't_good_rule'

    id = Column(Integer, primary_key=True)
    good_id = Column(Integer, comment='商品id')
    create_time = Column(TIMESTAMP, comment='创建时间')
    validate_day = Column(String(100), comment='有效期    例如： 2023.04.19   至  2024.04.19')
    unuseful_day = Column(String(100), comment='不可用日期     例如： 2023.05.01 至 2024.05.07')
    useful_time = Column(String(100), comment='可用时间      例如：24小时可用       14:00-20:00可用等')
    use_rule = Column(String(512), comment='使用规则')
    return_rule = Column(String(100), comment='退货规则')
    room = Column(TINYINT, comment='0:不可使用包间     1：可使用包间')
    title = Column(String(256))
    value = Column(String(256))


class TGoodSpec(Base):
    __tablename__ = 't_good_spec'
    __table_args__ = {'comment': '一个商品存在多个规格    关联商品表'}

    good_id = Column(Integer, comment='商品id')
    price = Column(Integer, comment='售价')
    cost = Column(Integer, comment='成本')
    value = Column(VARCHAR(128), comment='规格的值    例如：糖醋里脊的甜口、酸口')
    id = Column(Integer, primary_key=True, unique=True)
    stock = Column(Integer, comment='库存')
    price_line = Column(Integer, comment='划价线')
    image = Column(String(256), comment='图片url')
    is_sub_good = Column(TINYINT, server_default=text("'0'"))
    num_sale = Column(Integer, comment='销量')
    parent_fee = Column(Integer, server_default=text("'0'"), comment='分层奖，上一级的奖励')
    top_fee = Column(Integer, server_default=text("'0'"), comment='见点奖，第一高级会员分成')
    recommender_fee = Column(Integer, server_default=text("'0'"), comment='售出奖，推荐人的奖励')
    supplier_fee = Column(Integer, server_default=text("'0'"), comment='供货收益')
    lower_num_people = Column(Integer, comment='人数下限')
    upper_num_people = Column(Integer, comment='人数上限')
    room = Column(String(45), comment='包间')
    post = Column(Text)
    status = Column(TINYINT, server_default=text("'1'"), comment='0: 下架   1: 上架 ')
    share_fee = Column(Integer, server_default=text("'0'"), comment='分享商品收益')
    is_default = Column(TINYINT(1), server_default=text("'0'"), comment='是否默认规格')
    spec_num = Column(VARCHAR(200), comment='商品规格编号')
    profit = Column(Integer, server_default=text("'0'"), comment='产品利润')
    eqlevel_fee = Column(Integer, server_default=text("'0'"), comment='平级奖 直推关系下见点收益的推荐人收益')


class TGoodSpecCombo(Base):
    __tablename__ = 't_good_spec_combo'

    id = Column(Integer, primary_key=True)
    good_spec_id = Column(Integer)
    value = Column(String(45))
    price = Column(Integer)
    amount = Column(String(256), comment='数量')


class TGoodSpecDetail(Base):
    __tablename__ = 't_good_spec_detail'

    id = Column(Integer, primary_key=True)
    good_spec_id = Column(Integer, index=True)
    detail = Column(LONGTEXT)


class TGoodSpecImage(Base):
    __tablename__ = 't_good_spec_image'
    __table_args__ = {'comment': '该规格的图片'}

    id = Column(Integer, primary_key=True)
    spec_id = Column(Integer, comment='规格id')
    image = Column(String(256), comment='图片url')


class TGoodStore(Base):
    __tablename__ = 't_good_store'

    id = Column(Integer, primary_key=True)
    good_id = Column(Integer)
    store_id = Column(Integer)


class TGoodText(Base):
    __tablename__ = 't_good_text'

    id = Column(Integer, primary_key=True)
    good_id = Column(Integer, comment='商品id')
    description = Column(LONGTEXT, comment='图文详情   图片和文字放在一起')
    create_time = Column(TIMESTAMP, comment='创建时间')


class TGoodType(Base):
    __tablename__ = 't_good_type'

    id = Column(Integer, primary_key=True)
    type = Column(String(25))


class TGroupsir(Base):
    __tablename__ = 't_groupsir'
    __table_args__ = {'comment': '团购团长表'}

    id = Column(Integer, primary_key=True, unique=True, comment='团长id')
    user_id = Column(Integer, server_default=text("'0'"), comment='关联t_user表id')
    parent_id = Column(Integer, server_default=text("'0'"), comment='0:表示团长，非0表示下级成员')
    register_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='成团时间和入团')
    status = Column(TINYINT, server_default=text("'0'"), comment='0: 启用   1: 暂停  -1：出团或解散')
    is_empower = Column(TINYINT, server_default=text("'0'"), comment='0: 未授权   1:已授权（可以使用所有商品秒杀包）')
    notes = Column(VARCHAR(512), comment='团员备注')


class TLevel(Base):
    __tablename__ = 't_level'

    id = Column(Integer, primary_key=True, unique=True)
    title = Column(String(45))


class TLockBalance(Base):
    __tablename__ = 't_lock_balance'
    __table_args__ = {'comment': '锁定额历史记录表'}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, comment='外键')
    change = Column(Integer, server_default=text("'0'"), comment='变动')
    lock_balance = Column(Integer, comment='锁定金额')
    type = Column(VARCHAR(20), comment='类型')
    description = Column(VARCHAR(100), comment='描述')
    create_time = Column(TIMESTAMP, comment='创建时间')
    out_trade_no = Column(String(64))


class TModel(Base):
    __tablename__ = 't_model'
    __table_args__ = {'comment': '规格表，已被遗弃'}

    id = Column(Integer, primary_key=True, unique=True)
    product_id = Column(Integer)


class TOrder(Base):
    __tablename__ = 't_order'
    __table_args__ = {'comment': '商品订单表（不包含秒杀订单)    1.创建时间与支付时间有本质区别'}

    id = Column(Integer, primary_key=True, unique=True, comment='订单id')
    good_id = Column(Integer, comment='商品id')
    paider_id = Column(Integer, comment='付款人id')
    sale_price = Column(Integer, comment='售价      记录客户购买时的商品价格（因为价格可能变动）')
    cost_price = Column(Integer, comment='成本       记录客户购买时的商品成本（因为成本可能变动）')
    create_time = Column(TIMESTAMP, comment='创建时间    与支付时间有本质区别')
    paid_time = Column(TIMESTAMP, comment='支付时间')
    status_id = Column(TINYINT, nullable=False, comment='状态id        对应未发货、已发货、已完成')
    number = Column(Integer, comment='商品数量')
    consignee_address = Column(VARCHAR(128), comment='收货人地址')
    consignee_phone = Column(VARCHAR(25), comment='收货人联系电话')
    store_id = Column(Integer, comment='店铺id')
    paid_amount = Column(Integer, comment='实际第三方支付的金额     用于标记除客户账户以外支付的金额（比如微信、银行卡)')
    delivery_fee = Column(Integer, comment='运费金额')
    spec_id = Column(Integer, comment='规格编号')
    paid_coin = Column(Integer, comment='实际支付的积分      用于标记客户账户内支付的积分')
    delivery_track_code = Column(VARCHAR(25), comment='第三方物流单号  比如顺丰的单号')
    paid_channel_id = Column(Integer, comment='第三方支付渠道    比如微信支付  银行卡支付等')
    consignee_name = Column(VARCHAR(25), comment='收货人名称')
    delivery_time = Column(TIMESTAMP, comment='发货时间')
    good_name = Column(VARCHAR(45), comment='商品名称    记录客户购买时的商品名称（因为名称可能变动）')
    paid_track_code = Column(VARCHAR(45), comment='第三方支付流水号    比如微信支付提供的支付编码')
    paider_name = Column(String(100), comment='付款人姓名')
    paider_phone = Column(String(100), comment='付款人电话')
    paider_address = Column(VARCHAR(128), comment='付款人地址')
    supplier_id = Column(Integer, comment='商家id')
    paid_balance = Column(Integer, comment='实际支付的余额         用于标记客户账户内支付的余额')
    paid_lock_balance = Column(Integer, comment='实际支付的锁定额        用于标记客户账户内支付的锁定额')
    delivery_company = Column(VARCHAR(45), comment='第三方物流公司   比如圆通、顺丰等')
    complete_time = Column(TIMESTAMP, comment='订单完结时间')
    use_balance = Column(TINYINT(1), comment='是否使用余额')
    use_coin = Column(TINYINT(1), comment='是否使用积分')
    consignee_province = Column(String(45))
    consignee_description = Column(String(45))
    consignee_city = Column(String(45))
    consignee_area = Column(String(45))
    consignee_street = Column(String(45))
    out_trade_no = Column(String(64), comment='商户单号')
    code = Column(String(45), comment='虚拟消费券的code')
    code_expired_time = Column(TIMESTAMP, comment='虚拟消费券的过期时间')
    is_display = Column(TINYINT(1), nullable=False, server_default=text("'1'"), comment='是否可以展示')
    recommender_id = Column(Integer, comment='推荐人Id')
    detail = Column(Text, comment='订单备注,+=更新')
    is_assign_income = Column(TINYINT(1), server_default=text("'0'"), comment='是否分配收益')
    parent_uid = Column(Integer, server_default=text("'0'"), comment='层级收益人id')
    top_uid = Column(Integer, server_default=text("'0'"), comment='顶级收益人id')
    invited_uid = Column(Integer, server_default=text("'0'"), comment='直推收益人id')
    supplier_uid = Column(Integer, server_default=text("'0'"), comment='供货介绍收益人id')
    eqlevel_uid = Column(Integer, server_default=text("'0'"), comment='平级奖收益人id')


class TOrderBatch(Base):
    __tablename__ = 't_order_batch'
    __table_args__ = {'comment': '订单批次表，例如五个商品同时购买，生成了五个订单，但是这五个订单是一个批次'}

    id = Column(Integer, primary_key=True)
    create_time = Column(TIMESTAMP)


class TOrderCheck(Base):
    __tablename__ = 't_order_check'
    __table_args__ = {'comment': '核销记录表'}

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, comment='订单id')
    check_num = Column(Integer, comment='核销数量')
    check_time = Column(TIMESTAMP, comment='核销时间')
    worker_id = Column(Integer, comment='核销人id，对应店铺的人员')
    check_amount = Column(Integer, comment='核销金额')


class TOrderReturn(Base):
    __tablename__ = 't_order_return'
    __table_args__ = {'comment': '退货订单表'}

    id = Column(Integer, primary_key=True, comment='退货编号')
    returner_name = Column(VARCHAR(45), comment='退款人姓名   对应订单表的付款人')
    returner_phone = Column(VARCHAR(45), comment='退款人电话   对应订单表的付款人')
    returner_address = Column(VARCHAR(100), comment='退款人地址   对应订单表的付款人')
    delivery_fee = Column(Integer, comment='退货运费')
    return_amount = Column(Integer, comment='第三方支付退款额度    比如退还微信10元')
    return_submit_time = Column(TIMESTAMP, comment='退货申请时间')
    return_reason = Column(String(128), comment='退货原因')
    order_id = Column(Integer, nullable=False, comment='订单编号     关联订单表')
    good_id = Column(Integer, nullable=False, comment='商品id')
    return_num = Column(Integer, comment='退货商品数量')
    store_id = Column(Integer, comment='店铺id')
    return_delivery_track_code = Column(VARCHAR(45), comment='第三方退货物流单号')
    status_id = Column(TINYINT, server_default=text("'3'"), comment='状态id     对应退款协商中、未处理、已退货')
    consignee_name = Column(String(100), comment='收货人姓名')
    consignee_phone = Column(String(100), comment='收货人电话')
    consignee_address = Column(String(100), comment='收货人地址')
    return_balance = Column(Integer, comment='客户账户余额退还额度')
    return_lock_balance = Column(Integer, comment='客户账户锁定额退还额度')
    return_coin = Column(Integer, comment='客户账户积分退还额度')
    return_delivery_company = Column(String(45), comment='第三方物流公司')
    return_paid_track_code = Column(String(45), comment='第三方退款流水号')


class TOrderReturnState(Base):
    __tablename__ = 't_order_return_state'

    id = Column(Integer, primary_key=True)
    state = Column(String(25), comment='退换货状态')


class TOrderReturnType(Base):
    __tablename__ = 't_order_return_type'
    __table_args__ = {'comment': '订单退货类型表'}

    id = Column(Integer, primary_key=True)
    type = Column(String(45), comment='类型')


class TOrderSource(Base):
    __tablename__ = 't_order_source'
    __table_args__ = {'comment': '商城订单的商品来源表'}

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, comment='订单id')
    source_id = Column(Integer, comment='订单来源，来再t_flash_order.id，如果是空或者-1表示平台')
    amount = Column(Integer, comment='商品数量')
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    order_user_id = Column(Integer, server_default=text("'0'"), comment='订单购买用户id')
    package_user_id = Column(Integer, server_default=text("'0'"), comment='秒杀包用户id')


class TOrderState(Base):
    __tablename__ = 't_order_state'
    __table_args__ = {'comment': '订单状态表'}

    id = Column(Integer, primary_key=True)
    state = Column(VARCHAR(45), comment='订单状态')
    belong = Column(VARCHAR(100), comment='所属订单类别   比如发货  退货')


class TPackage(Base):
    __tablename__ = 't_package'
    __table_args__ = {'comment': '秒杀包表，记录商品，数量，以及价格等信息'}

    id = Column(Integer, primary_key=True, unique=True)
    good_id = Column(Integer, comment='产品id')
    amount = Column(Integer, comment='份数;the number of good in one amount一个包包含的产品的数量')
    flash_sale_price = Column(Integer, comment='秒杀价格;in cent,秒杀价格')
    num = Column(Integer, comment='包个数;一共有多少个包')
    stock = Column(Integer, comment='剩余包数量')
    seller_id = Column(Integer, comment='发布商品的卖家，如果id为空或者0，则为官方卖家')
    spec_id = Column(Integer, comment='规格id')
    share_fee = Column(Integer, comment='让利金额')
    status = Column(Integer, server_default=text("'0'"), comment='状态：-1删除, 默认0/null正常')


class TPackageExpress(Base):
    __tablename__ = 't_package_express'

    id = Column(Integer, primary_key=True)
    flash_order_id = Column(Integer)
    status = Column(Integer, comment='1: 申请中  2:  已发货  3: 拒绝发货退款  4：已签收  5:未使用  6:已使用')
    address_id = Column(Integer, comment='邮寄地址id')
    amount = Column(Integer, comment='邮寄数量')
    express_num = Column(String(128), comment='物流号')
    apply_time = Column(TIMESTAMP, comment='申请发货时间')
    delivery_time = Column(TIMESTAMP, comment='发货时间')
    complete_time = Column(TIMESTAMP, comment='签收或完成时间')
    detail = Column(Text, comment='订单备注,+=更新')


class TPackageExpressStatus(Base):
    __tablename__ = 't_package_express_status'

    id = Column(Integer, primary_key=True)
    title = Column(String(45))


class TPackageTime(Base):
    __tablename__ = 't_package_time'
    __table_args__ = {'comment': '秒杀包的秒杀时段'}

    id = Column(Integer, primary_key=True)
    start_time = Column(Integer, comment='开始时间;9*3600表示9:00')
    end_time = Column(Integer, comment='结束时间;以秒为单位')


class TPackageTimePair(Base):
    __tablename__ = 't_package_time_pair'
    __table_args__ = {'comment': '记录秒杀包和秒杀时段的关系'}

    id = Column(Integer, primary_key=True)
    package_id = Column(Integer)
    package_time_id = Column(Integer)
    status = Column(Integer, comment='状态; 0: 未激活, 1: 激活')
    package_num = Column(Integer, server_default=text("'0'"), comment='此时段秒杀包库存')


class TPayChannel(Base):
    __tablename__ = 't_pay_channel'

    id = Column(Integer, primary_key=True)
    type = Column(String(45), comment='支付方式')


class TPlatformLaw(Base):
    __tablename__ = 't_platform_law'

    id = Column(Integer, primary_key=True)
    create_time = Column(TIMESTAMP, comment='创建时间')
    admin_id = Column(Integer, comment='操作员id')
    law = Column(Text, comment='法律文本 用户协议')
    privacy = Column(Text, comment='隐私协议')
    purchase = Column(Text, comment='购买协议')
    flash_law = Column(Text, comment='批发协议')
    withdraw_law = Column(Text, comment='提现规则')


class TPlatformNotice(Base):
    __tablename__ = 't_platform_notice'
    __table_args__ = {'comment': '平台通知表'}

    id = Column(Integer, primary_key=True)
    title = Column(String(128), comment='通知内容')
    create_time = Column(TIMESTAMP, comment='创建时间')
    admin_id = Column(Integer, comment='添加人id    对应哪个管理员')


class TPoster(Base):
    __tablename__ = 't_poster'
    __table_args__ = {'comment': '海报文件列表'}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, server_default=text("'0'"), comment='用户id')
    poster_url = Column(String(256), comment='海报文件地址')
    status = Column(String(20), comment='状态')
    description = Column(String(100), comment='描述')
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')


class TSetting(Base):
    __tablename__ = 't_settings'
    __table_args__ = {'comment': '系统设置表'}

    id = Column(Integer, primary_key=True, unique=True, comment='标识id，修改时从1开始对应recommend_num之后的字段')
    recommend_num = Column(Integer, server_default=text("'0'"), comment='定义推荐系升级人数')
    flash_order_income = Column(Float, server_default=text("'0'"), comment='定义秒杀产品24小时停留收益比千分之')
    tuan_order_income = Column(Float, server_default=text("'0'"), comment='定义团长秒杀产品收益比（千分之）')
    flash_order_max = Column(Integer, server_default=text("'0'"), comment='秒杀用户持单量限制(未完成出售订单)')
    flash_order_money_max = Column(Integer, server_default=text("'0'"), comment='秒杀用户持单总金额限制(未完成出售订单)')
    flash_order_active_user = Column(Integer, server_default=text("'0'"), comment='秒杀并支付多少单，普通会员晋升活跃会员')
    consume_money_active_user = Column(Integer, server_default=text("'0'"), comment='完成商品订单达到指定额度，普通会员晋升活跃会员')
    many_high_user = Column(Integer, server_default=text("'0'"), comment='直推多少个活跃会员，晋升高级会员')
    many_top_user = Column(Integer, server_default=text("'0'"), comment='直推多少个高级会员，晋升顶级会员')
    flash_order_income_retio = Column(Float, server_default=text("'0'"), comment='秒杀人退货收益比（千分之）')
    flash_order_income_layer = Column(Float, server_default=text("'0'"), comment='秒杀人退货层级收益比（百分之）')
    flash_order_income_toper = Column(Float, server_default=text("'0'"), comment='秒杀人退货顶级收益比(百分比)')
    flash_order_income_groupsir = Column(Float, server_default=text("'0'"), comment='秒杀人退货团长收益比(百分比)')
    flash_order_owner_times = Column(Integer, server_default=text("'0'"), comment='秒杀包持有人退货时间限制（小时）')
    parent_user_limit = Column(Integer, server_default=text("'0'"), comment='推广人升级顶级时，留给原上级的人数')
    flash_order_income_subsidy = Column(Integer, server_default=text("'0'"), comment='团队补贴,秒杀的退款收益， 给直接推荐人 的一份')


class TStore(Base):
    __tablename__ = 't_store'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), comment='店铺名称')
    phone = Column(String(45), comment='电话')
    province = Column(VARCHAR(45), comment='省份')
    city = Column(String(45), comment='城市')
    area = Column(String(45), comment='区域')
    street = Column(String(45), comment='街道')
    address = Column(String(45), comment='详细地址')
    status = Column(TINYINT, comment='店铺状态')
    owner = Column(VARCHAR(45), comment='店铺负责人')
    recommender_id = Column(Integer, comment='推荐人id   对应某个用户')
    register_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='注册时间')
    type = Column(TINYINT, comment='商家类型    供应商或店铺等')
    expired_time = Column(TIMESTAMP, comment='合同到期时间')
    open_time = Column(Integer, comment='开始营业时间   9*3600表示9:00')
    close_time = Column(Integer, comment='结束营业时间   9*3600表示9:00，以秒为单位')
    image = Column(String(256), comment='商家门头图片')
    owner_id = Column(Integer, comment='负责人id')
    supplier_id = Column(Integer, comment='商家id')
    company_name = Column(String(128), comment='公司名称')
    reject_reason = Column(String(100), comment='驳回原因')
    reject_time = Column(TIMESTAMP, comment='驳回时间')
    reject_admin_id = Column(Integer, comment='管理员id   记录是谁驳回的')
    is_default = Column(TINYINT(1), comment='默认店铺')


class TStoreAmount(Base):
    __tablename__ = 't_store_amount'
    __table_args__ = {'comment': '商家金额表'}

    id = Column(Integer, primary_key=True)
    type = Column(TINYINT, comment='变动类型')
    change = Column(Integer, comment='资金变动额      +10    -5')
    amount = Column(Integer, comment='资金总额')
    create_time = Column(TIMESTAMP, comment='创建时间')
    store_id = Column(Integer, comment='店铺id')


class TStoreChangeType(Base):
    __tablename__ = 't_store_change_type'
    __table_args__ = {'comment': '商家资金变动类型'}

    id = Column(Integer, primary_key=True)
    type = Column(VARCHAR(100), comment='资金变动类型')


class TStoreContract(Base):
    __tablename__ = 't_store_contract'
    __table_args__ = {'comment': '商家合同表'}

    contract = Column(String(256), comment='合同照片')
    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, comment='商家编号')
    create_time = Column(TIMESTAMP, comment='创建时间')
    expired_time = Column(TIMESTAMP, comment='到期时间')


class TStoreIncome(Base):
    __tablename__ = 't_store_income'
    __table_args__ = {'comment': '商家收入表'}

    id = Column(Integer, primary_key=True)
    income_add = Column(Integer, comment='收入增加额')
    income_total = Column(Integer, comment='商家总收入')
    create_time = Column(TIMESTAMP, comment='创建时间')
    store_id = Column(Integer, comment='商家id')


class TStoreLicense(Base):
    __tablename__ = 't_store_license'
    __table_args__ = {'comment': '商家证件表    营业执照等'}

    id = Column(Integer, primary_key=True)
    license = Column(VARCHAR(256), comment='营业执照文本')
    store_id = Column(Integer, comment='商家id')
    create_time = Column(TIMESTAMP, comment='更新时间')


class TStoreMembership(Base):
    __tablename__ = 't_store_membership'
    __table_args__ = {'comment': '用户在店铺消费过  即成为此店的会员'}

    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, comment='商家id')
    user_id = Column(Integer, comment='用户id')
    status = Column(String(45))
    create_time = Column(TIMESTAMP)
    expired_time = Column(TIMESTAMP, comment='过期时间')


class TStoreOwner(Base):
    __tablename__ = 't_store_owner'
    __table_args__ = {'comment': '商家负责人表'}

    id = Column(Integer, primary_key=True)
    name = Column(String(100), comment='负责人姓名')
    phone = Column(String(100), comment='电话')
    password = Column(VARCHAR(100), comment='密码（哈希值）')
    id_card = Column(String(100), comment='身份证号')
    front_image = Column(String(256), comment='身份证正面照')
    back_image = Column(String(256), comment='身份证背面照')


class TStoreState(Base):
    __tablename__ = 't_store_state'

    id = Column(Integer, primary_key=True)
    status = Column(String(25), comment='商家类型')


class TSupplier(Base):
    __tablename__ = 't_supplier'
    __table_args__ = {'comment': '商家和供应商'}

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(128), comment='商家名称')
    phone = Column(String(45), comment='电话')
    province = Column(VARCHAR(45), comment='省份')
    city = Column(String(45), comment='城市')
    area = Column(String(45), comment='区域')
    street = Column(String(45), comment='街道')
    address = Column(String(45), comment='详细地址')
    status = Column(TINYINT, comment='商家状态')
    owner = Column(VARCHAR(45), comment='商家负责人')
    recommender_id = Column(Integer, comment='推荐人id   对应某个用户')
    register_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='注册时间')
    type = Column(TINYINT, comment='商家类型;   0: 商家  1:供应商')
    expired_time = Column(TIMESTAMP, comment='合同到期时间')
    open_time = Column(Integer, comment='开始营业时间   9*3600表示9:00')
    close_time = Column(Integer, comment='结束营业时间   9*3600表示9:00，以秒为单位')
    image = Column(String(256), comment='商家门头图片')
    owner_id = Column(Integer, comment='负责人id')
    category = Column(TINYINT, server_default=text("'1'"), comment='供应商类型  2：供应商   1：商家')
    balance = Column(Integer, comment='余额；以分为单位')
    reject_reason = Column(String(256), comment='驳回原因')
    reject_admin_id = Column(Integer, comment='管理员id   记录是谁审批的')
    reject_time = Column(TIMESTAMP, comment='驳回时间')
    company_name = Column(String(128), comment='公司名称')


class TSupplierAmount(Base):
    __tablename__ = 't_supplier_amount'
    __table_args__ = {'comment': '商家金额表'}

    id = Column(Integer, primary_key=True)
    type = Column(TINYINT, comment='变动类型')
    change = Column(Integer, comment='资金变动额      +10    -5')
    amount = Column(Integer, comment='资金总额')
    create_time = Column(TIMESTAMP, comment='创建时间')
    supplier_id = Column(Integer, comment='商家id')
    order_id = Column(Integer, comment='订单id')
    description = Column(String(100), comment='描述')


class TSupplierChangeType(Base):
    __tablename__ = 't_supplier_change_type'
    __table_args__ = {'comment': '商家资金变动类型'}

    id = Column(Integer, primary_key=True)
    type = Column(VARCHAR(100), comment='资金变动类型')


class TSupplierIncome(Base):
    __tablename__ = 't_supplier_income'
    __table_args__ = {'comment': '供应商的余额历史记录，不可修改，只能增加'}

    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, nullable=False, comment='外键,供应商id')
    change = Column(Integer, nullable=False, server_default=text("'0'"), comment='变动金额')
    balance = Column(Integer, nullable=False, comment='余额')
    type = Column(VARCHAR(20), comment='类型')
    description = Column(VARCHAR(100), comment='详细描述')
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    user_withdraw_id = Column(Integer)
    operator_id = Column(Integer, comment='操作员ID')
    out_trade_no = Column(String(64))


class TSupplierLicense(Base):
    __tablename__ = 't_supplier_license'
    __table_args__ = {'comment': '商家证件表    营业执照等'}

    id = Column(Integer, primary_key=True)
    license = Column(VARCHAR(256), comment='营业执照文本')
    supplier_id = Column(Integer, comment='商家id')
    create_time = Column(TIMESTAMP, comment='更新时间')


class TSupplierMembership(Base):
    __tablename__ = 't_supplier_membership'
    __table_args__ = {'comment': '用户在店铺消费过  即成为此店的会员'}

    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, comment='商家id')
    user_id = Column(Integer, comment='用户id')
    status = Column(String(45))
    create_time = Column(TIMESTAMP)
    expired_time = Column(TIMESTAMP, comment='过期时间')


class TSupplierOwner(Base):
    __tablename__ = 't_supplier_owner'
    __table_args__ = {'comment': '商家人员角色表'}

    id = Column(Integer, primary_key=True)
    name = Column(String(100), comment='负责人姓名')
    phone = Column(String(100), comment='电话')
    password = Column(VARCHAR(100), comment='密码（哈希值）')
    id_card = Column(String(100), comment='身份证号')
    front_image = Column(String(256), comment='身份证正面照')
    back_image = Column(String(256), comment='身份证背面照')
    open_id = Column(String(45))
    union_id = Column(String(45))
    level_id = Column(TINYINT(1), comment='角色id    0：负责人     1：财务人员      2：核销人员')


class TSupplierState(Base):
    __tablename__ = 't_supplier_state'

    id = Column(Integer, primary_key=True)
    status = Column(String(25), comment='商家类型')


class TSupplierType(Base):
    __tablename__ = 't_supplier_type'
    __table_args__ = {'comment': '供应商类型表'}

    id = Column(Integer, primary_key=True)
    type_ = Column(String(100), comment='类型')


class TUser(Base):
    __tablename__ = 't_user'
    __table_args__ = {'comment': 'user'}

    id = Column(Integer, primary_key=True, unique=True, comment='标识id')
    username = Column(VARCHAR(45), comment='用户名')
    email = Column(VARCHAR(45), comment='邮箱')
    open_id = Column(String(45), comment='openID from wechat channel')
    union_id = Column(String(45), comment='unionID from tecent')
    password = Column(VARCHAR(45), comment='密码（哈希值）')
    nickname = Column(VARCHAR(45), comment='昵称')
    phone = Column(VARCHAR(45), comment='联系方式')
    id_card = Column(VARCHAR(45), comment='身份证')
    level_id = Column(Integer, server_default=text("'0'"), comment='用户等等级 默认是0')
    status = Column(TINYINT, comment='0: 已实名   1: 未实名,被is_agree替代')
    register_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='注册时间')
    avatar = Column(VARCHAR(512), comment='头像url')
    invited_user_id = Column(Integer, comment='邀请人id')
    coin = Column(Integer, comment='积分')
    gender = Column(TINYINT, comment='0:  男  1:  女')
    last_active_time = Column(TIMESTAMP, comment='最近登录时间')
    name = Column(VARCHAR(45), comment='用户名')
    is_agree = Column(TINYINT(1), server_default=text("'0'"), comment='是否已经校验')
    parent_id = Column(Integer, comment='父级用户')
    parent_id_history = Column(VARCHAR(45), comment='曾经的上级(ID之间逗号分隔)')
    level_one_time = Column(TIMESTAMP, comment='升级活跃会员时间')
    level_two_time = Column(TIMESTAMP, comment='升级老板会员时间')
    level_three_time = Column(TIMESTAMP, comment='升级大老板会员时间')
    level_top_time = Column(TIMESTAMP, comment='升级推广顶级时间')


class TUserAccount(Base):
    __tablename__ = 't_user_account'
    __table_args__ = {'comment': '用户的账户信息，包括余额，锁定额，积分，以及冻结额'}

    id = Column(Integer, primary_key=True, comment='账户id')
    user_id = Column(Integer, nullable=False, comment='用户id')
    balance = Column(Integer, nullable=False, server_default=text("'0'"), comment='余额')
    lock_balance = Column(Integer, nullable=False, server_default=text("'0'"), comment='锁定额')
    coin = Column(Integer, nullable=False, server_default=text("'0'"), comment='积分')
    description = Column(String(100), comment='详细描述')
    create_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='记录生成时间')
    freeze_balance = Column(Integer, server_default=text("'0'"), comment='冻结额 单位：分')
    update_time = Column(TIMESTAMP)


class TUserBank(Base):
    __tablename__ = 't_user_bank'
    __table_args__ = {'comment': '用户银行卡信息'}

    id = Column(Integer, primary_key=True)
    bank_name = Column(VARCHAR(128), comment='开户行')
    username = Column(VARCHAR(100), comment='户主姓名')
    id_card = Column(VARCHAR(45), comment='银行卡号')
    user_id = Column(Integer, comment='用户id')
    phone = Column(String(25), comment='户主电话')
    bank_address = Column(String(100), comment='开户行地址')
    is_default = Column(TINYINT(1))


class TUserFav(Base):
    __tablename__ = 't_user_favs'
    __table_args__ = {'comment': '用户收藏的产品'}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    good_id = Column(Integer, nullable=False)
    create_time = Column(TIMESTAMP)
    spec_id = Column(Integer, comment='规格id')


class TUserLevel(Base):
    __tablename__ = 't_user_level'
    __table_args__ = {'comment': '用户会员等级'}

    id = Column(Integer, primary_key=True, unique=True)
    title = Column(String(45))


class TUserPaymentHistory(Base):
    __tablename__ = 't_user_payment_history'
    __table_args__ = {'comment': '用户所有的支付记录'}

    id = Column(Integer, primary_key=True)
    fee = Column(Integer)
    create_time = Column(TIMESTAMP)
    description = Column(String(256))


class TUserPhoneCode(Base):
    __tablename__ = 't_user_phone_code'
    __table_args__ = {'comment': '用户电话校验表'}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    code = Column(String(15), comment='6位验证码')
    expired_time = Column(Integer, comment='按秒计算')
    send_time = Column(TIMESTAMP, comment='短信发送时间')
    employee_id = Column(Integer)
    store_owner_id = Column(Integer, comment='店主管id')
    worker_id = Column(Integer, comment='普通员工id')
    phone = Column(String(45), comment='电话号码')


class TUserWithdraw(Base):
    __tablename__ = 't_user_withdraw'

    id = Column(Integer, primary_key=True)
    amount = Column(Integer, comment='提现金额，单位分')
    user_withdraw_status_id = Column(Integer, comment='状态')
    create_time = Column(TIMESTAMP, comment='申请时间')
    update_time = Column(TIMESTAMP, comment='更新时间')
    user_id = Column(Integer)
    type_id = Column(TINYINT, comment='提现类型')
    user_bank_id = Column(Integer, comment='当类型为银行卡时，该字段指向银行卡号')
    operator_id = Column(Integer)
    fee_type = Column(TINYINT(1), server_default=text("'0'"), comment='扣费类型')
    fee_pro = Column(Float(5), server_default=text("'0.0000'"), comment='扣费比例')
    out_batch_no = Column(VARCHAR(50), comment=' 商户系统内部的商家批次单号，要求此参数只能由数字、大小写字母组成，在商户系统内部唯一')
    batch_name = Column(VARCHAR(50), comment='该笔批量转账的名称')
    batch_remark = Column(VARCHAR(50), comment='转账说明，UTF8编码，最多允许32个字符')
    out_detail_no = Column(VARCHAR(50), comment=' 商户系统内部区分转账批次单下不同转账明细单的唯一标识，要求此参数只能由数字、大小写字母组成')
    user_name = Column(VARCHAR(50), comment=' 姓名')
    user_phone = Column(VARCHAR(50), comment=' 电话')
    fee_balance = Column(Integer, server_default=text("'0'"), comment='实际提现金额')
    deduct_balance = Column(Integer, server_default=text("'0'"), comment='扣除或返锁定额金额')


class TUserWithdrawStatus(Base):
    __tablename__ = 't_user_withdraw_status'

    id = Column(Integer, primary_key=True)
    title = Column(String(45))


class TUserWithdrawType(Base):
    __tablename__ = 't_user_withdraw_type'
    __table_args__ = {'comment': '用户提现类型表'}

    id = Column(Integer, primary_key=True)
    title = Column(String(25), comment='标注')
