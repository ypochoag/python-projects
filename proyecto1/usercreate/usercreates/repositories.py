from .models import Usuario
import requests

class UsuarioRepository:
    
    @staticmethod
    def crear_usuario(data):
        tipo = data.get('tipo')
        direccion = data.get('direccion') if tipo == 'comprador' else None
        cargo = data.get('cargo') if tipo == 'vendedor' else None

        usuario = Usuario(
            nombre=data.get('nombre'),
            apellido=data.get('apellido'),
            direccion=direccion,
            ciudad=data.get('ciudad'),
            tipo=tipo,
            cargo=cargo,
        )
        usuario.save()
        return usuario
    
    @staticmethod
    def obtener_todos_los_usuarios():
        return Usuario.objects.all()

    @staticmethod
    def obtener_usuario_por_id(usuario_id):
        try:
            return Usuario.objects.get(id=usuario_id)
        except Usuario.DoesNotExist:
            return None
    
    @staticmethod
    def eliminar_usuario(usuario_id):
        Usuario.objects.filter(id=usuario_id).delete()
    
    @staticmethod
    def geocodificar_compradores():

        usuarios_compradores_sin_geocodificar = Usuario.objects.filter(
            tipo='comprador', longitud=0, latitud=0
        )
        
        for usuario in usuarios_compradores_sin_geocodificar:
            address = f"{usuario.direccion}, {usuario.ciudad}"
            
            params = {
                'address': address,
                'key': 'AIzaSyD0txU5n7xlPZ3zkEsEjW09yVHmmEVjU4o'
            }
            
            response = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=params)
            data = response.json()

            if data['status'] == 'OK':
                location = data['results'][0]['geometry']['location']
                usuario.longitud = location['lng']
                usuario.latitud = location['lat']
                usuario.save()
            else:
                usuario.longitud = 0
                usuario.latitud = 0
                usuario.save()