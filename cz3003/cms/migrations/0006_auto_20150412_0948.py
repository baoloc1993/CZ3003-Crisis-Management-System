# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_auto_20150412_0415'),
    ]

    operations = [
        migrations.AddField(
            model_name='crisisinstance',
            name='crisisStatus',
            field=models.CharField(choices=[('P', 'Pending'), ('H', 'Happening'), ('S', 'Stopped')], max_length=200, default='Pending'),
        ),
        migrations.AlterField(
            model_name='crisisinstance',
            name='crisisType',
            field=models.CharField(choices=[('T', 'Tsunami'), ('H', 'Haze')], max_length=200),
        ),
    ]
