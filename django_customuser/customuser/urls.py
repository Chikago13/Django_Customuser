from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .endpoints import CustomUserViewSet


router = DefaultRouter()
router.register("custom_user_set", CustomUserViewSet)


urlpatterns = [
    path("", include(router.urls)), ]
