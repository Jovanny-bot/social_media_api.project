from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
  message = "This is not your post"
  def has_object_permission(self, request, view, obj):
    user = request.user

    if request.method in SAFE_METHODS:
      return True
    else:
      return obj.user == user


class IsAuthenticatedUser (BasePermission):
    message = "You must be logged in to perform this action."

    def has_permission(self, request, view):
        return request.user.is_authenticated
    
class canFollowUser (BasePermission):
    message = "You cannot follow yourself."

    def has_permission(self, request, view):
        if request.method == 'POST':
            user_to_follow = request.data.get('user_id')
            return user_to_follow != request.user.id
        return True
    
class CanEditProfile(BasePermission):
    message = "You can only edit your own profile."

    def has_object_permission(self, request, view, obj):
        return obj == request.user
    
class CanDeletePost(BasePermission):
    message = "You can only delete your own posts."

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
    
class CanLikePost(BasePermission):
    message = "You must be logged in to like a post."

    def has_permission(self, request, view):
        return request.user.is_authenticated
    
class CanCommentOnPost(BasePermission):
    message = "You must be logged in to comment on a post."

    def has_permission(self, request, view):
        return request.user.is_authenticated
    
class IsFollowingUser (BasePermission):
    message = "You must follow this user to view their posts."

    def has_permission(self, request, view):
        user_id = view.kwargs.get('user_id')
        return request.user.following.filter(id=user_id).exists()
    

