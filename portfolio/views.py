from django.views.generic import TemplateView, ListView, DetailView
from .models import Paisajes, Urbano

class VistaPortfolio(TemplateView):
    template_name='index.html'

class VistaDetalleUrbano(DetailView):
    model = Urbano
    template_name = 'urbano_detail.html'

class VistaUrbano(ListView):
    model = Urbano
    template_name = 'urbano_list.html'

class VistaDetallePaisajes(DetailView):
    model = Paisajes
    template_name = 'paisajes_detail.html'

class VistaPaisajes(ListView):
    model = Paisajes
    template_name = 'paisajes_list.html'