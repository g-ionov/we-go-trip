from django.utils.safestring import mark_safe


def get_image_html(img, width=50) -> str:
    """ 
    Получение HTML тега с переданным изображением (используется в админке)
    
    :param img: image file
    :param width: image width
    :return: image tag
    """
    return mark_safe(f"<img src='{img.url}' width={width}>") if img else "Изображение отсутствует"
