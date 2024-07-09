from django.urls import path

from apps.products.views import ProductListView, shop_single, shop, indexView

urlpatterns = [
       path('product', ProductListView.as_view(), name='product_list'),
       path('shop_single/', shop_single, name='shop_single'),
       path('shop/', shop, name='shop'),
       path('', indexView.as_view(), name='index'),

]