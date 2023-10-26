from rest_framework import serializers


class ProductListSerializer(serializers.Serializer):
    """Сериализатор для отображения списка товаров"""
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)
    content = serializers.CharField(read_only=True)
    price = serializers.IntegerField(read_only=True)