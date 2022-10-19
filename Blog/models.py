from tabnanny import verbose
from django.db import models

# Create your models here.


class Autor(models.Model):
    class Meta:
        verbose_name_plural = "Autores"

    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=500)
    profesion = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre


class Pais(models.Model):
    class Meta:
        verbose_name_plural = "Paises"

    nombre = models.CharField(max_length=250)
    habitantes = models.IntegerField()
    fechaindependencia = models.DateField()

    def __str__(self):
        return self.nombre


class Transporte(models.Model):
    class Meta:
        verbose_name_plural = "Transportes"

    clase = models.CharField(max_length=250)
    costo = models.IntegerField()

    def __str__(self):
        return self.clase
