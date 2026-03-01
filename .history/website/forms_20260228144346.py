from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import UserModels
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.Email_Field()
    first_name = fr
    last_name =
