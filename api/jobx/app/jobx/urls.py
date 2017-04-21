from tornado.web import url

from .public import views as public_views
from .spider import views as spider_views

handlers = [
    # public api
    url(r'/jobx/article', public_views.ArticleHandler),

    # spider api
    url(r'/spider/jobx/article', spider_views.ArticleHandler),
]
