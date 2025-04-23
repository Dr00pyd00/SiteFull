from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# formulaire pour creation de compte:
class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

# formualaire pour login:
class LoginForm(forms.Form):
    my_username = forms.CharField(max_length=300)
    my_password = forms.CharField(widget=forms.PasswordInput)