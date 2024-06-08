from django.db import models
from django.contrib.auth import get_user_model

from django.utils.safestring import mark_safe

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

    def __str__(self):
        return self.title

