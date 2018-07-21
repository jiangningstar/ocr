from django.conf.urls import url
from .views import UploadFileHandler, DownloadFileHandler

urlpatterns = [
    url(r'^upload/$', UploadFileHandler.as_view()),
    url(r'^download/$', DownloadFileHandler.as_view()),
]
