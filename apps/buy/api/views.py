from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from apps.buy.api.serializers import UserProfileSerializer, UserProfileCreateSerializer
from apps.buy.models import UserProfile


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


def get_serializer_class(self):
    if self.action in ['create']:
        return UserProfileCreateSerializer
    elif self.action == 'retrieve':
        return UserProfileSerializer
    return self.serializer_class


class UserProfileUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

