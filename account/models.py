from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils import timezone


# Creating Custom User Model

class CustomAccountManager(BaseUserManager):
    #creating custom superuser or admin 
    def create_superuser(self,email,full_name,password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        #Checking staff permission on create_superuser
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff == True'
            )
        #Checking superuser permission on create_superuser
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'superuser must be assigned to is_superuser == True'
            )
        
        return self.create_user(email,full_name,password,**other_fields)
    
    #Creating New User
    def create_user(self,email,full_name,password,**other_fields):
        
        #Checking Vaild email is Entered or Not 
        if not email:
            raise ValueError(_('You Must Provide An Email Address'))
        
        email = self.normalize_email(email)
        user = self.model(email=email,full_name=full_name, **other_fields)

        user.set_password(password)
        user.save()
        return user


#Creating User Model
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=70,unique=True)
    full_name = models.CharField(max_length=50)
    signup_date = models.DateTimeField(default=timezone.now)
    business_name = models.CharField(max_length=50,default='NA')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email' #Overriding username with email
    REQUIRED_FIELDS = ['full_name'] #Required for creating superuser

    def __str__(self):
        return self.full_name