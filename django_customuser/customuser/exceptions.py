from rest_framework.serializers import ValidationError


class EmailValidationError(ValidationError):
    def __init__(self, text):
        self.text = text
        