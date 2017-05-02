#! /usr/bin/env python3

# 加载 Python 内置库
import os
import logging

# 加载第三方库
import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.netutil

from elasticsearch import Elasticsearch

from eva.orm import get_db_session
from eva.utils.findapps import get_site_handlers
from eva.conf import settings


class Application(tornado.web.Application):

    def __init__(self):
        self.db_session = get_db_session()
        self.es = Elasticsearch([{
            'host': settings.ELATICSEARCH_HOST,
            'port': settings.ELATICSEARCH_PORT
        }])


        site_handlers = get_site_handlers()

        tornado_settings = {
            'xsrf_cookies': False,
            'gzip': True,
            'debug': True,
            'secret_key': 'RhXUowgi553yJYvM18xGNc',
        }

        tornado.web.Application.__init__(
            self, site_handlers, **tornado_settings)


def main():
    # 用户配置文件模块路径
    # 重要： EVA_SETTINGS_MODULE 变量设置后，才能使用 settings
    os.environ.setdefault("EVA_SETTINGS_MODULE", "conf.settings")

    import eva.wtforms_json
    eva.wtforms_json.init()

    # 设置 options
    tornado.options.define("port", default=3000, help="listen port", type=int)
    tornado.options.options.logging = "debug"
    tornado.options.parse_command_line()

    # 启动 Tornado
    app = Application()
    server = tornado.httpserver.HTTPServer(app, xheaders=True)

    port = tornado.options.options.port
    sockets = tornado.netutil.bind_sockets(port)

    server.add_sockets(sockets)
    logging.info("api server is running at %d", port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
