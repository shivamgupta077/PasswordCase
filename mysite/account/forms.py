from django import forms
from .models import Case, Profile, Passwords

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ('username', 'password', 'phone_number')

class LoginForm(forms.Form):
    inp_username = forms.CharField(label="Username ", max_length=100)
    inp_password = forms.CharField(label="Password ", max_length=100)
<<<<<<< HEAD

class AddPasswordForm(forms.Form):
    website = forms.CharField(label = "Website",max_length = 100)
    email = forms.CharField(label="Email", max_length=100)
    password = forms.CharField(label="Password", max_length=100)
=======
>>>>>>> 8860e33bee324f39168e82f90c176c1a309012ba
