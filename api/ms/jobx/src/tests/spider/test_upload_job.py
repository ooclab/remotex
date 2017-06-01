from eva.utils.time_ import rfc3339_string_utcnow
from codebase.models import JobxJob

from ..base import AsyncHTTPTestCase


class UploadJobTestCase(AsyncHTTPTestCase):

    def test_update_new_job(self):
        '''/spider/job - 上传
        '''

        BODY = '''
<section class="description clearfix">
        <h4 class="title">需求描述</h4>
        <div class="content">
          <p class="">一、需求描述</p>

<p class="">产品类别：活动售票小程序
<br>开发进度：已上线，较完善。
<br>功能：实现 服务通知功能、微信支付功能（已开通微信支付,待开发）、后台某些接口与前端打通
<br>技术：熟悉小程序开发。使用Python语言、django框架；其他语言不建议，重构较麻烦。</p>

<p class="">二、参考产品</p>

<p class="">活动行、秀动、Invite</p>

<p class="">三、人才要求</p>

<p class="">3 年以上Python开发经验，精通MySQL数据，有小程序开发经验。</p>

<p class="">四、其他要求</p>

<p class="">坐班要求：项目间坐班一次，其他时间可以远程。
<br>项目周期：总周期约3天。</p>
        </div>
      </section>
        '''

        d = {
            "platform": "实现网",
            "title": "微信小程序类项目",
            "body": BODY,
            "body_markup": "html",
            "url": "https://shixian.com/jobs/8579",
            "sid": "sx_8579",
            "price": 12000,
            "city": ["北京", "上海"],
            "category": ["微信小程序"],
            "role": ["前端"],
            "skill": ["HTML"],
            "release_date": rfc3339_string_utcnow(),
            "expire_date": rfc3339_string_utcnow(),
            "ext_data": {
                "a": 1,
                "b": 2,
            },
        }
        response = self.http_post('/spider/job', body=d)
        body = self.get_named_body(response)
        self.assertEqual(body.status, "created")

        job = self.db.query(JobxJob).filter_by(sid=d["sid"]).first()
        self.assertEqual(job.title, d["title"])
        self.assertEqual(job.platform.name, d["platform"])
