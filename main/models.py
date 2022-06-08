from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class AuthUser(AbstractUser):
    USER_TYPE_CHOICES = {
        ('1', 'Physician'),
        ('2', 'Patient'),
    }

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,null=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    birthdate = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    contact_no = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username

class Patient(models.Model):
    patient = models.ForeignKey(AuthUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.patient

class Physician(models.Model):
    physician = models.ForeignKey(AuthUser, on_delete=models.CASCADE, null=True)
    specialization = models.CharField(max_length=100, null=True, blank=True)
    hospital_affiliation = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.physician

class PatientConsultationRecord(models.Model):
    STATUS = {
        ('Upcoming', 'Upcoming'),
        ('Done', 'Done'),
    }

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='PCR', null=True)
    physician = models.ForeignKey(Physician, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=STATUS,null=True)

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescription', null=True)
    physician = models.ForeignKey(Physician, on_delete=models.CASCADE, related_name='prescription', null=True)
    file = models.FileField(upload_to='prescriptions/')

class Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='consultation', null=True)
    physician = models.ForeignKey(Physician, on_delete=models.CASCADE, related_name='consultation', null=True)

class Document(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='documents', null=True)
    file = models.FileField(upload_to='documents/')