from django.urls import path, include

from shop import views

urlpatterns = [
    path('product', views.ProductAPIView.as_view(), name='product'),
    path('order', views.OrderAPIView.as_view(), name='order'),
    path('payment', views.PaymentAPIView.as_view(), name='payment'),
]
