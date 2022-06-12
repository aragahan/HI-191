from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET

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
                if user.role == "SA":
                    return redirect("admin_landing", {'user': user})
                elif user.role == "PH":
                    return redirect("md_landing", {'user': user})
                elif user.role == "PA":
                    return redirect("patient_landing", {'user': user})

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
        #print("here0")
        #print(request.POST)
        if form.is_valid():
            #print("here")
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

def md_landing(request):
    return render(request, "main/md_landing.html", {})

def patient_landing(request):
    return render(request, "main/patient_landing.html", {})

def admin_landing(request):
    return render(request, "main/admin_landing.html", {})

def all_doctors_page(request):
    doctors = Physician.objects.all()

    context = {"doctors": doctors}
    return render(request, "main/all_doctors.html", context)

def all_patients_page(request):
    patients = Patient.objects.all()

    context = {"patients": patients}
    return render(request, "main/all_patients.html", context)

def patient_page(request, id):
    patient = Patient.objects.get(id=id)

    context = {"patient": patient}
    return render(request, "main/patient.html", context)