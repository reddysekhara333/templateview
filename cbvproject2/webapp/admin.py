from django.contrib import admin

# Register your models here.
from webapp.models import Book
class adminbook(admin.ModelAdmin):
    list_display = ['Name','author','pages','price']

admin.site.register(Book,adminbook)