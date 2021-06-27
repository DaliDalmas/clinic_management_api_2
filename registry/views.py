from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import PatientsSerializer
from rest_framework.views import APIView
from .models import Patients
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class PatientsView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = PatientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Patient successfully registered"})
        else:
            return Response({"msg":"patient is not registered"},status="400")

    def get(self,request):
        data = Patients.objects.all()
        serializer = PatientsSerializer(data,many=True)

        return Response(serializer.data)

