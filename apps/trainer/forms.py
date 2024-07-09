from django import forms
from apps.trainer.models import Trainer, AboutUs

from django import forms
from apps.trainer.models import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'specialization', 'salary', 'image_for_trainer']


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = ['title', 'content']
