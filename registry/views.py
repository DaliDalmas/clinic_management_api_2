from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import PatientsSerializer, VisitsSerializer, SymptomsSerializer,PrescriptionsSerializer
from rest_framework.views import APIView
from .models import Patients, Visit, Symptoms, Prescriptions
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

class VisitsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        data = Visit.objects.all()
        serializer = VisitsSerializer(data,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = VisitsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response({"msg":"Serializer invalid"},status="400")

class SymptomsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        data = Symptoms.objects.all()
        serializer = SymptomsSerializer(data,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = SymptomsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response({"msg":"Serializer invalid"},status="400")

class PrescriptionsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        data = Prescriptions.objects.all()
        serializer = PrescriptionsSerializer(data,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PrescriptionsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response({"msg":"Serializer invalid"},status="400")
