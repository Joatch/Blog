from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from AppBlog.models import *

class CrearLibrosForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    autor = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)
    estreno = forms.DateField()

class CrearJuegosForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    creador = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)
    publicación = forms.DateField()

class CrearSeriesForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)
    estreno = forms.DateField()

class CrearPeliculasForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)
    estreno = forms.DateField()

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

