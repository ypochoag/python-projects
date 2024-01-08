from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from datetime import timedelta
from rest_framework import status
from django.contrib.auth import authenticate

@api_view(['POST'])
def obtener_token(request):
    username = request.data.get('username')
    password = request.data.get('password')    
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        
        refresh = RefreshToken.for_user(request.user)
        access_token = str(refresh.token)   
           
        return Response({'access_token': access_token}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)




