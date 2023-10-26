from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, mixins

from shop import services
from shop.serializers import ProductListSerializer, OrderCreateSerializer, PaymentCreateSerializer
from shop.services import get_products, check_confirm_order_ability


class ProductAPIView(generics.ListAPIView):
    """
    Получение списка товаров.

    GET запрос для получения списка товаров.
    """
    queryset = get_products()
    serializer_class = ProductListSerializer


class OrderViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    Создание заказа.

    Эндпоинт для работы с заказом (создание и подтверждение).
    """
    queryset = services.get_orders()

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer

    @action(methods=['post'], detail=True, url_path='confirm')
    def confirm_order(self, request, pk=None):
        """
        Подтверждение заказа.

        Подтверждение заказа с отправкой запроса на внешний API.
        """
        obj = self.get_object()
        if not check_confirm_order_ability(obj):
            return Response({'error': 'Заказ не может быть подтвержден'},
                            status=status.HTTP_400_BAD_REQUEST)

        confirm_response = services.confirm_order(obj)
        if confirm_response.status_code != 200:
            return confirm_response
        return Response({'success': 'Заказ подтвержден'}, status=status.HTTP_200_OK)


class PaymentAPIView(generics.CreateAPIView):
    """
    Оплата.

    POST запрос для оплаты.
    """
    serializer_class = PaymentCreateSerializer

    def perform_create(self, serializer):
        serializer.validated_data['price'] = serializer.validated_data['order'].total_price
        serializer.save()
