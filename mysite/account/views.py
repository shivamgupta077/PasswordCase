from django.shortcuts import render
from .forms import CaseForm
from .models import Case, Profile, Passwords

# Create your views here.
def register(request):
    if request.method=='POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            #Save input in database
            case = Case()
            case.username = form.cleaned_data.get("username")
            case.password = form.cleaned_data.get("password")
            case.phone_number = form.cleaned_data.get("mobilenum")
            case.answer1 = form.cleaned_data.get("answer1")
            case.answer2 = form.cleaned_data.get("answer2")
            case.answer3 = form.cleaned_data.get("answer3")
            case.answer4 = form.cleaned_data.get("answer4")
            case.answer5 = form.cleaned_data.get("answer5")
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
    context = {}
    return render(request, 'account/login.html', context)
