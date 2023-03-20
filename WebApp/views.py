from django.shortcuts import HttpResponse, render, redirect
from WebApp.models import Estudiante, Profesor, Curso
from WebApp.forms import *

def inicio(request):

    return render(request, "WebApp/inicio.html")

def estudiantes(request):
    context = {
        "form": EstudianteForm(),
        "form_buscar": BuscarEstudianteForm(),
    }
    return render(request, "WebApp/estudiantes.html", context=context)

def crear_estudiante(request):
    if request.method == "POST":
        mi_formulario = EstudianteForm(request.POST)
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            estudiante_save = Estudiante(
                nombre=info["nombre"],
                apellido=info["apellido"],
                camada=info["camada"]
            )
            estudiante_save.save()
            return redirect("WebApp/estudiantes.html")
    return render(request, "WebApp/estudiantes.html")

def buscar_estudiante(request):
    mi_formulario = BuscarEstudianteForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        estudiantes_filtrados = Estudiante.objects.filter(nombre__icontains=informacion["nombre"])
        context = {
            "estudiantes": estudiantes_filtrados
        }
    return render(request, "WebApp/buscar_estudiante.html", context=context)

def profesores(request):

    return render(request, "WebApp/profesores.html")

def cursos(request):

    return render(request, "WebApp/cursos.html")

