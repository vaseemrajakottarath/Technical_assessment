from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from cust_admin.models import Department


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self,name,phone_number,email,department,password=None):
        if not email:
            raise ValueError('User must have an email address ')

        if not phone_number:
            raise ValueError('User must have a phone number')

        if not phone_number:
            raise ValueError('User must have a name')

        user = self.model(
            email = self.normalize_email(email),
            name = name,
            phone_number =phone_number,
            department= department,
        )
        user.role='User'
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,name,email,password,phone_number):
        if not email:
            raise ValueError('User must have an email address ')

        if not phone_number:
            raise ValueError('User must have a phone number')

        if not phone_number:
            raise ValueError('User must have a name')   
        user = self.model(
            email=self.normalize_email(email),
            name= name,
            phone_number=phone_number,
        )
        user.role='Admin'
        user.set_password(password)
        user.save()
        return user




class User(AbstractBaseUser):
    ROLE_CHOICES = (
        ('User','User'),
        ('Admin','Admin'),
    )
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,unique=True)
    phone_number = models.CharField(max_length=10,unique=True)
    department=models.ForeignKey(Department,null=True,blank=True,on_delete=models.CASCADE)
    role=models.CharField(max_length=50,choices=ROLE_CHOICES,default='User')

   
    created_by=models.CharField(max_length=50,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    last_updated_at=models.DateTimeField(auto_now_add=True)

    # date_joined = models.DateTimeField(auto_now_add=True)
    # last_login = models.DateTimeField(auto_now_add=True)
    # is_admin = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    # is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['name','phone_number']

    objects = MyUserManager()

    def __str__(self):
        return self.email

    # def has_perm(self,perm,obj=None):
    #     return self.is_admin
    
    # def has_module_perms(self,add_labels):
    #     return True


