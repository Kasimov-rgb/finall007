from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from apps.schedules.api.serializers import ScheduleSerializer, ScheduleCreateSerializer
from apps.schedules.models import Schedule


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


def get_serializer_class(self):
    if self.action in ['create']:
        return ScheduleCreateSerializer
    elif self.action == 'retrieve':
        return ScheduleSerializer
    return self.serializer_class


class ScheduleUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

