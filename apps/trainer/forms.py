from django import forms
from apps.trainer.models import Trainer, AboutUs


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'specialization', 'salary']


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = ['title', 'content']