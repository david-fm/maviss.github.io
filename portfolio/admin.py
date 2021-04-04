from django.contrib import admin
from .models import Paisajes, Urbano

@admin.register(Paisajes)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'img' )

@admin.register(Urbano)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'img' )