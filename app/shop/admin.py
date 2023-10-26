from django.contrib import admin

from base.services import get_image_html
from .models import Product, Order, Payment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'short_content', 'get_image')
    list_display_links = ('title',)
    readonly_fields = ('get_image_detail',)

    @staticmethod
    def get_image(obj):
        return get_image_html(obj.image)

    @staticmethod
    def get_image_detail(obj):
        return get_image_html(obj.image, 300)

    def short_content(self, obj):
        return obj.content[:20] + '...' if len(obj.content) > 20 else obj.content


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = readonly_fields = (
        'id', 'total_price', 'status', 'date_created', 'date_confirmed')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = readonly_fields= ('order', 'price', 'status', 'payment_type')
