from django.forms import ModelForm
from .models import Calificaciones

class CalificacionesForm(ModelForm):
    class Meta:
        model=Calificaciones
        fields='__all__'