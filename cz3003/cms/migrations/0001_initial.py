# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CallOperatorForm',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('id_of_caller', models.CharField(max_length=10)),
                ('name_of_caller', models.CharField(max_length=200)),
                ('contact_number', models.IntegerField(max_length=20)),
                ('nric', models.CharField(max_length=10)),
                ('content', models.CharField(max_length=200)),
                ('operator_id', models.CharField(max_length=200)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('X_coordinate', models.DecimalField(max_digits=30, decimal_places=10)),
                ('Y_coordinate', models.DecimalField(max_digits=30, decimal_places=10)),
                ('severity_level', models.CharField(max_length=200)),
                ('status', models.DecimalField(max_digits=1, decimal_places=0, default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CrisisInstance',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('type_crisis', models.CharField(max_length=200)),
                ('severity_level', models.CharField(max_length=200)),
                ('location_crisis', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField(max_length=200)),
                ('content', models.CharField(max_length=200)),
                ('staff_id', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmailMonitoring',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('crisis_content', models.CharField(max_length=200)),
                ('event_time', models.DateField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name_location', models.CharField(max_length=200)),
                ('x_location', models.FloatField(default=0.0)),
                ('y_location', models.FloatField(default=0.0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GoogleMap',
            fields=[
                ('map_ptr', models.OneToOneField(primary_key=True, to='cms.Map', auto_created=True, serialize=False, parent_link=True)),
            ],
            options={
            },
            bases=('cms.map',),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('crisis_instance', models.ForeignKey(to='cms.CrisisInstance')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=200)),
                ('time', models.DateTimeField(max_length=200)),
                ('type', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NEA',
            fields=[
                ('sensordata_ptr', models.OneToOneField(primary_key=True, to='cms.SensorData', auto_created=True, serialize=False, parent_link=True)),
            ],
            options={
            },
            bases=('cms.sensordata',),
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('sensordata_ptr', models.OneToOneField(primary_key=True, to='cms.SensorData', auto_created=True, serialize=False, parent_link=True)),
            ],
            options={
            },
            bases=('cms.sensordata',),
        ),
        migrations.AddField(
            model_name='map',
            name='sensor',
            field=models.ForeignKey(to='cms.SensorData'),
            preserve_default=True,
        ),
    ]
