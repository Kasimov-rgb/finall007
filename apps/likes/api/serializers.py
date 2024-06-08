from rest_framework import serializers

from apps.likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = [
            'user',
            'post',
            'comment',
            'count',

        ]


class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = [
            'user',
            'post',
            'comment',
            'count',

        ]
