# Generated by Django 3.1.3 on 2020-11-29 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0006_auto_20201129_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turnos',
            name='Consulta',
        ),
        migrations.AlterField(
            model_name='consulta',
            name='observaciones',
            field=models.ManyToManyField(to='clinica.Observacion', verbose_name='Observaciones'),
        ),
    ]
