from django.contrib import admin
from apps.trainer.models import Trainer, AboutUs
from apps.trainer.forms import TrainerForm


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    form = TrainerForm
    list_display = ['name', 'specialization', 'salary', 'display_photo']
    list_filter = ['specialization']
    search_fields = ['name', 'specialization']
    readonly_fields = ['display_photo']

    def display_photo(self, obj):
        if obj.photo:
            return '<img src="{}" height="100">'.format(obj.photo.url)
        else:
            return 'No Photo'

    display_photo.allow_tags = True
    display_photo.short_description = 'Photo'


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'content',)
    fieldsets = (
        (None, {
            'fields': ('title', 'content',)
        }),
    )
