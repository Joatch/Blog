from django.db import models

class Libros(models.Model):
    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    estreno = models.DateField()

class Juegos(models.Model):
    nombre = models.CharField(max_length=40)
    creador = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    publicación = models.DateField()

class Series(models.Model):
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    estreno = models.DateField()

class Peliculas(models.Model):
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    estreno = models.DateField()

class Usuario (models.Model):
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Mail = models.EmailField()
