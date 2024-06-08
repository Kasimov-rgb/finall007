from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    card_pin = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return self.user.username
