from django.db import models

from CTRS_course_project.movies.validators import validate_year


class Movie(models.Model):
    title = models.CharField(
        max_length=150,
        null=False,
        blank=False,
    )
    year = models.PositiveIntegerField(
        validators=(validate_year,),
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL"
    )
    runtime = models.IntegerField(
        null=False,
        blank=False,
    )
    plot = models.TextField(
        null=False,
        blank=False,
    )
    directors = models.TextField(
        null=False,
        blank=False,
    )
    writers = models.TextField(
        null=False,
        blank=False,
    )
    actors = models.TextField(
        null=False,
        blank=False,
    )
    genres = models.TextField(
        null=False,
        blank=False,
    )
    country = models.CharField(
        null=False,
        blank=False,
    )
    languages = models.CharField(
        null=False,
        blank=False,
    )
    contentRating = models.CharField(
        null=False,
        blank=False,
    )
    imbd_link = models.URLField(
        null=False,
        blank=False,
        verbose_name="Link to IMDB"
    )
