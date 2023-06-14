from django.urls import path
from .views import AllOrderApiView, AllObtainApiView, AllDeliveryAddressApiView, \
    AllPaymentMethodApiView, CreateOrderApiView, CreateObtainApiView, CreateDeliveryAddressApiView, \
    CreatePaymentMethodApiView

app_name = "order"

urlpatterns = {
    path('all-order/', AllOrderApiView.as_view()),
    path('all-obtain/', AllObtainApiView.as_view()),
    path('all-delivery-address/', AllDeliveryAddressApiView.as_view()),
    path('all-payment-method/', AllPaymentMethodApiView.as_view()),
    path('order-create/', CreateOrderApiView.as_view()),
    path('obtain-create/', CreateObtainApiView.as_view()),
    path('delivery-address-create/', CreateDeliveryAddressApiView.as_view()),
    path('payment-method-create/', CreatePaymentMethodApiView.as_view())
}
