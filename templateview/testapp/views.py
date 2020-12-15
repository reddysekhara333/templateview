from django.shortcuts import render

# Create your views here.
from testapp.models import student1
def modls(request):
    form=student1.objects.all()
    return render(request,'app/welocme.html',{'form':form})