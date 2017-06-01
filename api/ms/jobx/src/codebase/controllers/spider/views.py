import datetime

from eva.web import APIRequestHandler
from eva.utils.time_ import (
    utc_rfc3339_parse
)

from codebase.models import (
    JobxPlatform,
    JobxCity,
    JobxCategory,
    JobxRole,
    JobxSkill,
    JobxJob
)
from codebase.utils import get_markup_value
from .forms import JobNewForm


class JobHandler(APIRequestHandler):

    def post(self):
        '''上传Job'''

        body = self.get_body_json()
        form = JobNewForm.from_json(body)
        if not form.validate():
            return self.fail(errors=form.errors)

        platform = self.db.query(JobxPlatform).filter_by(
            name=form.platform.data).first()
        if not platform:
            platform = JobxPlatform(name=form.platform.data)
            self.db.add(platform)
            self.db.commit()

        body_markup = get_markup_value(form.body_markup.data)

        # TODO: checksum 和 url 只需要留一个即可?
        newJob = False  # TODO: drop this
        job = self.db.query(JobxJob).filter_by(
            sid=form.sid.data).first()
        if not job:
            newJob = True
            # TODO: 新建Job与更新不一定,需要单独的 Form 验证
            job = JobxJob(
                platform=platform,
                title=form.title.data,
                body=form.body.data,
                body_markup=body_markup
            )
            job.sid = form.sid.data

        if not form.body.is_missing:
            job.body = form.body.data
        if not form.body_markup.is_missing:
            job.body_markup = body_markup
        if not form.url.is_missing:
            job.url = form.url.data
        if not form.price.is_missing:
            job.price = form.price.data

        if not form.release_date.is_missing:
            job.release_date = utc_rfc3339_parse(form.release_date.data)
        if not form.expire_date.is_missing:
            job.expire_date = utc_rfc3339_parse(form.release_date.data)

        job.city = self.get_many(form.city, JobxCity)
        job.category = self.get_many(form.category, JobxCategory)
        job.role = self.get_many(form.role, JobxRole)
        job.skill = self.get_many(form.skill, JobxSkill)

        # 扩展属性
        if 'ext_data' in body:
            job.ext_data = body['ext_data']

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

    def get_many(self, form_column, cls):
        L = []
        if not form_column.is_missing:
            for n in form_column.data:
                item = self.db.query(cls).filter_by(name=n).first()
                if not item:
                    item = cls(name=n)
                L.append(item)
        return L
