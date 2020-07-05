from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout # Function for authentication
from django.shortcuts import HttpResponseRedirect
from django.urls import  reverse
from django.contrib.auth.decorators import login_required
from LogIn.forms import SignUp_form , UserProfileChange,  ProfilePic

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

@login_required
def user_profile(request):
    return render(request,'LogIn/user_profile.html',context={})

@login_required
def change_profile(request):
    current_user = request.user
    form = UserProfileChange(instance = current_user)

    if request.method == "POST":
        form = UserProfileChange(request.POST,instance=current_user)
        if form.is_valid():
            form.save()
            form =UserProfileChange(instance=current_user)

    return render(request,"LogIn/change_profile.html",context={'form':form})

@login_required
def pass_change(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)

    message = False

    if request.method == 'POST':
        form = PasswordChangeForm(current_user,data = request.POST)
        if form.is_valid():
            form.save()
            message = True

    return render(request,'LogIn/pass_change.html',context={'form':form,'message':message})

@login_required
def addpro_pic(request):
    form = ProfilePic()
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('LogIn:profile'))
    return render(request,'LogIn/pro_pic_add.html',context={'form':form})

@login_required
def change_pro_pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method == "POST":
        form = ProfilePic(request.POST, request.FILES,instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('LogIn:profile'))


    return render(request,'LogIn/pro_pic_add.html',context={'form':form})
