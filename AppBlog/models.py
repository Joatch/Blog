from django.db import models
from django.contrib.auth.models import User
class Libros(models.Model):
    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    def __str__(self):
        return f'Nombre: {self.nombre}, Autor: {self.autor}, Genero: {self.genero}' 

class Juegos(models.Model):
    nombre = models.CharField(max_length=40)
    creador = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    def __str__(self):
        return f'Nombre: {self.nombre}, Creador: {self.creador}, Genero: {self.genero}' 


class Series(models.Model):
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    def __str__(self):
        return f'Nombre: {self.nombre}, Genero: {self.genero}' 


class Peliculas(models.Model):
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    def __str__(self):
        return f'Nombre: {self.nombre}, Genero: {self.genero}' 

class Avatar (models.Model):
    user = models.ForeignKey (User, on_delete = models.CASCADE)
    imagen = models.ImageField (upload_to = 'images', null=True, blank = True)