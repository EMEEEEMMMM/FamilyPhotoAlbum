from django.db import models
from datetime import datetime


# Create your models here.
class Albumb2017(models.Model):
    img_path = models.CharField(max_length=255)
    pic_time = models.CharField(max_length=255)
    character = models.IntegerField(default=1)


