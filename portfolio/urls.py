from django.urls import path
from .views import VistaDetalle, VistaPortfolio

app_name = 'portfolio'

urlpatterns = [
    path('<pk>/', VistaDetalle.as_view(), name = 'detalle'),
    path('', VistaPortfolio.as_view(), name= 'portfolio'),
]