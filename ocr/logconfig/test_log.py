# -*- coding:UTF-8 -*-
"""
test log settings
"""

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(module)s.%(funcName)s:%(lineno)d %(message)s\n'
        },
        'data': {
            'format': '%(asctime)s|%(message)s',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'ocr': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },

    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'ocr': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },

    }
}


