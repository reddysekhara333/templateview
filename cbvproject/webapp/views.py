from django.shortcuts import render

# Create your views here.
from django.views.generic import View,TemplateView,ListView,DetailView
from webapp.models import Book
from django.http import HttpResponse
class Helloworld(View):
    def get(self,request):
        return HttpResponse('hello welocme to calss based views')

class templateview(TemplateView):
    template_name = 'test/view.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='chinna'
        context['id']='199'
        return context


class tembook(ListView):
    model = Book
    template_name = 'test/book_list.html'
    context_object_name = 'list_book'

class dtailer(DetailView):
    model = Book