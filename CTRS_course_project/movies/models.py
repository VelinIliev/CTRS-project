from django.db import models
from django.template.defaultfilters import slugify

from CTRS_course_project.movies.validators import validate_year


class Movie(models.Model):
    title = models.CharField(
        max_length=150,
        unique=True,
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
    slug = models.SlugField(
        null=False,
        blank=True,
        unique=True,
        editable=False,
    )
    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.title}-{self.year}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'