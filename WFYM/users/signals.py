from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import ParentProfile, ChildProfile

CustomUser = get_user_model() #sender
@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
	print("created")
	if created and instance.is_child:
		ChildProfile.objects.create(user=instance)
	elif created and instance.is_guardian_or_parent:
		ParentProfile.objects.create(user=instance)


#runs every time user is created
@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    if instance.is_child:
    	instance.child_profile.save()
    elif instance.is_guardian_or_parent:
    	instance.parent_profile.save()