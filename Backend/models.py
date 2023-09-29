from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=50,unique=True,blank=True)
    name=models.CharField(max_length=50,blank=True)
    contact=models.CharField(max_length=20,blank=True)
    description=models.TextField(blank=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=128)

    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USER_TYPE_CHOICES=(
        ('company','Company'),
        ('candidate','Candidate'),
        ('admin','Admin')
    )

    user_type=models.CharField(max_length=10,choices=USER_TYPE_CHOICES,default=USER_TYPE_CHOICES[2])


    USERNAME_FIELD="username"
    REQUIRED_FIELDS=['email','password']

    objects=CustomUserManager()


    def __str__(self) -> str:
        return self.username


class Candidate(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    candidate_uid=models.AutoField(primary_key=True)
    gender=models.CharField(max_length=50,blank=True)
    DOB=models.DateField(null=True,blank=True)
    SocialMediaPlatforms=models.JSONField(default=dict,blank=True)
    education=models.JSONField(default=dict,blank=True)
    work_experience=models.JSONField(default=dict,blank=True)
    skills=models.JSONField(default=dict,blank=True)
    about=models.TextField(default="",blank=True)




class Company(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    company_uid=models.AutoField(primary_key=True)



