from rest_framework import generics

from shop.serializers import ProductListSerializer
from shop.services import get_products


class ProductAPIView(generics.ListAPIView):
    """
    Получение списка товаров.

    GET запрос для получения списка товаров.
    """
    queryset = get_products()
    serializer_class = ProductListSerializer
