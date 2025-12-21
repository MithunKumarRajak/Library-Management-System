from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import Role, UserRole

User = get_user_model()

# ---------- User Serializer ----------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined')


# ---------- Register Serializer ----------
class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'role')

    def create(self, validated_data):
        role_name = validated_data.pop('role', None)
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        if role_name:
            role, _ = Role.objects.get_or_create(name=role_name)
            UserRole.objects.create(user=user, role=role)

        return user


# ---------- Login Serializer ----------
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email or password.")

        data['user'] = user
        return data
