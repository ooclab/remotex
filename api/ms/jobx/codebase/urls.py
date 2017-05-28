from tornado.web import url

from .controllers.public import views as public_views
from .controllers.spider import views as spider_views

handlers = [
    # public api
    url(r'/jobx/job', public_views.JobHandler),
    url(r'/jobx/job/([0-9]+)', public_views.SingleJobHandler),
    url(r'/jobx/job/([0-9]+)/url', public_views.JobURLHandler),

    # spider api
    url(r'/spider/jobx/job', spider_views.JobHandler),
    url(r'/spider/jobx/job/([0-9a-zA-Z_\-]+)', spider_views.SingleJobHandler),
]
