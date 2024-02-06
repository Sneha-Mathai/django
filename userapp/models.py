from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

#class Login(AbstractUser):
    #username=models.CharField(max_length=20)
    #viewpassword=models.CharField(max_length=20)

class Userprofile(models.Model):
    username=models.CharField(max_length=20)
    bio=models.TextField(max_length=50)
    pic=models.ImageField(upload_to="uploadimage",max_length=None,null=True)
    #user=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)