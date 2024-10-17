from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from .models import CustomUser
from tenants.models import Tenant
from rest_framework_simplejwt.tokens import RefreshToken

class RoleBasedAccessTests(APITestCase):
    def setUp(self):
        # Create tenants
        self.tenant1 = Tenant.objects.create(name='Tenant One', description='First Tenant')
        self.tenant2 = Tenant.objects.create(name='Tenant Two', description='Second Tenant')
        
        # Create users for tenant1
        self.admin_user = CustomUser.objects.create_user(
            username='admin1',
            password='adminpass',
            role='admin',
            tenant=self.tenant1
        )
        self.technician_user = CustomUser.objects.create_user(
            username='tech1',
            password='techpass',
            role='technician',
            tenant=self.tenant1
        )
        self.operator_user = CustomUser.objects.create_user(
            username='op1',
            password='oppass',
            role='operator',
            tenant=self.tenant1
        )
        self.regular_user = CustomUser.objects.create_user(
            username='user1',
            password='userpass',
            role='regular',
            tenant=self.tenant1
        )
        
        # Create users for tenant2
        self.admin_user2 = CustomUser.objects.create_user(
            username='admin2',
            password='adminpass2',
            role='admin',
            tenant=self.tenant2
        )
        
        # Initialize APIClient
        self.client = APIClient()
    
    def authenticate(self, user):
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.client.credentials(HTTP_X_TENANT_ID=user.tenant.id)
    
    def test_admin_access_admin_endpoint(self):
        self.authenticate(self.admin_user)
        url = reverse('admin_test')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['tenant_name'], 'Tenant One')
    
    def test_technician_access_admin_endpoint_forbidden(self):
        self.authenticate(self.technician_user)
        url = reverse('admin_test')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 403)
    
    def test_operator_access_operator_endpoint(self):
        self.authenticate(self.operator_user)
        url = reverse('operator_test')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['tenant_name'], 'Tenant One')
    
    def test_regular_user_access_user_endpoint(self):
        self.authenticate(self.regular_user)
        url = reverse('user_test')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['tenant_name'], 'Tenant One')
    
    def test_user_cross_tenant_access(self):
        # Authenticate admin_user2 (tenant2 admin)
        self.authenticate(self.admin_user2)
        # Attempt to access tenant1's admin endpoint
        url = reverse('admin_test')
        self.client.credentials(HTTP_X_TENANT_ID=self.tenant1.id)
        response = self.client.post(url)
        self.assertEqual(response.status_code, 403)
    
    def test_missing_tenant_id_header(self):
        self.authenticate(self.admin_user)
        self.client.credentials()  # Remove all credentials, including X-TENANT-ID
        url = reverse('admin_test')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 403)  # Or 400 based on middleware