# Generated by Django 5.0.3 on 2024-05-29 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nevera', '0003_cambio_tempe_usuario_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='cambio_tempe',
            name='puesto',
            field=models.CharField(default='COCINA', max_length=20),
            preserve_default=False,
        ),
    ]
