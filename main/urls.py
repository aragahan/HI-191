from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.login_page, name='login'),
    path('register/', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login_page'),
    
]
=======
    path("", views.login_user, name="login"),
    path("request_account/", views.request_account, name="request_account"),
    path("logout/", views.logout_user, name="logout"),
    # path('md_register/', views.md_register, name='md_register'),
    # path('patient_register/', views.patient_register, name='patient_register'),
]
>>>>>>> 7a6a3394833b7ad4fcdd4a0ebed67a79bc91ae03
