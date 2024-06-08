from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.categories.api import views


router = DefaultRouter()
router.register('', views.CategoryViewSet, basename="category_api")

urlpatterns = router.urls
