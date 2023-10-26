from django.urls import path, include
from rest_framework import routers

from shop import views

router = routers.DefaultRouter()

router.register(r'order', views.OrderViewSet, basename='orders')

urlpatterns = [
    path('product', views.ProductAPIView.as_view(), name='product'),
    path('payment', views.PaymentAPIView.as_view(), name='payment'),

    path('', include(router.urls)),
]
