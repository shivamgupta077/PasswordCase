from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import RegisterForm, LoginForm, AddPasswordForm
from .models import Case, Profile, Passwords
from .encryption import encrypt
from .getPasswords import main
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as l,logout


def getFromId(id):

    objList = Case.objects.all()
    for obj in objList:
        if obj.place.id == id:
            return obj


def is_valid(request):
    u=request['username_input']
    p=request['password_input']
    m=request['number_input']
    if u != "" and p!= "" and m!= "":
        return True
    return False
# Create your views here.

def is_valid2(request):
    u = request.POST['username_input']
    p = request.POST['password_input']

    if u != "" and p!= "":
        return True
    return False

def isExist(username):
    objList = Case.objects.all()
    for obj in objList:
        if str(obj.username) == str(username):
            return True

    return False

def register(request):
    print(request.method)
    if request.method=='POST':
        print(request.POST)
        form = RegisterForm(request.POST)
        print(form)
        if is_valid(request.POST):
            #Save input in database
            print(request)
            case = Case()
            case.username = request.POST['username_input']

            if isExist(case.username):
                blank_form = RegisterForm()
                context = {'form': blank_form}
                return render(request, 'account/register.html', context)

            case.password = request.POST['password_input']
            user = User.objects.create_user(case.username)
            user.set_password(case.password)
            user.save()
            x = encrypt(case.password)
            case.password = x
            case.phone_number = request.POST['number_input']
            profile = Profile()
            profile.save()
            case.place = profile
            case.save()

            blank_form = LoginForm()
            context = {'form': blank_form}
            #return render(request, 'account/login.html', context)
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

    logout(request)

    if request.method=='POST':
        if True:
            #Save input in database
            inpusername = request.POST['username_input']
            inppassword = request.POST['password_input']

            user = authenticate(request, username=inpusername, password=inppassword)


            if user is None:
                blank_form = LoginForm()
                context = {'form': blank_form}
                return render(request, 'account/login.html', context)
            else:
                l(request, user)
                x = encrypt(inppassword)
                inppassword = x
                CaseObjList = Case.objects.all()
                ReqObj = None
                for obj in CaseObjList:
                    if obj.username==inpusername and obj.password==x:
                        ReqObj = obj
                        break

                prof = ReqObj.place
                id = prof.id
                return redirect(profile,id = id)


        else:
            blank_form = LoginForm()
            context = {'form': blank_form}
            return render(request, 'account/login.html', context)
    else:   #if get method, create a blank form.
        blank_form = LoginForm()
        context = {'form': blank_form}
        return render(request, 'account/login.html', context)



def profile(request,id):
    print(request.user)

    if request.user.is_authenticated:
        objList = Case.objects.all()
        myObj = None
        for obj in objList:
            if obj.username == str(request.user):
                myObj = obj
        if int(myObj.place.id) != int(id):
            return redirect(login)

        objList = Case.objects.all()
        myObj = Case()
        for obj in objList:
            pro = obj.place
            if int(pro.id) == int(id):
                myObj = obj
                break
        myDict = main(myObj)
        context = {'info': myDict, 'id' : id}
        return render(request, 'account/hello.html', context)
    else:
        return redirect(login)


def addPassword(request, id):
    if request.user.is_authenticated:
        objList = Case.objects.all()
        myObj = None
        for obj in objList:
            if obj.username == str(request.user):
                myObj = obj
        if int(myObj.place.id) != int(id):
            return redirect(login)

        if request.method == 'POST':
            form = AddPasswordForm(request.POST)
            if form.is_valid():
                website = form.cleaned_data.get("website")
                email = form.cleaned_data.get("email")
                password = form.cleaned_data.get("password")

                password = encrypt(password)

                obj = Passwords()
                obj.email = email
                obj.encrypted_password = password
                obj.website = website

                objList = Profile.objects.all()
                reqObj = None
                for obj1 in objList:
                    if int(obj1.id) == int(id):
                        reqObj = obj1
                        break
                obj.belongs_to = reqObj
                obj.save()

                return redirect(profile,id = id)

            else:
                context = {}
                return render(request, 'account/addPassword.html', context)
        else:
            blank_form = AddPasswordForm()
            context = {'form' : blank_form,"id" : id}
            return render(request,'account/addPassword.html',context)
    else:
        redirect(login)

