"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppBlog.views import *
from AppBlog.admin import *
from AppBlog.forms import *
from AppBlog.models import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='Home'),
    path('agregarlibro', crear_libro, name='Agregar Libro'),
    path('agregarjuego', crear_juego, name='Agregar Juego'),
    path('agregarpelicula', crear_pelicula, name='Agregar Pelicula'),
    path('agregarserie', crear_serie, name='Agregar Serie'),
    path('signup', SignUp.as_view(), name='Sign Up'),
    path('login', Login.as_view(), name='Login'),
    path('logout', Logout.as_view(), name='Logout'),
    path('editarusuario', editar_usuario, name = 'Editar Usuario'),

    path('eliminarlibro/<pk>', LibrosDelete.as_view(), name = 'Eliminar Libro'),
    path('eliminarjuego/<pk>', JuegosDelete.as_view(), name = 'Eliminar Juego'),
    path('eliminarserie/<pk>', SeriesDelete.as_view(), name = 'Eliminar Serie'),
    path('eliminarpelicula/<pk>', PeliculasDelete.as_view(), name = 'Eliminar Pelicula'),

    path('actualizarlibro/<libros_id>', LibrosUpdate, name = 'Actualizar Libro'),
    path('actualizarjuego/<juegos_id>', JuegosUpdate, name = 'Actualizar Juego'),
    path('actualizarserie/<series_id>', SeriesUpdate, name = 'Actualizar Serie'),
    path('actualizarpelicula/<peliculas_id>', PeliculasUpdate, name = 'Actualizar Pelicula'),

    path('libroslist', LibrosList.as_view(), name = 'List Libros'),
    path('juegoslist', JuegosList.as_view(), name = 'List Juegos'),
    path('serieslist', SeriesList.as_view(), name = 'List Series'),
    path('peliculaslist', PeliculasList.as_view(), name = 'List Peliculas'),

    path('About', About, name = 'About')
]

urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)