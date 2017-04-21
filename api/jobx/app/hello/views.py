from eva.web import APIRequestHandler


class SayHandler(APIRequestHandler):

    def get(self):
        d = {"Hello": "World!"}
        self.success(**d)
