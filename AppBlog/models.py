from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    titulo=models.CharField(max_length=1000)
    titulo_de_pagina=models.CharField(max_length=1000)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)#Sirve para borrar todos los post cuando el autor elimine su usuario
    cuerpo=RichTextField(null=True, blank=True)
    #cuerpo=models.TextField()
    imagen=models.ImageField(null=True, blank=True, upload_to='blog')
    fecha=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)
    
    def get_absolute_url(self):
        return reverse('articulo', args=(str(self.id)))

class Perfil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    descripcion = models.TextField()
    imagen=models.ImageField(null=True, blank=True, upload_to='avatares')
    pagina_url=models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)

