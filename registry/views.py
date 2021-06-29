from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import PatientsSerializer, VisitsSerializer
from rest_framework.views import APIView
from .models import Patients, Visit
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
    def get(self,request):
        data = Visit.objects.all()
        serializer = VisitsSerializer(data,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = VisitsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"msg":"Serializer invalid"},status="400")
