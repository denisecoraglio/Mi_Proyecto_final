from django.shortcuts import render, get_object_or_404
from ejemplo.models import Cursos
from ejemplo.models import Alumnos
from ejemplo.models import Tutores
from ejemplo.forms import Buscar, CursosForm, AlumnosForm, TutoresForm
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

class AltaCursos(View):

    form_class = CursosForm
    template_name = 'ejemplo/alta_cursos.html'
    initial = {"nombre":"", "duracion":"", "dedicacion":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el curso {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class AltaAlumnos(View):

    form_class = AlumnosForm
    template_name = 'ejemplo/alta_alumnos.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el alumno {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class AltaTutores(View):

    form_class = TutoresForm
    template_name = 'ejemplo/alta_tutores.html'
    initial = {"nombre":"", "curso":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el tutor {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarCursos(View):
    form_class = CursosForm
    template_name = "ejemplo/actualizar_cursos.html"
    initial = {"nombre":"", "duracion":"", "dedicacion":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
    def get(self, request, pk): 
        cursos = get_object_or_404(Cursos, pk=pk)
        form = self.form_class(instance=cursos)
        return render(request, self.template_name, {"form":form,"cursos": cursos})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
    def post(self, request, pk): 
        cursos = get_object_or_404(Cursos, pk=pk)
        form = self.form_class(request.POST ,instance=cursos)
        if form.is_valid():
            form.save()
            msg_exito = f"se actualizó con éxito el curso {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial) # borra formulario
            return render(request, self.template_name, {"form":form, 
                                                      "cursos": cursos,
                                                      "msg_exito": msg_exito})
      
        return render(request, self.template_name, {"form": form})


class BorrarCursos(View):
    template_name = "ejemplo/cursos.html"
 
  
    def get(self, request, pk): 
      cursos = get_object_or_404(Cursos, pk=pk)
      cursos.delete()
      cursos = Cursos.objects.all()
      return render(request, self.template_name, {'lista_cursos': cursos})
