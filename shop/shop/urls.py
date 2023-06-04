from django.urls import path
from .views import AllShopApiView, ShopApiView, CityApiView, AllCityApiView

app_name = "shop"

urlpatterns = [
    path('all-shop/', AllShopApiView.as_view()),
    path('shop<int:pk>/', ShopApiView.as_view()),
    path('all-city/', AllCityApiView.as_view()),
    path('city<int:pk>/', CityApiView.as_view()),
]
