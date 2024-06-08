from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from apps.basket.api.serializers import (BasketSerializer, BasketCreateSerializer, ItemCreateSerializer, ItemSerializer,
                                         FavoriteCreateSerializer, FavoriteSerializer)
from apps.basket.models import Basket, Item, Favorite



class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


def get_serializer_class(self):
    if self.action in ['create']:
        return BasketCreateSerializer
    elif self.action == 'retrieve':
        return BasketSerializer
    return self.serializer_class


class BasketUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = BasketSerializer


def get_serializer_class(self):
    if self.action in ['create']:
        return ItemCreateSerializer
    elif self.action == 'retrieve':
        return ItemSerializer
    return self.serializer_class


class ItemUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer




class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = FavoriteSerializer


def get_serializer_class(self):
    if self.action in ['create']:
        return FavoriteCreateSerializer
    elif self.action == 'retrieve':
        return FavoriteSerializer
    return self.serializer_class


class FavoriteUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

















