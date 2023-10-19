from .exceptions import EmailValidationError


def correction_email(value):
    if value.endswith(('.com', '.by', '.ru')):
        raise EmailValidationError("Email cannot ends with '.com', '.by', '.ru'.")
    return value
