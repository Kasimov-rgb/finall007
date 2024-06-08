from django.contrib import admin
from apps.schedules.models import Schedule
from apps.schedules.forms import ScheduleForm


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    form = ScheduleForm
    list_display = ['date', 'time', 'event']
    list_filter = ['date']
    search_fields = ['event']
