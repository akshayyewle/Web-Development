from dataclasses import Field
from django.db import models

# Create your models here.
class Model01(models.Model):
    id = models.AutoField(primary_key=True)
    Field01 = models.CharField(max_length=100)
    Field02 = models.CharField(max_length=100)
    Field03 = models.DateField(max_length=100)
    Field04 = models.IntegerField(max_length=100)
    Field05 = models.FloatField(max_length=100)
    Field06 = models.BooleanField(max_length=100)
