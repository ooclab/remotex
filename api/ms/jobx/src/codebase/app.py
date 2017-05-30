# 加载第三方库
import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.netutil

from elasticsearch import Elasticsearch

from eva.sqlalchemy.orm import get_db_session
from eva.conf import settings
from codebase.urls import handlers

import eva.wtforms_json
eva.wtforms_json.init()


class Application(tornado.web.Application):

    def __init__(self):
        self.db_session = get_db_session()
        self.es = Elasticsearch([{
            'host': settings.ELATICSEARCH_HOST,
            'port': settings.ELATICSEARCH_PORT
        }])

        tornado_settings = {
            'xsrf_cookies': False,
            'gzip': True,
            'debug': settings.DEBUG,
            'secret_key': 'RhXUowgi553yJYvM18xGNc',
        }

        tornado.web.Application.__init__(
            self, handlers, **tornado_settings)


def make_app():
    return Application()
