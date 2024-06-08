
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from apps.categories.api.serializers import CategorySerializer, CategoryCreateSerializer
from apps.categories.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def get_serializer_class(self):
    if self.action in ['create']:
        return CategoryCreateSerializer
    elif self.action == 'retrieve':
        return CategorySerializer
    return self.serializer_class


class CategoryUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

