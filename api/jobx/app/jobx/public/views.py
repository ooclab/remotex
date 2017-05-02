import logging

from sqlalchemy import and_
from sqlalchemy.orm.exc import (
    NoResultFound,
    MultipleResultsFound,
)

from eva.web import APIRequestHandler
from eva.exceptions import EvaError
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


class _BaseSingleJobHandler(APIRequestHandler):

    def prepare(self):
        ID = self.path_args[0]
        try:
            self.job = self.db.query(JobxJob).filter(
                and_(
                    JobxJob.id == ID,
                    JobxJob.status == 0
                )).one()
        except NoResultFound:
            raise EvaError("can not find {0} with id {1}".format(
                JobxJob.__tablename__, ID))
        except MultipleResultsFound:
            raise EvaError(
                "found duplicate objects for {0}".format(JobxJob.__tablename__)
            )


class SingleJobHandler(_BaseSingleJobHandler):

    def get(self, ID):
        '''查看指定Job详情'''
        self.job.view_count += 1
        self.db.commit()
        self.success(**self.job.iview_public)


class JobURLHandler(_BaseSingleJobHandler):

    def get(self, ID):
        '''重定向到来源URL'''
        job = self.job
        es = self.es
        if es:
            body = {
                "ip": self.request.remote_ip,
                "job_id": job.id,
                "created": job.created,
                "Accept-Language": self.request.headers.get('Accept-Language'),
                "User-Agent": self.request.headers.get('User-Agent'),
                "Origin": self.request.headers.get('Origin'),
            }
            es.index(index='jobx_url_click', doc_type='url_click', body=body)
        else:
            logging.warn("Elasticsearch is not ready!")

        self.redirect(self.job.url)
