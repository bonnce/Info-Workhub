from django.db import models
from ..Usuarios.models import Usuarios
from ..Calificaciones.models import Calificaciones

class Stalkers(models.Model):
    usuario= models.OneToOneField(Usuarios,on_delete=models.CASCADE,related_name='Stalker')
    calificacion = models.ManyToManyField(Calificaciones, related_name='st_califica')
    