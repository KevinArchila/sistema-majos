# Generated by Django 5.0.3 on 2024-05-03 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_usuario_servicio_correo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo_usuarios',
            name='usuario_servicio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='login.usuario_servicio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuarios',
            name='usuario_servicio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='login.usuario_servicio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='login.cargo_usuarios'),
        ),
    ]