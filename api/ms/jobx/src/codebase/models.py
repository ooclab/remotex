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
from sqlalchemy import desc
from sqlalchemy.orm import relationship

from eva.sqlalchemy.orm import ORMBase, get_db
from eva.utils.time_ import utc_rfc3339_string

from codebase.utils import get_abstract


jobx_job__city = Table(
    'jobx_job__city', ORMBase.metadata,
    Column('job_id', Integer, ForeignKey('jobx_job.id')),
    Column('city_id', Integer, ForeignKey('jobx_city.id'))
)


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

    name = Column(String(64), nullable=False, unique=True)
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
    def last_sync(self):
        '''最后同步时间'''
        db = get_db()
        job = db.query(JobxJob.updated).filter_by(
            platform_id=self.id).order_by(
                desc(JobxJob.updated)).first()
        return job.updated

    @property
    def isimple(self):
        return {
            "id": self.id,
            "name": self.name,
            "home_url": self.home_url,
            "summary": self.summary,
            "last_sync": utc_rfc3339_string(self.last_sync)
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
            "last_sync": utc_rfc3339_string(self.last_sync),
            'created': utc_rfc3339_string(self.created),
            'updated': utc_rfc3339_string(self.updated),
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
            'created': utc_rfc3339_string(self.created),
            'updated': utc_rfc3339_string(self.updated),
        }

    @property
    def iuser(self):
        return self.ibase

    @property
    def iadmin(self):
        return self.ibase


class JobxCity(_Base, ORMBase):
    '''城市'''

    __tablename__ = 'jobx_city'

    id = Column(Integer, Sequence('jobx_city_id_seq'), primary_key=True)


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
    # Source ID, 唯一性校验值
    sid = Column(String(128), nullable=False)

    # TODO: 不用的币制
    price = Column(Integer, default=0)

    city = relationship(
        'JobxCity',
        secondary=jobx_job__city, backref='job'
    )
    category = relationship(
        'JobxCategory',
        secondary=jobx_job__categroy, backref='job'
    )
    role = relationship(
        'JobxRole',
        secondary=jobx_job__role, backref='job'
    )
    skill = relationship(
        'JobxSkill',
        secondary=jobx_job__skill, backref='job'
    )

    status = Column(Integer, default=0)
    platform_status = Column(String(64))  # 来源平台内部状态

    view_count = Column(Integer, default=0)
    vote_up = Column(Integer, default=0)
    vote_down = Column(Integer, default=0)

    release_date = Column(DateTime, nullable=False)
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
            'abstract': self.abstract,
            'price': self.price,
            'city': [x.name for x in self.city],
            'category': [x.name for x in self.category],
            'role': [x.name for x in self.role],
            'skill': [x.name for x in self.skill],
            'status': self.status,
            'platform_status': self.platform_status,
            'view_count': self.view_count,
            'vote_up': self.vote_up,
            'vote_down': self.vote_down,
            'release_date': utc_rfc3339_string(self.release_date),
            'expire_date': utc_rfc3339_string(self.expire_date),
            'created': utc_rfc3339_string(self.created),
            'updated': utc_rfc3339_string(self.updated),
        }

    @property
    def iview_public(self):
        return {
            'id': self.id,
            'platform': self.platform.isimple,
            'title': self.title,
            'abstract': self.abstract,
            'body': self.body,
            'body_markup': self.body_markup,
            'price': self.price,
            'city': [x.name for x in self.city],
            'category': [x.name for x in self.category],
            'role': [x.name for x in self.role],
            'skill': [x.name for x in self.skill],
            'status': self.status,
            'platform_status': self.platform_status,
            'view_count': self.view_count,
            'vote_up': self.vote_up,
            'vote_down': self.vote_down,
            'release_date': utc_rfc3339_string(self.release_date),
            'expire_date': utc_rfc3339_string(self.expire_date),
            'created': utc_rfc3339_string(self.created),
            'updated': utc_rfc3339_string(self.updated),
        }

    @property
    def iview_spider(self):
        return self.iview_public

    @property
    def abstract(self):
        return get_abstract(self.body, self.body_markup)
