from django.urls import path, include
from . import views

app_name='Trabajadores'

urlpatterns = [
    path('Registro',views.Registro.as_view(),name='registro'),
<<<<<<< HEAD
    path('Listar',views.Listar.as_view(),name='Listar'),
=======
    path('EditarPerfil/<str:pk>',views.EditarPerfil.as_view(),name='editarPerfil'),
>>>>>>> e4dba7ca57cd4efe659a07795059c758ca9187e5
]