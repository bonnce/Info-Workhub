from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth
from django.conf.urls.static import static
from django.conf import settings

#URL PRINCIPAL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='Home'),
    path('Usuarios/',include('apps.Usuarios.urls')),
    path('Trabajadores/',include('apps.Trabajadores.urls')),
    path('Stalkers/',include('apps.Stalkers.urls')),
    path('Comentarios/',include('apps.Comentarios.urls')),
    path('Zonas/',include('apps.Zonas.urls')),
    path('Calificaciones/',include('apps.Calificaciones.urls')),
    path('Login', auth.LoginView.as_view(template_name='Usuarios/Login.html'), name='login'),
    path('Logout', auth.LogoutView.as_view(template_name='Usuarios/Logout.html'), name='logout'),
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
