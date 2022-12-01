from django.contrib import admin
from cliente.models import Cliente, Coche
# Register your models here.


# Registramos los modelos que vayamos creando para administrarlos
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Coche)
