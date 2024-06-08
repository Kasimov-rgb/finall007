from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.trainer.api import views


router = DefaultRouter()
router.register('', views.TrainerViewSet, basename="trainer_api")

urlpatterns = router.urls
