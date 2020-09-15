from django.contrib.auth.forms import UserCreationForm 
from django import forms
from .models import Trabajadores,Rubros
from ..Usuarios.models import Usuarios
from django.db import transaction

class TrabajadoresForm(UserCreationForm):
    Especialidad=forms.CharField(max_length=50)
    Rubro=forms.ModelChoiceField(Rubros.objects.all())
    Certificado=forms.ImageField(required=False)
    
    class Meta:
        model=Usuarios
        fields=['first_name','last_name','username','password1','password2','email','phone','address']
    
    @transaction.atomic
    def save(self):
        usuario=super().save(commit=False)
        usuario.Trabajador=True
        usuario.save()
        Trabajadores.objects.create(usuario=usuario,       
        especialidad=self.cleaned_data.get('Especialidad'),rubro=self.cleaned_data['Rubro'],
        certificado=self.cleaned_data['Certificado'])

        return usuario

    