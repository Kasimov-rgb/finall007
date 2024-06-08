from django.contrib import admin
from apps.buy.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'card_number']
    search_fields = ['user__username', 'card_number']
    list_filter = ['card_number']