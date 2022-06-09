from django import forms
from django.forms import *
from django.forms.widgets import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *


class RequestAccountForm(UserCreationForm):
    password1 = CharField(
        widget=PasswordInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "placeholder": "Password",
                "id": "password1",
                "required": True,
            }
        )
    )
    password2 = CharField(
        widget=PasswordInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "placeholder": "Confirm Password",
                "id": "password2",
                "required": True,
            }
        )
    )

    role = ChoiceField(
        widget=Select(attrs={"class": "form-select", "id": "role"}),
        choices=[("PH", "Physician"), ("PA", "Patient")],
    )

    class Meta:
        model = Account
        fields = [
            "email",
            "first_name",
            "last_name",
            "birthdate",
            "sex",
            "contact_number",
            "role",
            "password1",
            "password2",
        ]
        widgets = {
            "first_name": TextInput(
                attrs={
                    "class": "form-control",
                    "id": "fname",
                    "placeholder": "First Name",
                    "required": True,
                }
            ),
            "last_name": TextInput(
                attrs={
                    "class": "form-control",
                    "id": "lname",
                    "placeholder": "Last Name",
                    "required": True,
                }
            ),
            "email": EmailInput(
                attrs={
                    "type": "email",
                    "class": "form-control",
                    "id": "email",
                    "placeholder": "Email Address",
                    "required": True,
                }
            ),
            "birthdate": DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                    "id": "birthdate",
                    "placeholder": "Birthdate",
                    "required": True,
                }
            ),
            "sex": Select(
                attrs={
                    "class": "form-select",
                    "id": "sex",
                    "placeholder": "Sex",
                    "required": True,
                }
            ),
            "contact_number": TextInput(
                attrs={
                    "class": "form-control",
                    "id": "contact_no",
                    "placeholder": "Contact Number",
                    "required": True,
                }
            ),
        }


# # class CreateUserForm(UserCreationForm):
# #     class Meta:
# #         model = AuthUser
# #         fields = ['first_name','last_name','username', 'email', 'password1', 'password2', 'user_type', 'address', 'birthdate', 'contact_no']

# class EditUserForm(UserChangeForm):
#     class Meta:
#         model = AuthUser
#         fields = ['first_name','last_name','username', 'email', 'password1', 'password2', 'user_type', 'address', 'birthdate', 'contact_no']

# class EditPhysicianForm(ModelForm):
#     class Meta:
#         model = Physician
#         fields = ['specialization', 'hospital_affiliation']

# class DocumentForm(ModelForm):
#     class Meta:
#         model = Document
#         fields = ['file']

# class PrescriptionForm(ModelForm):
#     class Meta:
#         model = Prescription
#         fields = ['file']

# class PatientConsultationRecordForm(ModelForm):
#     class Meta:
#         model = PatientConsultationRecord
#         fields = ['status', 'date']
