from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name="login"),
    path("request_account/", views.request_account, name="request_account"),
    path("logout/", views.logout_user, name="logout"),
    path("account_requests/", views.account_requests, name="account_requests"),
    # path('md_register/', views.md_register, name='md_register'),
    # path('patient_register/', views.patient_register, name='patient_register'),
]
