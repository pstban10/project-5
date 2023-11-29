from django.db import models
from django.contrib.auth.models import User


class PatronMovimiento(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class EjercicioCalistenia(models.Model):
    nombre = models.CharField(max_length=255)
    dificultad = models.IntegerField()
    musculos = models.CharField(max_length=255)
    patron = models.ForeignKey(PatronMovimiento, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre


class Rutina(models.Model):
    nombre = models.CharField(max_length=255)
    dificultad = models.IntegerField()
    Ejercicios = models.ManyToManyField(EjercicioCalistenia)
    creador = models.ForeignKey(User, on_delete=models.RESTRICT)
    creada_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
