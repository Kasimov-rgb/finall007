from rest_framework import serializers

from apps.trainer.models import Trainer


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = [
            'name',
            'specialization',
            'salary',
        ]


class TrainerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = [
            'name',
            'specialization',
            'salary',
        ]

