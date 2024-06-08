
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from apps.likes.api.serializers import LikeSerializer, LikeCreateSerializer
from apps.likes.models import Like


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


def get_serializer_class(self):
    if self.action in ['create']:
        return LikeCreateSerializer
    elif self.action == 'retrieve':
        return LikeSerializer
    return self.serializer_class


class LikeUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

