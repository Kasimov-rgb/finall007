from django.urls import path

from apps.products.views import ProductListView, shop_single, shop, indexView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
       path('product', ProductListView.as_view(), name='product_list'),
       path('shop_single/', shop_single, name='shop_single'),
       path('shop/', shop, name='shop'),
       path('', indexView.as_view(), name='index'),



       path('product/new/', ProductCreateView.as_view(), name='product_create'),
       path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
       path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

]