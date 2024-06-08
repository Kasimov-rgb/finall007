from rest_framework import serializers

from apps.schedules.models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            'date',
            'time',
            'event',
        ]


class ScheduleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            'date',
            'time',
            'event',
        ]
