<p align="center">
  <br>
  <img src="https://github.com/jecueva1997/ProgramacionAvanzada-Proyecto/blob/master/IMG/port.jpg">
  <br><br><b>UNIVERSIDAD TÉCNICA PARTICULAR DE LOJA
  <br><i>LA UNIVERSIDAD CATÓLICA DE LOJA</i>
  <br><br>PLataformas Web
  <br><br>Ciencias de la Computación
  <br><br><i>Sexto Ciclo</i>
  <br><br>Proyecto
  <br><br>Integrantes:
  <br><br><i>Jeferson Cueva
  <br>Frank Saca</i>
  <br><br>Docente:
  <br><br><i>Ing. René Elizalde</i>
  <br><br>Abril/2021 - Agosto/2021
  </b>
</p>

# Levantamiento en el servidor Nginx con Unicorn y Django en Ubunto 20.04

* __Paso 1__: Instalación de Unicorn 

`sudo apt-get install unicorn`

* __Paso 2__: Instalación del servidor Nginx

```
sudo apt-get install nginx
```

* __Paso 3__: Configurar nuestro proyecto Django

* __Paso 3.1__: Configurar la variable __ALLOWED_HOSTS__  en el archivo __settings.py__ del proyecto de tal manera que pueda ser desplegada en cualquiera de los siguientes puertos:

```
ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1", 'localhost']
```

* __Paso 3.2__: Configurar el archivo __urls.py__ del proyecto para poder manejar los archivos de la carpeta __static__ (imágenes, estilos, etc)

```
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
```

```
urlpatterns += staticfiles_urlpatterns()
```

* __Paso 4__: Obtener el contenido estático en la carpeta __static__

```
python manage.py collectstatic
```

* __Paso 5__: Levantar el proyecto con __Unicorn__ _esto se hace desde la carpeta raíz_ 

```
gunicorn --bind 0.0.0.0:8000 proyectoFinal.wsgi
```

_Donde proyectoFinal.wsgi es nuestro proyecto de Django_

* __Paso 6__: Crear un directorio en la carpeta __/etc/systemd/system/__ 

```
sudo gedit /etc/systemd/system/proyecto01.service
```

_Esto se debe hacer con permisos de administrador, donde proyecto01 es un nombre cualquiera_. Agregar lo siguiente:

```
[Unit]
# metadatos necesarios
Description=gunicorn daemon
After=network.target

[Service]
# usuario del sistema operativo que ejecutará el proceso
User=usuario-sistema-operativo
# el grupo del sistema operativo que permite la comunicación a desde el servidor web-nginx con gunicorn. No se debe cambiar el valor
Group=www-data

# a través de la variable WorkingDirectory se indica la dirección absoluta del proyecto de Django
WorkingDirectory=/home/usuario-sistema/carpeta/proyectos/nombre-proyecto

# En Environment se indica el path de python
# Ejemplo 1: /usr/bin/python3.9
# Ejemplo 2: (Opcional, con el uso de entornos virtuales) /home/usuario/entornos/entorno01/bin
Environment="PATH=agregar-path-python"

# Detallar el comando para iniciar el servicio
ExecStart=/usr/bin/gunicorn --workers 3 --bind unix:application.sock -m 007 proyectoDjango.wsgi:application

# Donde: aplicacion.sock es el nombre del archivo que se debe crear en el directorio del proyecto; proyectoDjango el nombre del proyecto que se intenta vincular con nginx.
# La expresión /bin/gunicorn no se debe modificar.

[Install]
# esta sección será usada para indicar que el servicio puede empezar cuando se inicie el sistema operativo. Se sugiere no cambiar el valor dado.
WantedBy=multi-user.target
```


* __Paso 7__: Iniciar y habilitar el servicio  

```
sudo systemctl start proyecto01
sudo systemctl enable proyecto01
sudo systemctl status proyecto01
```

__Donde proyecto01 es el nombre del servicio creado anteriormente__

* __Paso 8__: Verificar la existencia del directorio __static__ y el archivo __application.sock__ 

_Si todo marcha bien debe estar de la siguiente manera_

<p align="center">
  <br>
  <img src="https://github.com/PlataformasWeb-P-AA2021/trafinal-2bim-grupo-anonymous/blob/main/publicacion/WhatsApp%20Image%202021-07-22%20at%2023.09.35.jpeg">
  <br>
</p>


* __Paso 9__: Configuración del servidor __Nginx__ 

_Puede validar el funcionamiento del mismo con los siguientes comandos_

```
sudo service nginx start
sudo service nginx stop
sudo service nginx restart
sudo service nginx status
```

* __Paso 10__: Crear un archivo __sites_avaliable__ de __Nginx__ esto lo puede hacer con el siguiente comando

```
sudo gedit /etc/nginx/sites-available/proyecto01
```

_Esto se debe hacer con permisos de administrador, copiar y pegar lo siguiente:_ 

```
server {
    listen 81;
    server_name localhost;
    
    location / {
        include proxy_params;
        proxy_pass http://unix:/ruta/al/archivo/sock/application.sock;
    }

    
    location /static/ {
        root /ruta/a/la/carpeta/staticos/del/proyecto-django;
    }
  }
```

_Nota: La ruta del proyecto no debe ser muy extensa_

* __Paso 11__: Iniciar un enlace simbólico del archivo creado en el __Paso 10__

```
sudo ln -s /etc/nginx/sites-available/proyecto01 /etc/nginx/sites-enabled
```


* __Paso 12__: Reiniciar el servicio de __Nginx__

```
sudo service nginx restart
```

* __Paso 13__: Comprobar el levantamiendo del servidor 

_Si todo marcha bien se debe desplegar el proyecto_

* http://localhost:81

* http://0.0.0.0:81

* http://127.0.0.0:81

<p align="center">
  <br>
  <img src="https://github.com/PlataformasWeb-P-AA2021/trafinal-2bim-grupo-anonymous/blob/main/publicacion/WhatsApp%20Image%202021-07-22%20at%2023.12.38.jpeg">
  <br>
</p>


