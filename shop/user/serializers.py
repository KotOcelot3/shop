from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from shop.serializers import ShopVacanciesSerializer
from .models import Profile, Vacancies


class UserAllSerializer(ModelSerializer):
    """Сериалайзер всех пользователей"""

    class Meta:
        model = Profile
        fields = ['id', 'name', 'username', 'telephone_number', 'email', 'images', 'order']


class UserIDSerializer(ModelSerializer):
    """Сериалайзер вывода пользователя по ID"""

    class Meta:
        model = Profile
        fields = ['id', 'name', 'username', 'telephone_number', 'email', 'images', 'order']


class UpdateUserSerializer(ModelSerializer):
    """Сериалайзер для изменения пользователя"""

    class Meta:
        model = Profile
        fields = ['name', 'username', 'telephone_number', 'email', 'images']


class VacanciesAllSerializer(ModelSerializer):
    """Сериалайзер для вывода всех вакансий"""

    class Meta:
        model = Vacancies
        fields = ['id', 'title', 'Responsibilities', 'Requirements', 'Conditions', 'price', 'shop']


class VacanciesIDSerializer(ModelSerializer):
    """Сериалайзер для вывода вакансий по ID"""
    shop = ShopVacanciesSerializer(many=True)

    class Meta:
        model = Vacancies
        fields = ['id', 'title', 'Responsibilities', 'Requirements', 'Conditions', 'price', 'shop']


class VacanciesUpdateSerializer(ModelSerializer):
    """Сериалайзер для обновления вакансий"""

    class Meta:
        model = Vacancies
        fields = ['id', 'title', 'Responsibilities', 'Requirements', 'Conditions', 'price', 'shop']


class LoginSerializer(ModelSerializer):
    """ Сериалайзер для логина"""
    password = CharField(write_only=True, required=True)

    class Meta:
        model = Profile
        fields = ['username', 'password']


class RegisterSerializer(ModelSerializer):
    """ Сериалайзер для регистрации"""
    password = CharField(write_only=True, required=True)

    class Meta:
        model = Profile
        fields = ['id', 'name', 'username', 'telephone_number', 'email', 'images', 'password']


class UserOrderSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'telephone_number', 'cart']
