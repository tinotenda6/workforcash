from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from phone_field import PhoneField


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100,unique=True,default="") 
    email = models.EmailField(_('email address'))
    is_child = models.BooleanField(default=False)
    is_guardian_or_parent = models.BooleanField(default=False)
    phone_number =PhoneField(blank=True, help_text='add ext if you have a landline', E164_only=False)
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username

CustomUser = get_user_model()


    
class ParentProfile(models.Model):
    user = models.OneToOneField(CustomUser,related_name='parent_profile', on_delete=models.CASCADE)
    def __str__(self):
    	return self.user.username


class ChildProfile(models.Model):
    user = models.OneToOneField(CustomUser,related_name='child_profile', on_delete=models.CASCADE)
    parent_name = models.ForeignKey(ParentProfile, null=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
    	return self.user.username
    
    