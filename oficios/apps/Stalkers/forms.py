from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import Stalkers
from ..Usuarios.models import Usuarios
from django.db import transaction

class StalkersForm(UserCreationForm):
    class Meta:
        model=Usuarios
        fields=['first_name','last_name','username','password1','password2','email','phone','address']
    
    @transaction.atomic
    def save(self):
        usuario=super().save(commit=False)
        usuario.Trabajador=False
        usuario.save()
        Stalkers.objects.create(usuario=usuario)

        return usuario

class EditarForm(UserChangeForm):
    class Meta:
        model=Usuarios
        fields=['first_name','last_name','username','email','phone','address']