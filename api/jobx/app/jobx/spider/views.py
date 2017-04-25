from eva.web import APIRequestHandler

from app.jobx.models import (
    JobxPlatform,
    JobxCategory,
    JobxRole,
    JobxSkill,
    JobxJob
)
from .forms import JobNewForm
# FIXME! merge to eva
from app.jobx.utils import (
    utc_rfc3339_parse
)


class JobHandler(APIRequestHandler):

    def post(self):
        '''上传Job'''

        form = JobNewForm.from_json(self.get_body_json())
        if not form.validate():
            return self.fail(errors=form.errors)

        # TODO: checksum 和 url 只需要留一个即可?
        if self.db.query(JobxJob).filter_by(
                checksum=form.checksum.data).count() > 0:
            return self.fail("job-exist")

        platform = self.db.query(JobxPlatform).filter_by(
            name=form.platform.data).first()
        if not platform:
            platform = JobxPlatform(name=form.platform.data)
            self.db.add(platform)
            self.db.commit()

        job = JobxJob(
            platform=platform,
            title=form.title.data,
            body=form.body.data,
            body_markup=form.body_markup.data
        )
        job.url = form.url.data
        job.checksum = form.checksum.data
        job.price = form.price.data
        job.city = form.city.data

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
        self.db.add(job)
        self.db.commit()

        d = {"job_id": job.id}
        self.success(**d)
