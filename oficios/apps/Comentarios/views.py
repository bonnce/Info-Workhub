from django.views.generic.edit import CreateView 
from django.shortcuts import render
from .models import Comentarios
# Create your views here.

class Comentar(CreateView): 
  
    model = Comentarios  
  
    fields = ['description'] 

def Mostrar(request):
    objetos= Comentarios.objects.all()
    return render(request,'Comentarios/Mostrar.html',{'objetos':objetos})