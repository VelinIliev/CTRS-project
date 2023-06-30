from django.core.validators import MinValueValidator
from django.db import models


class Ticket(models.Model):
    ticket_type = models.CharField(
        null=False,
        blank=False,
    )
    price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=False,
        blank=False,
        validators=[MinValueValidator(0.01), ]
    )
    weekend_price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=False,
        blank=False,
        validators=[MinValueValidator(0.01), ]
    )

    def __str__(self):
        return self.ticket_type
