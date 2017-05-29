import datetime

from sqlalchemy import and_
from sqlalchemy.orm.exc import (
    NoResultFound,
    MultipleResultsFound,
)

from eva.web import APIRequestHandler
from eva.exceptions import EvaError
from eva.utils.time_ import (
    utc_rfc3339_parse
)

from codebase.models import (
    JobxPlatform,
    JobxCategory,
    JobxRole,
    JobxSkill,
    JobxJob
)
from .forms import JobNewForm, JobEditForm


class JobHandler(APIRequestHandler):

    def post(self):
        '''上传Job'''

        form = JobNewForm.from_json(self.get_body_json())
        if not form.validate():
            return self.fail(errors=form.errors)

        platform = self.db.query(JobxPlatform).filter_by(
            name=form.platform.data).first()
        if not platform:
            platform = JobxPlatform(name=form.platform.data)
            self.db.add(platform)
            self.db.commit()

        # TODO: checksum 和 url 只需要留一个即可?
        newJob = False  # TODO: drop this
        job = self.db.query(JobxJob).filter_by(
            checksum=form.checksum.data).first()
        if not job:
            newJob = True
            # TODO: 新建Job与更新不一定,需要单独的 Form 验证
            job = JobxJob(
                platform=platform,
                title=form.title.data,
                body=form.body.data,
                body_markup=form.body_markup.data
            )
            job.checksum = form.checksum.data

        if not form.body.is_missing:
            job.body = form.body.data
        if not form.body_markup.is_missing:
            job.body_markup = form.body_markup.data
        if not form.url.is_missing:
            job.url = form.url.data
        if not form.price.is_missing:
            job.price = form.price.data
        if not form.city.is_missing:
            job.city = form.city.data

        # TODO: many-to-many 关系更新是否一定删除了旧关系?
        if not form.categories.is_missing:
            categories = []
            for n in form.categories.data:
                item = self.db.query(JobxCategory).filter_by(name=n).first()
                if not item:
                    item = JobxCategory(name=n)
                categories.append(item)
            job.categories = categories

        if not form.roles.is_missing:
            roles = []
            for n in form.roles.data:
                item = self.db.query(JobxRole).filter_by(name=n).first()
                if not item:
                    item = JobxRole(name=n)
                categories.append(item)
            job.roles = roles

        if not form.skills.is_missing:
            skills = []
            for n in form.skills.data:
                item = self.db.query(JobxSkill).filter_by(name=n).first()
                if not item:
                    item = JobxSkill(name=n)
                categories.append(item)
            job.skills = skills

        if not form.release_date.is_missing:
            job.release_date = utc_rfc3339_parse(form.release_date.data)
        if not form.expire_date.is_missing:
            job.expire_date = utc_rfc3339_parse(form.release_date.data)

        # 最后更新
        platform.last_sync = datetime.datetime.utcnow()

        if newJob:
            self.db.add(job)
        else:
            job.updated = datetime.datetime.utcnow()

        self.db.commit()

        if newJob:
            d = {"status": "created", "job_id": job.id}
        else:
            d = {"status": "updated", "job_id": job.id}
        self.success(**d)


class _BaseSingleJobHandler(APIRequestHandler):

    def prepare(self):
        checksum = self.path_args[0]
        try:
            self.job = self.db.query(JobxJob).filter(
                and_(
                    JobxJob.checksum == checksum,
                    JobxJob.status == 0
                )).one()
        except NoResultFound:
            raise EvaError("can not find {0} with checksum {1}".format(
                JobxJob.__tablename__, checksum))
        except MultipleResultsFound:
            raise EvaError("found duplicate objects for {0}".format(JobxJob.__tablename__))


class SingleJobHandler(_BaseSingleJobHandler):

    def head(self, checksum):
        # TODO: 如何处理?
        self.success()

    def get(self, checksum):
        '''获取Job详情'''
        self.success(**self.job.iview_spider)

    def put(self, checksum):
        '''更新指定的Job

        TODO: 同上面JobHandler里的更新是否需要区分?
        '''
        job = self.job

        form = JobEditForm.from_json(self.get_body_json())
        if not form.validate():
            return self.fail(errors=form.errors)

        if not form.platform.is_missing:
            platform = self.db.query(JobxPlatform).filter_by(
                name=form.platform.data).first()
            if not platform:
                platform = JobxPlatform(name=form.platform.data)
                self.db.add(platform)
                self.db.commit()
            job.platform_id = platform.id
        if not form.title.is_missing:
            job.title = form.title.data
        if not form.body.is_missing:
            job.body = form.body.data
        if not form.body_markup.is_missing:
            job.body_markup = form.body_markup.data
        if not form.url.is_missing:
            job.url = form.url.data
        if not form.price.is_missing:
            job.price = form.price.data
        if not form.city.is_missing:
            job.city = form.city.data

        # TODO: many-to-many 关系更新是否一定删除了旧关系?
        if not form.categories.is_missing:
            categories = []
            for n in form.categories.data:
                item = self.db.query(JobxCategory).filter_by(name=n).first()
                if not item:
                    item = JobxCategory(name=n)
                categories.append(item)
            job.categories = categories

        if not form.roles.is_missing:
            roles = []
            for n in form.roles.data:
                item = self.db.query(JobxRole).filter_by(name=n).first()
                if not item:
                    item = JobxRole(name=n)
                categories.append(item)
            job.roles = roles

        if not form.skills.is_missing:
            skills = []
            for n in form.skills.data:
                item = self.db.query(JobxSkill).filter_by(name=n).first()
                if not item:
                    item = JobxSkill(name=n)
                categories.append(item)
            job.skills = skills

        if not form.release_date.is_missing:
            job.release_date = utc_rfc3339_parse(form.release_date.data)
        if not form.expire_date.is_missing:
            job.expire_date = utc_rfc3339_parse(form.release_date.data)

        self.db.commit()
        d = {"status": "updated", "job_id": job.id}
        self.success(**d)

    def delete(self, checksum):
        '''删除Job'''
        self.db.delete(self.job)
        self.db.commit()
        self.success()
