from django.db import models

from shop import services, signals
from shop.signals import handle_product_in_order_change


class Product(models.Model):
    """
    Модель товара.
    """
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Изображение', upload_to='images/%Y/%m/',
                              null=True, blank=True)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Status(models.Model):
    """
    Модель статуса.
    """
    title = models.CharField(max_length=60, verbose_name='Название')
    code = models.CharField(max_length=10, verbose_name='Код')

    def __str__(self):
        return self.title


class Order(models.Model):
    """
    Модель заказа.
    """
    product = models.ManyToManyField(Product, verbose_name='Товар')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_confirmed = models.DateTimeField(blank=True, null=True, verbose_name='Дата подтверждения')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Статус')
    total_price = models.DecimalField(max_digits=10, decimal_places=2,
                                      verbose_name='Итоговая сумма', default=0)

    def __str__(self):
        return f'Заказ №{self.pk}: {self.date_created}'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.status = services.get_initial_status('order')
        super().save(*args, **kwargs)


models.signals.m2m_changed.connect(handle_product_in_order_change, sender=Order.product.through)


class Payment(models.Model):
    """
    Модель оплаты.
    """
    PAYMENT_TYPE_CHOICES = [
        ('cash', 'Наличными'),
        ('card', 'Банковской картой')
    ]

    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Статус')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES,
                                    default='card', verbose_name='Тип оплаты')
    order = models.OneToOneField(Order, on_delete=models.CASCADE,
                                 verbose_name='Заказ', related_name='payment')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.status = services.get_initial_status('payment')
        super().save(*args, **kwargs)
