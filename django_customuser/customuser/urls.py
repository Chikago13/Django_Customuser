
from django.urls import path
from .views import CustomUserAPIView

urlpatterns = [
    path('users/', CustomUserAPIView.as_view(), name='customuser_api'),
    path('users/<int:pk>', CustomUserAPIView.as_view(), name='customuser_api'),
]

