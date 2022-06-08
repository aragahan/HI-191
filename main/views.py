from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import *
from .models import *

# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect('/communityboard/')
    else:
        if request.method == 'POST':
            form = CreateUserForm
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)
            if user is not None: #user exists
                login(request, user)
                return redirect('/communityboard/')
        form = CreateUserForm
        return render(request, 'login.html', {'form':form})

def md_register(request):
    if request.method == 'POST':
        form = CreateUserForm
        if(form.is_valid()):
            form.save()
    return render(request, 'md_register.html')

def patient_register(request):
    if request.method == 'POST':
        form = CreateUserForm
        if(form.is_valid()):
            form.save()
    return render(request, 'patient_register.html')
