from django.shortcuts import render,redirect

# Create your views here.
from webapp.forms import studentform
from webapp.models import student
def studet_view(request):
    hh=student.objects.all()
    return render(request,'test/read.html',{'hh':hh})

def delete_view(request,id):
    tt=student.objects.get(id=id)
    tt.delete()
    return redirect('/view')
def  update_view(request,id):
    t=student.objects.get(id=id)
    if request.method=='POST':
        torm=studentform(request.POST,instance=t)
        if torm.is_valid():
            torm.save()
        return redirect('/view')

    return render(request,'test/update.html',{'t':t})