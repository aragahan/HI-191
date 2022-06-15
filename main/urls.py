from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name="login"),
    path("request_account/", views.request_account, name="request_account"),
    path(
        "request_account_sent/", views.request_account_sent, name="request_account_sent"
    ),
    path("logout/", views.logout_user, name="logout"),
    path("account_requests/", views.account_requests, name="account_requests"),
    path(
        "account_request_approve/<int:pk>",
        views.account_request_approve,
        name="account_request_approve",
    ),
    path(
        "account_request_deny/<int:pk>",
        views.account_request_deny,
        name="account_request_deny",
    ),
    path("change_is_active/<int:pk>", views.change_is_active, name="change_is_active"),
    path("accounts/", views.accounts, name="accounts"),
    # path('md_register/', views.md_register, name='md_register'),
    # path('patient_register/', views.patient_register, name='patient_register'),
]
