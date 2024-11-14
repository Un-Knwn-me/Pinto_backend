from rest_framework import serializers
from .models import Category, Cuisine, Filter, Item, CitySpotlight

class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['id', 'title']