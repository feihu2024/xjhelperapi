#资金变动类型  3和13 重复
balance_type = {
    1:"层级收益",
    2:"团队收益",
    3:"分享收益",
    4:"团长收益",
    5:"管理变动收益",
    6:"批发退货收益",
    7:"批发单商品售出",
    8:"供应商收益",
    9:"提现退款",
    10: "批发单出售收益",
    11: "购买商品",
    12: "批发支出",
    13: "分享收益",
    14: "直推收益",
    15: "供货收益",
    16: "支付失败余额退款",
    17: "支付失败锁定额退款",
    18: "购买商品微信支付",
    19: "余额提现",
    20: "提现金额驳回",
    21: "提现结余锁定额",
    22: "平级收益",
    23: "团队补贴",
}

#订单相关配置
setting_orders = {
    "return_flash_order_income_days": 20,  # 新用户默认收益天数
    "rerun_flash_order_times":24,  #秒杀退货最低时限，小时   替换为t_settings里面的flash_order_owner_times 配置
    "card_income_times":7,  #卡券订单未完结情况下，超过规定天数，分配收益
    "body_income_times": 14,  # 实体订单未完结情况下，超过规定天数，分配收益
    "good_stock_cordon":10,  #默认 库存警戒线，如果t_good中stock_cordon为none
}

#导出相关配置
setting_orders_export = {
    "order_send_list": "发货订单导出"  # 发货导出类型
}

#提现相关配置，第一项定义返回锁定余额比例，第二项提现扣除比例
"""
|  0 | 粉丝      |  fans
|  1 | 会员      |  member
|  2 | 老板      |  boss
|  3 | 大老板    |  bigboss
"""
setting_withdraw = {
    "fans": [0.12, 0.06],
    "member": [0.1, 0.05],
    "boss": [0.08, 0.04],
    "bigboss": [0.06, 0.03]
}

valid_char = ["%p", "*l", "!z", "e@", "&g", "D", "B", "$j", "r", "(h", "m"]