import datetime

from elasticsearch import Elasticsearch

from eva.conf import settings


def get_elasticsearch():
    es = Elasticsearch([{
        'host': settings.ELATICSEARCH_HOST,
        'port': settings.ELATICSEARCH_PORT
    }])
    return es
