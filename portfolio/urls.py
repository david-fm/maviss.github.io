from django.urls import path
from .views import VistaPortfolio, VistaDetallePaisajes, VistaPaisajes, VistaDetalleUrbano, VistaUrbano

app_name = 'portfolio'

urlpatterns = [
    path('urbano/<pk>/',VistaDetalleUrbano.as_view(), name = 'urbano_detalle'),
    path('urbano/', VistaUrbano.as_view(), name = 'urbano'),
    path('paisajes/', VistaPaisajes.as_view(), name = 'paisajes'),
    path('paisajes/<pk>/', VistaDetallePaisajes.as_view(), name = 'paisajes_detalle'),
    path('', VistaPortfolio.as_view(), name= 'portfolio'),
]