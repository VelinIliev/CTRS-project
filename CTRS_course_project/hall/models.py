from django.db import models


class Hall(models.Model):
    name = models.CharField(
        max_length=35,
        null=False,
        blank=False,
    )
    rows = models.PositiveIntegerField(
        null=False,
        blank=False,
    )
    seats_per_row = models.PositiveIntegerField(
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
