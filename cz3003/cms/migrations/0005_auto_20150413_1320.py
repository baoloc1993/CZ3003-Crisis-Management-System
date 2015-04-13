# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20150412_1036'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CMSUser',
        ),
        migrations.RemoveField(
            model_name='nea',
            name='sensordata_ptr',
        ),
        migrations.DeleteModel(
            name='NEA',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='sensordata_ptr',
        ),
        migrations.DeleteModel(
            name='Weather',
        ),
        migrations.RenameField(
            model_name='crisisinstance',
            old_name='content',
            new_name='note',
        ),
        migrations.RemoveField(
            model_name='calloperatorform',
            name='X_coordinate',
        ),
        migrations.RemoveField(
            model_name='calloperatorform',
            name='Y_coordinate',
        ),
        migrations.RemoveField(
            model_name='calloperatorform',
            name='id_of_caller',
        ),
        migrations.RemoveField(
            model_name='crisisinstance',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='crisisinstance',
            name='location_crisis',
        ),
        migrations.RemoveField(
            model_name='crisisinstance',
            name='type_crisis',
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='data',
        ),
        migrations.AddField(
            model_name='calloperatorform',
            name='latitude',
            field=models.DecimalField(max_digits=30, default=1.3011873, decimal_places=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calloperatorform',
            name='longitude',
            field=models.DecimalField(max_digits=30, default=103.8495055, decimal_places=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crisisinstance',
            name='crisisStatus',
            field=models.CharField(default='Pending', max_length=200, choices=[('P', 'Pending'), ('H', 'Happening'), ('S', 'Stopped')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crisisinstance',
            name='crisisType',
            field=models.CharField(default=datetime.datetime(2015, 4, 13, 13, 20, 8, 717790, tzinfo=utc), max_length=200, choices=[('Tsunami', 'Tsunami'), ('Haze', 'Haze')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crisisinstance',
            name='latitude',
            field=models.DecimalField(max_digits=30, default=1.3011873, decimal_places=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crisisinstance',
            name='longitude',
            field=models.DecimalField(max_digits=30, default=103.8495055, decimal_places=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crisisinstance',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sensordata',
            name='sensorType',
            field=models.CharField(unique=True, default=datetime.datetime(2015, 4, 13, 13, 20, 29, 655359, tzinfo=utc), max_length=200, choices=[('PSI', 'PSI'), ('Wave speed', 'Wave speed'), ('Water level', 'Water level'), ('Earthquake level', 'Earthquake level')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensordata',
            name='value',
            field=models.DecimalField(max_digits=10, default=0.0, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
