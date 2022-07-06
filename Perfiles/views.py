from django.shortcuts import  get_object_or_404, render
from django.views import generic
from django.views.generic import DetailView
from django.urls import reverse_lazy
from AppBlog.models import Perfil
from .forms import EditarSettingsForm


# Create your views here.
class PerfilView(DetailView):
    model = Perfil
    template_name = 'perfil.html'

    def get_context_data(self, *args, **kwargs):
        users = Perfil.objects.all()
        context = super(PerfilView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Perfil, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

class EditarSettingsView(generic.UpdateView):
    form_class = EditarSettingsForm
    template_name = 'editarSettings.html'
    success_url = reverse_lazy('Home') 

    def get_object(self):
        return self.request.user

class EditarPerfilView(generic.UpdateView):
    model = Perfil
    template_name = 'editarPerfil.html'
    fields = ['descripcion','imagen']
    success_url = reverse_lazy('Home')

    