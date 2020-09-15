from django.urls import path, include
from . import views

app_name='Usuarios'
urlpatterns = [
    path('Perfil',views.Perfil,name='perfil')
]