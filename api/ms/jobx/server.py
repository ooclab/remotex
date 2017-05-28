#! /usr/bin/env python3

import logging
import tornado.options
from codebase.app import make_app


def main():
    import eva.wtforms_json
    eva.wtforms_json.init()

    # 设置 options
    tornado.options.define("port", default=3000, help="listen port", type=int)
    tornado.options.options.logging = "debug"
    tornado.options.parse_command_line()

    # 启动 Tornado
    app = make_app()
    server = tornado.httpserver.HTTPServer(app, xheaders=True)

    port = tornado.options.options.port
    sockets = tornado.netutil.bind_sockets(port)

    server.add_sockets(sockets)
    logging.info("api server is running at %d", port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
