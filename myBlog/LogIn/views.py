from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def SignUp(request):
    form = UserCreationForm()
    registered = False

    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            form.save()
            registered = True

    dict = {'form':form,'registered':registered}
    return render(request,'LogIn/signup.html',context=dict)
