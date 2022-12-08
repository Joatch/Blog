from django.shortcuts import render
from AppBlog.models import *
from AppBlog.forms import *
from AppBlog.forms import *
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView



def index (request):

    imagenes = Avatar.objects.filter(user=request.user.id)

    if imagenes.exists():
        url =  imagenes[0].imagen.url
    else:
        url = None

    return render (request, 'index.html', {'url': url})

@login_required
def crear_libro (request):
    if request.method == 'POST':
        formulario = CrearLibrosForm(request.POST)
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            usuario = Libros(nombre=formulario_limpio['nombre'], autor=formulario_limpio['autor'], genero=formulario_limpio['genero'])
            usuario.save()
            return render (request, 'index.html')
    else:
        formulario = CrearLibrosForm
    return render (request, 'crear_libro.html', {'formulario': formulario})

@login_required
def crear_juego (request):
    if request.method == 'POST':
        formulario = CrearJuegosForm(request.POST)
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            usuario = Juegos(nombre=formulario_limpio['nombre'], creador=formulario_limpio['creador'], genero=formulario_limpio['genero'])
            usuario.save()
            return render (request, 'index.html')
    else:
        formulario = CrearJuegosForm
    return render (request, 'crear_juego.html', {'formulario': formulario})

@login_required
def crear_serie (request):
    if request.method == 'POST':
        formulario = CrearSeriesForm(request.POST)
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            usuario = Series(nombre=formulario_limpio['nombre'], genero=formulario_limpio['genero'])
            usuario.save()
            return render (request, 'index.html')
    else:
        formulario = CrearSeriesForm
    return render (request, 'crear_serie.html', {'formulario': formulario})

@login_required
def crear_pelicula (request):
    if request.method == 'POST':
        formulario = CrearPeliculasForm(request.POST)
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            usuario = Peliculas(nombre=formulario_limpio['nombre'], genero=formulario_limpio['genero'])
            usuario.save()
            return render (request, 'index.html')
    else:
        formulario = CrearPeliculasForm
    return render (request, 'crear_pelicula.html', {'formulario': formulario})

@login_required
def mostrar_libros(request):
    libro = Libros.objects.all()
    context = {'Libros': libro}
    return render(request, 'mostrar_libros.html', context=context)

@login_required
def mostrar_series(request):
    serie = Series.objects.all()
    context = {'Series': serie}
    return render(request, 'mostrar_series.html', context=context)

@login_required
def mostrar_peliculas(request):
    pelicula = Peliculas.objects.all()
    context = {'Peliculas': pelicula}
    return render(request, 'mostrar_peliculas.html', context=context)

@login_required
def mostrar_juegos(request):
    juego = Juegos.objects.all()
    context = {'Juegos': juego}
    return render(request, 'mostrar_juegos.html', context=context)

class SignUp (LoginRequiredMixin,CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy ('Home')
    template_name = 'registro.html'

class Login (LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy ('Home')
    template_name = 'login.html'

class Logout (LoginRequiredMixin,LogoutView):
    template_name = 'logout.html'

@login_required
def editar_usuario(request):
    usuario = request.user
    if request.method == 'POST':
        usuario_form = UserEditForm(request.POST)
        if usuario_form.is_valid():
            informacion = usuario_form.cleaned_data
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            return render (request, 'index.html')
    else:
        usuario_form = UserEditForm(initial = {'username': usuario.username,'email': usuario.email})
    return render(request, 'editar_usuario.html', {
        'form': usuario_form,
        'usuario': usuario
        })

def eliminar_juego (request, juego_id):
    juego = Juegos.objects.get (id=juego_id)
    juego.delete()
    juegos = Juegos.objects.all()
    context = {'juegos': juegos}
    return render (request, 'mostrar_juegos.html', context=context)

def eliminar_serie (request, serie_id):
    serie = Series.objects.get (id=serie_id)
    serie.delete()
    series = Series.objects.all()
    context = {'series': series}
    return render (request, 'mostrar_series.html', context=context)

def eliminar_pelicula (request, pelicula_id):
    pelicula = Peliculas.objects.get (id=pelicula_id)
    pelicula.delete()
    peliculas = Peliculas.objects.all()
    context = {'pelicula': peliculas}
    return render (request, 'mostrar_peliculas.html', context=context)

def eliminar_libro (request, libro_id):
    libro = Libros.objects.get (id=libro_id)
    libro.delete()
    libros = Libros.objects.all()
    context = {'libros': libros}
    return render (request, 'mostrar_libros.html', context=context)

def actualizar_libro (request, libro_id):
    libro = Libros.objects.get (id=libro_id)
    if request.method == 'POST':
        formulario = CrearLibrosForm(request.POST)
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data

            libro.nombre = formulario_limpio['nombre']
            libro.autor = formulario_limpio ['autor']
            libro.genero = formulario_limpio['genero']

            libro.save()
            return render (request, 'index.html')
    else:
        formulario = CrearLibrosForm (initial={'nombre': libro.nombre, 'autor': libro.autor, 'genero': libro.genero})
    return render (request, 'mostrar_libros.html', {'formulario': CrearLibrosForm})

def actualizar_serie (request, serie_id):
    serie = Series.objects.get (id=serie_id)
    if request.method == 'POST':
        formulario = CrearSeriesForm(request.POST)
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data

            serie.nombre = formulario_limpio['nombre']
            serie.genero = formulario_limpio['genero']

            serie.save()
            return render (request, 'index.html')
    else:
        formulario = CrearSeriesForm (initial={'nombre': serie.nombre, 'genero': serie.genero})
    return render (request, 'mostrar_series.html', {'formulario': CrearSeriesForm})

def actualizar_pelicula (request, pelicula_id):
    pelicula = Peliculas.objects.get (id=pelicula_id)
    if request.method == 'POST':
        formulario = CrearPeliculasForm(request.POST)
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data

            pelicula.nombre = formulario_limpio['nombre']
            pelicula.genero = formulario_limpio['genero']

            pelicula.save()
            return render (request, 'index.html')
    else:
        formulario = CrearPeliculasForm (initial={'nombre': pelicula.nombre, 'genero': pelicula.genero})
    return render (request, 'mostrar_peliculas.html', {'formulario': CrearPeliculasForm})

def actualizar_juego (request, juego_id):
    juego = Juegos.objects.get (id=juego_id)
    if request.method == 'POST':
        formulario = CrearJuegosForm(request.POST)
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data

            juego.nombre = formulario_limpio['nombre']
            juego.creador = formulario_limpio ['creador']
            juego.genero = formulario_limpio['genero']

            juego.save()
            return render (request, 'index.html')
    else:
        formulario = CrearJuegosForm (initial={'nombre': juego.nombre, 'creador': juego.creador, 'genero': juego.genero})
    return render (request, 'mostrar_juegos.html', {'formulario': CrearJuegosForm})


class LibrosList (ListView):
    model = Libros
    template_name = 'libros_list.html'

class LibroDeleteView(DeleteView):
    model = Libros
    success_url = 'curso_list.html'