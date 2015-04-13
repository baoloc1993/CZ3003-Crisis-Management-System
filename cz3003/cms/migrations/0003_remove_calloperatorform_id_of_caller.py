# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20150412_0349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calloperatorform',
            name='id_of_caller',
        ),
    ]
