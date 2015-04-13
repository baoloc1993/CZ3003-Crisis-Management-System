# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20150412_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensordata',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='level',
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='longitude',
        ),
        migrations.AddField(
            model_name='sensordata',
            name='value',
            field=models.DecimalField(default=1, max_digits=10, decimal_places=2),
            preserve_default=False,
        ),
    ]
