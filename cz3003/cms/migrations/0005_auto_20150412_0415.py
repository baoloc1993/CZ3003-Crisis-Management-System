# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20150412_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crisisinstance',
            name='crisisType',
            field=models.CharField(default='Pending', choices=[('P', 'Pending'), ('H', 'Happening'), ('S', 'Stopped')], max_length=200),
        ),
    ]
