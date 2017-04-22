from eva.web import APIRequestHandler
from eva.sqlalchemy.list import get_limit_objects, get_filters
from app.jobx.models import JobxJob


def public_list_objects(handler, model, q):
    filters = get_filters(handler)
    total = q.count()
    q = get_limit_objects(handler, model, q, filters)

    return {
        'data': [x.ilist_public for x in q.all()],
        'total': total,
        'filter': filters,
    }


class JobHandler(APIRequestHandler):

    def get(self):
        '''查看 Job 列表'''
        q = self.db.query(JobxJob)
        d = public_list_objects(self, JobxJob, q)
        self.success(**d)


class SingleJobHandler(APIRequestHandler):

    def get(self, ID):
        '''查看指定Job详情'''
        job = self.db.query(JobxJob).get(ID)
        if not job:
            return self.fail("can-not-find")
        self.success(**job.iview_public)
