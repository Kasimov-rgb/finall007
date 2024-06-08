from rest_framework import serializers

from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'category',
            'title',
            'c',
            'image_for_product',
            'price',
            'created_at',

        ]


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'category',
            'title',
            'c',
            'image_for_product',
            'price',
            'created_at',

        ]
