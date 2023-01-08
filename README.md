# Mi_Proyecto_final

El proyecto final es el blog de Corrucal, empresa dedicada a la fabricacion y venta de articulos de carton corrugado. La página se admministra desde el vinculo Admin blog. Se podra visualizar el listado de los productos ofrecidos, como asi tambien efectuar un registro nuevo, actualizar uno existente y/o eliminar. La aplicacion tambien permite registrar usuarios nuevos, actualizar perfiles, ver y crear mensajes. Detallo a continuacion los pasos para la utilizaiocn del programa


1 Abrir VSCode.

2 Seleccionar o crear una carpeta del programa.

4 Para abrir el servidor, en la terminal ejecutar el comando python manage.py runserver 

5 Se visualiza la siguiente pagina: http://127.0.0.1:8000/

6 Para crear la base de datos ejecutar los comandos python manage.py makemigrations y python manage.py migrate

7 Se crea un archivo seed_data con las instancias de cada modelo para cargar datos en la base de datos

8 Luego se importa dicho archivo con los siguientes comandos: python manage.py shell y import seed_data

9 Agregar las url que se indican a continuacion en la barra de direcciones para poder utilizarlas. 




http://127.0.0.1:8000/corrucal/: Muestra el blog de inicio de la empresa



El blog se encuentra funcioncionando.




