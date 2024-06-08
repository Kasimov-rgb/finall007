from django.contrib import admin

from apps.basket.models import Basket, Item

admin.site.register(Basket)
admin.site.register(Item)

