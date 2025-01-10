from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Follower

@receiver(post_save, sender=User)
def create_or_save_user_follower(sender, instance, created, **kwargs):
    if created:
        # Create a new Follower instance when a User is created
        Follower.objects.create(user=instance)
    else:
        # Save the existing Follower instance
        if hasattr(instance, "follower_profile"):  # Use the related_name in your model
            instance.follower_profile.save()
