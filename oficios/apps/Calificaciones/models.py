from django.db import models
from ..Trabajadores.models import Trabajadores
# Create your models here.
class Calificaciones(models.Model):
    trabajador = models.ForeignKey(Trabajadores,on_delete=models.CASCADE,related_name='es_calificado')
    calificacion = models.PositiveSmallIntegerField()
    comentario = models.TextField(default=None)
    
    def __str__(self):
        return '%s %s'%(self.trabajador.usuario.first_name,self.trabajador.usuario.last_name)
