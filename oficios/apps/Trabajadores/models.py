from django.db import models
from ..Usuarios.models import Usuarios
# Create your models here.

class Rubros(models.Model):
    nombre=models.CharField(max_length=20)

class Trabajadores(models.Model):
    usuario= models.OneToOneField(Usuarios,on_delete=models.CASCADE,related_name='Worker')
    promedio= models.DecimalField(max_digits=3,decimal_places=2)
    especialidad= models.CharField(max_length=20)
    certificado = models.ImageField(upload_to='Trabajadores',null=True,blank=True)
    rubro = models.ForeignKey(Rubros,null=True,on_delete=models.SET_NULL,related_name='filtro_rubro')
