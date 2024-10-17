from rest_framework import serializers
from .models import Tenant, Domain, TenantConnection


class tenantSerializer(serializers.ModelSerializer):
    """
    Serializer for the Tenant model.
    """
    class Meta:
        model = Tenant
        fields = ['id', 'name', 'description']


class DomainSerializer(serializers.ModelSerializer):
    """
    Serializer for the Domain model.
    """
    class Meta:
        model = Domain
        fields = ['id', 'domain', 'tenant', 'is_primary']
        read_only_fields = ['tenant']


class TenantConnectionSerializer(serializers.ModelSerializer):
    """
    Serializer for the TenantConnection model.
    """
    tenant = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TenantConnection
        fields = ['tenant', 'db_name', 'db_user', 'db_password', 'db_host', 'db_port']
        read_only_fields = ['tenant']