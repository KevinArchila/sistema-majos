# Generated by Django 5.0.3 on 2024-05-06 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0006_rename_horario_limpieza_limpieza_puestos_horario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='limpieza_puestos',
            name='horario',
        ),
    ]
