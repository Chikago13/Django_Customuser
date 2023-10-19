from django.db import models


class CustomUser(models.Model):

    class Roles(models.TextChoices):
        USER = "user"
        MODERATOR = "moderator"
        ADMIN = "admin"

    email = models.EmailField(max_length=255, verbose_name='email address', unique=True)
    first_name = models.CharField(max_length=30, verbose_name="Name")
    last_name = models.CharField(max_length=50, verbose_name="Surname")
    recommendation = models.JSONField(blank=True, null=True)
    role = models.CharField(default="user", max_length=9, choices=Roles.choices)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField("verified", default=False)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email}, {self.first_name}, {self.last_name}, {self.recommendation}, {self.role}"

    def get_full_name(self):
        return f"{self.email}, {self.first_name}, {self.last_name}, {self.role}"
