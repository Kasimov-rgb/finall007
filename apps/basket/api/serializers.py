from rest_framework import serializers

from apps.basket.models import Basket, Item, Favorite


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = [
            'user',

        ]


class BasketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = [
            'user',

        ]


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'product',
            'quantity',
            'basket',

        ]


class ItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'product',
            'quantity',
            'basket',

        ]


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'user',
            'product',
        ]


class FavoriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'user',
            'product',
        ]
