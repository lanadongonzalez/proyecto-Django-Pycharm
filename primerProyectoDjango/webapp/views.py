from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
""""
def bienvenido(request):
    return HttpResponse("Hola Mundo")

def bienvenido(request):
    return render(request, "bienvenido.html")
    
"""


# al meter mensajes en el render le estamos pasando ese diccionario al html
def bienvenido(request):
    mensajes = {'mensaje1': 'valor mensaje1', 'mensaje2': 'valor mensaje2'}
    return render(request, "bienvenido.html", mensajes)


def listar_datos(request):
    listado_alumnos = [
        {'nombre': 'pepe', 'apellidos': 'garcia fernandez', 'dni': '111A'},
        {'nombre': 'nombre2', 'apellidos': 'apellidos2', 'dni': '222A'},
        {'nombre': 'nombre3', 'apellidos': 'apellido3', 'dni': '333A'},
    ]
    contexto = {'listado_alumnos': listado_alumnos}
    return render(request, "gestion/alumnos.html", contexto)


def adios(request):
    return render(request, "adios.html")
