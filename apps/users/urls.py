from django.urls import path

from apps.users.views import SignUpView, login_logics

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', login_logics, name='login')
]


