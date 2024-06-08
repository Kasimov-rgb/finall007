from django.urls import path
from apps.likes.views import (
    LikeCreateView,
    LikeDeleteView,
)
urlpatterns = [
    path('create/', LikeCreateView.as_view(), name='like_create'),
    path('<int:pk>/delete/', LikeDeleteView.as_view(), name='like_delete'),
]