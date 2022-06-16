from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.

phone_regex = RegexValidator(
    r"^(09|\+639)\d{9}$",
    message="Phone number must begin with +639 or 09 followed by a 9 digits",
)





class Patient(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.account.first_name


class Physician(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)
    specialization = models.CharField(max_length=100, null=True, blank=True)
    hospital_affiliation = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.account.first_name


class PatientConsultationRecord(models.Model):
    STATUS = {
        ("UP", "Upcoming"),
        ("DN", "Done"),
    }

    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="PCR", null=True
    )
    physician = models.ForeignKey(Physician, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=False, null=True, blank=True)


class Prescription(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="prescription", null=True
    )
    physician = models.ForeignKey(
        Physician, on_delete=models.CASCADE, related_name="prescription", null=True
    )
    file = models.FileField(upload_to="prescriptions/")


class Consultation(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="consultation", null=True
    )
    physician = models.ForeignKey(
        Physician, on_delete=models.CASCADE, related_name="consultation", null=True
    )


class Document(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="documents", null=True
    )
    file = models.FileField(upload_to="documents/")

class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=200)
    room_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
