from django import forms
from doctor.models import patientModel

class PatientRegisterForms(forms.ModelForm):
    class Meta:
        model=patientModel
        fields=("adharNumber","firstname","careof","lastname","age","weight","mobileNumber","place","gender")