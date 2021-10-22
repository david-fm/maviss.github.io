from django.db import models

class Paisajes(models.Model):
    titulo = models.CharField('titulo', max_length=140)
    img = models.ImageField()

class Urbano(models.Model):
    titulo = models.CharField('titulo', max_length=140)
    img = models.ImageField()
