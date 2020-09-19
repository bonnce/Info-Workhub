from django.db import models
from ..Trabajadores.models import Trabajadores

valores=[(1,1),(2,2),(3,3),(4,4),(5,5)]
class Calificaciones(models.Model):
    trabajador = models.ForeignKey(Trabajadores,on_delete=models.CASCADE,related_name='calificado')
    calificacion = models.PositiveSmallIntegerField(choices=valores)
    comentario = models.TextField(default=None)
    
    def __str__(self):
        return str(self.calificacion)
