from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from apps.tags.api.serializers import TagSerializer, TagCreateSerializer
from apps.tags.models import Tag


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


def get_serializer_class(self):
    if self.action in ['create']:
        return TagCreateSerializer
    elif self.action == 'retrieve':
        return TagSerializer
    return self.serializer_class


class TagUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

