# coding: utf-8
from sqlalchemy import Column, Integer, String, TIMESTAMP, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


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
