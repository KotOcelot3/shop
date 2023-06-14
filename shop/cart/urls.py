from django.urls import path
from .views import UpdateCartApiView

app_name = "cart"

urlpatterns = [
    path('cart-update<int:pk>/', UpdateCartApiView.as_view()),
]
