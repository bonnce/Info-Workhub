from django.urls import path, include
from . import views

app_name='Zonas'

urlpatterns = [
    path('Zonas',views.Mostrar,name='verZonas'),
    
]