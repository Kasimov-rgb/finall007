# import os
#
# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
# from utils.image_path import upload_avatar_for_user
#
#
# class CustomUser(AbstractUser):
#     display_name = models.CharField(
#         max_length=50,
#         verbose_name="Отоброжения имя",
#     )
#
#     is_buyer = models.BooleanField(
#         default=False,
#         verbose_name="Покупатель",
#     )
#
#     avatar = models.ImageField(
#         upload_to=upload_avatar_for_user,
#         verbose_name="Аватар",
#
#     )
#
#     def delete(self, using=None, keep_parents=False):
#         os.remove(self.avatar.path)
#         super().delete(using, keep_parents=False)
#
#     def __str__(self):
#         return self.username
#


from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='group',  # Change related_name to avoid clash
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_permissions',  # Change related_name to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
