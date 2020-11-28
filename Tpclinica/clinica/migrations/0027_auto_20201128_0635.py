# Generated by Django 3.1.3 on 2020-11-28 09:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clinica', '0026_merge_20201128_0632'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnos',
            name='FechaAlta',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='turnos',
            name='FechaBaja',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 9, 35, 22, 57284, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clinica_paciente', to='clinica.paciente'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='vendedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
