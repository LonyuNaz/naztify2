from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict



from .models import User

# Create your views here.

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class HomeView(APIView):
     
   permission_classes = (IsAuthenticated, )

   def get(self, request):
        content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
        return Response(content)
   

class SignupView(APIView):
     
     def post(self, request):

          serializer = UserSerializer(data=request.data)

          if not serializer.is_valid():
               return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

          user_created = serializer.create(serializer.validated_data)

          new_user = UserCreateSerializer(user_created)

          return Response(new_user.data, status=status.HTTP_201_CREATED)


class LogoutView(APIView):

     permission_classes = (IsAuthenticated,)

     def post(self, request):
          try:
               refresh_token = request.data["refresh_token"]
               token = RefreshToken(refresh_token)
               token.blacklist()
               return Response(status=status.HTTP_205_RESET_CONTENT)
          except Exception as e:
               return Response(status=status.HTTP_400_BAD_REQUEST)


class MeView(APIView):
     permission_classes = (IsAuthenticated,)

     def get(self, request):
          try:
               user_obj = User.objects.get(email=request.user.__dict__['email'])
               return Response(status=status.HTTP_200_OK, data=model_to_dict(user_obj))
          except Exception as e:
               print(e)
               return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=str(e))
          

class WeeklyUpdateSubscribeView(APIView):

     permission_classes = (IsAuthenticated,)

     def post(self, request):
          try:
               user_obj = User.objects.get(email=request.user.__dict__['email'])
               state
               user_obj.weekly_update = True
               user_obj.save()
               return Response(status=status.HTTP_200_OK, data=model_to_dict(user_obj))
          except Exception as e:
               print(e)
               return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=str(e))
          

class WeeklyUpdateUnsubscribeView(APIView):

     permission_classes = (IsAuthenticated,)

     def post(self, request):
          try:
               user_obj = User.objects.get(email=request.user.__dict__['email'])
               user_obj.weekly_update = False
               user_obj.save()
               return Response(status=status.HTTP_200_OK, data=model_to_dict(user_obj))
          except Exception as e:
               print(e)
               return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=str(e))
          
class WeeklyCallbackView(APIView):
     def post(self, request):
          return Response(status=status.HTTP_200_OK, data=request.GET.dict())
     
     def get(self, request):
          return Response(status=status.HTTP_200_OK, data=request.GET.dict())