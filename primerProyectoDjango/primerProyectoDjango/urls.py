"""primerProyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from cliente.views import formulario_aniadir_cliente
from deportes.views import sports, listar_selecciones, lista_futbolistas
from webapp.views import bienvenido, adios, listar_datos

urlpatterns = [
    path('', bienvenido),
    path('admin/', admin.site.urls, name='administrador'),
    # welcome es la petición del cliente (la url http://127.0.0.1:8000/welcome en este caso) y bienvenido la funcion
    # que se ejecuta. Las funciones están en views
    path('welcome/', bienvenido),
    path('goodbye/', adios),
    path('deportes/', sports, name='deportes'),
    path('listadoalumnos/', listar_datos, name='listado_alumnos'),
    path('deportes/futbol/listadoselecciones/', listar_selecciones, name='listado_selecciones'),
    path('clientes/add', formulario_aniadir_cliente, name='clientes_add'),
    path('deportes/futbol/listadofutbolista/', lista_futbolistas, name='listado_futbolistas'),
]
