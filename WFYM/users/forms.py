from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import CustomUser, ParentProfile, ChildProfile
from phone_field import PhoneField

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_number = PhoneField(blank=True)
    class Meta:
        model = CustomUser
        fields = ('username','email','first_name','last_name','phone_number')
class ChildRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_number = PhoneField(blank=True)

    class Meta:
        model = CustomUser
        fields = ('username','email','first_name','last_name','phone_number')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_child = True
        if commit:
            user.save()
        return user


class PGRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_number = PhoneField(blank=True)
    class Meta:
        model = CustomUser
        fields = ('username','email','first_name','last_name','phone_number')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_guardian_or_parent = True
        if commit:
            user.save()
        return user

# class ParentProfileform(forms.ModelForm):
# 	class Meta:
# 		model = ParentProfile
# 		fields = ('')

class parent_confirm(forms.Form):
	name = forms.EmailField()
	class Meta:
		model = ParentProfile
		fields = ('user',)

# class PGName(forms.ModelForm):
# # 	parent_name = forms.CharField()
# 	class Meta:
# 		model = ChildProfile
# 		fields = ('parent_name',)


class PGName(ModelForm):
  parent_username = forms.CharField(max_length=100)

  def save(self, commit=True):
      parent_name_ofchild = self.cleaned_data['parent_username']
      parent_id = CustomUser.objects.get(username=parent_name_ofchild)
#       print(parent_id)
      # print(ParentProfile.objects.get_or_create(user_id=parent_name_ofchild)[0])
      parent_name = ParentProfile.objects.get(user_id=parent_id)# returns (instance, <created?-boolean>)
      print(parent_name)
      self.instance.parent_name = parent_name

      return super(PGName, self).save(commit)

  class Meta:
    model=ChildProfile
    exclude = ('parent_name','user',)
   


# class TestForm(ModelForm):
#   attribution = forms.CharField(max_length=100)
# 
#   def save(self, commit=True):
#       attribution_name = self.cleaned_data['attribution']
#       attribution = TestSource.objects.get_or_create(name=attribution_name)[0]  # returns (instance, <created?-boolean>)
#       self.instance.attribution = attribution
# 
#       return super(TestForm, self).save(commit)
# 
#   class Meta:
#     model=TestModel
#     exclude = ('attribution')