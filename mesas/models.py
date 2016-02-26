from django.db import models

# Create your models here.
class Materias (models.Model):
    nombre = models.CharField(max_length = 60)
    anio = models.CharField(max_length = 50)
    carrera = models.CharField(max_length = 50)
    cuatrimestre = models.CharField(max_length = 20)
    sitioweb = models.URLField()

    primera_mesa = models.DateField()
    segunda_mesa = models.DateField()
    tercera_mesa = models.DateField()
    cuarta_mesa = models.DateField()
    quinta_mesa = models.DateField()
    sexta_mesa = models.DateField()
    septima_mesa = models.DateField()
    octava_mesa = models.DateField()
    novena_mesa = models.DateField()
    decima_mesa = models.DateField()

    def __str__(self):
        return self.nombre
