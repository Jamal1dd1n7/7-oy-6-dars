from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Asosiy sahifa
    path('products/', ProductsView.as_view(), name='products'),  # Barcha mahsulotlar
    path('products/<int:category_id>/', ProductsView.as_view(), name='category_products'),  # Kategoriya bo‘yicha mahsulotlar
    path('product/<slug:product_slug>/', ProductDetail.as_view(), name='product_detail'),  # Mahsulot tafsilotlari
]
