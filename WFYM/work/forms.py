from django import forms
from django.forms import ModelForm
from .models import Chores, Alltask
from users.models import ChildProfile


class ChoreForm(ModelForm):
	class Meta:
		model=Chores
		fields=('child','task','instruction')
	
	def __init__(self, *args, **kwargs):
		current_user = kwargs.pop('user')
		super(ChoreForm, self).__init__(*args, **kwargs)
		self.fields['child'].queryset = ChildProfile.objects.filter(parent_name=current_user)
		self.fields['task'].queryset = Alltask.objects.filter(parent=current_user)
	
    
class TaskForm(ModelForm):
	date_or_time_due = forms.DateTimeField(widget=forms.widgets.DateTimeInput(format="%d/%m/%Y %H:%M:%S",attrs={'placeholder':"DD/MM/YY HH:MM:SS",'class':'datetimefield',}))
	class Meta:
		model=Alltask
		fields=('task','payable_amount','date_or_time_due')
		
class TaskUpdateForm(ModelForm):
	class Meta:
		model=Alltask
		fields=('task','payable_amount','date_or_time_due')