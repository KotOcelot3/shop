from django.urls import path
from .views import AllProductApiView, AllCategoryApiView, CategoryApiView

app_name = "product"

urlpatterns = [
    path('all-products/', AllProductApiView.as_view()),
    path('all-category/', AllCategoryApiView.as_view()),
    path('category<int:pk>/', CategoryApiView.as_view())
]
