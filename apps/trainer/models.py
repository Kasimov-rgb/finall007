from django.db import models
from django.contrib.auth import get_user_model

from django.utils.safestring import mark_safe

from PIL import Image

User = get_user_model()


class Trainer(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Тренер",
    )
    specialization = models.CharField(
        max_length=100,
        verbose_name="Специализация",
    )
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Зарплата",
    )
    image_for_trainer = models.ImageField(
        upload_to="trainer_media/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренери'


class AboutUs(models.Model):
    title = models.CharField(
        max_length=100,
    )
    content = models.TextField()
    image = models.ImageField(
        upload_to='about_us/',
        blank=True,
        null=True,
        verbose_name="Изображение",
    )

    def __str__(self):
        return self.title
