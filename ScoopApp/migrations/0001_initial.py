# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CraftBeer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('beerID', models.CharField(default='BeerID', max_length=10)),
                ('beer_name', models.CharField(default='BeerName', max_length=200)),
                ('ABV', models.FloatField(default='4.5')),
                ('SRM', models.IntegerField(default='4')),
                ('IBU', models.FloatField(default='25')),
                ('acidity', models.IntegerField(default='0')),
                ('image_link', models.CharField(default='http://1.bp.blogspot.com/-lR_pck9k_t8/VFxRlkfDr4I/AAAAAAAAAOI/pw249IysvYo/s1600/How%2Bto%2Breload%2Bimage%2Bin%2Bchrome.png', max_length=300)),
            ],
        ),
    ]
