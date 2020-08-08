from django.urls import path
from .import views


urlpatterns = [
    path('phDashboard/', views.ph_dashboard, name="phDashboard"),
    path('phSignUpPage/', views.ph_SignUp_Page, name="phSignUpPage"),
    path('phLoginPage/', views.ph_Login_Page, name="phLoginPage"),
    path('phProfile/', views.ph_Profile_Page, name="phProfile"),
    path('phLogout/', views.logout, name="phLogout"),

    path('phPatientSignUpPage/', views.patient_SignUp_Page, name="phPatientSignUpPage"),
    path('phPatientLoginPage/', views.patient_Login_Page, name="phPatientLoginPage"),
    path('phPatientMedhistory/<int:id>',views.patientMedhistory, name="phPatientMedhistory"),
    # path('prescriptionDownload/<int:pk>', views.DownloadPDF.as_view(),name="prescriptionDownload"),
    path('prescriptionView/<int:pk>', views.ViewPDF.as_view(),name="prescriptionView"),
    path('updateMedicines/<int:pk>', views.update_medicines,name="updateMedicines"),
    
]