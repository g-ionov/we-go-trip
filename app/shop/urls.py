from django.urls import path, include

from shop import views

urlpatterns = [
    path('product', views.ProductAPIView.as_view(), name='product'),
]