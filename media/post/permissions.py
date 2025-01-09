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


  