from django.contrib import admin
from django.utils.safestring import mark_safe

from base.services import get_image_html, get_confirm_order_button_html
from .models import Product, Order, Payment
from .services import check_confirm_order_ability


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
        'id', 'total_price', 'status', 'date_created', 'date_confirmed', 'confirm_button')

    def get_queryset(self, request):
        self.request = request
        return super().get_queryset(request).select_related('status', 'payment')

    def confirm_button(self, obj):
        if check_confirm_order_ability(obj):
            return get_confirm_order_button_html(obj.pk, self.request)
        return ''

    confirm_button.short_description = ''


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'price', 'status', 'payment_type')
    readonly_fields = ('order', 'price', 'payment_type')
