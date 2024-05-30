# Proyecto Hipoteca Inversa en Python con practicas de Clean Code


## ¿Quién hizo esto?

- Alejandro Gutierrez Vallejo
- Andrea Márquez Sánchez

## ¿Qué es y para qué es?

Este proyecto tiene como objetivo calcular una Hipoteca Inversa.
Aplicación de base de datos de muestra que utiliza el patrón MVC vinculado a postgreSQL

## ¿Cómo lo hago funcionar?

Prerrequisitos:
- Asegurese de tener una base de datos PostgreSQL y sus respectivos datos de acceso

- Copie el archivo Secret_Config-sample.py como Secret_Config.py y establezca en este archivo los datos de conexion a su base de datos.


Instale el paquete psycopg2 con:
`
pip install psycopg2
`

## Estructura sugerida

La estructura del proyecto sigue las prácticas recomendadas para mantener un código organizado y modular. A continuación, se describe la estructura sugerida:

- src: Esta carpeta contiene el código fuente de la aplicación. Está organizada en capas para facilitar el mantenimiento y la escalabilidad del proyecto. La estructura de carpetas dentro de src es la siguiente:

* Controller: Contiene el codigo fuente con la conexion a la base de datos y los querys que se pueden ejecutar

* Model: Contiene el codigo fuente para modelar los usuarios que se van a ingresar a la base de datos.

* View_console: Contiene el codigo fuente de la interfaz por consola.

- tests: Esta carpeta contiene las pruebas unitarias para validar el correcto funcionamiento del código.
