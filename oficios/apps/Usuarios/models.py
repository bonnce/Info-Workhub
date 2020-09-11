from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuarios(AbstractUser):
	Trabajador=models.BooleanField(default=False)
	address=models.CharField(max_length=60,null=True)
	phone=models.BigIntegerField(null=True)

