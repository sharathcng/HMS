from django.db import models

# Create your models here.
class medicines(models.Model):
    drug_id = models.CharField(primary_key=True,max_length=10)
    drug_name = models.CharField(max_length=255)