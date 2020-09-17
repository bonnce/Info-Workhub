from django.forms import ModelForm
from .models import Comentarios
from django.utils import timezone

class Comentarios(ModelForm):
    class Meta:
        model = Comentarios

        fields =['descripcion', 'trabajador', 'stalker']
    
    def save(self):
        comentario = super().save(commit=False)
        comentario.fecha_pub = timezone.now()
        comentario.save()
        return comentario
