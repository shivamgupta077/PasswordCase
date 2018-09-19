from django.shortcuts import render
from .forms import CaseForm

# Create your views here.
def get_signup(request):
    if request.method=='POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            forminp = form.cleaned_data
            
            #Save input in database

            context = {}
            return render(request, 'account/login.html', context)
        else:
            blank_form = CaseForm()
            context = {'form': blank_form}
            return render(request, 'account/signup.html', context)
    else:   #if get method, create a blank form.
        blank_form = CaseForm()
        context = {'form': blank_form}
        return render(request, 'account/signup.html', context)

    form = CaseForm()
    context = {'form': form}
    return render(request, 'account/signup.html', context)
