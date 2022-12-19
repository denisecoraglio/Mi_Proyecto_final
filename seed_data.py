from ejemplo.models import Cursos
from ejemplo.models import Alumnos
from ejemplo.models import Tutores


Cursos(nombre="Python", duracion="12 semanas", dedicacion="alta").save()
Cursos(nombre="Data Engineering", duracion="42 semanas", dedicacion="alta").save()
Cursos(nombre="Data Sciencie", duracion="42 semanas", dedicacion="alta").save()
Cursos(nombre="Data Analytics", duracion="12 semanas", dedicacion="alta").save()
Cursos(nombre="Procesamiento de datos en excel", duracion="4 semanas", dedicacion="moderada").save()
Alumnos(nombre="Maria Denise Coraglio", edad=38, provincia= "Cordoba", curso="Python").save()
Alumnos(nombre="Martin Giuliano", edad=42, provincia= "Cordoba", curso="Python").save()
Tutores(nombre="Esteban Acevedo", curso="Python").save()
Tutores(nombre="Enzo Martin Zotti", curso="Python").save()
Tutores(nombre="Griselda Benitez", curso="Python").save()

print("Se cargo con éxito los usuarios de pruebas")