from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from .models import User, Vacancies


class UserAllSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'images']


class VacanciesAllSerializer(ModelSerializer):

    class Meta:
        model = Vacancies
        fields = ['title', 'Responsibilities', 'Requirements', 'Conditions', 'price', 'shop']


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
