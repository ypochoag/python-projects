from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .repositories import UsuarioRepository
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@csrf_exempt
@api_view(['POST']) 
def crear_usuario(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            UsuarioRepository.crear_usuario(serializer.validated_data)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'error': 'Metodo no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def lista_usuarios(request):
    usuarios = list(UsuarioRepository.obtener_todos_los_usuarios().values())
    return JsonResponse(usuarios, safe=False)

def obtener_usuario(request, pk):
    usuario = UsuarioRepository.obtener_usuario_por_id(pk)
    if usuario:
        return JsonResponse(model_to_dict(usuario))
    else:
        return JsonResponse({'mensaje': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def eliminar_usuario(request, pk):
    if request.method == 'DELETE':
        usuario = UsuarioRepository.obtener_usuario_por_id(pk)
        if usuario:
            UsuarioRepository.eliminar_usuario(pk)
            return JsonResponse({'mensaje': 'Usuario eliminado correctamente'})
        else:
            return JsonResponse({'mensaje': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'error': 'Metodo no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

def geocodificar_base(request):
    UsuarioRepository.geocodificar_compradores()
    return JsonResponse({'mensaje': 'Geocodificacion realizada correctamente'})
