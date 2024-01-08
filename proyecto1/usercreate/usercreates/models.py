from django.db import models

class Usuario(models.Model):

    TIPO_CHOICES = [
        ('comprador', 'Comprador'),
        ('vendedor', 'Vendedor'),
    ]

    CARGO_CHOICES = [
        ('asesor', 'Asesor'),
        ('cajero', 'Cajero'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    cargo = models.CharField(max_length=50, choices=CARGO_CHOICES, blank=True, null=True)
    longitud = models.FloatField(default=0, blank=True, null=True)
    latitud = models.FloatField(default=0, blank=True, null=True)
    estado_geo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"