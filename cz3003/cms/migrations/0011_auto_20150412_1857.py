# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_auto_20150412_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='sensorType',
            field=models.CharField(unique=True, choices=[('PSI', 'PSI'), ('Wave speed', 'Wave speed'), ('Water level', 'Water level'), ('Earthquake level', 'Earthquake level')], max_length=200),
        ),
    ]
