from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Role, UserRole

# Serializers for User Registration


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Assuming User model is imported or defined elsewhere
        fields = ('id', 'username', 'email', 'date_joined')

#  Serializers for User Login


class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User  # Assuming User model is imported or defined elsewhere
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password', 'role')

    def create(self, validated_data):
        role_name = validated_data.pop('role', None)
        password = validated_data.pop('password', None)
        first_name = validated_data.pop('first_name', '')
        last_name = validated_data.pop('last_name', '')
        username = validated_data.get('username')
        email = validated_data.get('email')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        if role_name:
            role, created = Role.objects.get_or_create(name=role_name)
            UserRole.objects.create(user=user, role=role)
        return user

# Serializer for Login


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
