from django.urls import path
from apps.schedules.views import schedule_list, add_schedule

urlpatterns = [
    path('schedule', schedule_list, name='schedules_list'),
    path('add/', add_schedule, name='add_schedules'),
]
