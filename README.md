Potaje
------

Un manojo de ideas

![build status](https://travis-ci.org/tutuca/potaje.svg?branch=master)

Instalación
-------------------

Se asume un sistema con:

- [python](http://python.org).
- [pip](http://www.pip-installer.org/), [virtualenv](http://www.virtualenv.org/)
  (incluídos con python 3.4).

Sólo para desarrollo:

- [node](http://nodejs.org/)
- [npm](https://www.npmjs.org/)

Clonar el repositorio

    $ git clone git@github.com:tutuca/potaje.git
    $ cd potaje

Opcional: Crear un entorno virtual.

    $ virtualenv .
    $ source ./bin/activate

Instalar las dependencias

    $ pip install -r requirements.txt

## Ajustar los parametros locales

    $ vim potaje/local_settings.py

Modificar los parámetros de la base de datos

    #local_settings.py
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'potaje',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
    }   

> En producción local_settings.py debería tener DEBUG=False

# Inicializar la base de datos.

Primero es necesario crear los esquemas y ejecutar las migraciones si hacen falta:

    $ manage migrate

En este punto tenemos nuestra instancia lista para correr el servidor de
desarrollo:

    $ manage runserver

# Assets státicos.

Ahora queda generar los recursos de estilos, imágenes, íconos y scripts.

Descargar las herramientas necesarias:

    $ npm install  

Compilar los assets:

    $ npm build

Se puede operar en modo `watch`, esto es: queda observando los archivos importantes de manera de re-ejecutar las tareas pertinentes.

    $ npm start

Ésto genera una carpeta `static/` en la raiz del proyecto, que podemos desplegar en nuestro servidor.
