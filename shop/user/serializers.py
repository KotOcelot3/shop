from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from shop.serializers import ShopVacanciesSerializer
from .models import User, Vacancies


class UserAllSerializer(ModelSerializer):
    """Сериалайзер всех пользователей"""

    class Meta:
        model = User
        fields = ['username', 'email', 'images']


class UserIDSerializer(ModelSerializer):
    """Сериалайзер вывода пользователя по ID"""

    class Meta:
        model = User
        fields = ['username', 'email', 'images']


class UpdateUserSerializer(ModelSerializer):
    """Сериалайзер для изменения пользователя"""

    class Meta:
        model = User
        fields = ['username', 'email', 'images']


class VacanciesAllSerializer(ModelSerializer):
    """Сериалайзер для вывода всех вакансий"""

    class Meta:
        model = Vacancies
        fields = ['title', 'Responsibilities', 'Requirements', 'Conditions', 'price', 'shop']


class VacanciesIDSerializer(ModelSerializer):
    """Сериалайзер для вывода вакансий по ID"""
    shop = ShopVacanciesSerializer(many=True)

    class Meta:
        model = Vacancies
        fields = ['title', 'Responsibilities', 'Requirements', 'Conditions', 'price', 'shop']


class VacanciesUpdateSerializer(ModelSerializer):
    """Сериалайзер для обновления вакансий"""

    class Meta:
        model = Vacancies
        fields = ['title', 'Responsibilities', 'Requirements', 'Conditions', 'price', 'shop']


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
