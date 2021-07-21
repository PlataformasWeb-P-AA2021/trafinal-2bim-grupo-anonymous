from django.db import models

# Create your models here.

class Persona(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30)
    correo = models.EmailField(max_length=30)

    def __str__(self):
        return "%s %s" % (
            self.nombre,
            self.apellido,
            )                      

class Barrio(models.Model):
    nombre = models.CharField("Nombre del Barrio", max_length=100)
    siglas = models.CharField("Siglas del barrio", max_length=10)

    def __str__(self):
        return "%s" % (
            self.nombre,)

class Casa(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE, 
            related_name="personasCasa")

    direccion = models.CharField("Direccion de la casa", max_length=100)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE, 
            related_name="barriosCasa")

    valorBien = models.DecimalField("Valor de la casa", max_digits=10, decimal_places=2)
    colorInmueble = models.CharField("Color del Inmueble", max_length=100)
    nroCuartos = models.IntegerField("Número de cuartos")
    nroPisos = models.IntegerField("Número de pisos")

    def __str__(self):
        return "%s - %f - %s - %d - %d" % (
            self.direccion,
            self.valorBien,
            self.colorInmueble,
            self.nroCuartos,
            self.nroPisos
            )

class Departamento(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE, 
            related_name="personasDepa")

    direccion = models.CharField("Direccion del departamento", max_length=100)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE, 
            related_name="barriosDepa")

    valorBien = models.DecimalField("Valor del departamento", max_digits=10, decimal_places=2)
    nroCuartos = models.IntegerField("Número de cuartos")
    valorMantenimiento = models.DecimalField("Valor del mantenimiento",  max_digits=10, decimal_places=2)

    def __str__(self):
        return "%s - %f - %d - %f" % (
            self.direccion,
            self.valorBien,
            self.nroCuartos,
            self.valorMantenimiento
            )