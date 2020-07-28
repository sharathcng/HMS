from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib import auth
from . models import extendedUser,patientModel,patientSymptomsDiseaseModel,patientMedicineModel
from pharmacy.models import medicines,symptoms
from doctor.forms import PatientRegisterForms
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import date

# Create your views here.

@login_required
def dr_dashboard(request):
    data1 = User.objects.filter(username=request.user)
    data2 = extendedUser.objects.filter(user=request.user)
    return render(request,'doctor/dashboard.html',{'data1':data1,'data2':data2})

def dr_SignUp_Page(request):
    if request.method == "POST":
        # to create new user
        if request.POST['password'] == request.POST['re_password']:
            #both the passwords matched
            #now check if a previous user exists
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'doctor/drSignUpPage.html',{'userNameError':"Username already exist"})
            except User.DoesNotExist:
                mobileNumber = request.POST['mobileNumber']
                gender = request.POST['gender']
                if len(mobileNumber) == 10 :
                    user = User.objects.create_user(username=request.POST['username'],first_name=request.POST['firstname'],last_name=request.POST['lastname'],password=request.POST['password'],email=request.POST['email'])
                    newExtendedUser = extendedUser(mobileNumber = mobileNumber,gender=gender,user=user) 
                    newExtendedUser.save()                   
                    auth.login(request,user)
                    return redirect(dr_dashboard)
                else:
                    return render(request,'doctor/drSignUpPage.html',{'mobileError':"Mobile number must be 10 digits"})
        else:
            return render(request,'doctor/drSignUpPage.html',{'passwordError':"Passwords doesnot match"})
    else:
        return render(request,'doctor/drSignUpPage.html')



def dr_Login_Page(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect(dr_dashboard)
        else:
            return render(request,'doctor/drLoginPage.html',{'usernameError':"Username doesnot exist"})
    else:
        return render(request,'doctor/drLoginPage.html')

def logout(request):
    auth.logout(request)
    return render(request,'hospital/homePage.html')


#patient_data

def patient_SignUp_Page(request):
    if request.method == "POST":
        forms = PatientRegisterForms(request.POST)
        try:
            patient = patientModel.objects.get(adharNumber=request.POST['adharNumber'])
            return render(request,'patients/patientSignUpPage.html',{'adharNumberError':"Patient with this Adhar number already exist"})
        except:
            mobileNumber = request.POST['mobileNumber']
            if len(str(mobileNumber)) != 10 :
                return render(request,'patients/patientSignUpPage.html',{'mobileError':"Mobile number must be 10 digits"})
            else:
                if forms.is_valid():
                    patient = forms.save()
                    context = {'patient':patient}
                    return render(request,'patients/patientPrescriptionPage.html',context)
                else:
                    return render(request,'patients/patientSignUpPage.html')
    else:
        return render(request,'patients/patientSignUpPage.html')

def patient_Login_Page(request):
    if request.method == "POST":
        patient = request.POST['adharNumber']
        if patientModel.objects.filter(adharNumber=patient):
            patient = patientModel.objects.filter(adharNumber=patient)
            medicine = medicines.objects.all()
            symptomsList = symptoms.objects.all()
            todaysmedicines =  patientMedicineModel.objects.filter(date = date.today())
            context = {'patient':patient,'medicine':medicine,'symptomsList':symptomsList,'todaysmedicines':todaysmedicines}
            return render(request,'patients/patientPrescriptionPage.html',context)
        else:
            return redirect(patient_SignUp_Page)
    else:
        return render(request,'patients/patientLoginPage.html')

def add_symptom(request,pk):
    pAdharNumber = patientModel.objects.get(adharNumber=pk)
    instance = patientSymptomsDiseaseModel.objects.create(symptom_name=request.POST['symptom'],disease_name=request.POST['disease'])
    instance.pAdharNumber = pAdharNumber
    instance.save()
    response = {
        'adharNumber':pk
    }
    return JsonResponse(response)


def add_medicines(request,pk):
    pAdharNumber = patientModel.objects.get(adharNumber=pk)
    instance = patientMedicineModel.objects.create(
        medicine_name=request.POST['medici'],
        mor=request.POST['morning'],
        aft=request.POST['afternoon'],
        nit=request.POST['night'],
        medicine_count=request.POST['count']
        )
    
    medi = {'id':instance.id, 'name':instance.medicine_name, 'count':instance.medicine_count,'mor':instance.mor,'aft':instance.aft,'nit':instance.nit}
        
    instance.pAdharNumber = pAdharNumber
    instance.save()
    data = {
        'adharNumber':pk,
        'medi':medi
    }
    return JsonResponse(data)

def delete_medicines(request,pk):
    patientMedicineModel.objects.delete(id = request.POST['id'])
    data = {
        'adharNumber':pk,
        'deleted': True
    }
    return JsonResponse(data)