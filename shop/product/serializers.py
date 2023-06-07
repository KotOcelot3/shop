from rest_framework.serializers import ModelSerializer
from .models import Product, Category, Comment


class ProductAllSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'price', 'category']


class ProductIDSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'price', 'category', 'comment']


class ProductSaleSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'price', 'price_discount']


class ProductCreateSerializer(ModelSerializer):
    """ Сериалайзер для создания продукции"""

    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'image', 'price', 'sale', 'discount']


class CategoryAllSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['title', 'products']


class CategoryIDSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['title', 'products']


class CommentAllSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['title', 'description', 'user', 'rating', 'products']


class CommentCreateSerializer(ModelSerializer):
    """ Сериалайзер для создания комментария"""

    class Meta:
        model = Comment
        fields = ['title', 'description', 'rating', 'products']


