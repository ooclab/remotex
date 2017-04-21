from eva.web import APIRequestHandler


class ArticleHandler(APIRequestHandler):

    def post(self):
        '''上传'''
        d = {"post_id": "xxx213"}
        self.success(**d)
