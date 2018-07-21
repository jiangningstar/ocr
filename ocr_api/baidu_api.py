# -*- coding:UTF-8 -*-
from aip import AipOcr
from django.conf import settings

import threading

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger('app_monitor')

Lock = threading.Lock()


def singleton(cls, *args, **kw):
    instance = {}

    def _singleton():
        if cls not in instance:
            try:
                Lock.acquire()
                instance[cls] = cls(*args, **kw)
            finally:
                Lock.release()
        return instance[cls]

    return _singleton


@singleton
class BaiDuClient(object):
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        try:
            api_client = AipOcr(settings.APP_ID, settings.API_KEY, settings.SECRET_KEY)
            return api_client
        except Exception as e:
            logger.error('Connected to baidu_api error message: %s' % e.message)
