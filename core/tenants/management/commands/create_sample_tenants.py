from django.core.management.base import BaseCommand
from tenants.models import Tenant, Domain, TenantConnection

class Command(BaseCommand):
    help = 'Create sample tenants'

    def handle(self, *args, **kwargs):
        tenants = [
            {
                'id': 1,
                'name': 'Tenant One',
                'schema_name': 'tenant_one',
                'description': 'Description for Tenant One',
                'domain': 'tenant1.localhost',
                'connection': {
                    'db_name': 'tenant1_db',
                    'db_user': 'tenant1_user',
                    'db_password': 'tenant1_pass',
                    'db_host': 'db',
                    'db_port': 5432,
                }
            },
            {
                'id': 2,
                'name': 'Tenant Two',
                'schema_name': 'tenant_two',
                'description': 'Description for Tenant Two',
                'domain': 'tenant2.localhost',
                'connection': {
                    'db_name': 'tenant2_db',
                    'db_user': 'tenant2_user',
                    'db_password': 'tenant2_pass',
                    'db_host': 'db',
                    'db_port': 5432,
                }
            },
        ]

        for tenant_data in tenants:
            tenant, created = Tenant.objects.get_or_create(id=tenant_data['id'], defaults={
                'name': tenant_data['name'],
                'description': tenant_data['description'],
                'schema_name': tenant_data['schema_name'],
            })
            if created:
                tenant.save()
                Domain.objects.create(domain=tenant_data['domain'], tenant=tenant, is_primary=True)
                TenantConnection.objects.create(
                    tenant=tenant,
                    db_name=tenant_data['connection']['db_name'],
                    db_user=tenant_data['connection']['db_user'],
                    db_password=tenant_data['connection']['db_password'],
                    db_host=tenant_data['connection']['db_host'],
                    db_port=tenant_data['connection']['db_port'],
                )
                self.stdout.write(self.style.SUCCESS(f"Created tenant {tenant.name}"))
            else:
                self.stdout.write(f"Tenant {tenant.name} already exists")