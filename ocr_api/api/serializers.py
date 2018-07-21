# -*- coding: utf-8 -*-
from rest_framework import serializers
from ocr_api.models import UploadFile
from ocr_api.baidu_api import BaiDuClient
from docx import Document
from django.conf import settings


class UploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFile
        fields = '__all__'

    def create(self, validated_data):
        obj = UploadFile.objects.create(**validated_data)
        file_path = obj.image.path
        print self.context
        file_name = self.context.get('file_name')
        print (file_name)
        result = ImageOcr(file_path=file_path).word_recognition()
        result_list = [x.get('words') for x in result.get('words_result')]
        TextToDoc(result=result_list, file_name=file_name).write_doc()
        return obj


class ImageOcr(object):
    def __init__(self, file_path):
        self.client = BaiDuClient()
        self.file_patn = file_path

    def get_file_content(self, file_path):
        with open(file_path, 'rb') as fp:
            return fp.read()

    def word_recognition(self):
        image = self.get_file_content(self.file_patn)
        options = dict()
        options["detect_direction"] = "true"
        options["probability"] = "true"

        """ 带参数调用通用文字识别（高精度版） """
        return self.client.basicAccurate(image, options)


class TextToDoc(object):
    def __init__(self, result, file_name):
        self.result = result
        self.file_name = file_name

    def write_doc(self):
        document = Document()
        for r in self.result:
            document.add_paragraph(r)
        document.save('%s%s.docx' % (settings.DOC_ROOT, self.file_name))
