from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import user_modelViewSet, PostViewSet , FollowerViewSet, PostListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = DefaultRouter()

router.register("users", user_modelViewSet)
router.register("posts", PostViewSet)
router.register(r'followers', FollowerViewSet, basename='follower')


urlpatterns = [
  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('api/posts/', PostListAPIView.as_view(), name="posts"),
]

urlpatterns += router.urls