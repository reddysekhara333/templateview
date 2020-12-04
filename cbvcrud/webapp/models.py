from django.db import models
from django.urls import reverse
# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=20)
    marks=models.IntegerField()
    school=models.CharField(max_length=20)
    cls=models.CharField(max_length=8)
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})