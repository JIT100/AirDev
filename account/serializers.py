from rest_framework import  serializers
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = User
        fields = ('id', 'username','first_name', 'last_name','email','password')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'username': {'required': True}

        }
    def create(self, validated_data):
        user = User.objects.create_user(username = validated_data['username'],email=validated_data['email'],password = validated_data['password'],first_name=validated_data['first_name'],last_name=validated_data['last_name'])
        return user

# Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'