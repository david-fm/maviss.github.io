from django.db import models

class Entrada(models.Model):
    titulo = models.CharField('titulo', max_length=140)
    img = models.ImageField()
    texto = models.TextField('texto', max_length=1000)

