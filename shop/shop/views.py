from rest_framework import generics, filters
from .models import Shop
from .serializers import ShopAllSerializer
from rest_framework.authentication import SessionAuthentication


class AllShopApiView(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    authentication_classes = (SessionAuthentication,)


class ShopApiView(generics.RetrieveAPIView):
    """Магазин по ID"""
    queryset = Shop.objects.all()
    serializer_class = ShopAllSerializer
    authentication_classes = (SessionAuthentication,)
