# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20150412_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crisisinstance',
            name='crisisType',
            field=models.CharField(max_length=200, choices=[('Tsunami', 'Tsunami'), ('Haze', 'Haze')]),
        ),
    ]
