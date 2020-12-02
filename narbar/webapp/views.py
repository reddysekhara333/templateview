from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'testapp/home.html')
def sportes(request):
    return render(request,'testapp/sportes.html')
def movies(request):
    return render(request,'testapp/movies.html')