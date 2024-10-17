from django_tenants.models import TenantMixin, DomainMixin
from django.db import models
from django.utils import timezone

class Tenant(TenantMixin):
    tenant_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    schema_name = models.CharField(max_length=100, unique=True)
    created_on = models.DateField(auto_now_add=True)
    description = models.TextField()
    domain_url = models.CharField(max_length=255)

    # Default true, schema will be created on save
    auto_create_schema = True

    def __str__(self):
        return self.name

class Domain(DomainMixin):
    """
    Represents a domain associated with a tenant.
    """
    # The `domain` and `tenant` fields are inherited from DomainMixin
    # You can add additional fields if necessary

    # Example additional field: indicates if this domain is the primary domain for the tenant
    is_primary = models.BooleanField(default=False, help_text="Is this the primary domain for the tenant?")

    # Timestamp fields for auditing purposes
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the domain was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the domain was last updated.")

    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = "Domains"
        unique_together = ('domain', 'tenant')  # Ensures that each domain is unique per tenant

    def __str__(self):
        return f"{self.domain} ({'Primary' if self.is_primary else 'Secondary'})"

    def save(self, *args, **kwargs):
        """
        Override the save method to ensure that only one domain is marked as primary per tenant.
        """
        if self.is_primary:
            # Unmark any other domains for the same tenant as primary
            Domain.objects.filter(tenant=self.tenant, is_primary=True).update(is_primary=False)
        super().save(*args, **kwargs)

class TenantConnection(models.Model):
    tenant = models.OneToOneField(Tenant, on_delete=models.CASCADE)
    db_name = models.CharField(max_length=100)
    db_user = models.CharField(max_length=100)
    db_password = models.CharField(max_length=100)
    db_host = models.CharField(max_length=100)
    db_port = models.IntegerField()