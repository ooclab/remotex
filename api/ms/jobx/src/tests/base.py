import eva.testing
from eva.orm import create_all, drop_all

from codebase.app import make_app


class AsyncHTTPTestCase(eva.testing.AsyncHTTPTestCase):

    unitid = '983628388108f1bb5e962bb012a8a5d6e69f126b'

    def get_app(self):
        return make_app()

    @classmethod
    def setUpClass(cls):
        create_all()

    @classmethod
    def tearDownClass(cls):
        drop_all()

    @property
    def db(self):
        if not hasattr(self, '_db'):
            app = self.get_app()
            setattr(self, '_db', app.db_session())
        return getattr(self, '_db')
