from multiprocessing import context
import re
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse
import random
import time
import json

from .forms import *
from .models import *

from django.views.decorators.csrf import csrf_exempt
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
                    return redirect("account_requests")
                elif user.role == "PH":
                    return redirect("all_patients")
                elif user.role == "PA":
                    return redirect("all_doctors")
                else:
                    return redirect("/admin", {'user':user})

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
    profile = request.user
    prescription_form = PrescriptionForm()
    pcr_form = PatientConsultationRecordForm()

    if request.method == "POST":
        prescription_form = PrescriptionForm(request.POST, request.FILES)
        pcr_form = PatientConsultationRecordForm(request.POST)

        if prescription_form.is_valid():
            prescription = prescription_form.save(False)
            prescription.patient = patient
            prescription.physician = profile.physician
            prescription.save()
            return redirect('patient_page', patient.id)
        
        if pcr_form.is_valid():
            pcr = pcr_form.save(False)
            pcr.patient = patient
            pcr.physician = profile.physician
            pcr.save()
            return redirect('patient_page', patient.id)
        
    context = {"patient": patient, "profile": profile, "pform": prescription_form, "pcr": pcr_form}
    return render(request, "main/patient.html", context)

def profile_page(request):
    profile = request.user
    document_form = DocumentForm()
    
    if request.method == "POST":
        document_form = DocumentForm(request.POST, request.FILES)
        if document_form.is_valid():
            document = document_form.save(False)
            document.patient = profile.patient
            document.save()
            return redirect('profile_page')

    context = {"profile": profile, "dform": document_form}
    return render(request, "main/profile.html", context)

def lobby(request):
    return render(request, 'main/lobby.html')

def room(request):
    return render(request, "main/room.html")

def getToken(request):
    appId = 'ab463b2c13cc40279dd71e7181ba55af'
    appCertificate = '74b688a4e2ab4d5895b987e4eabadcef'
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role =  1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token': token, 'uid': uid}, safe=False)

@csrf_exempt
def createMember(request):
    data = json.loads(request.body)

    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name': data['name']}, safe=False)

def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )

    name = member.name
    return JsonResponse({'name': member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)

    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )   

    member.delete()

    return JsonResponse('Member was deleted', safe=False)

def account_requests(request):
    req_list = Account.objects.filter(is_active='true')
    context = {'user':request.user}
    return render(request, "main/account_requests.html", context)