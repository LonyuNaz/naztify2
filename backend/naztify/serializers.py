from rest_framework import serializers
from .models import User, UserCreate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCreate
        fields = ('username', 'email')

