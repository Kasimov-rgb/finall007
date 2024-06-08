from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.likes.api import views


router = DefaultRouter()
router.register('', views.LikeViewSet, basename="like_api")

urlpatterns = router.urls
