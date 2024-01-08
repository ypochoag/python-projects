from rest_framework import serializers
from usercreates import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'nombre',
            'apellido',
            'direccion',
            'ciudad',
            'tipo',
            'cargo',
            'longitud',
            'latitud',
            'estado_geo',
        )
        model = models.Usuario

    def validate(self, data):
        tipo = data.get('tipo')
        cargo = data.get('cargo')

        if tipo == 'comprador' and not data.get('direccion'):
            raise serializers.ValidationError("La direccion es obligatoria para compradores.")
        
        if tipo == 'comprador' and cargo:
            raise serializers.ValidationError("El cargo no es requerido para compradores.")
        
        if tipo == 'vendedor' and not cargo:
            raise serializers.ValidationError("El cargo es obligatorio para vendedores.")
        
        return data    