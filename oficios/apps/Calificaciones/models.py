from django.db import models
from ..Trabajadores.models import Trabajadores
# Create your models here.
class Calificaciones(models.Model):
    calificacion = models.PositiveSmallIntegerField()
    comentario = models.TextField(default=None)
    trabajador = models.ForeignKey(Trabajadores,on_delete=models.CASCADE,related_name='calificado')
    
    def __str__(self):
        return self.calificacion
