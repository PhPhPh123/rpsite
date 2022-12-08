import os
from django import forms
from django.core.exceptions import ValidationError
from dotenv import load_dotenv, find_dotenv

from .models import *


def registration_password_validate(value):
    load_dotenv(find_dotenv())
    registration_password = os.environ['registration_password']
    if value != registration_password:
        raise ValidationError('Пароль для регистрации можно запросить у ГМа', params={'value': value}, )


class PlayerRegisterForm(forms.ModelForm):
    registration_password = forms.CharField(validators=[registration_password_validate])

    class Meta:
        model = PlayerRegister
        fields = '__all__'
        widgets = {'character_background': forms.Textarea(attrs={'cols': 200, 'raws': 100})}

