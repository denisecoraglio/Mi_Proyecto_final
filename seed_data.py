from ejemplo.models import Curso
from ejemplo.models import Alumno
from ejemplo.models import Tutor


Curso(nombre="Python", duracion="12 semanas", dedicacion="alta").save()
Curso(nombre="Data Engineering", duracion="42 semanas", dedicacion="alta").save()
Curso(nombre="Data Sciencie", duracion="42 semanas", dedicacion="alta").save()
Curso(nombre="Data Analytics", duracion="12 semanas", dedicacion="alta").save()
Curso(nombre="Procesamiento de datos en excel", duracion="4 semanas", dedicacion="moderada").save()
Alumno(nombre="Maria Denise Coraglio", edad=38, provincia= "Cordoba", curso="Python").save()
Alumno(nombre="Martin Giuliano", edad=42, provincia= "Cordoba", curso="Python").save()
Tutor(nombre="Esteban Acevedo", curso="Python").save()
Tutor(nombre="Enzo Martin Zotti", curso="Python").save()
Tutor(nombre="Griselda Benitez", curso="Python").save()

print("Se cargo con éxito los usuarios de pruebas")