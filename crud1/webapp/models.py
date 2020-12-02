from django.db import models

# Create your models here.
class student(models.Model):
    sname=models.CharField(max_length=20)
    sid=models.IntegerField()
    smarks=models.IntegerField()
    sclass=models.CharField(max_length=20)
