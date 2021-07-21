from django.contrib import admin

# Register your models here.
# Importar las clases del modelo
from administrativo.models import Persona, Barrio, Casa, Departamento

# Agregar la clase Estudiante para administrar desde
# interfaz de administración
# admin.site.register(Estudiante)

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Persona
class PersonaAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'apellido', 'cedula', 'correo')
    search_fields = ('nombre', 'apellido')

admin.site.register(Persona, PersonaAdmin)

class BarrioAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'siglas')
    search_fields = ('nombre', 'siglas')

admin.site.register(Barrio, BarrioAdmin)

# Agregar la clase NumeroTelefonico para administrar desde
# interfaz de administración
# admin.site.register(NumeroTelefonico)

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# NumeroTelefonico

class CasaAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('direccion', 'valorBien', 'colorInmueble', 'nroCuartos', 'nroPisos')
    # se agrega el atributo 
    # raw_id_fields que permite acceder a una interfaz 
    # para buscar los estudiantes y seleccionar el que 
    # se desee
    raw_id_fields = ('propietario', 'barrio', )

admin.site.register(Casa, CasaAdmin)


class DepartamentoAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('direccion', 'valorBien', 'nroCuartos', 'valorMantenimiento')
    # se agrega el atributo 
    # raw_id_fields que permite acceder a una interfaz 
    # para buscar los estudiantes y seleccionar el que 
    # se desee
    raw_id_fields = ('propietario', 'barrio', )

admin.site.register(Departamento, DepartamentoAdmin)

