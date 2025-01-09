from rest_framework import serializers
from .models import user_model,Post,Follower

class user_modelserializer(serializers.ModelSerializer):
  class Meta:
    model = user_model
    fields = ("username", "email", "password", "profile", "bio")
    extra_kwargs = {
      "password" : {"write_only" : True}
    }

  def create(self, validated_data):
    username = validated_data.get("username")
    passwords = validated_data.get("password")
    email = validated_data.get("email")
    user = user_model.objects.create_user(username=username, email=email, password=passwords)
    return user

  def validate(self, attrs):
    if len(attrs.get("password")) < 5:
      raise serializers.ValidationError("Your password is too short!")
    return attrs


class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ("user", "title", "content", "media")
    read_only_fields = ["user"]

class FollowerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Follower
    fields = ("user", "followers")