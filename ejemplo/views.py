from django.shortcuts import render
from ejemplo.models import Cursos
from ejemplo.models import Alumnos
from ejemplo.models import Tutores

def mostrar_cursos(request):
  lista_cursos = Cursos.objects.all()
  return render(request, "ejemplo/cursos.html", {"lista_cursos": lista_cursos})

def mostrar_alumnos(request):
  lista_alumnos = Alumnos.objects.all()
  return render(request, "ejemplo/alumnos.html", {"lista_alumnos": lista_alumnos})

def mostrar_tutores(request):
  lista_tutores = Tutores.objects.all()
  return render(request, "ejemplo/tutores.html", {"lista_tutores": lista_tutores})
