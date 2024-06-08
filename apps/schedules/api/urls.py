from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.schedules.api import views


router = DefaultRouter()
router.register('', views.ScheduleViewSet, basename="schedule_api")

urlpatterns = router.urls
