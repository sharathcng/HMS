from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date

# Create your models here.
class extendedUser(models.Model):
    mobileNumber = models.CharField(max_length = 10)
    gender = models.CharField(max_length = 10)
    aboutMe = models.CharField(max_length = 200)
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    
class patientModel(models.Model):
    adharNumber = models.BigIntegerField(primary_key=True)
    firstname = models.CharField(max_length = 20)
    careof = models.CharField(max_length = 10)
    lastname = models.CharField(max_length = 20)
    age = models.IntegerField()
    weight = models.IntegerField()
    mobileNumber = models.CharField(max_length = 15)
    place = models.CharField(max_length = 15)
    gender = models.CharField(max_length = 10)

class patientSymptomsDiseaseModel(models.Model):
    pAdharNumber = models.ForeignKey(patientModel,on_delete=models.CASCADE,null=True,blank=True)
    symptom_name = models.CharField(max_length=255)
    disease_name = models.CharField(max_length=255)
    date=models.DateField(auto_now_add=True)

class patientMedicineModel(models.Model):
    pAdharNumber = models.ForeignKey(patientModel,on_delete=models.CASCADE,null=True,blank=True)
    medicine_name = models.CharField(max_length=255)
    medicine_count = models.IntegerField()
    mor = models.CharField(max_length=255, default='null')
    aft = models.CharField(max_length=255, default='null')
    nit = models.CharField(max_length=255, default='null')
    date = models.DateField(auto_now_add = True)
    status = models.CharField(max_length = 50,default='null')
    count = models.CharField(max_length = 50,default='null')