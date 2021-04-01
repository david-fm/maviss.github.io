from django.db import models

class Portfolio(models.Model):
    titulo = models.CharField('titulo', max_length=140)
    img = models.ImageField()
