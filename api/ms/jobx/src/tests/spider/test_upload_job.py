from eva.utils.time_ import rfc3339_string_utcnow
from codebase.models import JobxJob

from ..base import AsyncHTTPTestCase


class UploadJobTestCase(AsyncHTTPTestCase):

    def test_update_new_job(self):
        '''/spider/job - 上传
        '''

        d = {
            "title": "Project 1",
            "url": "https://remotex.ooclab.org/project/30214",
            "release_date": rfc3339_string_utcnow(),
            "platform": "码市",
            "checksum": "30214"
        }
        response = self.http_post('/spider/job', body=d)
        body = self.get_named_body(response)
        self.assertEqual(body.status, "created")

        job = self.db.query(JobxJob).filter_by(checksum=d["checksum"]).first()
        self.assertEqual(job.title, d["title"])
        self.assertEqual(job.platform.name, d["platform"])
