from django.shortcuts import render, redirect
from AppBlog.models import *
from AppBlog.forms import *
from AppBlog.forms import *
from django.urls import reverse_lazy
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def index (request):
    return render (request, 'index.html')

def crear_libro (request):
    if request.method == 'POST':
        formulario = CrearLibrosForm(request.POST)
        if formulario.is_valid():
            formulario1_limpio = formulario.cleaned_data
            usuario = Usuario(nombre=request.POST['nombre'], autor=request.POST['autor'], genero=request.POST['genero'], estreno=request.POST['estreno'])
            usuario.save
            return render (request, 'index.html')
    else:
        formulario = CrearLibrosForm
    return render (request, 'crear_libro.html', {'formulario': formulario})

def crear_juego (request):
    if request.method == 'POST':
        formulario = CrearJuegosForm(request.POST)
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            usuario = Usuario(nombre=request.POST['nombre'], creador=request.POST['creador'], genero=request.POST['genero'], publicacion=request.POST['publicacion'])
            usuario.save
            return render (request, 'index.html')
    else:
        formulario = CrearJuegosForm
    return render (request, 'crear_juego.html', {'formulario': formulario})

def crear_serie (request):
    if request.method == 'POST':
        formulario3 = CrearSeriesForm(request.POST)
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            usuario = Usuario(nombre=request.POST['nombre'], autor=request.POST['autor'], genero=request.POST['genero'], estreno=request.POST['estreno'])
            usuario.save
            return render (request, 'index.html')
    else:
        formulario = CrearSeriesForm
    return render (request, 'crear_serie.html', {'formulario': formulario})

def crear_pelicula (request):
    if request.method == 'POST':
        formulario4 = CrearPeliculasForm(request.POST)
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            usuario = Usuario(nombre=request.POST['nombre'], autor=request.POST['autor'], genero=request.POST['genero'], estreno=request.POST['estreno'])
            usuario.save
            return render (request, 'index.html')
    else:
        formulario = CrearPeliculasForm
    return render (request, 'crear_pelicula.html', {'formulario': formulario})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registo exitoso." )
			return redirect("Registrarse")
		messages.error(request, "No se pudo registrar. Información puesta es inválida.")
	form = NewUserForm()
	return render (request=request, template_name="registro.html", context={"register_form":form})

def mostrar_usuario (request):
    Uuario = Usuario.objects.all()
    context = {'Usuario': Usuario}
    
    return render (request, 'mostrar_usuarios.html', context=context)

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Cumpleaños: {self.cumpleaños}, Mail: {self.mail}' 