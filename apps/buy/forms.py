from django import forms
from apps.buy.models import UserProfile


class CardForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['card_number', 'card_pin']
