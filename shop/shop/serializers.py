from rest_framework.serializers import ModelSerializer
from .models import Shop, City


class ShopAllSerializer(ModelSerializer):

    class Meta:
        model = Shop
        fields = ['title', 'address', 'city']


class CityAllSerializer(ModelSerializer):

    class Meta:
        model = City
        fields = ['title']


class ShopVacanciesSerializer(ModelSerializer):
    city = CityAllSerializer(many=True)

    class Meta:
        model = Shop
        fields = ['title', 'address', 'city']
