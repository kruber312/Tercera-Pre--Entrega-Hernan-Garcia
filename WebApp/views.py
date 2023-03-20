from django.shortcuts import HttpResponse, render, redirect

def inicio(request):

    return render(request, "WebApp/inicio.html")

def estudiantes(request):

    return render(request, "WebApp/estudiantes.html")

def profesores(request):

    return render(request, "WebApp/profesores.html")

def cursos(request):

    return render(request, "WebApp/cursos.html")
