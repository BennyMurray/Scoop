from __future__ import division
import sys
from ast import literal_eval
from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from findBeer import *
from findStyle import *
from .models import CraftBeer
from .models import Visitor
from .serializers import CraftBeerSerializer, VisitorSerializer


#ADD VISITOR OBJECT FUNCTION
#-------------#
def add_Visitor(visitor_number, ip_address, geolocation, search_parameters):
    v, created = Visitor.objects.get_or_create(visitor_number=visitor_number, ip_address=ip_address, geolocation=geolocation, search_parameters=search_parameters)
    print ("- Visitor: {0}, Created: {1}".format(str(v), str(created)))
    return v

#HOMEPAGE VIEW
#-------------#
def indexView(request):
    return render(request, 'ScoopApp/index.html', {})


#ABOUT PAGE VIEW
#-------------#
def aboutView(request):
    return render(request, 'ScoopApp/about.html', {})


#MAP PAGE VIEW
#-------------#
def mapView(request):
    return render(request, 'ScoopApp/map.html', {})






#CRAFTBEER API VIEW
#------------------#
class CraftBeerAPIViewSet(viewsets.ModelViewSet):
    queryset = CraftBeer.objects.all()
    serializer_class = CraftBeerSerializer


    def retrieve(self, request, *args, **kwargs):
        return Response({'something1': 'my custom JSON1'})

    def list(self, request, *args, **kwargs):


        #Convert model objects to dictionary
        new_dict = {}
        for beer in CraftBeer.objects.all():
            converted_object = model_to_dict(beer,
                              #fields to include
                              fields=['beer_name', 'beerID', 'ABV', 'IBU', 'SRM', 'acidity', 'image_link'],
                              #fields to exclude
                              exclude=['sequence_added'],
                              )
            #populate empty_dictionary with converted beer objects
            new_dict[converted_object['beer_name']] = [converted_object['ABV'], converted_object['IBU'], converted_object['SRM'], converted_object['acidity'], converted_object['image_link']]

        #pickle.dump(new_dict, open("printme.p", "wb"))


        # Receive Data from client
        abv = request.GET.get('a', '')
        colour = request.GET.get('b', '')
        ibu = request.GET.get('c', '')
        acidity = request.GET.get('d', '')
        ip_address = request.GET.get('e', '')
        user_region = request.GET.get('f', '')


        #Client Search Parameters
        user_input = [float(abv), float(colour), float(ibu), float(acidity)]

        # Create Visitor Object with Search Parameters
        existing_ip_count = Visitor.objects.filter(ip_address=ip_address).count()
        if existing_ip_count < 1:

            add_Visitor(Visitor.objects.count() + 1, ip_address, user_region, str(user_input))

        #Run user's data through beer-finding algorithm and return the results as JSON
        json_for_export = find_beer(user_input, new_dict)

        return Response(json_for_export)





#AVERAGES LIST VALUES (for use with Visitor API)
#----------------------------------------------#
def averageListValues(a):
    return round(sum(a) / len(a),1)



#VISITOR API VIEW
#------------------#
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



        leinster_style = findStyle(map(averageListValues, zip(*leinster_list)))
        connaught_style = findStyle(map(averageListValues, zip(*connaught_list)))
        ulster_style = findStyle(map(averageListValues, zip(*ulster_list)))
        munster_style = findStyle(map(averageListValues, zip(*munster_list)))


        json_for_export = {

            'leinster': map(averageListValues, zip(*leinster_list)),
            'munster': map(averageListValues, zip(*munster_list)),
            'ulster': map(averageListValues, zip(*ulster_list)),
            'connaught': map(averageListValues, zip(*connaught_list)),
            'styles': [leinster_style, connaught_style, ulster_style, munster_style]
                           }

        # print >> '!!!!!!!', type(ip_address) is str
        # Visitor.objects.get(ip_address='128').update(search_parameters='string')
        # print >> sys.stderr, "USER INPUT RECORDED"



        #Run user's data through beer-finding algorithm and return the results as JSON


        return Response(json_for_export)