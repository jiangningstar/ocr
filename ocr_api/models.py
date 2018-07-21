from django.db import models


# Create your models here.

class UploadFile(models.Model):
    file_name = models.CharField(max_length=100)
    image = models.ImageField(max_length=1000, upload_to='photos')
