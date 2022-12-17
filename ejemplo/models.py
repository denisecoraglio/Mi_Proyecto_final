from django.db import models

class Cursos(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.CharField(max_length=200)
    dedicacion = models.CharField(max_length=100)
    
    def __str__(self):
      return f"{self.nombre}, {self.duracion}, {self.id}, {self.dedicacion}"

class Alumnos(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    edad = models.IntegerField()
    curso = models.CharField(max_length=200)
    
    def __str__(self):
      return f"{self.nombre}, {self.direccion}, {self.edad}, {self.curso}, {self.id}"

class Tutores(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.CharField(max_length=200)
    
    def __str__(self):
      return f"{self.nombre}, {self.curso}, {self.id}"
