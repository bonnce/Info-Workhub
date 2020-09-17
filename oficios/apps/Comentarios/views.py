from django.views.generic.edit import CreateView 
from django.shortcuts import render
from .models import Comentarios
from django.urls import reverse_lazy
from .forms import Comentarios
# Create your views here.

class Comentar(CreateView): 
    template_name = 'Comentarios/Comentar.html'
  
    model = Comentarios  

    form_class = Comentarios

    success_url = reverse_lazy('Trabajadores:Listar')

def Mostrar(request):
    objetos= Comentarios.objects.all()
    return render(request,'Comentarios/Mostrar.html',{'objetos':objetos})