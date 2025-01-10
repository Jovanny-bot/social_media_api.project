from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


# Create your models here.

class user_model(AbstractUser):
  email = models.EmailField(unique=True)
  profile = models.ImageField(upload_to="profile_pic/", null=True, blank=True)
  bio = models.TextField(blank=True,)
  

User = get_user_model()

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")  
  title = models.CharField(max_length=255,null=True)
  content = models.TextField()
  timestamp = models.DateTimeField(auto_now = True,)
  media   = models.URLField(blank=True, null=True,)
  
  def __str__(self):
    return f"{self.user.username} - {self.title}"

class Follower(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='follower_profile')  # One-to-one relationship with User
    followers = models.ManyToManyField(
        "self", 
        symmetrical=False,  # Non-symmetrical relationship (A follows B doesn't imply B follows A)
        related_name="following",  # Users that this user is following
    )

    def __str__(self):
        return f"{self.user.username}"