import json
import time

import requests
from django.db.models import QuerySet
from django.utils import timezone
from rest_framework.response import Response

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


def check_confirm_order_ability(order: 'models.Order') -> bool:
    """Проверка возможности подтверждения заказа."""
    try:
        return order.payment.status.code == 'paid' and order.status.code != 'confirmed'
    except models.Payment.DoesNotExist:
        return False


def get_orders() -> QuerySet:
    """Получение списка заказов"""
    return models.Order.objects.select_related('status')


def send_order_confirmation_request(order: 'models.Order') -> Response:
    """Отправка запроса с данными подтвержденного заказа."""
    payload = {
        'id': order.pk,
        'amount': float(order.total_price),
        'date': order.date_confirmed.strftime('%Y-%m-%d %H:%M:%S')
    }
    webhook_url = 'https://webhook.site/36693e00-8f59-4f7b-9a85-1d1e7ddde4d4'
    return requests.post(webhook_url, data=json.dumps(payload))


def confirm_order(order: 'models.Order') -> Response:
    """Подтверждение заказа."""
    order.status = models.Status.objects.get(code='confirmed')
    order.date_confirmed = timezone.now()
    order.save()
    time.sleep(3)
    return send_order_confirmation_request(order)
