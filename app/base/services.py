from django.http import HttpRequest
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from rest_framework.reverse import reverse


def get_image_html(img, width=50) -> str:
    """ 
    Получение HTML тега с переданным изображением (используется в админке)
    
    :param img: image file
    :param width: image width
    :return: image tag
    """
    return mark_safe(f"<img src='{img.url}' width={width}>") if img else "Изображение отсутствует"


def get_confirm_order_button_html(order_id: int, request: HttpRequest) -> str:
    """
    Получение HTML тега кнопки подтверждения заказа (используется в админке)

    :param request:
    :param order_id: order id
    :return: confirm order button
    """
    url = request.build_absolute_uri(reverse('orders-confirm-order', args=[order_id]))
    print(111111111, url)
    return format_html(
        '<button class="btn btn-success" href="{}">Подтвердить</button>',
        url)

