# P1: Sistema de Creación de Usuarios con CRUD y Autenticación

Este es un sistema sencillo de creación de usuarios que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en la base de datos. Además, se implementa un proceso de autenticación utilizando un token fijo para un servicio de autenticación según el estándar OAUTH 2.0.

## Características
- La creación de usuarios se realiza por medio de la funcionalidad /admin/ del Framework Django, por lo tanto para hacer gestion de los mismos (creación, edición, activación, desactivación y eliminación) se hace a travez de la siguiente url: (es necesario primero ejecutar el proyecto)
   `/admin/` : <http://localhost:8000/admin/>
```javaScript
    "username": "admin",
    "password": "admin12345"
```
  
- Base de Datos: Se crea una tabla llamada usuarios con campos como id, nombre, apellido, dirección, ciudad, tipo, longitud, latitud, estado_geo, y cargo.
- Autenticación: Se implementa un token fijo para autenticar al usuario y proporcionar un token de sesión para acceder a los endpoints.

## Endpoints:

- POST /crear: Permite crear usuarios diferenciando entre compradores y vendedores. La dirección es obligatoria para compradores, mientras que los vendedores tienen opciones de cargo.
- GET /lista: Retorna el listado de todos los usuarios con sus atributos.
- GET /usuario: Retorna un usuario específico por ID.
- DELETE /eliminar: Elimina un usuario específico por ID.
- GET /geocodificar_base: Actualiza la georreferenciación de compradores utilizando el servicio de geocoder de Google.

## Implementación
Tecnologías Utilizadas
- Django: Framework web para Python.
- OAuth 2.0: Para la autenticación [rest_framework_simplejwt].
- Google Geocoding API: Para georreferenciación.

## Nota:
- Se utilizó un **patrón de repositorio** para separar la lógica de acceso a datos, debido a la necesidad de creación de diferentes tipos de usuarios.
- Se diseñaron serializadores con restricciones adecuadas para garantizar el ingreso de los datos solicitados según especificaciones.
- Se optimizó el uso de la API geo codificación de Google, mediante la implementación de una tabla en base de datos la cual guardaba la longitud y latitud de acuerdo con la dirección ingresada, dicha información era usada antes de solicitar la información a la API de tal modo que si ya se había realizado una consulta anterior, se usaba los datos previos. 

## Documentación
Para la documentación de la solución se implementó la herramienta [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) por lo tanto, una vez se encuentre en ejecución del proyecto, puedes acceder a la documentación de la API en los siguientes enlaces:

- [Documentación Swagger (Swagger UI)](http://localhost:8000/docs/)
- [Documentación Redoc (ReDoc)](http://localhost:8000/redocs/)

## Ejecución: Instrucciones para ejecutar el Proyecto Localmente

A continuación, se detallan los pasos necesarios para descargar y ejecutar el proyecto en máquina local.

- Clonar el Repositorio

Para comenzar, clona el repositorio en tu máquina local utilizando el siguiente comando en tu terminal:

```bash
git clone https://github.com/ypochoag/python-projects.git
```
- Acceder al Directorio del Proyecto
Navega al directorio del proyecto utilizando el siguiente comando

```bash
cd .\python-projects\proyecto1\usercreate\ 
```

- API KEY
Asegúrate de configurar adecuadamente las variables de entorno en un archivo `.env`. Se proporciona un Ejemplo de un archivo en `.env.example`.

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
Esto iniciará el servidor de desarrollo. Una vez iniciado, puedes acceder al proyecto a través de tu navegador web utilizando la URL local proporcionada, por ejemplo: http://localhost:8000/.

- Superusuario
La aplicacion fue configurada con los siguientes datos de superusuario
```javaScript
{
    "username": "admin",
    "password": "admin12345"
}
```
- Generación de tokens
La aplicación fue configurada para tener dos tokens de sesión, uno esta configurado para tener disponibilidad por 10 minutos  "access" el cual nos sirve para usar los endpoints protegidos y el otro tiene disponibilidad de uso de un dia "refresh", el cual, se usa para obtener una nueva actualización del token access, para hacer uso de estos se dispone de los siguientes endpoints:

 `POST` : <http://localhost:8000/api/token/>

 ```javaScript
body = {
    "username": "admin",
    "password": "admin12345"
}
```
 
 `POST` : <http://localhost:8000/api/token/refresh/>
 ```javaScript
body = {
    "refresh": TOKEN_REFRESH
}
```
Para ejecutar las funcionalidades de la aplicación puedes usar Postman y recuerda configurar la autorización de tipo Bearer Token e ingresar el "access" token valido.
