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
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/communityboard/')

        return render(request, 'main/login.html')
