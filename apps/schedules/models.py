from django.db import models
import datetime


class Schedule(models.Model):
    DAY_CHOICES = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    day = models.CharField(
        max_length=10,
        choices=DAY_CHOICES,
        verbose_name="День недели"
    )
    opening_time = models.TimeField(
        verbose_name="Время открытия"
    )

    closing_time = models.TimeField(
        verbose_name="Время закрытия",
        default=datetime.time(hour=23, minute=59, second=59)
    )

    def __str__(self):
        return f"{self.get_day_display()} - ({self.opening_time} - {self.closing_time})"

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
