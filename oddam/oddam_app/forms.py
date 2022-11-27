from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.ModelForm):
    pass

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']