from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=10)
    marks=models.IntegerField()
    date=models.CharField(max_length=10)