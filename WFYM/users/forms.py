from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from phone_field import PhoneField

class UserRegisterForm(UserCreationForm):
    username = None
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_number = PhoneField(blank=True)
    class Meta:
        model = CustomUser
        fields = ('email','first_name','last_name','phone_number')
class ChildRegisterForm(UserCreationForm):
    username = None
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_number = PhoneField(blank=True)

    class Meta:
        model = CustomUser
        fields = ('email','first_name','last_name','phone_number')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_child = True
        if commit:
            user.save()
        return user


class PGRegisterForm(UserCreationForm):
    username = None
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_number = PhoneField(blank=True)
    class Meta:
        model = CustomUser
        fields = ('email','first_name','last_name','phone_number')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_guardian_or_parent = True
        if commit:
            user.save()
        return user
