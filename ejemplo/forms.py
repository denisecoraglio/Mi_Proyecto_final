from django import forms
from ejemplo.models import Cursos, Alumnos, Tutores


class Buscar(forms.Form):
    nombre = forms.CharField(max_length=10, widget= forms.TextInput(attrs= {"placeholder": "Busque un curso..."}))

class CursosForm(forms.ModelForm):
  class Meta:
    model = Cursos
    fields = ['nombre', 'duracion', 'dedicacion']

class AlumnosForm(forms.ModelForm):
  class Meta:
    model = Alumnos
    fields = ['nombre', 'edad', 'provincia', 'curso' ]

class TutoresForm(forms.ModelForm):
  class Meta:
    model = Tutores
    fields = ['nombre', 'curso' ]