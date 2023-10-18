from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import serializers, status

class CustomUserAPIView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)