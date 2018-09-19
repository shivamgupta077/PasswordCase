from django import forms
from .models import Case

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ('username', 'password', 'mobilenum', 'ans1', 'ans2', 'ans3', 'ans4', 'ans5', )
