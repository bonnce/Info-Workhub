from django.contrib import admin
from django.urls import path
from . import views

app_name='Calificaciones'

urlpatterns = [
    path('Calificar/',views.Calificar.as_view(),name='Calificar'),
]