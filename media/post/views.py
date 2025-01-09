from django.shortcuts import render
from rest_framework import viewsets
from .serializer import user_modelserializer, PostSerializer, FollowerSerializer
from .models import user_model,Post,Follower
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics




class user_modelViewSet(viewsets.ModelViewSet):
  serializer_class = user_modelserializer
  queryset = user_model.objects.all()
  permission_classes = []

class PostViewSet(viewsets.ModelViewSet):
  serializer_class=PostSerializer
  queryset = Post.objects.all()
  permission_classes = [IsOwnerOrReadOnly]

  def perform_create(self, serializer):
    user = self.request.user
    serializer.save(user=user)
    return super().perform_create(serializer)

class PostListAPIView(generics.ListAPIView):
  serializer_class = PostSerializer
  queryset = Post.objects.all()
  permission_classes= [IsAuthenticated]

class FollowerViewSet(viewsets.ModelViewSet):
  serializer_class = FollowerSerializer
  queryset = Follower.objects.filter()











