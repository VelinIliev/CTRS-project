from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from django.template.defaultfilters import slugify

from CTRS_course_project.movies.validators import validate_year

UserModel = get_user_model()


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
    rating = models.DecimalField(
        default=0,
        max_digits=3,
        decimal_places=1,
        null=False,
        blank=False,
    )
    votes = models.PositiveIntegerField(
        default=0,
        null=False,
        blank=False,
    )
    temp_img = models.URLField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.title}-{self.year}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} ({self.year})'


class MovieComment(models.Model):
    text = models.CharField(
        max_length=300,
        null=False,
        blank=False,
    )
    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )


class MovieVotes(models.Model):
    user = models.ForeignKey(
        UserModel,
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
    rating = models.IntegerField(
        validators=[validators.MinValueValidator(0), validators.MaxValueValidator(10), ],
        null=False,
        blank=False,
    )
