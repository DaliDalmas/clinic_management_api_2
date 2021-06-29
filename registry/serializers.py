from django.db.models import fields
from rest_framework.serializers import ModelSerializer,PrimaryKeyRelatedField
from .models import Patients, Visit, Symptoms

class PatientsSerializer(ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'

class VisitsSerializer(ModelSerializer):
    patient_id = PatientsSerializer(source='patients_relation')
    class Meta:
        model = Visit
        fields = ('date','patient_id','id')

   