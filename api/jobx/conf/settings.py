import os

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
    'app.hello',
)
