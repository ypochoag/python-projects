# P3: Gestor de tareas con CRUD 

En este proyecto, se desarrolló un Sistema de Gestión de Tareas utilizando Python y Django Rest Framework,  que permite realizar operaciones básicas en tareas. A continuación, se detallan los requisitos, tecnologías utilizadas y pasos para implementar y utilizar este sistema.

### Descripción del Proyecto ###

El Sistema de Gestión de Tareas permite a los usuarios realizar las siguientes operaciones en las tareas:
- Crear una nueva tarea.
- Obtener la lista de todas las tareas.
- Obtener detalles de una tarea específica.
- Actualizar el estado de una tarea (pendiente, en progreso, completada).
- Eliminar una tarea.

### Implementación
Tecnologías Utilizadas
- Python
- Django: Framework web para Python.
  
### Características

- Operaciones Básicas (CRUD): Se implementan las operaciones CRUD para gestionar las tareas a través de la Django Rest Framework.
- Validaciones: Se implementan validaciones para garantizar que los campos obligatorios (título, descripción) estén presentes y que el estado sea uno de los valores permitidos (pendiente, en progreso, completada).
- Documentación: Se proporciona documentación sobre cómo utilizar la API mediante DRF YASG para generar documentación interactiva de la API.
- Pruebas Unitarias: Se escriben pruebas unitarias de todas las funcionalidades del Sistema de Gestión de Tareas.
- Base de Datos: Se crea una tabla llamada todos con campos como id, titulo, descripcion y estado.

### Endpoints

`POST` /api/v1 : Crear una nueva tarea. 

`GET` /api/v1 : Obtener la lista de todas las tareas. 

`GET` /api/v1/{id_tarea}: Obtener detalles de una tarea específica. 

`PUT` /api/v1/{id_tarea} : Actualizar el estado de una tarea (pendiente, en progreso, completada).  

`DELETE` : /api/v1/{id_tarea}: Eliminar una tarea.  

### Documentación

Para la documentación de la solución se implementó la herramienta [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) por lo tanto, una vez se encuentre en ejecución del proyecto, puedes acceder a la documentación de la API en los siguientes enlaces:

- [Documentación Swagger (Swagger UI)](http://localhost:8000/docs/)
- [Documentación Redoc (ReDoc)](http://localhost:8000/redocs/)

### Ejecución: Instrucciones para ejecutar el Proyecto Localmente

A continuación, se detallan los pasos necesarios para descargar y ejecutar el proyecto en máquina local.

- Clonar el Repositorio
Para comenzar, clona el repositorio en tu máquina local utilizando el siguiente comando en tu terminal:

```bash
git clone https://github.com/ypochoag/python-projects.git
```
- Acceder al Directorio del Proyecto
Navega al directorio del proyecto utilizando el siguiente comando

```bash
cd .\python-projects\proyecto3\todo\ 
```
- Instalar Dependencias y ejecutar entorno de trabajo
Una vez en el directorio del proyecto, instala las dependencias necesarias. Necesitas las herramientas pip y pipenv, ademas de una version de Python 3.10+ instaladas en tu computador. Luego ejecutar el siguiente comando:

```bash
pipenv shell 
```

- Ejecutar el Proyecto
Finalmente, ejecuta el proyecto utilizando el siguiente comando:

```bash
python manage.py runserver
```

Esto iniciará el servidor de desarrollo. Una vez iniciado, puedes acceder al proyecto a través de tu navegador web utilizando la URL local proporcionada, por ejemplo: http://localhost:8000/admin.

- Superusuario
La aplicacion fue configurada con los siguientes datos de superusuario:

```javaScript
{
    "username": "admin",
    "password": "admin12345"
}
```

