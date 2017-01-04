# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScoopApp', '0003_auto_20170104_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='craftbeer',
            name='sequence_added',
            field=models.IntegerField(default=0),
        ),
    ]
