# Mi_Proyecto_final

El proyecto trae informacion de Coderhouse. La página de inicio, va a contar con un menu donde se podran seleccionar los vinculos relacionados a cursos, profesores y alumnos. Para cada vinculo se listaran los registros pudiendo asimismo dar de alta un registro nuevo, actualizar uno existente y/o eliminar. Para el proyecto utilicé 3 clases de modelos: Curso, Alumno y Tutor y las url que detallo a continuacion junto con pasos para la utilizacion del programa


1 Abrir VSCode.

2 Seleccionar o crear una carpeta del programa.

4 Para abrir el servidor, en la terminal ejecutar el comando python manage.py runserver 

5 Se visualiza la siguiente pagina: http://127.0.0.1:8000/

6 Para crear la base de datos ejecutar los comandos python manage.py makemigrations y python manage.py migrate

7 Se crea un archivo seed_data con las instancias de cada modelo para cargar datos en la base de datos

8 Luego se importa dicho archivo con los siguientes comandos: python manage.py shell y import seed_data

9 Agregar las url que se indican a continuacion en la barra de direcciones para poder utilizarlas. 

Tomando como ejemplo el modelo Curso, las url serian las siguientes siendo las mismas para los modelos restantes:


http://127.0.0.1:8000/cursos/: Muestra los Cursos ofrecidos por Coderhouse
http://127.0.0.1:8000/cursos/buscar: Permite buscar un curso determinado
http://127.0.0.1:8000/cursos/alta: Permite dar de alta a un nuevo curso
http://127.0.0.1:8000/cursos/actualizar: Permite actualizar un curso
http://127.0.0.1:8000/cursos/borrar: Permite borrar un curso


Todas se encuentran probadas y funcionan correctamente.




