from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from ..utils.funciones import PermisosMixin,PasajeMixin
from .forms import CalificacionesForm
from ..Trabajadores.models import Trabajadores
from .models import Calificaciones

class Calificar(LoginRequiredMixin,PermisosMixin,PasajeMixin,CreateView):
    model=Calificaciones
    form_class=CalificacionesForm
    template_name='Calificaciones/Calificar.html'
    rol='stalker'
    campos=['perfil','objeto']