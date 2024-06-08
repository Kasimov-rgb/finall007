from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.products.api import views

router = DefaultRouter()
router.register('', views.ProductViewSet, basename="product_api")

urlpatterns = [
    path('create/<int:pk>/', views.ProductUpdateDeleteRetrieveAPIView.as_view(), name='product'),
]

urlpatterns += router.urls