from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.CharField(max_length=200)
    dedicacion = models.CharField(max_length=100)
    
    def __str__(self):
      return f"{self.nombre}, {self.duracion}, {self.id}, {self.dedicacion}"

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.CharField(max_length=200)
    edad = models.IntegerField()
    curso = models.CharField(max_length=200)
    
    def __str__(self):
      return f"{self.nombre}, {self.provincia}, {self.edad}, {self.curso}, {self.id}"

class Tutor(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.CharField(max_length=200)
    
    def __str__(self):
      return f"{self.nombre}, {self.curso}, {self.id}"
