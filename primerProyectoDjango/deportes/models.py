from django.db import models


# Create your models here.

class Futbolista(models.Model):
    nombre = models.CharField(max_length=40)
    equipo = models.CharField(max_length=60)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=60)
    posicion = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre}{self.equipo}{self.edad}{self.nacionalidad}{self.posicion}"
