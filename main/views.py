from django.views.generic import TemplateView
from .models import Iniciales
# Create your views here.

class VistaMain(TemplateView):
    model = Iniciales
    template_name='index.html'