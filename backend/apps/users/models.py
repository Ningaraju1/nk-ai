from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager

class User(AbstractUser):
    """
    Custom User model.
    """

    class Role(models.TextChoices):
        SUPER_ADMIN = "SUPER_ADMIN", "Super Admin"
        ADMIN = "ADMIN", "Admin"
        DEVELOPER = "DEVELOPER", "Developer"
        SUPPORT = "SUPPORT", "Support"
        USER = "USER", "User"

    email = models.EmailField(
        unique=True,
    )

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )


    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


    @property
    def is_admin(self):
        return self.role in [
            self.Role.ADMIN,
            self.Role.SUPER_ADMIN,
        ]

    @property
    def is_super_admin(self):
        return self.role == self.Role.SUPER_ADMIN

    @property
    def is_developer(self):
        return self.role == self.Role.DEVELOPER

    @property
    def is_support(self):
        return self.role == self.Role.SUPPORT

    @property
    def is_regular_user(self):
        return self.role == self.Role.USER