from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.login_user, name="login"),
    path("request_account/", views.request_account, name="request_account"),
    path("logout/", views.logout_user, name="logout"),

    # i think we can remove these two na? since plano daw ni julius is to combine the register for md and patient
    # path('md_register/', views.md_register, name='md_register'),
    # path('patient_register/', views.patient_register, name='patient_register'),
    
    path('profile/', views.profile_page, name='profile_page'),

    path('md_landing/', views.md_landing, name='md_landing'),
    path('patient_landing/', views.patient_landing, name='patient_landing'),

    path('doctors/', views.all_doctors_page, name="all_doctors_page"),
    path('patients/', views.all_patients_page, name="all_patients_page"),

    path('patients/<int:id>/', views.patient_page, name="patient_page"),

    path('lobby/', views.lobby),
    path('room/', views.room),

    path('get_token/', views.getToken),
    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
    path('account_requests/', views.account_requests, name='account_requests'),
    path('all_patients/', views.all_patients_page, name="all_patients"),
    path('all_doctors/', views.all_doctors_page, name="all_doctors")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
