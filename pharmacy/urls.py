from django.urls import path
from .import views


urlpatterns = [
    path('phDashboard/', views.ph_dashboard, name="phDashboard"),
    path('phSignUpPage/', views.ph_SignUp_Page, name="phSignUpPage"),
    path('phLoginPage/', views.ph_Login_Page, name="phLoginPage"),
    path('logout/', views.logout, name="logout"),

    path('phPatientSignUpPage/', views.patient_SignUp_Page, name="phPatientSignUpPage"),
    path('phPatientLoginPage/', views.patient_Login_Page, name="phPatientLoginPage"),
    path('phPatientMedhistory/<int:id>',views.patientMedhistory, name="phPatientMedhistory"),
    # path('prescriptionDownload/<int:pk>', views.DownloadPDF.as_view(),name="prescriptionDownload"),
    path('prescriptionView/<int:pk>', views.ViewPDF.as_view(),name="prescriptionView"),
    
]