from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('cursos/', views.cursos, name="Cursos"),
    path('profesores/', views.profesores, name="Profesores"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('curso-formulario/', views.curso_formulario, name="CursoFormulario"),
    # --- AGREGÁ ESTAS DOS LÍNEAS ABAJO ---
    path('busqueda-camada/', views.busqueda_camada, name="BusquedaCamada"),
    path('buscar/', views.buscar, name="Buscar"),
]