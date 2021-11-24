from django.db import models

# Create your models here.
# from django.db import models
from selenium import webdriver
# Create your models here.
import uuid
from django.utils.translation import ugettext_lazy as _
# from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.contrib.auth.models import User   
from .managers import CustomUserManager
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
# Create your models here.

    # These fields tie to the roles!
# ADMIN = 1
# TECHNICIAN = 2
# EMPLOYEE = 3

# ROLE_CHOICES = (
#     (ADMIN, 'Admin'),
#     (TECHNICIAN, 'Technician'),
#     (EMPLOYEE, 'Employee')
# )
    
# class Meta:
#         verbose_name = 'user'
#         verbose_name_plural = 'users'
        

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

  # Roles created here
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
   
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    is_staff= models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    created_by = models.EmailField()
    modified_by = models.EmailField()
    
    # @property
    # def is_staff(self):
    #     return self.is_admin

    # def get_full_name(self):
    #     return ('%s %s') % (self.first_name, self.last_name)

    # def get_short_name(self):
    #     return self.username

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email   



