# backend/users/middleware.py

from django.http import JsonResponse
from django.db import connection
from tenants.models import Tenant

class TenantMiddleware:
    """
    Middleware to parse X-TENANT-ID from request headers and set PostgreSQL schema.
    Exempts admin paths from tenant identification.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # Define paths that do not require tenant identification
        self.exempt_paths = [
            '/admin/',  # Exempt all admin URLs
            '/api/auth/login/',  # Exempt login endpoint
            '/api/auth/logout/',
            '/swagger/'  # Exempt logout endpoint
        ]

    def __call__(self, request):
        # Check if the request path starts with any of the exempt paths
        if any(request.path.startswith(path) for path in self.exempt_paths):
            # For exempt paths, set the schema to 'public'
            tenant_schema = 'public'
        else:
            # For other paths, require the X-TENANT-ID header
            tenant_id = request.headers.get('X-TENANT-ID')

            if not tenant_id:
                return JsonResponse({'detail': 'X-TENANT-ID header missing.'}, status=400)

            try:
                tenant = Tenant.objects.get(tenant_id=tenant_id)
            except Tenant.DoesNotExist:
                return JsonResponse({'detail': 'Invalid Tenant ID.'}, status=400)

            tenant_schema = tenant.schema_name

        # Set the search_path for the duration of the request
        with connection.cursor() as cursor:
            cursor.execute(f'SET search_path TO {tenant_schema}, public;')

        response = self.get_response(request)
        return response