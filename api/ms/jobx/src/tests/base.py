import tornado.testing
import json

from eva.utils.dict import convert
from eva.sqlalchemy.orm import create_all, drop_all

from codebase.app import make_app
from eva.sqlalchemy.orm import get_db_session


class AsyncHTTPTestCase(tornado.testing.AsyncHTTPTestCase):

    def get_app(self):
        return make_app()

    @classmethod
    def setUpClass(cls):
        drop_all()
        create_all()

    @classmethod
    def tearDownClass(cls):
        drop_all()

    @property
    def db(self):
        # FIXME! 有时候会死锁
        if not hasattr(self, '_db_session'):
            setattr(self, '_db_session', get_db_session())
        return getattr(self, '_db_session')()

    def get_named_body(self, response, code=0,
                       status_code=200, msg=None, data=None):
        """response 的基本测试并返回 body
        """
        # Check HTTP Status code
        self.assertEqual(response.code, status_code)
        if not response.body:
            return

        body = json.loads(response.body.decode('utf8'))

        # Check Sibbay server return status
        # self.assertEqual(body['status'], status)

        if msg is not None:
            self.assertEqual(body['msg'], msg)

        if data is not None:
            self.assertEqual(body['data'], data)

        if body:
            return convert(body)

    def http_request(self, method, url, headers=None, body=None, **kwargs):
        # TODO: 目前这个 http_request 受限于 sibbay 接口，
        # 绑定了 unitid, uri 等参数设置
        # 另外，也限定了 testcase 的写法最好是一个API对应一个testcase类
        _headers = {}
        if headers:
            _headers.update(headers)

        _body = {"uri": kwargs.get('uri', None)}
        if body:
            _body.update(body)

        return self.fetch(
            url,
            method=method,
            headers=_headers,
            body=json.dumps(_body),
            allow_nonstandard_methods=True
        )

    def http_get(self, url, headers=None, body=None, **kwargs):
        return self.http_request('GET', url, headers, body, **kwargs)

    def http_post(self, url, headers=None, body=None, **kwargs):
        return self.http_request('POST', url, headers, body, **kwargs)

    def http_put(self, url, headers=None, body=None, **kwargs):
        return self.http_request('PUT', url, headers, body, **kwargs)

    def http_delete(self, url, headers=None, body=None, **kwargs):
        return self.http_request('DELETE', url, headers, body, **kwargs)

    def http_patch(self, url, headers=None, body=None, **kwargs):
        return self.http_request('PATCH', url, headers, body, **kwargs)
