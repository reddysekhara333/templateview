from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q
# Create your vie here.
from django.db.models import Avg,Sum,Count,Max,Min
from testapp.models import student
from django.views import View

def view(request):
    emp=student.object.all()
    return render(request,'app/home.html',{'emp':emp})
