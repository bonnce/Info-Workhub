from django.db import models
from ..Trabajadores.models import Trabajadores


class Calificaciones(models.Model):
    trabajador = models.ForeignKey(Trabajadores,on_delete=models.CASCADE,related_name='calificado')
    calificacion = models.PositiveSmallIntegerField()
    comentario = models.TextField(default=None)
    
    def __str__(self):
        return str(self.calificacion)
