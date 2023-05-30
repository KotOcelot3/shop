from rest_framework import generics, filters
from .models import Product, Category
from .serializers import ProductAllSerializer, CategoryAllSerializer, ProductIDSerializer, ProductSaleSerializer


class AllProductApiView(generics.ListCreateAPIView):
    """Вся продукция"""
    queryset = Product.objects.all()
    serializer_class = ProductAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class SaleProductApiView(generics.ListCreateAPIView):
    """Продукция по скидке"""
    queryset = Product.objects.filter(sale=True)
    serializer_class = ProductSaleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class AllCategoryApiView(generics.ListCreateAPIView):
    """Все категории"""
    queryset = Category.objects.all()
    serializer_class = CategoryAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class CategoryApiView(generics.RetrieveAPIView):
    """Категории по ID"""
    queryset = Category.objects.all()
    serializer_class = ProductIDSerializer
