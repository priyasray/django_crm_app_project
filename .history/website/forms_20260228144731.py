from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import UserModels
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.tTextIn)
    first_name = forms.CharField(abel="", widget=forms.tTextIn)
    last_name = forms.CharField(label="", widget=forms.tTextIn)
