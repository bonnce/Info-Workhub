from django.db import models

# Create your models here.
class Calificaciones(models.Model):

    calificacion = models.DecimalField(max_digits=1, decimal_places=None)
    comentario = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.calificacion
    
    pass