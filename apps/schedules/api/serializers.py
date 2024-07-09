# from rest_framework import serializers
#
# from apps.schedules.models import Schedule
#
#
# class ScheduleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Schedule
#         fields = [
#             'date',
#             'time',
#         ]
#
#
# class ScheduleCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Schedule
#         fields = [
#             'date',
#             'time',
#         ]


from rest_framework import serializers
from apps.schedules.models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            'day_of_week',
            'opening_time',
            'closing_time',
        ]


class ScheduleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            'day_of_week',
            'opening_time',
            'closing_time',
        ]
