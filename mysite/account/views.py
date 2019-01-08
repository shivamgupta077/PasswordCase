from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, AddPasswordForm
from .models import Case, Profile, Passwords
from .encryption import encrypt
from .getPasswords import main


# Create your views here.
def is_valid(request):
    u=request['username_input']
    p=request['password_input']
    m=request['number_input']
    if u != None and p!= None and m!= None:
        return True
    return False


def register(request):
    if request.method=='POST':
        #print(request.POST)
        #form = RegisterForm(request.POST)
        #print(form)
        if is_valid(request.POST):
            #Save input in database
            case = Case()
            case.username = request.POST['username_input']
            case.password = request.POST['password_input']
            x = encrypt(case.password)
            case.password = x
            case.phone_number = request.POST['number_input']
            profile = Profile()
            profile.save()
            case.place = profile
            case.save()
            return redirect(login)
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
            inpusername = form.cleaned_data.get("inp_username")
            inppassword = form.cleaned_data.get("inp_password")
            x = encrypt(inppassword)
            CaseObjList = Case.objects.all()
            ReqObj = None
            for obj in CaseObjList:
                if obj.username==inpusername and obj.password==x:
                    ReqObj = obj
                    break
            if ReqObj==None:
                blank_form = LoginForm()
                context = {'form': blank_form}
                return render(request, 'account/login.html', context)
            else:
                #Collect all data of ReqObj and send it to template.
                myDict = main(ReqObj)
                context = {'info': myDict}
                return render(request, 'account/hello.html', context)
        else:
            blank_form = LoginForm()
            context = {'form': blank_form}
            return render(request, 'account/login.html', context)
    else:   #if get method, create a blank form.
        blank_form = LoginForm()
        context = {'form': blank_form}
        return render(request, 'account/login.html', context)

def addPassword(request):
    if request.method == 'POST':
        form = AddPasswordForm(request.POST)
        if form.is_valid():
            website = form.cleaned_data.get("website")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            password = encrypt(password)
            obj = Passwords()
            obj.email = email
            obj.eccrypted_password = password
            obj.website = website
            obj.save()
            context = {}
            return render(request,'account/hello.html',context)
    else:
        blank_form = AddPasswordForm()
        context = {'form' : blank_form}
        return render(request,'account/addPassword.html',context)