from django.urls import path
from WebApp import views

urlpatterns = [
    path('', views.inicio, name="WebAppInicio"),
    path('estudiantes/', views.estudiantes, name="WebAppEstudiantes"),
    path('estudiantes/crear', views.crear_estudiante, name="WebAppCrearEstudiantes"),
    path('estudiantes/buscar', views.buscar_estudiante, name="WebAppBuscarEstudiantes"),
    path('profesores/', views.profesores, name="WebAppProfesores"),
    path('cursos/', views.cursos, name="WebAppCursos"),
]
