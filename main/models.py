from distutils.command.upload import upload
<<<<<<< HEAD
<<<<<<< HEAD
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.models import Group

# Create your models here.

class AuthUser(AbstractUser):
    USER_TYPE_CHOICES = {
        (1, 'Physician'),
        (2, 'Patient'),
    }
=======
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.

=======
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.

>>>>>>> jm-changes
phone_regex = RegexValidator(
    r"^(09|\+639)\d{9}$",
    message="Phone number must begin with +639 or 09 followed by a 9 digits",
)

# Account Manger and Account model used to modify base User Model
# it is used to change login from username to email
class AccountManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("Users must have an email address.")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=self.normalize_email(email), password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=225, unique=True)
    first_name = models.CharField(
        verbose_name="first name", max_length=225, null=True, blank=True
    )
    last_name = models.CharField(
        verbose_name="last name", max_length=225, null=True, blank=True
    )
    birthdate = models.DateField(auto_now_add=False, null=True, blank=True)
    age = models.PositiveSmallIntegerField(
        null=True,
        blank=False,
        validators=[MaxValueValidator(200), MinValueValidator(0)],
    )
    sex = models.CharField(
        max_length=1, choices=[("M", "Male"), ("F", "Female")], null=True, blank=True
    )
    contact_number = models.CharField(
        max_length=13, validators=[phone_regex], null=True, blank=True
    )
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    role = models.CharField(
        verbose_name="role",
        max_length=2,
        choices=[
            ("SA", "System Admin"),
            ("PH", "Physician"),
            ("PA", "Patient"),
        ],
    )
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
<<<<<<< HEAD
>>>>>>> 7a6a3394833b7ad4fcdd4a0ebed67a79bc91ae03

    objects = AccountManager()

=======

    objects = AccountManager()

>>>>>>> jm-changes
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> jm-changes

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

<<<<<<< HEAD
>>>>>>> 7a6a3394833b7ad4fcdd4a0ebed67a79bc91ae03
=======
>>>>>>> jm-changes

class Patient(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.patient.first_name



class Physician(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)
    specialization = models.CharField(max_length=100, null=True, blank=True)
    hospital_affiliation = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.physician.first_name


# class PatientConsultationRecord(models.Model):
#     STATUS = {
#         ("Upcoming", "Upcoming"),
#         ("Done", "Done"),
#     }

#     patient = models.ForeignKey(
#         Patient, on_delete=models.CASCADE, related_name="PCR", null=True
#     )
#     physician = models.ForeignKey(Physician, on_delete=models.CASCADE, null=True)
#     date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
#     status = models.PositiveSmallIntegerField(choices=STATUS, null=True)


# class Prescription(models.Model):
#     patient = models.ForeignKey(
#         Patient, on_delete=models.CASCADE, related_name="prescription", null=True
#     )
#     physician = models.ForeignKey(
#         Physician, on_delete=models.CASCADE, related_name="prescription", null=True
#     )
#     file = models.FileField(upload_to="prescriptions/")


# class Consultation(models.Model):
#     patient = models.ForeignKey(
#         Patient, on_delete=models.CASCADE, related_name="consultation", null=True
#     )
#     physician = models.ForeignKey(
#         Physician, on_delete=models.CASCADE, related_name="consultation", null=True
#     )


# class Document(models.Model):
#     patient = models.ForeignKey(
#         Patient, on_delete=models.CASCADE, related_name="documents", null=True
#     )
#     file = models.FileField(upload_to="documents/")
