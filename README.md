# Mi_Proyecto_final
Proyecto final Curso Python
# Comienzo con la instalacion de Django

# Creo una carpeta con el nombre proyecto

Para correr el programa, realizar los siguientes pasos:

1 Abrir VSCode.

2 Seleccionar o crear una carpeta del programa.

4 En la terminal ejecutar el comando python manage.py runserver para abrir el servidor

5 Se visualiza la siguiente pagina: http://127.0.0.1:8000/

6 Para crear la base de datos ejecutar los comandos python manage.py makemigrations y python manage.py migrate

7 Se crea un archivo seed_data con las instancias de cada modelo para cargar datos en la base de datos

8 Luego se importa dicho archivo con los siguientes comandos: python manage.py shell y import seed_data


En la web hay 3 tipos de modelos: Cursos, Alumnos y Tutores:

9 Agregar las url que se indican a continuacion en la barra de direcciones para poder utilizarlas. 

http://127.0.0.1:8000/cursos-datos/: Muestra los Cursos de data ofrecidos por Coderhouse
http://127.0.0.1:8000/alumnos-coder/: Muestra los alumnos de Coderhouse
http://127.0.0.1:8000/tutores/ : Muestra los tutores Coderhouse
http://127.0.0.1:8000/cursos-datos/buscar: Permite buscar por nombre de curso
http://127.0.0.1:8000/cursos-datos/alta: Permite dar de alta a un curso
http://127.0.0.1:8000/alumnos-coder/alta: Permite dar de alta a un alumno
http://127.0.0.1:8000/tutores/: Permite dar de alta a un tutor
cursos-datos/actualizar/<int:pk>: Permite actualizar el registro 
cursos-datos/borrar/<int:pk>Permite borrar el registro 


Se encuentran funcionando todas excepto la funcion actualizar que no genera el mensaje de exito como corresponde




