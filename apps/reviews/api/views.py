
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from apps.reviews.api.serializers import ReviewSerializer, ReviewCreateSerializer
from apps.reviews.models import Reviews


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer


def get_serializer_class(self):
    if self.action in ['create']:
        return ReviewCreateSerializer
    elif self.action == 'retrieve':
        return ReviewSerializer
    return self.serializer_class


class ReviewUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer

