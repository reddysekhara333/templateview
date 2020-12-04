from django.contrib import admin

# Register your models here.
from webapp.models import  student
class viewadin(admin.ModelAdmin):
    list_display = ['name','marks','school','cls']
admin.site.register(student,viewadin)