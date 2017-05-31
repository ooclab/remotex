DEBUG = True
SECRET_KEY = '2PfQWK452fmIul3Kjfc0IJPpCyipjI5pQ3sv0Kc1rtwKfgbrYTepb1v'
SERVER_EMAIL = 'admin@ooclab.com'

DB = {
    'engine': 'postgresql+psycopg2',
    'host': 'postgres',
    'path': '',
    'database': 'remotex',
    'username': 'remotex',
    'password': 'remotex',
}
# DB_URI = "postgresql+psycopg2://remotex:remotex@postgres/remotex"

ELATICSEARCH_HOST = "elasticsearch"
ELATICSEARCH_PORT = 9200

ABSTRACT_MAX = 128
