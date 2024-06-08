
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from apps.trainer.api.serializers import TrainerSerializer, TrainerCreateSerializer
from apps.trainer.models import Trainer


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


def get_serializer_class(self):
    if self.action in ['create']:
        return TrainerCreateSerializer
    elif self.action == 'retrieve':
        return TrainerSerializer
    return self.serializer_class


class TrainerUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

