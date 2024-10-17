from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from tenants.models import Tenant
from django.utils import timezone
from .constants import Role

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, role='regular_user', tenant=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not tenant:
            raise ValueError('Users must be associated with a tenant')
        if isinstance(tenant, int):
          tenant = Tenant.objects.get(id=tenant)
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, role=role, tenant=tenant)
        user.set_password(password)
        user.date_joined= timezone.now()
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, role='admin', tenant=None):
        if isinstance(tenant, int):
          tenant = Tenant.objects.get(id=tenant)
        user = self.create_user(username, email, password, role, tenant)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name=models.CharField(max_length=50,unique=True)
    last_name=models.CharField(max_length=50,unique=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=Role.CHOICES, default='regular_user')
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='users')

    date_joined = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'tenant']

    def __str__(self):
        return self.username

# class UserProfile(models.Model):
#     user = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE)
#     # ... other fields

#     def save(self, *args, **kwargs):
#         if not self.user.tenant:
#             raise Exception("User must be associated with a tenant")
#         super().save(*args, **kwargs)