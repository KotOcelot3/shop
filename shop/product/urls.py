from django.urls import path
from .views import AllProductApiView, AllCategoryApiView, CategoryApiView, SaleProductApiView, \
    CreateCommentApiView, CreateProductApiView, ProductApiView, AllCommentApiView

app_name = "product"

urlpatterns = [
    path('all-products/', AllProductApiView.as_view()),
    path('products<int:pk>/', ProductApiView.as_view()),
    path('create-products/', CreateProductApiView.as_view()),
    path('sale-products/', SaleProductApiView.as_view()),
    path('all-category/', AllCategoryApiView.as_view()),
    path('category<int:pk>/', CategoryApiView.as_view()),
    path('all-comments/', AllCommentApiView.as_view()),
    path('create-comment/', CreateCommentApiView.as_view())
]
