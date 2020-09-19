from django.views.generic.edit import CreateView 
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comentarios
from django.urls import reverse_lazy
from ..utils.funciones import PermisosMixin,PasajeMixin
from ..Trabajadores.models import Trabajadores
from ..Stalkers.models import Stalkers
from .forms import ComentariosForm
from django.http import HttpResponseRedirect
# Create your views here.

class Comentar(PermisosMixin,PasajeMixin,LoginRequiredMixin,CreateView):
    template_name = 'Comentarios/Comentar.html'
    model = Comentarios
    modelo=Trabajadores
    form_class = ComentariosForm
    rol='stalker'
    campos=['perfil','objeto']
    
    # Aqui redefinimos el form_valid, para obtener una instacia del formulario y de ahi sacar el pk
    # entonces con eso cmabiamos el succes_url para que al comentar la pagina se refresque en el mismo lugar del perfil 
    def form_valid(self, form):
        instancia = form.save(commit=False)
        return HttpResponseRedirect(reverse_lazy('Trabajadores:mostrarPerfil', args = [str(instancia.trabajador.pk)])) 

def Mostrar(request):
    objetos= Comentarios.objects.all()
    return render(request,'Comentarios/Mostrar.html',{'objetos':objetos})