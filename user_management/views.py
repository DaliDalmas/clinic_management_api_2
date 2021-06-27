from django.shortcuts import render
from .serializers import RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class RegistrationView(APIView):
    def post(self,request):
        serializer = RegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"User created successfully"})
