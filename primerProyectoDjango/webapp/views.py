from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
""""
def bienvenido(request):
    return HttpResponse("Hola Mundo")

def bienvenido(request):
    return render(request, "bienvenido.html")
    
"""
#al meter mensajes en el render le estamos pasando ese diccionario al html
def bienvenido(request):
    mensajes = {'mensaje1':'valor mensaje1', 'mensaje2':'valor mensaje2'}
    return render(request, "bienvenido.html", mensajes)

def adios(request):
    return render(request, "adios.html")