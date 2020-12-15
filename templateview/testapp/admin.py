from django.contrib import admin

# Register your models here.
from testapp.models import  student1
class modeladm(admin.ModelAdmin):
    list_display = ['name','subject','marks']
admin.site.register(student1,modeladm)