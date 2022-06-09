from pickle import TRUE
from django import forms
from django.forms import ModelChoiceField, ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = AuthUser
        fields = ['first_name','last_name', 'username', 'email', 'password1', 'password2', 'user_type']

class EditUserForm(UserChangeForm):
    class Meta:
        model = AuthUser
        fields = ['first_name','last_name','username', 'email', 'password', 'user_type', 'address', 'birthdate', 'contact_no']

class EditPhysicianForm(ModelForm):
    class Meta:
        model = Physician
        fields = ['specialization', 'hospital_affiliation']

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['file']

class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = ['file']

class PatientConsultationRecordForm(ModelForm):
    class Meta:
        model = PatientConsultationRecord
        fields = ['status', 'date']