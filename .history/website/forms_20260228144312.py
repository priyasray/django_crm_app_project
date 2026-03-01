from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import UserModels


class SignUpForm(UserCreationForm):
    email = forms.Email_F
    first_name = 
    last_name =
