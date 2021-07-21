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
        path('vistaDepartamento', views.vistaDepartamento, name='vistaDepartamento'),
        path('crearCasa', views.crearCasa, name='crearCasa'),
        path('editar_casa/<int:id>', views.editar_casa, name='editar_casa'),
        path('eliminar_casa/<int:id>', views.eliminar_casa, name='eliminar_casa'),

        # url Departamento
        path('crearDepartamento', views.crearDepartamento, name='crearDepartamento'),
        path('editar_departamento/<int:id>', views.editar_departamento, 
            name='editar_departamento'),
        path('eliminar_departamento/<int:id>', views.eliminar_departamento, 
            name='eliminar_departamento'),
        
        # url Barrio
        path('crearBarrio', views.crearBarrio, name='crearBarrio'),

        # url Persona
        path('crearPersona', views.crearPersona, name='crearPersona'),

        # Ingreso/Salida del sistema
        path('saliendo/logout/', views.logout_view, name="logout_view"),
        path('entrando/login/', views.ingreso, name="login"),
 ]
