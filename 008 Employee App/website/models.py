from django.db import models

# Create your models here.
class Student_Model(models.Model):
    name = models.CharField(max_length=50)
    college = models.CharField(max_length=100)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)