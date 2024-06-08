from rest_framework import serializers

from apps.buy.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
           'user',
        'card_number',
        'card_pin',


        ]


class UserProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'user',
            'card_number',
            'card_pin',


        ]
