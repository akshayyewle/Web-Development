from django.db import models

# Create your models here.
class Emp(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=20)
    emp_phone = models.IntegerField()
    emp_dept = models.CharField(max_length=20)
    emp_working = models.BooleanField()