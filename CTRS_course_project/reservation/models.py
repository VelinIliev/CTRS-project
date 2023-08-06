from django.contrib.auth import get_user_model
from django.db import models

from CTRS_course_project.projection.models import Projection

UserModel = get_user_model()


class Reservation(models.Model):
    date = models.DateField(
        null=False,
        blank=False,
    )
    projection = models.ForeignKey(
        Projection,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    number_of_tickets = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    type_of_tickets = models.TextField(
        null=True,
        blank=True,
    )
    total_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
    )
    reserved_seats = models.TextField(
        null=True,
        blank=True,
    )
    is_finished = models.BooleanField(
        default=False,
        null=False,
        blank=False
    )

    def __str__(self):
        return f'{self.date} - {self.projection.movie} - {self.projection.hall} - {self.user}'
