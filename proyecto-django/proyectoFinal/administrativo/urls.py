"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        # url Casa
        path('crearCasa', views.crearCasa, name='crearCasa'),

        # url Departamento
        path('crearDepartamento', views.crearDepartamento, name='crearDepartamento'),

        # url Barrio
        path('crearBarrio', views.crearBarrio, name='crearBarrio'),

        # url Persona
        path('crearPersona', views.crearPersona, name='crearPersona'),

 ]
