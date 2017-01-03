from __future__ import unicode_literals
from django.db import models


class Beer(models.Model):
    beer_name = models.CharField(max_length=200, primary_key=True)
    ABV = models.FloatField()
    SRM = models.IntegerField
    IBU = models.FloatField()
    acidity = models.IntegerField


    def __str__(self):
        return self.beer_name