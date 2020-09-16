from django.db import models
from ..Usuarios.models import Usuarios
from ..Calificaciones.models import Calificaciones

class Stalkers(models.Model):
    usuario= models.OneToOneField(Usuarios,on_delete=models.CASCADE,related_name='Stalker')
<<<<<<< HEAD
    calificacion = models.ManyToManyField(Calificaciones, related_name='st_califica')

    def __str__(self):
        return '%s %s'%(self.usuario.first_name,self.usuario.last_name)
=======
    calificacion = models.ManyToManyField(Calificaciones,related_name='califica',blank=True)

    def __str__(self):
        return self.usuario.username
>>>>>>> e4dba7ca57cd4efe659a07795059c758ca9187e5
