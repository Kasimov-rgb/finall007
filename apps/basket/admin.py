from django.contrib import admin
from apps.basket.models import Basket, Item, Favorite

admin.site.register(Basket)
admin.site.register(Item)
admin.site.register(Favorite)
