from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
""""
def bienvenido(request):
    return HttpResponse("Hola Mundo")
"""
def bienvenido(request):
    return render(request, "bienvenido.html")

def adios(request):
    return render(request, "adios.html")