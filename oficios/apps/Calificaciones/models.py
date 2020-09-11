from django.db import models

# Create your models here.
class Calificaciones(models.Model):

    calificacion = models.IntegerField(default=None)
    comentario = models.TextField(default=None)
    
    def __str__(self):
        return self.calificacion
    
 