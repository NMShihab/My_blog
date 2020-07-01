from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout # Function for authentication
from django.shortcuts import HttpResponseRedirect
from django.urls import  reverse
from django.contrib.auth.decorators import login_required
from LogIn.forms import SignUp_form

# Create your views here.

# Function for signup
def SignUp(request):
    form = SignUp_form()
    registered = False

    if request.method == 'POST':
        form = SignUp_form(data=request.POST)

        if form.is_valid():
            form.save()
            registered = True

    dict = {'form':form,'registered':registered}
    return render(request,'LogIn/signup.html',context=dict)



# Function for LogIn
def LogIn(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username,password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

    return render(request,'LogIn/login.html',context={'form':form})

# Function for logout

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
