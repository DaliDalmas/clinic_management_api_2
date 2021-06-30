from django.db.models import fields
from rest_framework.serializers import ModelSerializer,PrimaryKeyRelatedField
from .models import Patients, Visit, Symptoms, Prescriptions

class PatientsSerializer(ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'

class VisitsSerializer(ModelSerializer):
    #patient_bio = PatientsSerializer(source="patient")
    class Meta:
        model = Visit
        fields = ('id','date','patient')
        depth = 0

class SymptomsSerializer(ModelSerializer):
    class Meta:
        model = Symptoms
        fields = ('id','visit','detail','created_at')
        depth = 0

class PrescriptionsSerializer(ModelSerializer):
    class Meta:
        model = Prescriptions
        fields = ('id','symptoms','detail','created_at')
        depth = 0
   