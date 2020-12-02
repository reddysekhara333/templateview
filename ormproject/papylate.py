import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ormproject.settings')
import django
django.setup()
from faker import Faker
from random import *
from testapp.models import *
faker=Faker()
def hello(n):
    for i in range(n):
        fname=faker.name()
        fmarks=randint(40,99)
        fdate=faker.name()
        record=student.objects.get_or_create(name=fname,marks=fmarks,date=fdate)
hello(15)