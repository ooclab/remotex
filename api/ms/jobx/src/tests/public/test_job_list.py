import datetime

from codebase.models import JobxJob, JobxPlatform
from ..base import AsyncHTTPTestCase


class JobTestCase(AsyncHTTPTestCase):

    def create_job(self):

        platform = JobxPlatform(name="码市")
        self.db.add(platform)
        self.db.commit()

        job = JobxJob(
            title="Project 1",
            platform=platform,
            body="项目１"
        )
        job.url = "https://shixian.com/jobs/8579"
        job.release_date = datetime.datetime.utcnow()
        job.sid = 'sx_8579'
        job.price = 12000
        self.db.add(job)
        self.db.commit()
        return job

    def delete_job(self, job):
        self.db.delete(job.platform)
        self.db.delete(job)
        self.db.commit()

    def test_list(self):
        '''/job - 列表
        '''
        db_job = self.create_job()
        response = self.http_get('/job')
        body = self.get_named_body(response)
        job = body.data[0]
        self.assertEqual(db_job.id, job.id)
        self.assertEqual(db_job.title, job.title)
        self.assertEqual(db_job.price, job.price)
        self.assertEqual(db_job.platform.name, job.platform)
        self.delete_job(db_job)

    def test_page(self):
        '''/job - 分页
        '''
        db_job = self.create_job()
        response = self.http_get('/job?p=2')
        body = self.get_named_body(response)
        self.assertEqual(body.total, 0)
        self.delete_job(db_job)
