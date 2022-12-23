from django import forms
from ejemplo.models import Curso, Alumno, Tutor


class Buscar(forms.Form):
    nombre = forms.CharField(max_length=10, widget= forms.TextInput(attrs= {"placeholder": "Busque un curso..."}))

class CursoForm(forms.ModelForm):
  class Meta:
    model = Curso
    fields = ['nombre', 'duracion', 'dedicacion']

class AlumnoForm(forms.ModelForm):
  class Meta:
    model = Alumno
    fields = ['nombre', 'edad', 'provincia', 'curso' ]

class TutorForm(forms.ModelForm):
  class Meta:
    model = Tutor
    fields = ['nombre', 'curso' ]