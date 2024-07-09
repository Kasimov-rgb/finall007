from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Trainer, AboutUs


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'salary', 'image_preview')
    list_filter = ('specialization',)
    search_fields = ('name', 'specialization',)

    def image_preview(self, obj):
        if obj.image_for_trainer:
            return mark_safe(f'<img src="{obj.image_for_trainer.url}" height="50"/>')
        else:
            return '(No image)'

    image_preview.short_description = 'Image Preview'


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_preview', 'image_preview')

    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" height="50"/>')
        else:
            return '(No image)'

    content_preview.short_description = 'Content Preview'
    image_preview.short_description = 'Image Preview'
