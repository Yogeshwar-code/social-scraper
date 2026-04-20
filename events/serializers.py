from rest_framework import serializers
from .models import EventRegistration
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


# Event Registration Serializer
class EventRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventRegistration
        fields = '__all__'


# User Registration Serializer or Custom Registraton API
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(     # User.objects.create_user() -->create_user()--> hashes password, normalizes username, uses set_password internally
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
            #user.set_password(validated_data['password'])  # 🔐 hashing
            #user.save()
        )
        return user
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

# Login Serializer or Custom Login API
#Using authenticate()
# Generating JWT manually
# Returning structured response
# Not exposing password
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError("Invalid username or password")

        if not user.is_active:
            raise serializers.ValidationError("User account is disabled")

        refresh = RefreshToken.for_user(user)

        return {
            "message": "Login successful",
            "username": user.username,
            "email": user.email,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }