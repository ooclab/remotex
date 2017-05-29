import os
from gettext import gettext as _

DEBUG = True
SECRET_KEY = 'FPiCX4lennPwDuXoh'
SERVER_EMAIL = 'admin@ooclab.com'

# TODO: make default
PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        ".."
    )
)

INSTALLED_APPS = (
    'eva.contrib.app.auth',
    'app.jobx',
)

ELATICSEARCH_HOST = "es"
ELATICSEARCH_PORT = 9200


MARKUP_CHOICES = (
    (0, _("Txt")),
    (1, _("Markdown")),
    (2, _("rst")),
)

ABSTRACT_MAX = 128
