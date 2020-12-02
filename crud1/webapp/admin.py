from django.contrib import admin

# Register your models here.
from webapp.models import student
class studentadmin(admin.ModelAdmin):
    list_display = ['sname','sid','smarks','sclass']

admin.site.register(student,studentadmin)