# Proyectos Backend con Python

## P1: Sistema de Creación de Usuarios con CRUD y Autenticación

Este es un sistema sencillo de creación de usuarios que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en la base de datos. Además, se implementa un proceso de autenticación utilizando un token fijo para un servicio de autenticación según el estándar OAUTH 2.0.

### Características

- Base de Datos: Se crea una tabla llamada usuarios con campos como id, nombre, apellido, dirección, ciudad, tipo, longitud, latitud, estado_geo, y cargo.
- Autenticación: Se implementa un token fijo para autenticar al usuario y proporcionar un token de sesión para acceder a los endpoints.

### Endpoints:

- POST /crear: Permite crear usuarios diferenciando entre compradores y vendedores. La dirección es obligatoria para compradores, mientras que los vendedores tienen opciones de cargo.
- GET /lista: Retorna el listado de todos los usuarios con sus atributos.
- GET /usuario: Retorna un usuario específico por ID.
- DELETE /eliminar: Elimina un usuario específico por ID.
- GET /geocodificar_base: Actualiza la georreferenciación de compradores utilizando el servicio de geocoder de Google.

### Implementación
Tecnologías Utilizadas
- Django: Framework web para Python.
- OAuth 2.0: Para la autenticación [rest_framework_simplejwt].
- Google Geocoding API: Para georreferenciación.

### Nota:
- Se utilizó un **patrón de repositorio** para separar la lógica de acceso a datos, debido a la necesidad de creación de diferentes tipos de usuarios.
- Se diseñaron serializadores con restricciones adecuadas para garantizar el ingreso de los datos solicitados según especificaciones.
- Se optimizó el uso de la API geo codificación de Google, mediante la implementación de una tabla en base de datos la cual guardaba la longitud y latitud de acuerdo con la dirección ingresada, dicha información era usada antes de solicitar la información a la API de tal modo que si ya se había realizado una consulta anterior, se usaba los datos previos. 

### Documentación
Para la documentación de la solución se implementó la herramienta [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) por lo tanto, una vez se encuentre en ejecución del proyecto, puedes acceder a la documentación de la API en los siguientes enlaces:

- [Documentación Swagger (Swagger UI)](http://localhost:8000/docs/)
- [Documentación Redoc (ReDoc)](http://localhost:8000/redocs/)

## API KEY
Asegúrate de configurar adecuadamente las variables de entorno en un archivo `.env`. Se proporciona un Ejemplo de un archivo en `.env.example`.
