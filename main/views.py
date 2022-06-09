from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import *
from .models import *

from datetime import date


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


# Create your views here.
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
        if form.is_valid():
            instance = form.save(commit=False)
            instance.age = calculate_age(instance.birthdate)
            instance.is_active = False
            instance.save()
            return redirect("login")
    data = {"request_account_form": form}
    return render(request, "main/request_account.html", data)


# def reset_password(request):
#     return render(request)


def logout_user(request):
    logout(request)
    return redirect("/")
