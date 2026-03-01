from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import UserModels
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget='fo')
    first_name = forms.CharField(abel="", widget='fo')
    last_name = forms.CharField(label="", widget='fo')
