from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
=======
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
>>>>>>> 7a6a3394833b7ad4fcdd4a0ebed67a79bc91ae03

from .forms import *
from .models import *

from datetime import date


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


# Create your views here.
<<<<<<< HEAD
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
=======
def login_user(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login success")
                # if user.role == "SA":
                #     return redirect("")
                # elif user.role == "PH":
                #     return redirect("")
                # elif user.role == "PA":
                #     return redirect("")
                return redirect("login")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    data = {"login_form": form}
    return render(request, "main/login.html", data)


def request_account(request):
    form = RequestAccountForm()
    if request.method == "POST":
        form = RequestAccountForm(request.POST)
        print("here0")
        print(request.POST)
        if form.is_valid():
            print("here")
            instance = form.save(commit=False)
            instance.age = calculate_age(instance.birthdate)
            instance.password1 = f"{instance.first_name} {instance.last_name}"
            instance.password2 = f"{instance.first_name} {instance.last_name}"
            instance.is_active = False
            instance.save()
            return redirect("login")
        else:
            print("here2")
    data = {"request_account_form": form}
    return render(request, "main/request_account.html", data)


# def reset_password(request):
#     return render(request)


def logout_user(request):
    logout(request)
    return redirect("/")
>>>>>>> 7a6a3394833b7ad4fcdd4a0ebed67a79bc91ae03
