from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from apps.products.api.serializers import ProductSerializer, ProductCreateSerializer 
from apps.products.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def get_serializer_class(self):
    if self.action in ['create']:
        return ProductCreateSerializer
    elif self.action == 'retrieve':
        return ProductSerializer
    return self.serializer_class


class ProductUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

