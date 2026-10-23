from django.db import models


# Create your models here.
# Nombre del modelo con mayuscula
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    titulo_academico = models.CharField(max_length=100)
    biografia = models.CharField(max_length=500)
    correo = models.CharField(max_length=100)
    dedicacion = models.CharField(max_length=200)

    class Meta:
        ordering = ('apellidos',)
        db_table = 'Persona'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return self.apellidos
