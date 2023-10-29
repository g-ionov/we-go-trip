from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from base.services import get_image_html
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
        'id', 'total_price', 'status', 'date_created', 'date_confirmed')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('status', 'payment')

    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_content = {
            'confirm_button_check': check_confirm_order_ability(self.get_object(request, object_id)),
            'confirm_url': request.build_absolute_uri(reverse('orders-confirm-order', args=[object_id])),
            'current_url': request.build_absolute_uri()
        }
        return super().change_view(request, object_id, form_url, extra_content)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'price', 'status', 'payment_type')
    readonly_fields = ('order', 'price', 'payment_type')
