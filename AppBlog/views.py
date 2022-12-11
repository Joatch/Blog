from django.shortcuts import render
from AppBlog.models import *
from AppBlog.forms import *
from AppBlog.forms import *
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView 
from django.shortcuts import redirect



def index (request):
    imagenes = Avatar.objects.filter(user=request.user.id)
    if imagenes.exists():
        url =  imagenes[0].imagen.url
    else:
        url = None
    return render (request, 'index.html', {'url': url})

def About (request):
    return render(request, 'About.html')

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

class LibrosList (LoginRequiredMixin,ListView):
    model = Libros
    template_name = 'list_libros.html'

class LibrosUpdate (LoginRequiredMixin,UpdateView):
    model = Libros
    success_url = 'List Libros'
    fields = ['nombre', 'autor', 'genero']

class LibrosDelete (LoginRequiredMixin, DeleteView):
    model = Libros
    template_name = 'delete_libro.html'
    success_url = reverse_lazy ('List Libros')



class SeriesList (LoginRequiredMixin,ListView):
    model = Series
    template_name = 'list_series.html'

class SeriesUpdate (LoginRequiredMixin,UpdateView):
    model = Series
    success_url = 'List Series'
    fields = ['nombre', 'genero']

class SeriesDelete (LoginRequiredMixin, DeleteView):
    model = Series
    template_name = 'delete_serie.html'
    success_url = reverse_lazy ('List Series')




class PeliculasList (LoginRequiredMixin,ListView):
    model = Peliculas
    template_name = 'list_peliculas.html'

class PeliculasUpdate (LoginRequiredMixin,UpdateView):
    model = Peliculas
    success_url = 'List Peliculas'
    fields = ['nombre', 'genero']

class PeliculasDelete (LoginRequiredMixin, DeleteView):
    model = Peliculas
    template_name = 'delete_pelicula.html'
    success_url = reverse_lazy ('List Peliculas')



class JuegosList (LoginRequiredMixin,ListView):
    model = Juegos
    template_name = 'list_juegos.html'

class JuegosUpdate (LoginRequiredMixin,UpdateView):
    model = Juegos
    success_url = 'List Juegos'
    fields = ['nombre', 'creador', 'genero']

class JuegosDelete (LoginRequiredMixin, DeleteView):
    model = Juegos
    template_name = 'delete_juego.html'
    success_url = reverse_lazy ('List Juegos')



class SignUp (CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy ('Home')
    template_name = 'registro.html'

class Login (LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy ('Home')
    template_name = 'login.html'

class Logout (LoginRequiredMixin,LogoutView):
    template_name = 'logout.html'