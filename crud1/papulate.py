import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crud1.settings')
import django
django.setup()
from webapp.models import *
from faker import Faker
from random import *
faker=Faker()
def papulate(n):
    for i in range(n):
        fsname=faker.name()
        fsid=randint(1,69)
        fsmarks=randint(70,100)
        fsclass=faker.city()
        student_record=student.objects.get_or_create(sname=fsname,sid=fsid,smarks=fsmarks,sclass=fsclass)

papulate(20)