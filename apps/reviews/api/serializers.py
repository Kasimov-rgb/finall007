from rest_framework import serializers

from apps.reviews.models import Reviews


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = [
            'trainer',
            'user',
            'text',
            'created_at'
        ]


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = [
            'trainer',
            'user',
            'text',
            'created_at'
        ]



