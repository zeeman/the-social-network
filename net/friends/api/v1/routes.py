from rest_framework import routers

from .api import UserViewSet, PostViewSet


router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('post', PostViewSet)