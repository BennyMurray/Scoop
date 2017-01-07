
from __future__ import division
from django.shortcuts import render
from rest_framework import viewsets
from .models import CraftBeer
from .models import Test
from .models import Visitor
from .serializers import CraftBeerSerializer, VisitorSerializer
from django.forms.models import model_to_dict
import json
import sys
from rest_framework.views import APIView
from rest_framework.response import Response
from findBeer import *
from geolocator import getGeoLocation
from time import sleep

from ast import literal_eval


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





    # dict = model_to_dict(CraftBeer)



    def retrieve(self, request, *args, **kwargs):
        return Response({'something1': 'my custom JSON1'})



    def list(self, request, *args, **kwargs):






        #Convert model objects to dictionary
        new_dict = {}


        # for i in range(1, CraftBeer.objects.count()+1):
        for beer in CraftBeer.objects.all():



            x = model_to_dict(beer,
                              fields=['beer_name', 'beerID', 'ABV', 'IBU', 'SRM', 'acidity', 'image_link'],
                              # fields to include
                              exclude=['sequence_added'],  # fields to exclude
                              )
            # print >> sys.stderr, x['beer_name']

            new_dict[x['beer_name']] = [x['ABV'], x['IBU'], x['SRM'], x['acidity'], x['image_link']]
        #pickle.dump(new_dict, open("evenbetterdatabase.p", "wb"))


        # Receive Data from user
        abv = request.GET.get('a', '')
        colour = request.GET.get('b', '')
        ibu = request.GET.get('c', '')
        acidity = request.GET.get('d', '')
        ip_address = request.GET.get('e', '')
        user_region = request.GET.get('f', '')



        user_input = [float(abv), float(colour), float(ibu), float(acidity)]

        # Create Visitor Object with Search Parameters

        existing_ip_count = Visitor.objects.filter(ip_address=ip_address).count()
        

        if existing_ip_count < 1:
            add_Visitor(Visitor.objects.count() + 1, ip_address, user_region, str(user_input))




        # print >> '!!!!!!!', type(ip_address) is str
        # Visitor.objects.get(ip_address='128').update(search_parameters='string')
        # print >> sys.stderr, "USER INPUT RECORDED"


        #user_input = [10,10,10,10]


        #Run user's data through beer-finding algorithm and return the results as JSON
        json_for_export = find_beer(user_input, new_dict)

        return Response(json_for_export)



def averageListValues(a):
    return round(sum(a) / len(a),1)




class VisitorAPIViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer



    def retrieve(self, request, *args, **kwargs):
        return Response({'something1': 'my custom JSON1'})



    def list(self, request, *args, **kwargs):






        #Convert model objects to dictionary
        leinster_list = []
        munster_list = []
        ulster_list = []
        connaught_list = []

        # for i in range(1, CraftBeer.objects.count()+1):
        for visitor in Visitor.objects.all():

            x = model_to_dict(visitor,
                              fields=['ip_address', 'geolocation', 'search_parameters'],
                              # fields to include
                              exclude=[''],  # fields to exclude
                              )
            # print >> sys.stderr, x['beer_name']

            # list_of_lists.append(literal_eval(x['search_parameters']))
            if x['search_parameters'] != 'placeholder':
                if x['geolocation'].lower() == 'leinster':
                    leinster_list.append(literal_eval(x['search_parameters']))
                elif x['geolocation'].lower() == 'munster':
                    munster_list.append(literal_eval(x['search_parameters']))
                elif x['geolocation'].lower() == 'ulster':
                    ulster_list.append(literal_eval(x['search_parameters']))
                elif x['geolocation'].lower() == 'connaught':
                    connaught_list.append(literal_eval(x['search_parameters']))



            json_for_export = {

                'leinster': map(averageListValues, zip(*leinster_list)),
                'munster': map(averageListValues, zip(*munster_list)),
                'ulster': map(averageListValues, zip(*ulster_list)),
                'connaught': map(averageListValues, zip(*connaught_list))

                               }

        # print >> '!!!!!!!', type(ip_address) is str
        # Visitor.objects.get(ip_address='128').update(search_parameters='string')
        # print >> sys.stderr, "USER INPUT RECORDED"



        #Run user's data through beer-finding algorithm and return the results as JSON


        return Response(json_for_export)