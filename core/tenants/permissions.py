from rest_framework import permissions

class IsSuperAdmin(permissions.BasePermission):
    """
    Custom permission to only allow super admins to manage tenants.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)