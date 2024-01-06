from django.db import models

class Todo(models.Model):
    ESTADOS= (
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    )

    titulo = models.CharField(max_length=200, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return self.titulo