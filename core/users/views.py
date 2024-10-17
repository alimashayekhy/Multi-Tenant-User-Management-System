from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsAdmin, IsTechnician, IsOperator, IsRegularUser
from .serializers import TenantSerializer

class AdminTestView(generics.CreateAPIView):
    permission_classes = [IsAdmin]
    serializer_class = TenantSerializer

    def post(self, request):
        tenant = getattr(request, 'tenant', None)
        if not tenant:
            return Response({"detail": "Tenant information not found."}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            'tenant_name': tenant.name,
            'tenant_description': tenant.description
        }
        return Response(data, status=status.HTTP_200_OK)

class TechnicianTestView(generics.CreateAPIView):
    permission_classes = [IsTechnician]
    serializer_class = TenantSerializer

    def post(self, request):
        tenant = getattr(request, 'tenant', None)
        if not tenant:
            return Response({"detail": "Tenant information not found."}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            'tenant_name': tenant.name,
            'tenant_description': tenant.description
        }
        return Response(data, status=status.HTTP_200_OK)

class OperatorTestView(generics.CreateAPIView):
    permission_classes = [IsOperator]
    serializer_class = TenantSerializer

    def post(self, request):
        tenant = getattr(request, 'tenant', None)
        if not tenant:
            return Response({"detail": "Tenant information not found."}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            'tenant_name': tenant.name,
            'tenant_description': tenant.description
        }
        return Response(data, status=status.HTTP_200_OK)

class RegularUserTestView(generics.CreateAPIView):
    permission_classes = [IsRegularUser]
    serializer_class = TenantSerializer

    def post(self, request):
        tenant = getattr(request, 'tenant', None)
        if not tenant:
            return Response({"detail": "Tenant information not found."}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            'tenant_name': tenant.name,
            'tenant_description': tenant.description
        }
        return Response(data, status=status.HTTP_200_OK)