from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse

from .forms import *
from .models import *

# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect('/communityboard/')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            loguser = AuthUser.objects.get(email=email)
            if loguser.is_active == False:
                messages.error(request, "Your account is still inactive.")
                return redirect('login_page')

            print(email, password)

            user = authenticate(request, email=email, password=password)

            if user is not None: #user exists
                login(request, user)
                return redirect('/communityboard/')
            else:
                messages.error(request, "Incorrect credentials.")

        return render(request, 'login.html')

def register_page(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(False)
            print(form.cleaned_data.get('user_type'))
            if form.cleaned_data.get('user_type') == 1:
                user.is_active = False
                user.save()
                Physician.objects.create(
                    physician = user,
                )
            elif form.cleaned_data.get('user_type') == 2:
                user.is_active = False
                user.save()
                Patient.objects.create(
                    patient = user,
                )
            messages.success(request, 'Account created!')

            return redirect('login_page')
    
    context = {'form': form}
    return render(request, 'md_register.html', context)
