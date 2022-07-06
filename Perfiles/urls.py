from django.urls import path
from .views import EditarPerfilView, EditarSettingsView, PerfilView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('editar_settings', EditarSettingsView.as_view(), name= 'Editar_Settings' ),
    path('password/', auth_views.PasswordChangeView.as_view(), name='Cambiar_Contraseña'),
    path('<int:pk>/perfil/', PerfilView.as_view(), name='perfil'),
    path('<int:pk>/editar_perfil/', EditarPerfilView.as_view(), name='editar_perfil'),
]
