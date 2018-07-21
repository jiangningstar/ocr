# -*- coding: utf-8 -*-

from .base import *

# DEFAULT_CHARSET = "UTF-8"

GUARDIAN_MONKEY_PATCH = False

DOMAIN_SMEDIA = '10.0.255.235:8000'

MEDIA_ROOT = '/data/www/htdocs/smedia/'
MEDIA_URL = '/smedia/'

DOC_ROOT = '/data/doc/'

LOG_ROOT = "/data/logs/linkedsee/"

""" baidu_aip settings """
APP_ID = '11555428'
API_KEY = 'mYby7Q5BL6Ygr3yrxGpIrRMo'
SECRET_KEY = 'UuIkSGiRt6yjTri0D3BF8Qg1iOG2qvgI'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ocr',  # Or path to database file if using sqlite3.
        'USER': 'root',  # Not used with sqlite3.
        'PASSWORD': '',  # Not used with sqlite3.
        'HOST': 'localhost',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
    }
}

LOG_LEVEL = {'root': 'DEBUG', }

from .log import *

LOGGING = get_logging(LOG_ROOT, LOG_LEVEL)
