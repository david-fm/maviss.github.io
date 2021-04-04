from django.views.generic import TemplateView, ListView, DetailView
from .models import Paisajes, Urbano

class VistaPortfolio(TemplateView):
    template_name='Portfolio'

class VistaDetalleUrbano(DetailView):
    model = Urbano

class VistaUrbano(ListView):
    model = Urbano

class VistaDetallePaisajes(DetailView):
    model = Paisajes

class VistaPaisajes(ListView):
    model = Paisajes