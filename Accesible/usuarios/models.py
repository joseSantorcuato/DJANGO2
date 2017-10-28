from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ocupacion = models.CharField(max_length=100)

class Discapacidad(models.Model):
    beneficiario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    discap = models.CharField(max_length=100)
    anoingreso = models.DateField()
    evaluacion = models.IntegerField()
