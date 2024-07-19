from django.contrib import admin

from apps.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['category']
    search_fields = ['title']
