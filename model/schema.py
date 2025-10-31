# coding: utf-8
from sqlalchemy import Column, Integer, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


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
    register_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    last_active_time = Column(TIMESTAMP)
    status = Column(String(20))
    business_id = Column(Integer, server_default=text("'0'"), comment='商家ID_busiess_content')
    admin_id = Column(Integer, server_default=text("'0'"), comment='所属商家管理id')
    user_pic = Column(String(512), comment='头像url')
    user_info = Column(Text, comment='用户备注')


class TBalance(Base):
    __tablename__ = 't_balance'
    __table_args__ = {'comment': '用户账户余额表，用户的余额历史 记录，不可修改，只能增加'}

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


class TChinesePointSubject(Base):
    __tablename__ = 't_chinese_point_subject'
    __table_args__ = {'comment': '语文知识点与重点题表'}

    cps_id = Column(Integer, primary_key=True, comment='主键id')
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    cps_content = Column(Text, comment='知识点或重点题内容')
    cps_create_name = Column(String(100), comment='创建人')
    class_id = Column(Integer, server_default=text("'0'"), comment='所属年级id')
    subject_id = Column(Integer, server_default=text("'0'"), comment='所属科目点id')
    knowledge_id = Column(Integer, server_default=text("'0'"), comment='所属知识点id')
    answer_txt = Column(Text, comment='文本回答')
    answer_pic_path = Column(String(200), comment='图片回答路径')
    answer_audio_path = Column(String(200), comment='多媒体回答路径')
    knowledge_list = Column(String(200), comment='所属知识点列表，逗号分割')


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


class TEnglishPointSubject(Base):
    __tablename__ = 't_english_point_subject'
    __table_args__ = {'comment': '英语知识点与重点题表'}

    eps_id = Column(Integer, primary_key=True, comment='主键id')
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    eps_content = Column(Text, comment='知识点或重点题内容')
    eps_create_name = Column(String(100), comment='创建人')
    class_id = Column(Integer, server_default=text("'0'"), comment='所属年级id')
    subject_id = Column(Integer, server_default=text("'0'"), comment='所属科目点id')
    knowledge_id = Column(Integer, server_default=text("'0'"), comment='所属知识点id')
    answer_txt = Column(Text, comment='文本回答')
    answer_pic_path = Column(String(200), comment='图片回答路径')
    answer_audio_path = Column(String(200), comment='多媒体回答路径')
    knowledge_list = Column(String(200), comment='所属知识点列表，逗号分割')


class TKnowledgePoint(Base):
    __tablename__ = 't_knowledge_point'
    __table_args__ = {'comment': '知识点目录表'}

    kn_id = Column(Integer, primary_key=True, comment='主键id')
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    kn_name = Column(String(100), comment='知识点名称')
    kn_create_name = Column(String(100), comment='创建人')
    class_id = Column(Integer, server_default=text("'0'"), comment='所属年级id')
    subject_id = Column(Integer, server_default=text("'0'"), comment='所属科目点id')


class TMathPointSubject(Base):
    __tablename__ = 't_math_point_subject'
    __table_args__ = {'comment': '数学知识点与重点题表'}

    mps_id = Column(Integer, primary_key=True, comment='主键id')
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    mps_content = Column(Text, comment='知识点或重点题内容')
    mps_create_name = Column(String(100), comment='创建人')
    class_id = Column(Integer, server_default=text("'0'"), comment='所属年级id')
    subject_id = Column(Integer, server_default=text("'0'"), comment='所属科目点id')
    knowledge_id = Column(Integer, server_default=text("'0'"), comment='所属知识点id')
    answer_txt = Column(Text, comment='文本回答')
    answer_pic_path = Column(String(200), comment='图片回答路径')
    answer_audio_path = Column(String(200), comment='多媒体回答路径')
    knowledge_list = Column(String(200), comment='所属知识点列表，逗号分割')


class TQuestionType(Base):
    __tablename__ = 't_question_type'
    __table_args__ = {'comment': '题型目录表'}

    qu_id = Column(Integer, primary_key=True, comment='主键id')
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    qu_name = Column(String(100), comment='题型目录名称')
    qu_create_name = Column(String(100), comment='创建人')
    class_id = Column(Integer, server_default=text("'0'"), comment='所属年级id')
    subject_id = Column(Integer, server_default=text("'0'"), comment='所属科目点id')
    knowledge_id = Column(Integer, server_default=text("'0'"), comment='所属知识点id')
    knowledge_list = Column(String(200), comment='所属知识点列表，逗号分割')


class TRemainPointSubject(Base):
    __tablename__ = 't_remain_point_subject'
    __table_args__ = {'comment': '其他知识点与重点题表'}

    rps_id = Column(Integer, primary_key=True, comment='主键id')
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    rps_content = Column(Text, comment='知识点或重点题内容')
    rps_create_name = Column(String(100), comment='创建人')
    class_id = Column(Integer, server_default=text("'0'"), comment='所属年级id')
    subject_id = Column(Integer, server_default=text("'0'"), comment='所属科目点id')
    knowledge_id = Column(Integer, server_default=text("'0'"), comment='所属知识点id')
    answer_txt = Column(Text, comment='文本回答')
    answer_pic_path = Column(String(200), comment='图片回答路径')
    answer_audio_path = Column(String(200), comment='多媒体回答路径')
    knowledge_list = Column(String(200), comment='所属知识点列表，逗号分割')


class TShClas(Base):
    __tablename__ = 't_sh_class'
    __table_args__ = {'comment': '年级表'}

    cl_id = Column(Integer, primary_key=True, comment='主键id')
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    cl_name = Column(String(100), comment='年级名称')
    cl_create_name = Column(String(100), comment='创建人')


class TShSubject(Base):
    __tablename__ = 't_sh_subject'
    __table_args__ = {'comment': '学科表'}

    su_id = Column(Integer, primary_key=True, comment='主键id')
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    su_name = Column(String(100), comment='学科名称')
    su_create_name = Column(String(100), comment='创建人')
    class_id = Column(Integer, server_default=text("'0'"), comment='所属年级id')
    knowledge_list = Column(String(200), comment='所属知识点列表，逗号分割')


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
    manage_id = Column(Integer, server_default=text("'0'"), comment='管理等级 默认是0')
