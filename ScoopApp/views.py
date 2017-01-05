from django.shortcuts import render
from rest_framework import viewsets
from .models import CraftBeer
from .models import Test
from .models import Visitor
from .serializers import CraftBeerSerializer
from django.forms.models import model_to_dict
import json
import sys
from rest_framework.views import APIView
from rest_framework.response import Response
from findBeer import *
from geolocator import getGeoLocation
from time import sleep


from django.shortcuts import get_list_or_404, get_object_or_404

def get_ip_address(request):
    """ use requestobject to fetch client machine's IP Address """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')    ### Real IP address of client Machine
    return ip


def add_Visitor(visitor_number, ip_address, geolocation, search_parameters):
    v, created = Visitor.objects.get_or_create(visitor_number=visitor_number, ip_address=ip_address, geolocation=geolocation, search_parameters=search_parameters)
    print ("- Visitor: {0}, Created: {1}".format(str(v), str(created)))
    return v

#INDEX VIEW
def indexView(request):
    visitor_number = Visitor.objects.count() + 1
    ip_address = get_ip_address(request)
    geolocation = getGeoLocation(ip_address)
    add_Visitor(visitor_number, ip_address, geolocation, "placeholder")

    return render(request, 'ScoopApp/index.html', {})


#INDEX VIEW
def mapView(request):
    return render(request, 'ScoopApp/map.html', {})

class CraftBeerAPIViewSet(viewsets.ModelViewSet):
    queryset = CraftBeer.objects.all()
    serializer_class = CraftBeerSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = CraftBeer.objects.all()
    serializer_class = CraftBeerSerializer

    # dict = model_to_dict(CraftBeer)



    def retrieve(self, request, *args, **kwargs):
        return Response({'something1': 'my custom JSON1'})

    def list(self, request, *args, **kwargs):


        from django.core import serializers
        new_dict = {}
        for i in range(1,150):
            my_obj = CraftBeer.objects.get(sequence_added=i)
            x = model_to_dict(my_obj,
                          fields=['beer_name', 'beerID', 'ABV', 'IBU', 'SRM', 'acidity', 'image_link'],  # fields to include
                          exclude=['sequence_added'],  # fields to exclude
                          )
            #print >> sys.stderr, x['beer_name']
            new_dict[x['beer_name']] = [x['ABV'], x['IBU'], x['SRM'], x['acidity'], x['image_link']]

        json_for_export = find_beer([100,100,100,100], new_dict)
        print >> sys.stderr, "\n",json_for_export
        return Response(json_for_export)