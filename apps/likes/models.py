from django.db import models
# from apps.users.models import User
from apps.trainer.models import Trainer
from apps.reviews.models import Reviews

from django.contrib.auth import get_user_model

User = get_user_model()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Reviews, on_delete=models.CASCADE, null=True, blank=True)
    count = models.IntegerField(default=0)

    def str(self):
        return f'Like by {self.user.username}'
