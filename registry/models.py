from django.db import models
from django.db.models.base import Model


# Create your models here.
class Patients(models.Model):
    patient_first_name = models.CharField(max_length=255)
    patient_last_name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    sex = models.CharField(max_length=10)


class Visit(models.Model):
    patient = models.ForeignKey(Patients,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    

class Symptoms(models.Model):
    visit = models.ForeignKey(Visit,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    detail = models.TextField()


class Prescriptions(models.Model):
    visit = models.ForeignKey(Visit,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    detail = models.TextField()
