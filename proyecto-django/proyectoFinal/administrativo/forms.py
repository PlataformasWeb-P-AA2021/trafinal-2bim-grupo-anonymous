from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Persona, Barrio, Casa, Departamento

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'cedula', 'correo']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'apellido': _('Ingrese el apellido por favor'),
            'cedula': _('Ingrese la cedula por favor'),
            'correo': _('Ingrese el correo por favor')
        }

class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'siglas']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'apellido': _('Ingrese las siglas por favor')
        }

class CasaForm(ModelForm):
    class Meta:
        model = Casa
        fields = ['propietario', 'direccion', 'barrio', 'valorBien', 'nroCuartos', 'nroPisos']

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['propietario', 'direccion', 'barrio', 'valorBien', 'nroCuartos', 'valorMantenimiento']
   