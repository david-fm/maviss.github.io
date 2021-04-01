from django.contrib import admin
from .models import Items

@admin.register(Items)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'img', 'texto', 'precio', 'unidades' )