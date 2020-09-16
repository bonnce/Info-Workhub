from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms
# Create your views here.

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
