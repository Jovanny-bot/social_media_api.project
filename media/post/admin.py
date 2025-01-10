from django.contrib import admin
from.models import User, Post, Follower

# Register your models here.

@admin.register(User)
class user_modelAdmin(admin.ModelAdmin):
  list_display = ("username","email","bio")

@admin.register(Post)
class post_modelAdmin(admin.ModelAdmin):
  list_display = ("user","title","timestamp")

@admin.register(Follower)
class follower_modelAdmin(admin.ModelAdmin):
  list_display = ['user__username']
  search_fields = ("username","followers")
  search_display = ("user","followers")
  