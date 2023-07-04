from django.db import models
from django.template.defaultfilters import slugify


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
    slug = models.CharField(
        unique=True,
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image URL'
    )
    temp_img = models.URLField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
