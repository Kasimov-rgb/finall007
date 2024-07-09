from django.urls import path
from apps.schedules.views import schedule_list, add_schedule

from . import views

urlpatterns = [
    # path('schedule', schedule_list, name='schedules_list'),
    # path('add/', add_schedule, name='add_schedules'),

    path('schedule/', views.schedule_list, name='schedule_list'),
    path('schedule/add/', views.add_schedule, name='add_schedule'),
]
