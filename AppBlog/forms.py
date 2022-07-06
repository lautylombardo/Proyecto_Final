from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('titulo', 'titulo_de_pagina','cuerpo','imagen')

        widgets={
            'titulo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Titulo del post'}),
            'titulo_de_pagina': forms.TextInput(attrs={'class': 'form-control','placeholder':'Titulo de la pagina'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control','placeholder':'Añade tu contenido '}),
        }


class EditarForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('titulo','titulo_de_pagina','cuerpo')

        widgets={
            'titulo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Titulo del post'}),
            'titulo_de_pagina': forms.TextInput(attrs={'class': 'form-control','placeholder':'Titulo de la pagina'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control','placeholder':'Añade tu contenido '}),
        }