# users/serializers.py

from rest_framework import serializers
from .models import CustomUser
from tenants.models import Tenant


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model.
    """
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'tenant']
        read_only_fields = ['tenant']


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating new users.
    Assumes that the tenant is set based on the request's context (e.g., X-TENANT-ID header).
    """
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, label='Confirm Password', style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs.pop('password2'):
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
from rest_framework import serializers
from tenants.models import Tenant

class TenantSerializer(serializers.Serializer):
    tenant_name = serializers.CharField(source='name')
    tenant_description = serializers.CharField(source='description')