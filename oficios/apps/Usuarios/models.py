from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuarios(AbstractUser):
	Trabajador=models.BooleanField(default=False)
	address=models.CharField(max_length=60,null=True)
	phone=models.BigIntegerField(null=True)
	
	def ObtenerDatos(self):
		cositas={'Usuario':self.username,'Nombre':self.first_name,'Apellido':self.last_name,
		'Direccion':self.address,'Telefono':self.phone}
		if(self.Trabajador):
			cositas.update({'Especialidad':self.Worker.especialidad,'Valoracion':self.Worker.promedio,
			'Rubro':self.Worker.rubro,'Certificado':self.Worker.certificado})
		return cositas