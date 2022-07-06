from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import RegistroForm
# Create your views here.

class RegistroUsuarioView(generic.CreateView):
    form_class = RegistroForm
    template_name = 'registro.html'
    success_url = reverse_lazy('Home')