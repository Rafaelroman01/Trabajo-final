from django.db import models

# Create your models here.
class Excursion(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return f"Excursion: {self.nombre} | Email: {self.camada}"
    
class Participantes(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    
    def __str__(self):
        return f"{self.apellido.upper()}, {self.nombre.capitalize()}"
    
class Recreadores(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    
    def __str__(self):
        return f"{self.apellido.upper()}, {self.nombre.capitalize()} [{self.profesion.title()}]"
    
    
class Documentacion(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
    
    def __str__(self):
        return f"{self.nombre} -> {self.fecha_de_entrega}"