from django.db.models import QuerySet

from shop import models


def get_products() -> QuerySet:
    """Получение списка товаров"""
    return models.Product.objects.all()


def get_initial_status(model_name: str) -> 'models.Status':
    """
    Получение начального статуса для создания заказа/оплаты

    :param model_name: имя модели ('order', 'payment')
    :return: начальный статус
    """
    code_for_model = {
        'order': 'new',
        'payment': 'not_paid',
    }
    return models.Status.objects.get(code=code_for_model[model_name])


def calculate_order_total_price(order: 'models.Order') -> None:
    """Подсчет общей стоимости заказа."""
    order.total_price = sum([product.price for product in order.product.all()])
    order.save()
