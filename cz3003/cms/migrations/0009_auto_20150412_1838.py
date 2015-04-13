# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_auto_20150412_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='sensorType',
            field=models.CharField(choices=[('PSI', 'PSI'), ('Wave speed', 'Wave speed'), ('Wave level', 'Wave level'), ('Earthquake level', 'Earthquake level')], max_length=200),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10, default=0.0),
        ),
    ]
