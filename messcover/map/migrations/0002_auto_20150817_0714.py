# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='link',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='tree',
            name='name',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
