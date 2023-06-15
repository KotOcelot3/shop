from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from user.serializers import UserOrderSerializer
from .models import Order, Obtain, DeliveryAddress, PaymentMethod


class OrderAllSerializer(ModelSerializer):
    """Сериалайзер всех заказов"""
    user = UserOrderSerializer()

    class Meta:
        model = Order
        fields = ['user', 'how_to_obtain', 'delivery_address', 'payment_method']


class ObtainAllSerializer(ModelSerializer):
    """Сериалайзер всех способов получения"""

    class Meta:
        model = Obtain
        fields = '__all__'


class DeliveryAddressAllSerializer(ModelSerializer):
    """Сериалайзер всех адресов доставки"""

    class Meta:
        model = DeliveryAddress
        fields = '__all__'


class PaymentMethodAllSerializer(ModelSerializer):
    """Сериалайзер всех способов оплаты"""

    class Meta:
        model = PaymentMethod
        fields = '__all__'


class OrderCreateSerializer(ModelSerializer):
    """Сериалайзер для создания заказа"""

    class Meta:
        model = Order
        exclude = ['user']


class ObtainCreateSerializer(ModelSerializer):
    """Сериалайзер для создания способа получения"""

    class Meta:
        model = Obtain
        fields = '__all__'


class DeliveryAddressCreateSerializer(ModelSerializer):
    """Сериалайзер для создания адреса доставки"""

    class Meta:
        model = DeliveryAddress
        fields = '__all__'


class PaymentMethodCreateSerializer(ModelSerializer):
    """Сериалайзер для создания способа оплаты"""

    class Meta:
        model = PaymentMethod
        fields = '__all__'


class OrderUpdateSerializer(ModelSerializer):
    """Сериалайзер для обновдления заказа"""

    class Meta:
        model = Order
        exclude = ['user']


class ObtainUpdateSerializer(ModelSerializer):
    """Сериалайзер для обновления способо получения"""

    class Meta:
        model = Obtain
        fields = '__all__'


class DeliveryAddressUpdateSerializer(ModelSerializer):
    """Сериалайзер для обновления адреса доставок"""

    class Meta:
        model = DeliveryAddress
        fields = '__all__'


class PaymentMethodUpdateSerializer(ModelSerializer):
    """Сериалайзер для обновления способа оплаты"""

    class Meta:
        model = PaymentMethod
        fields = '__all__'
