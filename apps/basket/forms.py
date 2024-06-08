from django import forms
from apps.basket.models import Favorite


class AddToFavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = []