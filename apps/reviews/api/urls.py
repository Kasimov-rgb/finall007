from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.reviews.api import views


router = DefaultRouter()
router.register('', views.ReviewViewSet, basename="review_api")

urlpatterns = router.urls
