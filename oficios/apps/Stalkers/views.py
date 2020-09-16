from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms
from ..Usuarios.models import Usuarios
# Create your views here.

class Registro(generic.CreateView):
    template_name='Usuarios/Registro.html'
    model=models.Stalkers
    form_class=forms.StalkersForm
    success_url=reverse_lazy('Home')
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['usuario'] = 'Buscador'
        return context

class EditarPerfil(generic.edit.UpdateView):
    template_name='Usuarios/EditarPerfil.html'
    model=models.Usuarios
    form_class=forms.EditarForm
    success_url=reverse_lazy('Usuarios:perfil')