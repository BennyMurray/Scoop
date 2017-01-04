from django.shortcuts import render
from rest_framework import viewsets
from .models import CraftBeer
from .models import Test
from .serializers import CraftBeerSerializer
from django.forms.models import model_to_dict
import json
import sys
from rest_framework.views import APIView
from rest_framework.response import Response
from findBeer import *


from django.shortcuts import get_list_or_404, get_object_or_404



#INDEX VIEW
def indexView(request):
    return render(request, 'ScoopApp/index.html', {})

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