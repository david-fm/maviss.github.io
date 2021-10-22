from django.urls import path
from .views import VistaDetalle, VistaLista

app_name = 'nankurunaisa'

urlpatterns = [
    path('', VistaLista.as_view(), name='lista'),
    path('<pk>/',VistaDetalle.as_view(), name='paella'),
]