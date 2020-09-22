from django.views.generic.edit import CreateView 
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from ..Zonas.models import Zonas
from django.urls import reverse_lazy
from ..utils.funciones import PermisosMixin,PasajeMixin
from .forms import ZonasForm
from django.views.generic.list import ListView
# Create your views here.

class ListarZonas(ListView):
	model = Zonas
	template_name = 'Zonas/listar.html'
     