from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    camada = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    cursos = models.IntegerField()

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()