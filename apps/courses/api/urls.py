from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.courses.api import views


router = DefaultRouter()
router.register('', views.CourseViewSet, basename="course_api")

urlpatterns = router.urls
