# Generated by Django 5.0.1 on 2024-01-05 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='description',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='title',
            new_name='titulo',
        ),
        migrations.AddField(
            model_name='todo',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('en_progreso', 'En Progreso'), ('completada', 'Completada')], default='pendiente', max_length=20),
        ),
    ]
