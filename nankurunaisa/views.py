from django.views.generic import TemplateView, ListView, DetailView
from .models import Entrada

class VistaDetalle(DetailView):
    model = Entrada
   # template_name = 'Nankurunaisa.html'
class VistaLista(ListView):
    model =Entrada
