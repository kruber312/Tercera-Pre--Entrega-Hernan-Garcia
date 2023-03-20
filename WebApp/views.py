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
    context = {
        "form": ProfesorForm(),
        "form_buscar": BuscarProfesorForm(),
    }
    return render(request, "WebApp/profesores.html", context=context)

def crear_profesor(request):
    if request.method == "POST":
        mi_formulario = ProfesorForm(request.POST)
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            profesor_save = Profesor(
                nombre=info["nombre"],
                apellido=info["apellido"],
                cursos=info["curso"]
            )
            profesor_save.save()
            return redirect("WebAppProfesores")
    return render(request, "WebApp/profesores.html")

def buscar_profesor(request):
    mi_formulario = BuscarProfesorForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        profesores_filtrados = Profesor.objects.filter(nombre__icontains=informacion["nombre"])
        context = {
            "profesores": profesores_filtrados
        }
    return render(request, "WebApp/buscar_profesor.html", context=context)

def cursos(request):
    context = {
        "form": CursoForm(),
        "form_buscar": BuscarCursoForm(),
    }
    return render(request, "WebApp/cursos.html", context=context)

def crear_curso(request):
    if request.method == "POST":
        mi_formulario = CursoForm(request.POST)
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            curso_save = Curso(
                nombre=info["nombre"],
                camada=info["camada"],
            )
            curso_save.save()
            return redirect("WebAppCursos")
    return render(request, "WebApp/cursos.html")

def buscar_curso(request):
    mi_formulario = BuscarCursoForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        cursos_filtrados = Curso.objects.filter(nombre__icontains=informacion["nombre"])
        context = {
            "cursos": cursos_filtrados
            }
    return render(request, "WebApp/buscar_curso.html", context=context)

