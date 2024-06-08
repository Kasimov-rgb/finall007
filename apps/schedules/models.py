from django.db import models


# from apps.schedules.models import


class Schedule(models.Model):
    date = models.DateField(
        max_length=100,
        verbose_name="Дата",
    )
    time = models.TimeField(
        max_length=5,
        verbose_name="Время"
    )
    event = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return f"{self.date} - {self.time}: {self.event}"

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписании'
