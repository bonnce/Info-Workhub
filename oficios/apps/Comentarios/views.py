from django.shortcuts import render
from .models import Comentarios
# Create your views here.
def Mostrar(request):
    objetos= Comentarios.objects.all()
    return render(request,'Comentarios/Mostrar.html',{'objetos':objetos})