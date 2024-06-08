from django import forms
from apps.schedules.models import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['date', 'time', 'event']
