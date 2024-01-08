from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_usuarios, name='lista_usuarios'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('usuario/<int:pk>', views.obtener_usuario, name='obtener_usuario' ),
    path('eliminar/<int:pk>', views.eliminar_usuario, name='eliminar_usuario'),
    path('geocodificar_base/', views.geocodificar_base, name='geocodificar_base'),
]
