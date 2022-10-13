from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import uuid
from datetime import datetime


class RevportalUserManager(BaseUserManager):

    def create_user(self, email_address, username, first_name, last_name, date_of_birth, password = None):
        if not email_address: 
            raise ValueError("Users must have an email address. ")
        user = self.model(
            email_address = self.normalize_email(email = email_address),
            username = username, 
            first_name = first_name,
            last_name = last_name,
            date_of_birth = date_of_birth,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user 

    def create_superuser(self, email_address, username, first_name, last_name, date_of_birth, password = None):
        user = self.create_user(email_address, username, first_name, last_name, date_of_birth, password)
        user.is_superuser = True 
        user.save(using = self._db)
        return user


class RevportalUser(AbstractBaseUser, PermissionsMixin): 

    USERNAME_FIELD = 'email_address'
    EMAIL_FIELD = 'email_address'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth']

    user_id = models.UUIDField(verbose_name = 'User ID', default = uuid.uuid4, editable = False)
    email_address = models.EmailField(verbose_name = 'Email Address', max_length = 255, unique = True)
    username = models.CharField(verbose_name = 'Username', max_length = 255, unique = True)
    date_of_birth = models.DateField(verbose_name = 'Date of Birth')
    first_name  = models.CharField(verbose_name = 'First Name', max_length = 255)
    last_name   = models.CharField(verbose_name = 'Last Name', max_length = 255)
    middle_name = models.CharField(verbose_name = 'Middle Name(s)', max_length = 255, default = '', blank = True)
    phone_number = models.CharField(verbose_name = 'Phone Number', max_length = 15, null = True, blank = True)
    objects = RevportalUserManager()
    
    class Meta:
        verbose_name = 'Revportal User'
        verbose_name_plural = 'Revportal Users'
    
    @property
    def is_staff(self): 
        return self.is_superuser
    
    is_active = models.BooleanField(verbose_name = 'Account Active', default = True)
    is_superuser  = models.BooleanField(verbose_name = 'Account Admin',  default = False)
    is_verified = models.BooleanField(verbose_name = 'Account Verified', default = False)

    created_at = models.DateTimeField(verbose_name = 'Created At', auto_now_add = True)
    updated_at = models.DateTimeField(verbose_name = 'Created At', auto_now_add = True)

    def has_perm(self, perm, obj=None): 
        return True
    def has_module_perms(self, app_label): 
        return True


class RevportalUserAuthentication(models.Model):

    user = models.OneToOneField(RevportalUser, on_delete = models.CASCADE, related_name = 'auth')
    verification_token = models.CharField(verbose_name = 'Verfication Token', max_length = 200, null = True, blank = True)
    reset_password_token =  models.CharField(verbose_name = 'Reset Password Token', max_length = 200, null = True, blank = True)
    reset_instance_token = models.CharField(verbose_name = 'Reset Instance Token', max_length = 200, null = True, blank = True)
    password_reset_at = models.DateTimeField(default = datetime.now, null = True,  blank = True)

    class Meta:
        verbose_name = 'Revportal User Authentication'
        verbose_name_plural = 'Revportal Users Authentication'
    
    def __str__(self):
        return self.user.email_address
    

@receiver(post_save, sender = RevportalUser)
def create_auth(sender, instance, created, **kwargs):
    if created:
        RevportalUserAuthentication.objects.create(user = instance)




