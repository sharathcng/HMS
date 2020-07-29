
from django.urls import path
from .import views


urlpatterns = [
    
    path('drDashboard/', views.dr_dashboard, name="drDashboard"),
    path('drSignUpPage/', views.dr_SignUp_Page, name="drSignUpPage"),
    path('drLoginPage/', views.dr_Login_Page, name="drLoginPage"),
    path('logout/', views.logout, name="logout"),

    path('drPatientSignUpPage/', views.patient_SignUp_Page, name="drPatientSignUpPage"),
    path('drPatientLoginPage/', views.patient_Login_Page, name="drPatientLoginPage"),
    path('addSymptom/<int:pk>', views.add_symptom,name="addSymptom"),
    path('addMedicines/<int:pk>', views.add_medicines,name="addMedicines"),
    path('deleteMedicines/<int:pk>', views.delete_medicines,name="delete_Medicines"),
    path('patientMedhistory/<int:id>',views.patientMedhistory, name="patientMedhistory"),
]
