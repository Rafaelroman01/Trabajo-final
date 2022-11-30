from django.db import models

# Create your models here.
class Excursion(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    def trabajos
    
class Participantes(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    
class Recreadores(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    
    
    
class Documentacion(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()