# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calloperatorform',
            name='status',
            field=models.DecimalField(decimal_places=0, max_digits=1),
            preserve_default=True,
        ),
    ]
