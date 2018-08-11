from .base import *
from decouple import config
import django_heroku

# Lembre-se de adicionar essas variáveis
# em "Environment variables" do Heroku!
DROPBOX_OAUTH2_TOKEN = config('DROPBOX_OAUTH2_TOKEN')
DROPBOX_ROOT_PATH = config('DROPBOX_ROOT_PATH')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = config('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = config('SENDGRID_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

django_heroku.settings(locals())

INSTALLED_APPS += ('django_storages', )
DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'