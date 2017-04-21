from tornado.web import url

from . import views

handlers = [
    url(r'/hello/say', views.SayHandler),
]
