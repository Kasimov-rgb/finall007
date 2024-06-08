from django import forms

from apps.likes.models import Like


class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['fast', 'review']
