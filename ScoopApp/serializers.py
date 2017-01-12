from rest_framework import serializers
from .models import CraftBeer, Visitor
from django.forms.models import model_to_dict


class CraftBeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CraftBeer
        #fields = '__all__'
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """

        dict = model_to_dict(CraftBeer)
        print dict

        return CraftBeer.objects.all()



class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        #fields = '__all__'

    def get_queryset(self):

        dict = model_to_dict(Visitor)

        return Visitor.objects.all()

