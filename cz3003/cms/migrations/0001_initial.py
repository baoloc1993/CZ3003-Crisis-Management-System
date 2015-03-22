# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallOperatorForm',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('id_caller', models.CharField(max_length=10)),
                ('name_caller', models.CharField(max_length=200)),
                ('contact_number', models.IntegerField(max_length=20)),
                ('nric', models.CharField(max_length=10)),
                ('content', models.CharField(max_length=200)),
                ('operator_id', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField(verbose_name='date published')),
                ('location', models.CharField(max_length=200)),
                ('severity_level', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name_location', models.CharField(max_length=200)),
                ('x_location', models.FloatField(default=0.0)),
                ('y_location', models.FloatField(default=0.0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReportForm',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
    ]
