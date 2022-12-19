from django.shortcuts import render
from ejemplo.models import Cursos
from ejemplo.models import Alumnos
from ejemplo.models import Tutores
from ejemplo.forms import Buscar 
from django.views import View 


def mostrar_cursos(request):
  lista_cursos = Cursos.objects.all()
  return render(request, "ejemplo/cursos.html", {"lista_cursos": lista_cursos})

def mostrar_alumnos(request):
  lista_alumnos = Alumnos.objects.all()
  return render(request, "ejemplo/alumnos.html", {"lista_alumnos": lista_alumnos})

def mostrar_tutores(request):
  lista_tutores = Tutores.objects.all()
  return render(request, "ejemplo/tutores.html", {"lista_tutores": lista_tutores})

class BuscarCursos(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_cursos = Cursos.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, "lista_cursos": lista_cursos})
        return render(request, self.template_name, {"form": form})
