from eva.web import APIRequestHandler
from eva.sqlalchemy.list import get_limit_objects, get_filters
from app.jobx.models import JobxJob


def public_list_objects(handler, model, q):
    filters = get_filters(handler)
    total = q.count()
    q = get_limit_objects(handler, model, q, filters)

    return {
        'data': [x.ipublic for x in q.all()],
        'total': total,
        'filter': filters,
    }


class JobHandler(APIRequestHandler):

    def get(self):
        '''查看 article 列表'''
        q = self.db.query(JobxJob)
        d = public_list_objects(self, JobxJob, q)
        self.success(**d)
