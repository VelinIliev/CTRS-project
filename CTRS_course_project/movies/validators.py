from django.core.exceptions import ValidationError


def validate_year(value):
    if value < 1895:
        raise ValidationError("There was no cinema back then.")
