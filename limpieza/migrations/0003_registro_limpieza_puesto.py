# Generated by Django 5.0.3 on 2024-05-29 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limpieza', '0002_rename_usuario_id_registro_limpieza_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro_limpieza',
            name='puesto',
            field=models.CharField(default='COCINA', max_length=20),
            preserve_default=False,
        ),
    ]
