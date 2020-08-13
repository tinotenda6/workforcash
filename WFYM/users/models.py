from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from phone_field import PhoneField
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_child = models.BooleanField(default=False)
    is_guardian_or_parent = models.BooleanField(default=False)
    phone_number =PhoneField(blank=True, help_text='add ext if you have a landline', E164_only=False)
    USERNAME_FIELD = 'email' #sest the the USERNAME_FIELD which defines the unique identifier to email
    REQUIRED_FIELDS = []
    objects = CustomUserManager() #specified that all objects for the class come form CustomUserManager
    def __str__(self):
        return self.email
