# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20150410_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calloperatorform',
            name='status',
            field=models.SmallIntegerField(),
            preserve_default=True,
        ),
    ]
