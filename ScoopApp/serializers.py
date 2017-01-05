from rest_framework import serializers
from .models import CraftBeer

from django.forms.models import model_to_dict
from django.forms.models import model_to_dict
import json
from django.http import HttpResponse

import json


from rest_framework import generics

class CraftBeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CraftBeer
        fields = '__all__'
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """

        dict = model_to_dict(CraftBeer)
        print dict

        user = self.request.user


        return CraftBeer.objects.filter(purchaser=user)




#
# def json_response(something):
#     return HttpResponse(json.dumps(something
#
#
