from django.shortcuts import render, get_object_or_404
from ejemplo.models import Curso
from ejemplo.models import Alumno
from ejemplo.models import Tutor
from ejemplo.forms import Buscar, CursoForm, AlumnoForm, TutorForm
from django.views import View 
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView





def mostrar_cursos(request):
  lista_cursos = Curso.objects.all()
  return render(request, "ejemplo/cursos.html", {"lista_cursos": lista_cursos})

def mostrar_alumnos(request):
  lista_alumnos = Alumno.objects.all()
  return render(request, "ejemplo/alumnos.html", {"lista_alumnos": lista_alumnos})

def mostrar_tutores(request):
  lista_tutores = Tutor.objects.all()
  return render(request, "ejemplo/tutores.html", {"lista_tutores": lista_tutores})

class BuscarCurso(View):
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
            lista_cursos = Curso.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, "lista_cursos": lista_cursos})
        return render(request, self.template_name, {"form": form})

class AltaCurso(View):

    form_class = CursoForm
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

    form_class = AlumnoForm
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

    form_class = TutorForm
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

class ActualizarCurso(View):
    form_class = CursoForm
    template_name = "ejemplo/actualizar_cursos.html"
    initial = {"nombre":"", "duracion":"", "dedicacion":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
    def get(self, request, pk): 
        curso = get_object_or_404(Curso, pk=pk)
        form = self.form_class(instance=curso)
        return render(request, self.template_name, {"form":form,"curso": curso})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
    def post(self, request, pk): 
        curso = get_object_or_404(Curso, pk=pk)
        form = self.form_class(request.POST ,instance=curso)
        if form.is_valid():
            form.save()
            msg_exito = f"se actualizó con éxito el curso {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial) # borra formulario
            return render(request, self.template_name, {"form":form, 
                                                      "curso": curso,
                                                      "msg_exito": msg_exito})
      
        return render(request, self.template_name, {"form": form})


class BorrarCurso(View):
    template_name = "ejemplo/cursos.html"
 
  
    def get(self, request, pk): 
      curso = get_object_or_404(Curso, pk=pk)
      curso.delete()
      cursos = Curso.objects.all()
      return render(request, self.template_name, {'lista_cursos': cursos})

class ActualizarAlumno(View):
    form_class = AlumnoForm
    template_name = "ejemplo/actualizar_alumnos.html"
    initial = {"nombre":"", "duracion":"", "dedicacion":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
    def get(self, request, pk): 
        alumno = get_object_or_404(Alumno, pk=pk)
        form = self.form_class(instance=alumno)
        return render(request, self.template_name, {"form":form,"alumno": alumno})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
    def post(self, request, pk): 
        alumno = get_object_or_404(Alumno, pk=pk)
        form = self.form_class(request.POST ,instance=alumno)
        if form.is_valid():
            form.save()
            msg_exito = f"se actualizó con éxito el alumno {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial) 
            return render(request, self.template_name, {"form":form, 
                                                      "alumno": alumno,
                                                      "msg_exito": msg_exito})
      
        return render(request, self.template_name, {"form": form})


class BorrarAlumno(View):
    template_name = "ejemplo/alumnos.html"
 
  
    def get(self, request, pk): 
      alumno = get_object_or_404(Alumno, pk=pk)
      alumno.delete()
      alumno = Alumno.objects.all()
      return render(request, self.template_name, {'lista_alumnos': alumno})

class ActualizarTutor(View):
    form_class = TutorForm
    template_name = "ejemplo/actualizar_tutores.html"
    initial = {"nombre":"", "curso":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
    def get(self, request, pk): 
        tutor = get_object_or_404(Tutor, pk=pk)
        form = self.form_class(instance=tutor)
        return render(request, self.template_name, {"form":form,"tutor": tutor})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
    def post(self, request, pk): 
        tutor = get_object_or_404(Tutor, pk=pk)
        form = self.form_class(request.POST ,instance=tutor)
        if form.is_valid():
            form.save()
            msg_exito = f"se actualizó con éxito el tutor {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial) 
            return render(request, self.template_name, {"form":form, 
                                                      "tutor": tutor,
                                                      "msg_exito": msg_exito})
      
        return render(request, self.template_name, {"form": form})

class BorrarTutor(View):
    template_name = "ejemplo/tutores.html"
 
  
    def get(self, request, pk): 
      tutor = get_object_or_404(Tutor, pk=pk)
      tutor.delete()
      tutor = Tutor.objects.all()
      return render(request, self.template_name, {'lista_tutores': tutor})

class CursoList(ListView):
  model = Curso

class CursoCrear(CreateView):
  model = Curso
  success_url = "/panel-curso"
  fields = ["nombre", "duracion", "dedicacion"]

class CursoBorrar(DeleteView):
  model = Curso
  success_url = "/panel-curso"

class CursoActualizar(UpdateView):
  model = Curso
  success_url = "/success_update_message"
  fields = ["nombre", "duracion", "dedicacion"]

class CursoDetalle(DetailView):
  model = Curso
  

