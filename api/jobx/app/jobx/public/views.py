from eva.web import APIRequestHandler


class ArticleHandler(APIRequestHandler):

    def get(self):
        '''查看 article 列表'''
        d = {"article": "list"}
        self.success(**d)
