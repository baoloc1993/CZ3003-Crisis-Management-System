# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20150323_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailMonitoring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GoogleMap',
            fields=[
                ('map_ptr', models.OneToOneField(auto_created=True, to='cms.Map', primary_key=True, parent_link=True, serialize=False)),
            ],
            options={
            },
            bases=('cms.map',),
        ),
        migrations.CreateModel(
            name='NEA',
            fields=[
                ('sensordata_ptr', models.OneToOneField(auto_created=True, to='cms.SensorData', primary_key=True, parent_link=True, serialize=False)),
            ],
            options={
            },
            bases=('cms.sensordata',),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('crisis_instance', models.ForeignKey(to='cms.CrisisInstance')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('sensordata_ptr', models.OneToOneField(auto_created=True, to='cms.SensorData', primary_key=True, parent_link=True, serialize=False)),
            ],
            options={
            },
            bases=('cms.sensordata',),
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='id',
        ),
        migrations.AddField(
            model_name='map',
            name='sensor',
            field=models.ForeignKey(to='cms.SensorData', default=datetime.datetime(2015, 3, 23, 18, 29, 29, 322414, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='time',
            field=models.DateTimeField(primary_key=True, serialize=False, max_length=200),
            preserve_default=True,
        ),
    ]
