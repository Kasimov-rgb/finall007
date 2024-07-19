# from django.urls import path
# from apps.trainer.views import TrainerListView, TrainerAddView, AboutUsView, trainner_details, TrainerCreateView, TrainerUpdateView, TrainerDeleteView

# urlpatterns = [
#     path('trainers/', TrainerListView.as_view(), name='trainer'),
#     path('add/', TrainerAddView.as_view(), name='add_trainer'),
#     path('about/', AboutUsView.as_view(), name='about'),
#     path('trainner_details/', trainner_details, name='trainner_details'),




#        path('trainer/new/', TrainerCreateView.as_view(), name='trainer_create'),
#        path('trainer/<int:pk>/edit/', TrainerUpdateView.as_view(), name='trainer_update'),
#        path('trainer/<int:pk>/delete/', TrainerDeleteView.as_view(), name='trainer_delete'),
# ]


from django.urls import path
from apps.trainer.views import (
    TrainerListView, TrainerCreateView, TrainerUpdateView, TrainerDeleteView,
    AboutUsView, trainner_details, shop
)

urlpatterns = [
    path('trainers/', TrainerListView.as_view(), name='trainer'),
    
    path('trainer/new/', TrainerCreateView.as_view(), name='trainer_create'),
    path('trainer/<int:pk>/edit/', TrainerUpdateView.as_view(), name='trainer_update'),
    path('trainer/<int:pk>/delete/', TrainerDeleteView.as_view(), name='trainer_delete'),

    path('about/', AboutUsView.as_view(), name='about'),
    path('trainner_details/', trainner_details, name='trainner_details'),
    path('shop/', shop, name='shop'),
]
