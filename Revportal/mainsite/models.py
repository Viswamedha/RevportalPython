from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class User(AbstractBaseUser):

    email = models.EmailField(verbose_name = 'Email Address', primary_key = True, unique = True)

    first_name = models.CharField(verbose_name = 'First Name', max_length = 255)
    last_name = models.CharField(verbose_name = 'Last Name', max_length = 255)
    date_of_birth = models.DateField(verbose_name = 'Date of Birth')






    

