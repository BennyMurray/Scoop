# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScoopApp', '0002_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='id',
        ),
        migrations.AlterField(
            model_name='test',
            name='first_name',
            field=models.CharField(max_length=30, serialize=False, primary_key=True),
        ),
    ]
