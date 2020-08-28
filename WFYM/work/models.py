from django.db import models
from users.models import ChildProfile, ParentProfile
from django.utils import timezone


class Alltask(models.Model):
	parent=models.ForeignKey(ParentProfile,null=True,on_delete=models.CASCADE)
	task = models.CharField(max_length=100,default="") 
	payable_amount = models.DecimalField(max_digits=6,decimal_places=2) 
	date_or_time_due = models.DateTimeField(blank=True, default=timezone.now) 	
	
	def __str__(self):
		return self.task
		
class Chores(models.Model):
	parent=models.ForeignKey(ParentProfile,null=True,on_delete=models.CASCADE)
	child = models.ManyToManyField(ChildProfile,blank=True)
	task = models.ManyToManyField(Alltask,blank=True)
	instruction = models.CharField(max_length=100,default="") 
	created_date = models.DateTimeField(default=timezone.now)
	class Meta:
		ordering = ('-created_date',)
	def __str__(self):
		return str(self.parent)