from django.views.generic import TemplateView, ListView, DetailView
from .models import Portfolio

class VistaDetalle(DetailView):
    model = Portfolio

class VistaPortfolio(ListView):
    model = Portfolio