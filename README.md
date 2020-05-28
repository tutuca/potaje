## Potaje

Un manojo de ideas

![build status](https://travis-ci.org/tutuca/potaje.svg?branch=master)

## Instalación

Se asume un sistema con:

- [python](http://python.org).
- [pip](http://www.pip-installer.org/), [virtualenv](http://www.virtualenv.org/)

Solo para desarrollo:

- [node](http://nodejs.org/)
- [npm](https://www.npmjs.org/)

Clonar el repositorio

```sh
    $ git clone git@github.com:tutuca/potaje.git
    ...
    $ cd potaje
```

Instalar las dependencias

    $ pip install -r requirements.txt

## Configuración local

Se usa [django-environ](https://django-environ.readthedocs.io/en/latest/) para las configuraciones de entorno.
Los valores por defecto deberían funcionar sin más configuración.

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
