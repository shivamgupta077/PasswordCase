from django import forms
from .models import Case, Profile, Passwords

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ('username', 'password', 'phone_number', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5')

