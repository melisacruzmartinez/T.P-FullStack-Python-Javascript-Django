# Generated by Django 3.1.3 on 2020-11-28 09:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0027_auto_20201128_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 9, 36, 4, 975267, tzinfo=utc)),
        ),
    ]
