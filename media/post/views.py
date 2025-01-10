from django.shortcuts import render
from rest_framework import viewsets
from .serializer import user_modelserializer, PostSerializer, FollowerSerializer
from .models import user_model,Post,Follower
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from .permissions import IsOwnerOrReadOnly, canFollowUser, CanEditProfile, CanDeletePost, CanLikePost, CanCommentOnPost
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


class user_modelViewSet(viewsets.ModelViewSet):
  serializer_class = user_modelserializer
  queryset = user_model.objects.all()
  permission_classes = []

class PostViewSet(viewsets.ModelViewSet):
  serializer_class=PostSerializer
  queryset = Post.objects.all()
  permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

  def perform_create(self, serializer):
    user = self.request.user
    serializer.save(user=user)
    return super().perform_create(serializer)

class PostListAPIView(generics.ListAPIView):
  serializer_class = PostSerializer
  queryset = Post.objects.all()
  permission_classes= [IsAuthenticated]


class FollowerViewSet(viewsets.ModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'head', 'options']

    def get_queryset(self):
        # Restrict access to only the current user's Follower instance
        return self.queryset.filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        # Prevent direct creation of a Follower instance
        raise ValidationError({"detail": "You cannot create a Follower instance directly."})

    def partial_update(self, request, *args, **kwargs):
        # Update the followers field of the Follower instance
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            # Use add() to prevent duplicate entries
            followers = serializer.validated_data.get("followers", [])
            instance.followers.add(*followers)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)













