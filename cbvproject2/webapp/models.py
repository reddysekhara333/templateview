from django.db import models
from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    Name=models.CharField(max_length=20)
    author=models.CharField(max_length=15)
    pages=models.PositiveIntegerField()
    price=models.FloatField()

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

