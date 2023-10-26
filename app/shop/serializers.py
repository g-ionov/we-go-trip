from rest_framework import serializers

from shop.models import Order, Status


class ProductListSerializer(serializers.Serializer):
    """Сериализатор для отображения списка товаров"""
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)
    content = serializers.CharField(read_only=True)
    price = serializers.IntegerField(read_only=True)


class OrderCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания заказа"""

    class Meta:
        model = Order
        fields = ['product']
