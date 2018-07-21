# -*- coding:UTF-8 -*-
from django.conf import settings


class DisableCSRF(object):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
