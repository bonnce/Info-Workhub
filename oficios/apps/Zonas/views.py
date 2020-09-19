from django.views.generic.edit import CreateView 
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Zonas
from django.urls import reverse_lazy
from ..utils.funciones import PermisosMixin,PasajeMixin
from ..Zonas.models import Zonas
from ..Zonas.models import Zonas
from .forms import ZonasForm
# Create your views here.

class verZonas(PermisosMixin,PasajeMixin,LoginRequiredMixin,CreateView):
    template_name = 'Zonas/verZonas.html'
    model = Zonas
    modelo = Zonas
    form_class = ZonasForm
    success_url = reverse_lazy('Home')
    rol='trabajador'
    campos=['perfil','objeto']

def Mostrar(request):
    objetos= Zonas.objects.all()
    return render(request,'Zonas/verZonas.html',{'objetos':objetos})