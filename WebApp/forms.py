from django import forms

class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class BuscarEstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=40)

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    curso = forms.IntegerField()

class BuscarProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=40)

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class BuscarCursoForm(forms.Form):
    nombre = forms.CharField(max_length=40)
