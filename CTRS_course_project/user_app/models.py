from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models

from CTRS_course_project.user_app.validators import validate_only_letters


class AppUser(AbstractUser):
    first_name = models.CharField(
        max_length=35,
        validators=[validators.MinLengthValidator(2), validate_only_letters, ],
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=35,
        validators=[validators.MinLengthValidator(2), validate_only_letters, ],
        null=False,
        blank=False,
    )
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
