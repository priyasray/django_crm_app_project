from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import UserModels
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=)
    first_name = forms.CharField(abel="", widget=)
    last_name = forms.CharField(label="", widget=)
