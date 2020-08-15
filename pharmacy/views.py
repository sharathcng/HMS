from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib import auth
from doctor.models import patientModel,patientMedicineModel
from .models import extendedPharmacyUser,medicines,symptoms
from doctor.forms import PatientRegisterForms
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import date
from math import ceil
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from HomePage.views import home_page

# Create your views here.


@login_required(login_url='phLoginPage')
def ph_dashboard(request):
    data1 = User.objects.filter(username=request.user)
    data2 = extendedPharmacyUser.objects.filter(user=request.user)
    return render(request,'pharmacy/dashboard.html',{'data1':data1,'data2':data2})

@login_required
def ph_Profile_Page(request):
    data1 = User.objects.filter(username=request.user)
    data2 = extendedPharmacyUser.objects.filter(user=request.user)
    return render(request,'pharmacy/phProfile.html',{'data1':data1,'data2':data2})

def ph_SignUp_Page(request):
    if request.method == "POST":
        # to create new user
        if request.POST['password'] == request.POST['re_password']:
            #both the passwords matched
            #now check if a previous user exists
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'pharmacy/phSignUpPage.html',{'userNameError':"Username already exist"})
            except User.DoesNotExist:
                mobileNumber = request.POST['mobileNumber']
                gender = request.POST['gender']
                if len(mobileNumber) == 10 :
                    user = User.objects.create_user(username=request.POST['username'],first_name=request.POST['firstname'],last_name=request.POST['lastname'],password=request.POST['password'],email=request.POST['email'])
                    newExtendedUser = extendedPharmacyUser(mobileNumber = mobileNumber,gender=gender,user=user) 
                    newExtendedUser.save()                   
                    auth.login(request,user)
                    return redirect(ph_dashboard)
                else:
                    return render(request,'pharmacy/phSignUpPage.html',{'mobileError':"Mobile number must be 10 digits"})
        else:
            return render(request,'pharmacy/phSignUpPage.html',{'passwordError':"Passwords doesnot match"})
    else:
        return render(request,'pharmacy/phSignUpPage.html')



def ph_Login_Page(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect(ph_dashboard)
        else:
            return render(request,'pharmacy/phLoginPage.html',{'usernameError':"Username doesnot exist"})
    else:
        return render(request,'pharmacy/phLoginPage.html')

def logout(request):
    auth.logout(request)
    return redirect(home_page)


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
                return render(request,'patients/phPatientSignUpPage.html',{'mobileError':"Mobile number must be 10 digits"})
            else:
                if forms.is_valid():
                    patient = forms.save()
                    context = {'patient':patient}
                    return render(request,'patients/phPatientMedicinePage.html',context)
                else:
                    return render(request,'patients/phPatientSignUpPage.html')
    else:
        return render(request,'patients/phPatientSignUpPage.html')

def patient_Login_Page(request):
    if request.method == "POST":
        patient = request.POST['adharNumber']
        if patientModel.objects.filter(adharNumber=patient):
            patient = patientModel.objects.filter(adharNumber=patient)
            medicine = medicines.objects.all()
            symptomsList = symptoms.objects.all()
            todaysmedicines =  patientMedicineModel.objects.filter(date = date.today())
            context = {'patient':patient,'medicine':medicine,'symptomsList':symptomsList,'todaysmedicines':todaysmedicines}
            return render(request,'patients/phPatientMedicinePage.html',context)
        else:
            return redirect(patient_SignUp_Page)
    else:
        return render(request,'patients/phPatientLoginPage.html')


def patientMedhistory(request,id):
    if patientModel.objects.filter(adharNumber=id):
        patient = patientModel.objects.filter(adharNumber=id)
        medicine = medicines.objects.all()
        symptomsList = symptoms.objects.all()
        todaysmedicines = patientMedicineModel.objects.filter(pAdharNumber=id)
        context = {'patient': patient, 'medicine': medicine,
                'symptomsList': symptomsList, 'todaysmedicines': todaysmedicines}
        return render(request, 'patients/phPatientMedicinehistoryPage.html',context)


# pdf generator

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

#View
class ViewPDF(View):
	def get(self, request, *args, **kwargs):
		patient = patientModel.objects.filter(adharNumber=kwargs['pk'])
		todaysmedicines = patientMedicineModel.objects.filter(date=date.today(),pAdharNumber=kwargs['pk'],status="Delivered")
		data = {'patient': patient,'todaysmedicines': todaysmedicines}
		pdf = render_to_pdf('patients/pdf.html', data)
		return HttpResponse(pdf, content_type='application/pdf')

#Automaticly downloads to PDF file
# class DownloadPDF(View):
# 	def get(self, request, *args, **kwargs):
# 		patient = patientModel.objects.filter(adharNumber=kwargs['pk'])
# 		todaysmedicines = patientMedicineModel.objects.filter(date=date.today(),pAdharNumber=kwargs['pk'])
# 		data = {'patient': patient,'todaysmedicines': todaysmedicines}
# 		pdf = render_to_pdf('patients/pdf.html', data)
# 		response = HttpResponse(pdf, content_type='application/pdf')
# 		filename = "Invoice_%s.pdf" %("12341231")
# 		content = "attachment; filename='%s'" %(filename)
# 		response['Content-Disposition'] = content
# 		return response

def update_medicines(request,pk):
    patientMedicineModel.objects.filter(id=request.POST['id']).update(status="Delivered",count=request.POST['count'])
    data = {
        'adharNumber':pk,
    }
    return JsonResponse(data)

