from rest_framework import generics
from cart.models import Cart
from cart.serializers import UpdateCartSerializer
from core.permissions import IsUserOwner


class UserCartApiView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()


class UpdateCartApiView(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = UpdateCartSerializer
    permission_classes = (IsUserOwner,)
