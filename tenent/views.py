from django.shortcuts import render
from rest_framework import request, viewsets
from django.conf import settings
from .models import Tenent
from .serializers import TenentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token
from django.shortcuts import render,HttpResponse
from rest_framework import status

# Create your views here.

# User = get_user_model()
class TenentViewSet(viewsets.ModelViewSet,IsAdminOrReadOnly):
    queryset=Tenent.objects.all()
    serializer_class = TenentSerializer
    permission_classes =[IsAdminOrReadOnly]
    authentication_classes = (TokenAuthentication,)
    
    

@api_view(['POST'])
def login(request):
    print(request.data)
    try:
        user=Tenent.objects.get(email=request.data['email'])
    except Exception as e:
       
        return Response(' email error')
    if user.check_password(request.data['password']):
        token, _=Token.objects.get_or_create(user=user)
        return Response({'token':token.key})
    return Response('Password incorrect',status=status.HTTP_401_UNAUTHORIZED)


 

    # def delete(self,request,id):        
    #     Tenent =self.get_object(id=id)
    #     tenent.hidden = True
    #     tenent.save()
    #     logout(request)
    #     messages.success(request, 'Profile successfully disabled.')
    #     return redirect('index')

# class TenentList(APIView):
#     permission_classes =[IsAdminOrReadOnly]
#     def get(self,request):
#         Tenents =Tenent.objects.all()
#         serializer = TenentSerializer( Tenents,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = TenentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,)

# class TenentDetails(APIView):
#     permission_classes =[IsAdminOrReadOnly]
#     def get_object(self, id):
#         try:
#            return Tenent.objects.get(id = id)
#         except Tenent.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self,request,id):
#         Tenent =self.get_object(id=id)
#         serializer = TenentSerializer(Tenent,many=True)
#         return Response(serializer.data)

#     def put(self,request,id):
#         Tenent =self.get_object(id=id)
#         serializer =  TenentSerializer(Tenent,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,id):
#         Tenent =self.get_object(id=id)
#         Tenent.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)