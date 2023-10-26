from django.db.models import QuerySet

from shop import models


def get_products() -> QuerySet:
    """Получение списка товаров"""
    return models.Product.objects.all()


def get_initial_status_for_order() -> 'models.Status':
    """Получение статуса для создания заказа"""
    return models.Status.objects.get(code='new')


def calculate_order_total_price(order: 'models.Order') -> None:
    """Подсчет общей стоимости заказа."""
    order.total_price = sum([product.price for product in order.product.all()])
    order.save()

