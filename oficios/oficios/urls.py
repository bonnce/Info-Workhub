from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth


#URL PRINCIPAL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='Home'),
    path('Usuarios/',include('apps.Usuarios.urls')),
    path('Comentarios/',include('apps.Comentarios.urls')),
    path('Zonas/',include('apps.Zonas.urls')),
    path('Calificaciones/',include('apps.Calificaciones.urls')),
    path('Login', auth.LoginView.as_view(template_name='Usuarios/Login.html'), name='login'),
]
