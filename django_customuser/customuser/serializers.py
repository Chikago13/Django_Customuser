from rest_framework import serializers

from .models import CustomUser
from .validators import correction_email
from .exceptions import EmailValidationError


class CustomUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=50)
    recommendation = serializers.JSONField(default=dict, allow_null=True)
    role = serializers.ChoiceField(choices=CustomUser.Roles.choices)

    def validate_email(self, value):
        try:
            correction_email(value)
            return value
        except EmailValidationError:
            raise serializers.ValidationError("Email cannot ends with '.com', '.by', '.ru'.")

    def create(self, validated_data):
        email = validated_data.get("email")
        self.validate_email(value=email)
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.recommendation = validated_data.get('recommendation', instance.recommendation)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance
