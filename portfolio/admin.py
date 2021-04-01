from django.contrib import admin
from .models import Portfolio

@admin.register(Portfolio)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'img' )