from django.views.generic.edit import CreateView 
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comentarios
from django.urls import reverse_lazy
from ..Trabajadores.models import Trabajadores
from ..Stalkers.models import Stalkers
from .forms import ComentariosForm
# Create your views here.

class Comentar(LoginRequiredMixin,CreateView):
    template_name = 'Comentarios/Comentar.html'
    model = Comentarios
    form_class = ComentariosForm
    success_url = reverse_lazy('Trabajadores:Listar')

#Redefinicion del post para asignarle el trabajador y stalker antes de guardarlo en la bd cuando ya
#se completo el formulario
    def post(self, request, *args, **kwargs):
        trabajador=Trabajadores.objects.get(pk=kwargs['pk'])
        stalker=request.user.ObtenerPerfil()
        form = self.form_class(request.POST)
        if form.is_valid():
            coment=form.save()
            coment.trabajador=trabajador
            coment.stalker=stalker
            form.save(commit=True)
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

def Mostrar(request):
    objetos= Comentarios.objects.all()
    return render(request,'Comentarios/Mostrar.html',{'objetos':objetos})