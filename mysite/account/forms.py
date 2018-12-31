from django import forms
from .models import Case, Profile, Passwords

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ('username', 'password', 'phone_number', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5')

class LoginForm(forms.ModelForm):
    inp_username = forms.CharField(label="Username ", max_length=100)
    inp_password = forms.CharField(label="Password ", max_length=100)