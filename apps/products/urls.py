from django.urls import path

from apps.products.views import ProductListView, shop_single, shop

urlpatterns = [
       path('product', ProductListView.as_view(), name='index'),
       path('shop_single/', shop_single, name='shop_single'),
       path('shop/', shop, name='shop'),

]