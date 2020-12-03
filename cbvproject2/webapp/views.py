from django.shortcuts import render

# Create your views here.
from webapp.models import Book
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
class List_view(ListView):
    model = Book
    template_name = 'testapp/book_list.html'
    context_object_name = 'book_list'

class Detalie_view(DetailView):
    model = Book
    template_name = 'testapp/book_detail.html'
    context_object_name = 'book'
class create_view(CreateView):
    model = Book
    fields = ('Name','author','pages','price')
    template_name = 'testapp/book_form.html'

class update(UpdateView):
    model = Book
    fields = ('author','price')
    template_name = 'testapp/book_form.html'