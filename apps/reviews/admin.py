from django.contrib import admin
from .models import Reviews


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('user', 'trainer', 'text', 'created_at')
    list_filter = ('trainer', 'created_at')
    search_fields = ('user__username', 'trainer__title', 'text')
    readonly_fields = ('created_at',)
    fields = ('user', 'trainer', 'text', 'image')
