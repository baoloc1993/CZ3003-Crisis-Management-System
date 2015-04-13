# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_remove_calloperatorform_id_of_caller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crisisinstance',
            name='crisisType',
            field=models.CharField(max_length=200, choices=[('M', 'Male'), ('F', 'Female')]),
        ),
    ]
