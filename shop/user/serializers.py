from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from .models import User


class UserAllSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'images']


class UserIDSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['title', 'product', 'images']


class LoginSerializer(ModelSerializer):
    """ Сериалайзер для логина"""
    password = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterSerializer(ModelSerializer):
    """ Сериалайзер для регистрации"""
    password = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'images', 'password']
