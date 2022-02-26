# Proyecto Base para desarrollo del backend con docker

Este es una base o estructura basica para implementar en los proyectos version de python 3.7, usando todo con docker

`Para correr el proyecto primero se comenta ciudad en person luego migraciones, si las migraciones se eliminaron`

# Crear Documentacion
1. Crear una carpeta en la raiz del proyecto que se llame doc
2. entrar en esa carpeta y dar el siguiente comando `sphinx-quickstart`
3. Se creara unos archivos, luego buscamos en esa carpeta en el archivo `conf.py` pegamos la estructura que tenemos 
4. luego ejecutamos el siguiente comando `sphinx-apidoc -o modules ..`
5. Recordar que todo se llama y se organiza en index.rst
6. luego hacer `make html`.
7. Guia --> `https://davidcasr.medium.com/c%C3%B3mo-documentar-un-proyecto-django-con-sphinx-80e4a090896e`
# Variables de entorno
* Archivo de varibles de entorno .env
```
#Django DB
POSTGRES_DB=backend
POSTGRES_USER=postgres
POSTGRES_PASSWORD=123456
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432

#Config django
SECRET_KEY= django-insecure-_33yemiuffdbatcf@w#d!8e7^cj6cn=x^q(*w+mna1reubk_i=
DEBUG=True
DJANGO_SETTINGS_MODULE=backend.settings.develop

#Email
EMAIL_HOST=smtp.gmail.com
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER=pruebas.jcsq@gmail.com
EMAIL_HOST_PASSWORD=CamiloSuarez04
DEFAULT_FROM_EMAIL=pruebas.jcsq@gmail.com

#Db_test
DB_NAME_TEST=backend
DB_USER_TEST=postgres
DB_PASS_TEST=123456
DB_SERVICE_TEST=127.0.0.1
DB_PORT_TEST=5432
```
# Makefile
En el se encuentran comandos configurados para la facilidad, 
ejecucion y desarrollo del proyecto; los comandos 
disponibles son:


* Ejecutar migraciones
``` bash
make migrate
```
* correr el servidor
``` bash
make up
```
* Crear superusuario
``` bash
make superuser
```
* Crear app
``` bash
make app name=my_app
```
* correr los test
``` bash
make test
```
* Entrar a la terminal de python
``` bash
make shell
```
* Instalar requerimientos
``` bash
make requirements
```
* Exportar los datos a json
``` bash
make export_data
```
* Cargar datos al sistema del archivo disponible
``` bash
make import_data
```
* Vaciar Base de datos
``` bash
make clean_data
```

* Cargar los estaticos
``` bash
make statics
```
### Pre-requisitos
1. install python
2. install pip

### inicio 

1. install virtualenv
    * abre una terminal y digita
      `apt-get install virtualenv`
    

2. crear entorno virtual 
    * Dentro de la terminal digita `virtualenv env -p python3`
    

3. Entrar al entorno y activarlo    
    * Dentro del directorio que se creo
      el entorno escribir `source env/bin/activate
      

4. Iniciar todo el cargue del sistema
   * `make start` solo se usa una vez este carga todas
   las dependencias del sistema, requerimientos, datos, apps
     etc.
  
### Readme development
* Desarrollando la app en local

  1.`make migrate` prepara y carga las migraciones.
       
  2.`make up` corre el servidor local para desarrollo.
    
