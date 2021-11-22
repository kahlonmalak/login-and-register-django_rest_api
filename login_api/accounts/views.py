from rest_framework import status
from django.template import RequestContext
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework import status
from rest_framework import generics
# from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializer import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated 
from django.contrib.auth import get_user_model
from .serializer import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserListSerializer
)




# from order.models import *
# from API.serializers import *

# from rest_framework import status

# from rest_framework.response import Response

# from .serializer import ChangePasswordSerializer
# from rest_framework.permissions import IsAuthenticated   



class UserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny, )

    def post(self, request,format='json'):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        # serializer.save()
        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
                'user': serializer.data
            }

            return Response(response, status=status_code)
        
class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                  
                }
            }

            return Response(response, status=status_code)   
        
        

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    
# queryset= User.objects.all()
    serializer_class = ChangePasswordSerializer
    # model = User
    permission_classes = (IsAuthenticated,)
    permission_classes=(AllowAny,)
    def get_object(self, queryset=True):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)