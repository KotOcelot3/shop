from rest_framework import generics, filters, permissions
from .models import Product, Category, Comment
from .serializers import ProductAllSerializer, CategoryAllSerializer, ProductIDSerializer, \
    ProductSaleSerializer, CommentCreateSerializer, ProductCreateSerializer, CategoryIDSerializer, \
    CommentAllSerializer


class AllProductApiView(generics.ListCreateAPIView):
    """Вся продукция"""
    queryset = Product.objects.all()
    serializer_class = ProductAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = (permissions.IsAuthenticated,)


class ProductApiView(generics.RetrieveAPIView):
    """Продукция по ID"""
    queryset = Product.objects.all()
    serializer_class = ProductIDSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SaleProductApiView(generics.ListCreateAPIView):
    """Продукция по скидке"""
    queryset = Product.objects.filter(sale=True)
    serializer_class = ProductSaleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = (permissions.IsAuthenticated,)


class AllCategoryApiView(generics.ListCreateAPIView):
    """Все категории"""
    queryset = Category.objects.all()
    serializer_class = CategoryAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = (permissions.IsAuthenticated,)


class CategoryApiView(generics.RetrieveAPIView):
    """Категории по ID"""
    queryset = Category.objects.all()
    serializer_class = CategoryIDSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AllCommentApiView(generics.ListCreateAPIView):
    """Все комментарии"""
    queryset = Comment.objects.all()
    serializer_class = CommentAllSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CreateCommentApiView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreateProductApiView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # def perform_create(self, serializer):
    #     if Product.sale:
    #         Product.price_discount = Product.price + Product.discount
    #         return Product.price_discount
