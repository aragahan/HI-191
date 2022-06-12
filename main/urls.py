from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name="login"),
    path("request_account/", views.request_account, name="request_account"),
    path("logout/", views.logout_user, name="logout"),

    # i think we can remove these two na? since plano daw ni julius is to combine the register for md and patient
    # path('md_register/', views.md_register, name='md_register'),
    # path('patient_register/', views.patient_register, name='patient_register'),

    path('md_landing/', views.md_landing, name='md_landing'),
    path('patient_landing/', views.patient_landing, name='patient_landing'),
]
