from django.db import models

# Clase especifica para las imagenes que se pondran en el inicio.

class Iniciales(models.Model):
    titulo = models.CharField('titulo', max_length=140)
    img = models.ImageField()
    texto = models.TextField('texto', max_length=1000)