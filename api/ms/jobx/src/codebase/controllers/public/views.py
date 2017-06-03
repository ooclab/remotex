import logging
import datetime

from sqlalchemy import and_, desc, asc
from sqlalchemy.orm.exc import (
    NoResultFound,
    MultipleResultsFound,
)

from eva.web import APIRequestHandler
from eva.exceptions import EvaError
from eva.conf import settings

from codebase.models import JobxJob


class JobHandler(APIRequestHandler):

    ALLOW_ORDER_BY = [
        'created', 'updated', 'release_date', 'expire_date',
        'price', 'status', 'view_count']

    def get(self):
        '''查看 Job 列表'''

        # 查询指定天数内的Job
        days = self.get_argument('days', 90)
        after_date = datetime.datetime.utcnow() - datetime.timedelta(days=days)

        q = self.db.query(JobxJob).filter(
            and_(
                JobxJob.release_date > after_date,
                JobxJob.inner_status == 0
            )
        )

        total = q.count()

        # order
        is_asc = self.get_argument('asc', False)
        order_by = self.get_argument('order_by', 'created')
        if order_by not in self.ALLOW_ORDER_BY:
            return self.fail('unknown-order')
        q = q.order_by(asc(order_by) if is_asc else desc(order_by))

        # 分页
        current_page = int(self.get_argument('current_page', 1))
        if current_page < 1:
            return self.fail('no such page')
        page_size = int(self.get_argument('page_size', settings.PAGE_SIZE))
        start = (current_page - 1) * page_size
        stop = current_page * page_size
        q = q.slice(start, stop)

        self.success(**{
            'data': [x.ilist_public for x in q.all()],
            'total': total,
            'filter': {
                'page_size': page_size,
                'current_page': current_page,
                'asc': str(is_asc).lower(),
                'order_by': order_by,
            },
        })


class _BaseSingleJobHandler(APIRequestHandler):

    def prepare(self):
        ID = self.path_args[0]
        try:
            self.job = self.db.query(JobxJob).filter(
                and_(
                    JobxJob.id == ID,
                    JobxJob.inner_status == 0
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

        job.view_count += 1
        self.db.commit()

        self.redirect(self.job.url)
