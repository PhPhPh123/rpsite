import os
from django import forms
from django.core.exceptions import ValidationError
from dotenv import load_dotenv, find_dotenv
from django.utils.translation import gettext_lazy as _

from .models import *


# def registration_password_validate(value):
#     print(value)
#     load_dotenv(find_dotenv())
#     registration_password = os.environ['registration_password']
#     if value != registration_password:
#         raise ValidationError(_('Пароль для регистрации можно запросить у ГМа'), params={'value': value},)


class PlayerRegister(forms.Form):
    player_name = forms.CharField(max_length=30)
    character_name = forms.CharField(max_length=30)
    character_power = forms.IntegerField(min_value=1, max_value=4)
    character_background = forms.CharField(widget=forms.Textarea(attrs={'cols': 200, 'raws': 100}), min_length=800)
    registration_password = forms.CharField()
