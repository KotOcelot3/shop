from django.urls import path
from .views import AllShopApiView, ShopApiView

app_name = "shop"

urlpatterns = [
    path('all-shop/', AllShopApiView.as_view()),
    path('shop<int:pk>/', ShopApiView.as_view()),
]
