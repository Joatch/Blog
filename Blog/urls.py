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
    path('mostrarlibros', mostrar_libros, name = 'Mostrar Libros'),
    path('mostrarseries', mostrar_series, name = 'Mostrar Series'),
    path('mostrarpeliculas', mostrar_peliculas, name = 'Mostrar Peliculas'),
    path('mostrarjuegos', mostrar_juegos, name = 'Mostrar Juegos'),
    path('editarusuario', editar_usuario, name = 'Editar Usuario'),
    path('eliminarjuego/<juego_id>', eliminar_juego, name = 'Eliminar Juego'),
    path('eliminarserie/<serie_id>', eliminar_serie, name = 'Eliminar Serie'),
    path('eliminarpelicula/<pelicula_id>', eliminar_pelicula, name = 'Eliminar Pelicula'),
    path('eliminarlibro/<libro_id>', eliminar_libro, name = 'Eliminar Libro'),
    path('actualizar_libro/<libro_id>', actualizar_libro, name = 'Actualizar Libro'),
    path('actualizar_pelicula/<pelicula_id>', actualizar_pelicula, name = 'Actualizar Pelicula'),
    path('actualizar_serie/<serie_id>', actualizar_serie, name = 'Actualizar Serie'),
    path('actualizar_juego/<juego_id>', actualizar_juego, name = 'Actualizar Juego'),
    path('librolist', LibrosList.as_view(), name = 'List Libros'),
    path('librodetalle/<pk>', LibrosList.as_view(), name = 'Detail Libros'),
]

urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)