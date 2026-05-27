from django import forms
from django.contrib.auth.models import User
from .models import TravelPreference

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class TravelForm(forms.ModelForm):
    class Meta:
        model = TravelPreference
        fields = ['budget', 'place_type', 'weather', 'days']