from django.forms import ModelForm
from .models import Comentarios

class Comentarios(ModelForm):
    class Meta:
        model = Comentarios

        fields ='__all__'
    