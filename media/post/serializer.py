from rest_framework import serializers
from .models import user_model,Post,Follower

class user_modelserializer(serializers.ModelSerializer):
  class Meta:
    model = user_model
    fields = ("pk","username", "email", "password", "profile", "bio")
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
  author = serializers.CharField(source= "user.username")
  class Meta:
    model = Post
    fields = ("id","user", "author","title", "content", "media")
    read_only_fields = ["user"]

class FollowerSerializer(serializers.ModelSerializer):
    followers = serializers.PrimaryKeyRelatedField(
        many=True, read_only = True
    )  # Handles a list of follower IDs

    class Meta:
        model = Follower
        fields = ["user", "followers"]
        read_only_fields = ["user"]  # `user` is read-only to avoid modifying it directly

    def update(self, instance, validated_data):
        followers = validated_data.get("followers", [])
        instance.followers.add(*followers)  # Add the new followers
        return instance