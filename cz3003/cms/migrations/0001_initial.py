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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('account_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CallOperatorForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
                ('status', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CrisisInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('crisisType', models.CharField(max_length=200)),
                ('severity_level', models.CharField(max_length=200)),
                ('lattitude', models.DecimalField(max_digits=30, decimal_places=10, default=1.3011873)),
                ('longtitude', models.DecimalField(max_digits=30, decimal_places=10, default=103.8495055)),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('note', models.CharField(max_length=200)),
                ('staff_id', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='EmailMonitoring',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('crisis_content', models.CharField(max_length=200)),
                ('event_time', models.DateField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name_location', models.CharField(max_length=200)),
                ('x_location', models.FloatField(default=0.0)),
                ('y_location', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('crisis_instance', models.ForeignKey(to='cms.CrisisInstance')),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('sensorType', models.CharField(max_length=200)),
                ('lattitude', models.DecimalField(max_digits=30, decimal_places=10, default=1.3011873)),
                ('longtitude', models.DecimalField(max_digits=30, decimal_places=10, default=103.8495055)),
                ('level', models.SmallIntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='GoogleMap',
            fields=[
                ('map_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to='cms.Map', primary_key=True)),
            ],
            bases=('cms.map',),
        ),
        migrations.AddField(
            model_name='map',
            name='sensor',
            field=models.ForeignKey(to='cms.SensorData'),
        ),
    ]
