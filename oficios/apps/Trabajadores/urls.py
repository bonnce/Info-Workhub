from django.urls import path, include
from . import views

app_name='Trabajadores'

urlpatterns = [
    path('Registro',views.Registro.as_view(),name='registro'),
    path('Listar',views.Listar.as_view(),name='Listar'),
    path('EditarPerfil/<str:pk>',views.EditarPerfil.as_view(),name='editarPerfil'),
]