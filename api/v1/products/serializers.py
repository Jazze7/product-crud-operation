from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from products.models import Product


class ProductSerializer(ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Product
        fields = ("name", "price", "quantity", "image", "status", "user")
