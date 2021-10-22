from django.urls import path
from .views import VistaMain

app_name = 'main'

urlpatterns = [
    path('', VistaMain.as_view(), name = 'main')
]