from django import forms
from .models import Case, Profile, Passwords

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ('username', 'password', 'phone_number')

class LoginForm(forms.Form):
    inp_username = forms.CharField(label="Username ", max_length=100)
    inp_password = forms.CharField(label="Password ", max_length=100)