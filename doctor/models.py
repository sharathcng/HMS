from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date

# Create your models here.
class extendedUser(models.Model):
    mobileNumber = models.CharField(max_length = 10)
    gender = models.CharField(max_length = 10)
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

class patientSymptomsModel(models.Model):
    pAdharNumber = models.ForeignKey(patientModel,on_delete=models.CASCADE,null=True,blank=True)
    symptom_name = models.CharField(max_length=255)
    date=models.DateField(auto_now_add=True)

class patientDiseasesModel(models.Model):
    pAdharNumber = models.ForeignKey(patientModel,on_delete=models.CASCADE,null=True,blank=True)
    disease_name = models.CharField(max_length=255)
    date=models.DateField(auto_now_add=True)