from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for the CustomUser model.
    Extends Django's UserAdmin to include the 'role' and 'tenant' fields.
    """
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'tenant', 'is_staff']
    list_filter = ['role', 'tenant', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['username']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'tenant')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'tenant')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)