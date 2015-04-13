# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crisisinstance',
            old_name='lattitude',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='crisisinstance',
            old_name='longtitude',
            new_name='longitude',
        ),
        migrations.RenameField(
            model_name='sensordata',
            old_name='lattitude',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='sensordata',
            old_name='longtitude',
            new_name='longitude',
        ),
        migrations.RemoveField(
            model_name='calloperatorform',
            name='X_coordinate',
        ),
        migrations.RemoveField(
            model_name='calloperatorform',
            name='Y_coordinate',
        ),
        migrations.AddField(
            model_name='calloperatorform',
            name='latitude',
            field=models.DecimalField(max_digits=30, decimal_places=10, default=1.3011873),
        ),
        migrations.AddField(
            model_name='calloperatorform',
            name='longitude',
            field=models.DecimalField(max_digits=30, decimal_places=10, default=103.8495055),
        ),
    ]
