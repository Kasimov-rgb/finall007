from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.basket.api import views


router = DefaultRouter()
router.register('', views.BasketViewSet, basename="basket_api")

urlpatterns = router.urls
