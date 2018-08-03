from .base import *
from decouple import config
import django_heroku

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = config('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = config('SENDGRID_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

django_heroku.settings(locals())