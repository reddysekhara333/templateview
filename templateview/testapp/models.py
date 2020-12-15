from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=20)
    subject=models.CharField(max_length=15)
    marks=models.IntegerField

class student1(models.Model):
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=15)
    marks = models.IntegerField()