from rest_framework.serializers import ModelSerializer
from .models import Shop, City


class ShopAllSerializer(ModelSerializer):

    class Meta:
        model = Shop
        fields = ['address']


class CityAllSerializer(ModelSerializer):

    class Meta:
        model = City
        fields = ['title']
