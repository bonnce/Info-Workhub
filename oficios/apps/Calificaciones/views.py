from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CalificacionesForm
from .models import Calificaciones

class Calificar(loginRequiredMixin,CreateView):
    model=Calificaciones
    form_class=CalificacionesForm
    template_name='Calificaciones/Calificar.html'
    succes_url=reverse_lazy('Home')