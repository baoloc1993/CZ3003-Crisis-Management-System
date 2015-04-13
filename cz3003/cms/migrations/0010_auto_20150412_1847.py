# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_auto_20150412_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='sensorType',
            field=models.CharField(unique=True, max_length=200, choices=[('PSI', 'PSI'), ('Wave speed', 'Wave speed'), ('Wave level', 'Wave level'), ('Earthquake level', 'Earthquake level')]),
        ),
    ]
