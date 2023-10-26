from django.db.models import QuerySet

from shop.models import Product


def get_products() -> QuerySet:
    """Получение списка товаров"""
    return Product.objects.all()
