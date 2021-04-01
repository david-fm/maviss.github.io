from django.views.generic import TemplateView, ListView, DetailView
from .models import Items

class VistaDetalle(DetailView):
    model = Items

class VistaTienda(ListView):
    model = Items