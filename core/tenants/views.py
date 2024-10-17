from rest_framework import viewsets
from .models import Tenant
from .serializers import tenantSerializer
from .permissions import IsSuperAdmin

class TenantViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing tenant instances.
    Only accessible by super admin users.
    """
    queryset = Tenant.objects.all()
    serializer_class = tenantSerializer
    permission_classes = [IsSuperAdmin]