from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionManager, PermissionsMixin, BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):

class User(abstractBaseUser, PermissionMixin):
    email=models.EmailField(db_index=True, unique=True, max_length=200)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    mobile=models.CharField(max_length=50)
    address=models.CharField(max_length=200)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superpower = models.BooleanField(default=True)


    USERNAME_FIELD= 'email'
    REQUIRED_FEIDLS=['first_name', 'last_name', 'mobile']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

