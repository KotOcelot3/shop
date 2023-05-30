from rest_framework.serializers import ModelSerializer
from .models import Shop


class ShopAllSerializer(ModelSerializer):

    class Meta:
        model = Shop
        fields = ['address']
