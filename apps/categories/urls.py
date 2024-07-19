# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.category_list, name='category_list'),
#     path('category/<int:pk>/', views.category_detail, name='category_detail'),
#     path('category/create/', views.category_create, name='category_create'),
#     path('category/update/<int:pk>/', views.category_update, name='category_update'),
#     path('category/delete/<int:pk>/', views.category_delete, name='category_delete'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('category/create/', views.category_create, name='category_create'),
    path('category/update/<int:pk>/', views.category_update, name='category_update'),
    path('category/delete/<int:pk>/', views.category_delete, name='category_delete'),
]
