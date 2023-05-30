from rest_framework import generics, filters
from .models import Shop, City
from .serializers import ShopAllSerializer, CityAllSerializer
from rest_framework.authentication import SessionAuthentication


class AllShopApiView(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['address']
    authentication_classes = (SessionAuthentication,)


class AllCityApiView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    authentication_classes = (SessionAuthentication,)


class ShopApiView(generics.RetrieveAPIView):
    """Магазин по ID"""
    queryset = Shop.objects.all()
    serializer_class = ShopAllSerializer
    authentication_classes = (SessionAuthentication,)


class CityApiView(generics.RetrieveAPIView):
    """Город по ID"""
    queryset = City.objects.all()
    serializer_class = CityAllSerializer
    authentication_classes = (SessionAuthentication,)