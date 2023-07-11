from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password = None, **extra_fields):
        if username is None:
            raise ValueError('Username cannot be empty')
        extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model(username = username, **extra_fields)
        user.set_password(password)  
        user.save(using=self._db)
        return user
        
    def create_superuser(self, username, password = None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)

        return self.create_user(username, password, **extra_fields)

class User(AbstractUser):
    username = models.CharField(unique=True,max_length=50)
    email = models.EmailField(unique=True, null=True)
    public_visibility = models.BooleanField(default=False)
    birth_year = models.CharField(max_length=4, null=True)
    address = models.TextField(max_length=100, null=True)
    created = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()