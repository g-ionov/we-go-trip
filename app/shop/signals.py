from shop.services import calculate_order_total_price


def handle_product_in_order_change(sender, action, instance, **kwargs):
    if action in ('post_add', 'post_remove', 'post_clear'):
        calculate_order_total_price(instance)
