# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-19 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='file_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]