from rest_framework import generics

from shop.models import Product
from shop.serializers import ProductListSerializer, OrderCreateSerializer, PaymentCreateSerializer
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


class PaymentAPIView(generics.CreateAPIView):
    """
    Оплата.

    POST запрос для оплаты.
    """
    serializer_class = PaymentCreateSerializer

    def perform_create(self, serializer):
        serializer.validated_data['price'] = serializer.validated_data['order'].total_price
        serializer.save()
