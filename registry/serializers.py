from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Patients

class PatientsSerializer(ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'