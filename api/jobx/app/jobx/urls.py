from tornado.web import url

from .public import views as public_views
from .spider import views as spider_views

handlers = [
    # public api
    url(r'/jobx/job', public_views.JobHandler),

    # spider api
    url(r'/spider/jobx/job', spider_views.JobHandler),
]
