# MedServ

Pasos para hacer un ambiente virtual 1 crear ambiente virtual con python python -m venv ambV

2 despues activar el ambiente ambV/scripts/activate

3 instalar las dependencias de este proyecto. En proyecto MedServ-main esta el requirements.txt pip install -r requirements.txt

 Para levantar servicios en proveedor sera en el puerto 4000

\MedServ-main\Proveedor>py manage.py runserver 4000

 Para levantar servicios en MedServ-main sera en el puerto 8000

\MedServ-main\MedServ-main>py manage.py runserver

# En caso de repetir el proceso de llenar la base de datos hacer los sgtes pasos

 Eliminar archivo db.sqlite3
\MedServ-main\MedServ-main> rm db.sqlite3
(o si no borrarlo manualmente)

Luego ejecutar en consola:

\MedServ-main\MedServ-main> py manage.py makemigrations
\MedServ-main\MedServ-main> py manage.py migrate

Crear usuario administrador
\MedServ-main\MedServ-main> py manage.py createsuperuser
admin
--sin correo
1234
1234
y        <---- hay que poner y para confirmar la clave 
