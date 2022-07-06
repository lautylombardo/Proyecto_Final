from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    username = forms.CharField(max_length=20, label='Nombre de usuario',widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Correo Electronico',widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=200, label='Nombre',widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=200, label='Apellido',widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.Field(label='Contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.Field(label='Confirme su contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        help_texts = {k:"" for k in fields}

    
