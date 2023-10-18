from rest_framework.serializers import ModelSerializer
from rest_framework import serializers, status
from .models import CustomUser

class EmailValidator:
    def __call__(self, value):
        if value.endswith(('.com', '.by', '.ru')):
            raise serializers.ValidationError("Недопустимое значение для поля email")

class CustomUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=50)
    recommendation = serializers.JSONField(default=dict, allow_null=True)
    role = serializers.ChoiceField(choices=CustomUser.Roles.choices)

        
    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.recommendation = validated_data.get('recommendation', instance.recommendation)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance
