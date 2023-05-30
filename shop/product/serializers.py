from rest_framework.serializers import ModelSerializer
from .models import Product, Category


class ProductAllSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'price', 'category']


class ProductSaleSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'price', 'sale', 'discount']


class CategoryAllSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['title', 'product']


class ProductIDSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'product']
