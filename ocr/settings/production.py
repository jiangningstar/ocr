# -*- coding: utf-8 -*-

from .base import *

# DEFAULT_CHARSET = "UTF-8"

DEBUG = False

GUARDIAN_MONKEY_PATCH = False

DOMAIN_SMEDIA = '127.0.0.1:8000'

MEDIA_ROOT = '/data/www/htdocs/smedia/'
MEDIA_URL = '/smedia/'

DOC_ROOT = '/data/doc/'

LOG_ROOT = "/data/logs/linkedsee/"

""" baidu_aip settings """
APP_ID = '11555428'
API_KEY = 'mYby7Q5BL6Ygr3yrxGpIrRMo'
SECRET_KEY = 'UuIkSGiRt6yjTri0D3BF8Qg1iOG2qvgI'

LOG_LEVEL = {'root': 'DEBUG', }

from .log import *

LOGGING = get_logging(LOG_ROOT, LOG_LEVEL)
