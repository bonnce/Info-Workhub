from django.views.generic.edit import CreateView 
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comentarios
from django.urls import reverse_lazy
from ..utils.funciones import PermisosMixin,PasajeMixin
from ..Trabajadores.models import Trabajadores
from ..Stalkers.models import Stalkers
from .forms import ComentariosForm
# Create your views here.

class Comentar(PermisosMixin,PasajeMixin,LoginRequiredMixin,CreateView):
    template_name = 'Comentarios/Comentar.html'
    model = Comentarios
    modelo=Trabajadores
    form_class = ComentariosForm
    success_url = reverse_lazy('Trabajadores:Listar')
    rol='stalker'
    campos=['perfil','objeto']

def Mostrar(request):
    objetos= Comentarios.objects.all()
    return render(request,'Comentarios/Mostrar.html',{'objetos':objetos})