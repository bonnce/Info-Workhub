from django.forms import ModelForm, RadioSelect
from .models import Calificaciones

class CalificacionesForm(ModelForm):
    class Meta:
        model=Calificaciones
        fields=['calificacion','comentario']
        widgets = {
            'calificacion': RadioSelect(),
        }