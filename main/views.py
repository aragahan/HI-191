from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET


from .forms import *
from .models import *
from .decorators import *

from datetime import date
import re


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


# Create your views here.


@unauthenticated_user
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
                if user.role == "SA":
                    return redirect("account_requests")
                # elif user.role == "PH":
                #     return redirect("")
                # elif user.role == "PA":
                #     return redirect("")
                else:
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
        print(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.age = calculate_age(instance.birthdate)
            instance.save()
            return redirect("login")
        else:
            print(form.errors)
    data = {"request_account_form": form}
    return render(request, "main/request_account.html", data)


# def reset_password(request):
#     return render(request)


def logout_user(request):
    logout(request)
    return redirect("/")


def account_requests(request):
    account_requests = AccountRequest.objects.all()
    data = {"account_requests": account_requests}
    return render(request, "main/account_requests.html", data)


def account_request_approve(request, pk):
    account_request = AccountRequest.objects.get(pk=pk)
    temp_pass = re.search(r"\w+(?=@)", account_request.email).group()
    Account.objects.create(
        email=account_request.email,
        first_name=account_request.first_name,
        last_name=account_request.last_name,
        birthdate=account_request.birthdate,
        age=account_request.age,
        sex=account_request.sex,
        contact_number=account_request.contact_number,
        role=account_request.role,
        password=temp_pass,
    )
    account_request.delete()
    # Send email here
    return redirect("/account_requests/")


def account_request_deny(request, pk):
    account_request = AccountRequest.objects.get(pk=pk)
    account_request.delete()
    # Send email here
    return redirect("/account_requests/")


def change_is_active(request, pk):
    account = Account.objects.get(pk=pk)
    account.is_active = not account.is_active
    account.save()
    return redirect("/accounts/")


def accounts(request):
    accounts_list = Account.objects.all()
    data = {"accounts_list": accounts_list}
    return render(request, "main/accounts.html", data)
