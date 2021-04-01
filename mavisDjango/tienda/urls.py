from django.urls import path
from .views import VistaDetalle, VistaTienda

app_name = 'tienda'

urlpatterns = [
    path('', VistaTienda.as_view(), name='tienda'),
    path('<pk>/',VistaDetalle.as_view(), name='detalle'),
]