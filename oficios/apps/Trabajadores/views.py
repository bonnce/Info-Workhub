from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms
from ..Usuarios.models import Usuarios
from ..Comentarios.models import Comentarios

class Registro(generic.CreateView):
    template_name='Usuarios/Registro.html'
    model=models.Trabajadores
    form_class=forms.TrabajadoresForm
    success_url=reverse_lazy('Home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = 'Trabajador'
        return context   

class Listar(generic.ListView):
    model = models.Trabajadores
    template_name = "Usuarios/Trabajadores/Listar.html"


#Se usa el modelo Usuario ya que es el modelo usado por el form y el modelo que se instancia
#Para que django se ocupe de lo complicado
class EditarPerfil(generic.edit.UpdateView):
    template_name='Usuarios/EditarPerfil.html'
    model=Usuarios
    form_class=forms.EditarForm
    success_url=reverse_lazy('Usuarios:perfil')


class MostrarPerfil(generic.DetailView):
    model = models.Trabajadores
    template_name = 'Usuarios/Trabajadores/MostrarPerfil.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentario'] = Comentarios.objects.filter(trabajador=context['object'])
        print(context)
        return context