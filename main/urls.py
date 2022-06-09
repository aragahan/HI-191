from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name="login"),
    # path('md_register/', views.md_register, name='md_register'),
    # path('patient_register/', views.patient_register, name='patient_register'),
]
