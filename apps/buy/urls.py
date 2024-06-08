from django.urls import path
from apps.buy.views import update_card, successful_payment

urlpatterns = [
    path('checkout/', update_card, name='checkout'),
    path('successful_payment/', successful_payment, name='successful'),

]
