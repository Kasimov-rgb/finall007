from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.tags.api import views


router = DefaultRouter()
router.register('', views.TagViewSet, basename="tag_api")

urlpatterns = router.urls
