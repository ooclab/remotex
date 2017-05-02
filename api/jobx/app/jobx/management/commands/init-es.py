from eva.management.common import EvaManagementCommand

from app.jobx.utils import get_elasticsearch


url_click_mappings = {
    "url_click": {
        "_all": {
            "analyzer": "ik_smart",
            "search_analyzer": "ik_smart",
            "term_vector": "no",
            "store": "false"
        },
        "properties": {
            "ip": {
                "type": "ip",
            },
            "job_id": {
                "type": "integer",
            },
            "created": {
                "type": "date",
            },
            "Accept-Language": {
                "type": "string",
            },
            "User-Agent": {
                "type": "text",
                "analyzer": "ik_smart",
                "search_analyzer": "ik_smart",
                "include_in_all": "true",
                "boost": 8
            },
            "Origin": {
                "type": "string",
            },
        }
    }
}


class Command(EvaManagementCommand):

    def __init__(self):
        super(Command, self).__init__()

        self.cmd = 'init-es'
        self.help = '初始化Elasticsearch'

    def run(self):

        es = get_elasticsearch()

        index_name = 'jobx_url_click'

        # 删除旧索引
        es.indices.delete(index_name, ignore=404)

        # ignore 400 cause by IndexAlreadyExistsException
        es.indices.create(
            index=index_name,
            ignore=400,
            body={"mappings": url_click_mappings}
        )
