# from django.contrib import admin
# from apps.schedules.models import Schedule
# from apps.schedules.forms import ScheduleForm
#
#
# @admin.register(Schedule)
# class ScheduleAdmin(admin.ModelAdmin):
#     form = ScheduleForm
#     list_display = ['date', 'time']
#     list_filter = ['date']
#


from django.contrib import admin
from .models import Schedule


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('day', 'opening_time', 'closing_time')
    list_filter = ('day', 'opening_time', 'closing_time')
    search_fields = ('day',)
    ordering = ('day', 'opening_time')


admin.site.register(Schedule, ScheduleAdmin)
