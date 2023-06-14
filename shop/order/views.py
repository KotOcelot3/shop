from rest_framework import generics, filters, permissions
from .models import Order, Obtain, DeliveryAddress, PaymentMethod
from .serializers import OrderAllSerializer, ObtainAllSerializer, DeliveryAddressAllSerializer, \
    PaymentMethodAllSerializer, OrderCreateSerializer, ObtainCreateSerializer, \
    DeliveryAddressCreateSerializer, PaymentMethodCreateSerializer


class AllOrderApiView(generics.ListAPIView):
    """Все заказы"""
    queryset = Order.objects.all()
    serializer_class = OrderAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username']
    permission_classes = (permissions.IsAdminUser,)


class AllObtainApiView(generics.ListAPIView):
    """Все способы получения"""
    queryset = Obtain.objects.all()
    serializer_class = ObtainAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = (permissions.IsAdminUser,)


class AllDeliveryAddressApiView(generics.ListAPIView):
    """Все адреса доставки"""
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['city__title', 'address']
    permission_classes = (permissions.IsAdminUser,)


class AllPaymentMethodApiView(generics.ListAPIView):
    """Все способы оплаты"""
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = (permissions.IsAdminUser,)


class CreateOrderApiView(generics.CreateAPIView):
    """Создать заказ"""
    serializer_class = OrderCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreateObtainApiView(generics.CreateAPIView):
    """Создать способ получения"""
    serializer_class = ObtainCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CreateDeliveryAddressApiView(generics.CreateAPIView):
    """Создать адрес доставки"""
    serializer_class = DeliveryAddressCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CreatePaymentMethodApiView(generics.CreateAPIView):
    """Создать способ оплаты"""
    serializer_class = PaymentMethodCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)
