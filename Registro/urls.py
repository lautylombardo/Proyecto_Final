from django.urls import path
from .views import RegistroUsuarioView


urlpatterns = [
    path('', RegistroUsuarioView.as_view(), name='registro'),
]
