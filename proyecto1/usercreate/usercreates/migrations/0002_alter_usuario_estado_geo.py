# Generated by Django 5.0.1 on 2024-01-08 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercreates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='estado_geo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]