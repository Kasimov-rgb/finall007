from django import forms

from apps.courses.models import Course


class EnrollmentForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=50,
        label='Имя',
    )
    last_name = forms.CharField(
        max_length=50,
        label='Фамилия',
    )
    email = forms.EmailField(
        label='Email',
    )
    phone_number = forms.CharField(
        max_length=15,
        label='Номер телефона',
    )

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']  # проверка только по цифрам
        if not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры')
        return phone_number
