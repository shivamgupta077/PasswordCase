from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from .models import Case, Profile, Passwords
from .encryption import encrypt
# Create your views here.
def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            #Save input in database
            case = Case()
            case.username = form.cleaned_data.get("username")
            case.password = form.cleaned_data.get("password")
            x,y = encrypt(case.password)
            case.password = x
            case.phone_number = form.cleaned_data.get("phone_number")
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
            blank_form = RegisterForm()
            context = {'form': blank_form}
            return render(request, 'account/register.html', context)
    else:   #if get method, create a blank form.
        blank_form = RegisterForm()
        context = {'form': blank_form}
        return render(request, 'account/register.html', context)


def login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #Save input in database
            inpusername = form.cleaned_data.get("inpusername")
            inppassword = form.cleaned_data.get("inppassword")
            CaseObjList = Case.objects.all()
            ReqObj = None
            for obj in CaseObjList:
                if obj.username==inpusername and obj.password==inppassword:
                    ReqObj = obj
                    break
            if ReqObj==None:
                blank_form = LoginForm()
                context = {'form': blank_form}
                return render(request, 'account/login.html', context)
            #
            #
            #Collect all data of ReqObj and send it to template.
            #
            #
            context = {}
            return render(request, 'account/profile.html', context)
        else:
            blank_form = LoginForm()
            context = {'form': blank_form}
            return render(request, 'account/login.html', context)
    else:   #if get method, create a blank form.
        blank_form = LoginForm()
        context = {'form': blank_form}
        return render(request, 'account/login.html', context)
