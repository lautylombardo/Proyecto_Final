from django.urls import path

from Blog.Perfiles.views import PerfilView
from .views import  login


urlpatterns = [
    path('', login, name='Login'),
    path('<int:pk>/perfil', PerfilView.as_view(),name = 'perfil'),
]


