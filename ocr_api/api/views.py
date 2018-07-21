# -*- coding: utf-8 -*-
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UploadFileSerializer
from django.http import StreamingHttpResponse
from django.conf import settings


class UploadFileHandler(generics.GenericAPIView):
    serializer_class = UploadFileSerializer

    def post(self, request):
        serializer = UploadFileSerializer(data=request.data, context={'file_name': request.data.get('file_name')})
        if serializer.is_valid():
            serializer.save()
            return Response({'download_url': 'http://%s/api/v1/download/?file_name=%s' % (
                settings.DOMAIN_SMEDIA, request.data.get('file_name'))}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DownloadFileHandler(APIView):
    def get(self, request):
        file_name = request.query_params.get('file_name')
        _file = open('/data/doc/%s.docx' % file_name, 'rb')
        response = StreamingHttpResponse(_file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="%s.docx"' % file_name
        return response
