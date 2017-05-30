from eva.utils.time_ import rfc3339_string_utcnow
from codebase.models import JobxJob

from ..base import AsyncHTTPTestCase


class UploadJobTestCase(AsyncHTTPTestCase):

    def test_update_new_job(self):
        '''/spider/job - 上传
        '''

        d = {
            "platform": "码市",
            "title": "项目1",
            "url": "https://path/to/job/1222",
            "body": "abc",
            "sid": "12345",
            "release_date": rfc3339_string_utcnow()
        }
        response = self.http_post('/spider/job', body=d)
        body = self.get_named_body(response)
        self.assertEqual(body.status, "created")

        # FIXME! self.db 会死锁
        from eva.sqlalchemy.orm import get_db
        db = get_db()

        job = db.query(JobxJob).filter_by(sid=d["sid"]).first()
        self.assertEqual(job.title, d["title"])
        self.assertEqual(job.platform.name, d["platform"])
