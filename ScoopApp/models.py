from __future__ import unicode_literals
from django.db import models


class CraftBeer(models.Model):
    beerID = models.CharField(max_length=10, default="BeerID")
    beer_name = models.CharField(max_length=200, default="BeerName")
    ABV = models.FloatField(default="4.5")
    SRM = models.IntegerField(default="4")
    IBU = models.FloatField(default="25")
    acidity = models.IntegerField(default="0")
    image_link = models.CharField(max_length=300, default="http://1.bp.blogspot.com/-lR_pck9k_t8/VFxRlkfDr4I/AAAAAAAAAOI/pw249IysvYo/s1600/How%2Bto%2Breload%2Bimage%2Bin%2Bchrome.png")
    sequence_added = models.IntegerField(default=0)



    def __str__(self):
        return self.beer_name




class Test(models.Model):
    first_name = models.CharField(max_length=30, primary_key=True)
    last_name = models.CharField(max_length=30)