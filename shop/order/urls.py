from django.urls import path
from .views import AllOrderApiView, AllObtainApiView, AllDeliveryAddressApiView, \
    AllPaymentMethodApiView, CreateOrderApiView, CreateObtainApiView, CreateDeliveryAddressApiView, \
    CreatePaymentMethodApiView, UpdateOrderApiView, UpdateObtainApiView, UpdateDeliveryAddressApiView, \
    UpdatePaymentMethodApiView, OrderDeleteApiView, ObtainDeleteApiView, DeliveryAddressDeleteApiView, \
    PaymentMethodDeleteApiView

app_name = "order"

urlpatterns = {
    path('all-order/', AllOrderApiView.as_view()),
    path('all-obtain/', AllObtainApiView.as_view()),
    path('all-delivery-address/', AllDeliveryAddressApiView.as_view()),
    path('all-payment-method/', AllPaymentMethodApiView.as_view()),
    path('order-create/', CreateOrderApiView.as_view()),
    path('obtain-create/', CreateObtainApiView.as_view()),
    path('delivery-address-create/', CreateDeliveryAddressApiView.as_view()),
    path('payment-method-create/', CreatePaymentMethodApiView.as_view()),
    path('order-update/', UpdateOrderApiView.as_view()),
    path('obtain-update/', UpdateObtainApiView.as_view()),
    path('delivery-address-update/', UpdateDeliveryAddressApiView.as_view()),
    path('payment-method-update/', UpdatePaymentMethodApiView.as_view()),
    path('order-delete/', OrderDeleteApiView.as_view()),
    path('obtain-delete/', ObtainDeleteApiView.as_view()),
    path('delivery-address-delete/', DeliveryAddressDeleteApiView.as_view()),
    path('payment-method-delete/', PaymentMethodDeleteApiView.as_view()),
}
