from django.shortcuts import render
from .forms import CaseForm
from .models import Case, Profile

# Create your views here.
def register(request):
    if request.method=='POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            #Save input in database
            case = Case()
            case.username = form.cleaned_data.get("username")
            case.password = form.cleaned_data.get("password")
            case.mobilenum = form.cleaned_data.get("mobilenum")
            case.ans1 = form.cleaned_data.get("ans1")
            case.ans2 = form.cleaned_data.get("ans2")
            case.ans3 = form.cleaned_data.get("ans3")
            case.ans4 = form.cleaned_data.get("ans4")
            case.ans5 = form.cleaned_data.get("ans5")
            profile = Profile()
            profile.save()
            case.place = profile
            case.save()
            context = {}
            return render(request, 'account/login.html', context)
        else:
            blank_form = CaseForm()
            context = {'form': blank_form}
            return render(request, 'account/register.html', context)
    else:   #if get method, create a blank form.
        blank_form = CaseForm()
        context = {'form': blank_form}
        return render(request, 'account/register.html', context)


def login(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            forminp = form.cleaned_data

            # Check input and if valid guide to profile

            context = {}
            return render(request, 'account/profile.html', context)
        else:
            blank_form = CaseForm()
            context = {'form': blank_form}
            return render(request, 'account/login.html', context)
    else:  # if get method, create a blank form.
        blank_form = CaseForm()
        context = {'form': blank_form}
        return render(request, 'account/login.html', context)
