from django.urls import path
from apps.trainer.views import TrainerListView, TrainerAddView, AboutUsView, trainner_details

urlpatterns = [
    path('trainers/', TrainerListView.as_view(), name='trainer'),
    path('add/', TrainerAddView.as_view(), name='add_trainer'),
    path('about/', AboutUsView.as_view(), name='about'),
    path('trainner_details/', trainner_details, name='trainner_details'),
]