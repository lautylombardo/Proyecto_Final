from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User



class EditarSettingsForm(UserChangeForm):
    #imagen = forms.ImageField(label='Cambiar avatar',widget=forms.FileInput(attrs={'class': 'form-control'}))
    password = None

    #descripcion = forms.CharField(max_length=20, label='Descripcion',widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }