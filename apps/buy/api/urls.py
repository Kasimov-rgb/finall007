from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.buy.api import views


router = DefaultRouter()
router.register('', views.UserProfileViewSet, basename="userprofile_api")

urlpatterns = router.urls
