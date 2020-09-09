# from django.db import models

# # Create your models here.
# class Usuarios(models.Model):
#     pass

# class Trabajadores(Usuarios):
#     pass

# class Stalkers(Usuarios):
#     pass

# class Rubros(models.Model):
#     pass

from django.db import models

from django.contrib.auth.models import AbstractUser


class Usuarios(AbstractUser):
	pass

