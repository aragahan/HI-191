from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(AuthUser)
admin.site.register(Patient)
admin.site.register(Physician)
admin.site.register(PatientConsultationRecord)
admin.site.register(Prescription)
admin.site.register(Consultation)
admin.site.register(Document)