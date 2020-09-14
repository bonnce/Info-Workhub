from django.urls import path, include
from . import views

app_name='Trabajadores'

urlpatterns = [
    path('Registro',views.Registro.as_view(),name='registro'),
]