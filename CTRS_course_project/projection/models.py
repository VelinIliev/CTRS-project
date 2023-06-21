from django.db import models
from django.template.defaultfilters import slugify

from CTRS_course_project.hall.models import Hall
from CTRS_course_project.movies.models import Movie


class Projection(models.Model):
    date = models.DateField(
        null=False,
        blank=False,
    )
    hour = models.TimeField(
        null=False,
        blank=False,
    )
    hall = models.ForeignKey(
        Hall,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    slug = models.SlugField(
        null=False,
        blank=True,
        unique=True,
        editable=False,
        max_length=100,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.date}-{self.hour}-{self.hall.name}-{self.movie.title}')
        return super().save(*args, **kwargs)


class Seat(models.Model):
    projection = models.ForeignKey(
        Projection,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    row_n = models.CharField(
        null=False,
        blank=False,
    )
    seat_n = models.CharField(
        null=False,
        blank=False,
    )
    is_taken = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
