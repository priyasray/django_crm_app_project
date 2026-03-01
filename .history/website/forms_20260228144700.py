from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import UserModels
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", )
    first_name = forms.CharField(abel="", )
    last_name = forms.CharField(label="", )
