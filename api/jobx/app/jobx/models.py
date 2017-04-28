import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Sequence,
    DateTime,
    ForeignKey,
    Table
)
from sqlalchemy.orm import relationship

from eva.orm import ORMBase
from eva.utils.time_ import rfc3339_string


jobx_job__categroy = Table(
    'jobx_job__categroy', ORMBase.metadata,
    Column('job_id', Integer, ForeignKey('jobx_job.id')),
    Column('category_id', Integer, ForeignKey('jobx_category.id'))
)


jobx_job__role = Table(
    'jobx_job__role', ORMBase.metadata,
    Column('job_id', Integer, ForeignKey('jobx_job.id')),
    Column('role_id', Integer, ForeignKey('jobx_role.id'))
)


jobx_job__skill = Table(
    'jobx_job__skill', ORMBase.metadata,
    Column('job_id', Integer, ForeignKey('jobx_job.id')),
    Column('skill_id', Integer, ForeignKey('jobx_skill.id'))
)


class JobxPlatform(ORMBase):
    '''任务来源平台
    '''

    __tablename__ = 'jobx_platform'

    id = Column(Integer, Sequence('jobx_platform_id_seq'), primary_key=True)

    name = Column(String(64), nullable=False)
    home_url = Column(String(64))  # 首页地址
    summary = Column(String(1024))
    body = Column(Text)
    body_markup = Column(Integer, default=1)

    created = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, home_url='', summary='', body='', body_markup=1):
        self.name = name
        self.home_url = home_url
        self.summary = summary
        self.body = body
        self.body_markup = body_markup

    @property
    def isimple(self):
        return {
            "id": self.id,
            "name": self.name,
            "home_url": self.home_url,
            "summary": self.summary
        }

    @property
    def ibase(self):
        return {
            "id": self.id,
            "name": self.name,
            "home_url": self.home_url,
            "summary": self.summary,
            "body": self.body,
            "body_markup": self.body_markup,
            'created': rfc3339_string(self.created),
            'updated': rfc3339_string(self.updated),
        }

    @property
    def iuser(self):
        return self.ibase

    @property
    def iadmin(self):
        return self.ibase


class _Base(object):
    '''基本数据表及结构
    '''
    name = Column(String(64), nullable=False)
    summary = Column(String(1024))
    body = Column(Text)
    body_markup = Column(Integer, default=1)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, summary='', body='', body_markup=1):
        self.name = name
        self.summary = summary
        self.body = body
        self.body_markup = body_markup

    @property
    def isimple(self):
        return {
            "id": self.id,
            "name": self.name,
            "summary": self.summary
        }

    @property
    def ibase(self):
        return {
            "id": self.id,
            "name": self.name,
            "summary": self.summary,
            "body": self.body,
            "body_markup": self.body_markup,
            'created': rfc3339_string(self.created),
            'updated': rfc3339_string(self.updated),
        }

    @property
    def iuser(self):
        return self.ibase

    @property
    def iadmin(self):
        return self.ibase


class JobxCategory(_Base, ORMBase):
    '''工作类别

    如：网站, 移动应用, 微信, H5, 咨询
    '''

    __tablename__ = 'jobx_category'

    id = Column(Integer, Sequence('jobx_category_id_seq'), primary_key=True)


class JobxRole(_Base, ORMBase):
    '''工作角色

    如：项目管理, 产品经理, 设计, 开发, 测试, 运维, 市场, 运营
    '''

    __tablename__ = 'jobx_role'

    id = Column(Integer, Sequence('jobx_role_id_seq'), primary_key=True)


class JobxSkill(_Base, ORMBase):
    '''技能

    C/C++, C#, PHP, RUBY, PYTHON, IOS, ANDROID, JAVA, GO, NODEJS, ...
    '''

    __tablename__ = 'jobx_skill'

    id = Column(Integer, Sequence('jobx_skill_id_seq'), primary_key=True)


class JobxJob(ORMBase):

    '''工作/任务

    - 远程
    - 兼职
    - 外包
    - 众包
    '''

    __tablename__ = 'jobx_job'

    id = Column(Integer, Sequence('jobx_job_id_seq'), primary_key=True)

    platform_id = Column(Integer, ForeignKey('jobx_platform.id'))
    platform = relationship("JobxPlatform", backref="jobs")

    title = Column(String(512), nullable=False)
    body = Column(Text)
    body_markup = Column(Integer, default=1)

    # 来源网址
    url = Column(String(1024), nullable=False)
    # 唯一性校验值
    checksum = Column(String(128), nullable=False)

    # TODO: 不用的币制
    price = Column(Integer, default=0)
    city = Column(String(64))

    categories = relationship(
        'JobxCategory',
        secondary=jobx_job__categroy, backref='jobs'
    )
    roles = relationship(
        'JobxRole',
        secondary=jobx_job__role, backref='jobs'
    )
    skills = relationship(
        'JobxSkill',
        secondary=jobx_job__skill, backref='jobs'
    )

    status = Column(Integer, default=0)

    view_count = Column(Integer, default=0)
    vote_up = Column(Integer, default=0)
    vote_down = Column(Integer, default=0)

    release_date = Column(DateTime)
    expire_date = Column(DateTime)

    created = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, platform, title, body, body_markup=1):
        self.platform_id = platform.id
        self.title = title
        self.body = body
        self.body_markup = body_markup

    def to_vote(self, vote):
        if vote > 0:
            self.vote_up += vote
        else:
            self.vote_down += vote

    @property
    def ilist_public(self):
        return {
            'id': self.id,
            'platform': self.platform.isimple,
            'title': self.title,
            'url': self.url,
            'price': self.price,
            'city': self.city,
            'categories': [x.isimple for x in self.categories],
            'roles': [x.isimple for x in self.roles],
            'skills': [x.isimple for x in self.skills],
            'status': self.status,
            'view_count': self.view_count,
            'vote_up': self.vote_up,
            'vote_down': self.vote_down,
            'release_date': rfc3339_string(self.release_date),
            'expire_date': rfc3339_string(self.expire_date),
            'created': rfc3339_string(self.created),
            'updated': rfc3339_string(self.updated),
        }

    @property
    def iview_public(self):
        return {
            'id': self.id,
            'platform': self.platform.isimple,
            'title': self.title,
            'body': self.body,
            'body_markup': self.body_markup,
            'url': self.url,
            'price': self.price,
            'city': self.city,
            'categories': [x.isimple for x in self.categories],
            'roles': [x.isimple for x in self.roles],
            'skills': [x.isimple for x in self.skills],
            'status': self.status,
            'view_count': self.view_count,
            'vote_up': self.vote_up,
            'vote_down': self.vote_down,
            'release_date': rfc3339_string(self.release_date),
            'expire_date': rfc3339_string(self.expire_date),
            'created': rfc3339_string(self.created),
            'updated': rfc3339_string(self.updated),
        }

    @property
    def iview_spider(self):
        return self.iview_public
