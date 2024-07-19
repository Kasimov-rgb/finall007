from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView, LogoutView
from apps.courses.views import CourseListView

# from core.admin import admin
from core.swagger import docs

from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

api_urlpatterns = [
    #
    # path('basket/', include('apps.cart.api.urls')),
    path('buy/', include('apps.buy.api.urls')),
    path('categories/', include('apps.categories.api.urls')),
    path('course/', include('apps.courses.api.urls')),
    path('like/', include('apps.likes.api.urls')),
    path('product/', include('apps.products.api.urls')),
    path('reviews/', include('apps.reviews.api.urls')),
    path('schedules/', include('apps.schedules.api.urls')),
    path('docs/', docs.with_ui('swagger', cache_timeout=0), name="docs"),
    path('tags/', include('apps.tags.api.urls')),
    path('trainer/', include('apps.trainer.api.urls')),
    # path('users/', include('apps.users.api.urls')),

    path('token_create/', TokenObtainPairView.as_view()),
    path('token_refresh/', TokenRefreshView.as_view())
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.products.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('apps.reviews.urls')),
    path('', include('apps.cart.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('apps.tags.urls')),
    path('', include('apps.trainer.urls')),
    path('', include('apps.schedules.urls')),
    path('', include('apps.courses.urls')),
    path('', CourseListView.as_view(), name='home'),
    path('', include('apps.buy.urls')),
    path('', include('apps.users.urls')),

    path('docs/', docs.with_ui('swagger', cache_timeout=0), name="docs"),

] + api_urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

