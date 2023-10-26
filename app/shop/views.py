from rest_framework import generics

from shop.models import Product
from shop.serializers import ProductListSerializer, OrderCreateSerializer
from shop.services import get_products


class ProductAPIView(generics.ListAPIView):
    """
    Получение списка товаров.

    GET запрос для получения списка товаров.
    """
    queryset = get_products()
    serializer_class = ProductListSerializer


class OrderAPIView(generics.CreateAPIView):
    """
    Создание заказа.

    POST запрос для создания заказа.
    """
    serializer_class = OrderCreateSerializer
