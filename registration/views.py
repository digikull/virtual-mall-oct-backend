from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .RegistrationSerializer import RegistrationSerializer
from django.contrib.auth import get_user_model



# Calling Custom User
User = get_user_model() 

class Registration(APIView):

    def post(self,request):
        
        serialized = RegistrationSerializer(data=request.data)
        
        if serialized.is_valid():
           
            serialized.save()
            # return Response({'success': True})
            
        else:
            
            return Response({'error':'Email is Already Registered'})
        result = User.objects.all()
        output_serialized = RegistrationSerializer(result, many=True)

        return Response({
            'User_Registered': 'Registed Suceesfully'
            
           
        })