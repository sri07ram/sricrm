from django.db import models
from sricrm.models.organization import Organization
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from sricrm.models.company import Company


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=10, primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)

    # Roles
    is_user_id = models.BooleanField(default=False)
    is_org_id = models.BooleanField(default=False)
    is_com_id = models.BooleanField(default=False)

    # Extra fields
    role = models.CharField(max_length=50, null=True, blank=True)

    # Foreign keys
    com = models.ForeignKey(Company, related_name='users', on_delete=models.CASCADE, null=True, blank=True)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.user_id:
            last_user = Users.objects.order_by('-user_id').first()
            if last_user and last_user.user_id.startswith('user'):
                try:
                    last_num = int(last_user.user_id.replace('user', ''))
                except ValueError:
                    last_num = 0
            else:
                last_num = 0
            self.user_id = f"user{last_num + 1:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.email} ({self.user_id})"
