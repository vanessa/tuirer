from .base import *
from decouple import config
import django_heroku
import dj_database_url

# Lembre-se de adicionar essas variáveis
# em "Environment variables" do Heroku!
DROPBOX_OAUTH2_TOKEN = config('DROPBOX_OAUTH2_TOKEN')
DROPBOX_ROOT_PATH = config('DROPBOX_ROOT_PATH')
DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'

ALLOWED_HOSTS = ['.herokuapp.com']

DATABASES['default'] = dj_database_url.parse(config('DATABASE_URL'), conn_max_age=600)

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = config('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = config('SENDGRID_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

