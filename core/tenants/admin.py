from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from .models import Tenant, Domain, TenantConnection


@admin.register(Tenant)
class TenantAdmin(TenantAdminMixin, admin.ModelAdmin):
    """
    Admin interface for the Tenant model.
    TenantAdminMixin adds tenant-specific functionalities to the admin.
    """
    list_display = ('name', 'description','created_on')
    search_fields = ('name',)


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    """
    Admin interface for the Domain model.
    DomainAdminMixin adds domain-specific functionalities to the admin.
    """
    list_display = ('domain', 'tenant', 'is_primary')
    search_fields = ('domain',)


@admin.register(TenantConnection)
class TenantConnectionAdmin(admin.ModelAdmin):
    """
    Admin interface for the TenantConnection model.
    """
    list_display = ('tenant', 'db_name', 'db_user', 'db_host', 'db_port')
    search_fields = ('tenant__name', 'db_name', 'db_user', 'db_host')