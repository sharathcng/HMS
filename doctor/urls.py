
from django.urls import path
from .import views


urlpatterns = [
    
    path('drDashboard/', views.dr_dashboard, name="drDashboard"),
    path('drSignUpPage/', views.dr_SignUp_Page, name="drSignUpPage"),
    path('drLoginPage/', views.dr_Login_Page, name="drLoginPage"),
    path('logout/', views.logout, name="logout"),

    path('patientSignUpPage/', views.patient_SignUp_Page, name="patientSignUpPage"),
    path('patientLoginPage/', views.patient_Login_Page, name="patientLoginPage"),
    path('addSymptom/<int:pk>', views.add_symptom,name="addSymptom"),
]
