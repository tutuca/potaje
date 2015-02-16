Instalación
-------------------

Se asume un sistema con:

- [python](http://python.org) 2.6 o superior, incluso python 3.
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
        'NAME': 'fudepan',
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

Ahora podemos cargar el fixture para poblar nuestra base de datos:

    $ manage loaddata dump.json

De realizarse cambios en algún modelo ejecutar:

    $ manage makemigrations albums

Reemplazar *albums* con la aplicación que necesitamos migrar

En este punto tenemos nuestra instancia lista para correr el servidor de 
desarrollo:

    $ manage runserver

# Assets státicos.

Ahora queda generar los recursos de estilos, imágenes, íconos y scripts.
Para esto integramos [grunt](http://gruntjs.com/) y [bower](http://bower.io/).

Descargar las herramientas necesarias:

    $ npm install  

> a la fecha, grunt no incluye la interfaz de linea de comandos por defecto y 
> necesita ser instalado separado.
> para esto invocar:
    $ npm install -g grunt-cli
> utilizar *sudo* en caso que sea necesario

Instalar las bibliotecas utilizadas

    $ bower install

Ejecutar las tareas de grunt:

    $ grunt

Por defecto grunt funciona en modo `watch`, esto es: queda observando los archivos importantes de manera de re-ejecutar las tareas pertinentes.

Si sólo necesitamos `compilar` los recursos estáticos, invocar:

    $ grunt build

Ésto genera una carpeta `static/` en la raiz del proyecto, que podemos desplegar en nuestro servidor.
