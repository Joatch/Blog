from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from AppBlog.models import *

class CrearLibrosForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    autor = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)

class CrearJuegosForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    creador = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)

class CrearSeriesForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)

class CrearPeliculasForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    username = forms.CharField (label='Usuario')
    email = forms.EmailField (label='Modificar Email')
    password1 = forms.CharField (label='Contraseña', widget = forms.PasswordInput)
    password2 = forms.CharField (label='Repetir la Contraseña', widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

