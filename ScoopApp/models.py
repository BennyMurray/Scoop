from __future__ import unicode_literals
from django.db import models


class CraftBeer(models.Model):
    beerID = models.CharField(max_length=10, default="BeerID")
    beer_name = models.CharField(max_length=200, default="BeerName")
    ABV = models.FloatField(default="4.5")
    SRM = models.IntegerField(default="4")
    IBU = models.FloatField(default="25")
    acidity = models.IntegerField(default="0")
    image_link = models.CharField(max_length=300, default="http://i.imgur.com/kB5Xe4v.jpg")
    sequence_added = models.IntegerField(default=0)


    def __str__(self):
        return self.beer_name

class Visitor(models.Model):
    visitor_number = models.IntegerField(primary_key=True)
    ip_address = models.CharField(max_length=30)
    geolocation = models.CharField(max_length=100, null=True)
    search_parameters = models.CharField(max_length=100)

    @classmethod
    def create(cls, ip_address, geolocation, search_parameters):
        visitor = cls(ip_address=ip_address, geolocation=geolocation, search_parameters=search_parameters)

        return visitor
