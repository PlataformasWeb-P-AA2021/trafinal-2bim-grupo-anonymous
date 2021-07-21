from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/casa")
def casa():
    """
    """
    r = requests.get("http://localhost:8000/api/casa/",
            auth=('jecueva11', 'root'))
    casa = json.loads(r.content)['results']
    numero_casas = json.loads(r.content)['count']
    datos2 = []
    for d in casa:
        datos2.append({'propietario': obtener_persona(d['propietario']), 'direccion':d['direccion'],
        'barrio': obtener_barrio(d['barrio']) , 'valorBien':d['valorBien'],
        'colorInmueble':d['colorInmueble'], 'nroCuartos':d['nroCuartos'],
        'nroPisos':d['nroPisos'] })
    return render_template("casa.html", casa=datos2,
    numero_casas=numero_casas)


@app.route("/departamento")
def departamento():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamento/",
            auth=('jecueva11', 'root'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({'propietario': obtener_persona(d['propietario']), 'direccion':d['direccion'],
        'barrio': obtener_barrio(d['barrio']), 'valorBien':d['valorBien'],
        'nroCuartos':d['nroCuartos'], 'valorMantenimiento':d['valorMantenimiento'] })
    return render_template("departamento.html", datos=datos2,
    numero=numero)


@app.route("/persona")
def persona():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/persona/",
            auth=('jecueva11', 'root'))
    personas = json.loads(r.content)['results']
    numero_personas = json.loads(r.content)['count']
    return render_template("persona.html", personas=personas,
    numero_personas=numero_personas)

@app.route("/barrio")
def barrio():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/barrio/",
            auth=('jecueva11', 'root'))
    barrios = json.loads(r.content)['results']
    numero_barrios = json.loads(r.content)['count']
    return render_template("barrio.html", barrios=barrios,
    numero_personas=numero_barrios)

# funciones ayuda

def obtener_persona(url):
    """
    """
    r = requests.get(url, auth=('jecueva11', 'root'))
    nombre_persona = json.loads(r.content)['nombre'] + ' ' + json.loads(r.content)['apellido']
    return nombre_persona

def obtener_barrio(url):
    """
    """
    r = requests.get(url, auth=('jecueva11', 'root'))
    nombre_barrio = json.loads(r.content)['nombre'] 
    return nombre_barrio
