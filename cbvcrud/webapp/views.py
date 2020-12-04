from django.shortcuts import render
from webapp.models import student
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView
# Create your views here.
class listview(ListView):
    model = student
    template_name = 'test/student_list.html'
    context_object_name = 'student_list'

class Detali(DetailView):
    model = student
    template_name = 'test/student_detail.html'
    context_object_name = 'student_detail'
class create(CreateView):
    model =student
    fields = ('name','marks','school','cls')
    template_name = 'test/student_form.html'
class update(UpdateView):
    model = student
    fields = ('marks','cls')
    template_name = 'test/student_form.html'
class delete(DeleteView):
    model = student
    template_name = 'test/student_confirm_delete.html'
    success_url = reverse_lazy('list')