from rest_framework import serializers
from todos import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'titulo',
            'descripcion',
            'estado',
        )
        model = models.Todo
    