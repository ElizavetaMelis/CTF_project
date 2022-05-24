from django.urls import path

from applications.product.views import ProductListView, ProductDetailView
from . import views

urlpatterns = [
    path('', ProductListView.as_view(), name='product_page'),
    path('product-detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    # path('product_page', views.product_page, name="product_page"),
]