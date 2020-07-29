from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date

# Create your models here.

class extendedPharmacyUser(models.Model):
    mobileNumber = models.CharField(max_length = 10)
    gender = models.CharField(max_length = 10)
    user = models.OneToOneField(User,on_delete = models.CASCADE)

class medicines(models.Model):
    drug_id = models.CharField(primary_key=True,max_length=10)
    drug_name = models.CharField(max_length=255)

class symptoms(models.Model):
    symptom_name = models.CharField(max_length=255)

class diseases(models.Model):
    disease_name = models.CharField(max_length=255)