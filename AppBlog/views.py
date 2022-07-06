from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog
from .forms import BlogForm, EditarForm
from django.urls import reverse_lazy

# Create your views here.
class HomeView(ListView):
    model = Blog
    template_name = "home.html"
    ordering = ['fecha']

class ArticuloView(DetailView):
    model = Blog
    template_name = "articulo.html"

class AgregarView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'agregar.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class EditarView(UpdateView):
    model = Blog
    form_class = EditarForm
    template_name = 'editar.html'

class EliminarView(DeleteView):
    model = Blog
    template_name = 'eliminar.html'
    success_url = reverse_lazy('Home')
