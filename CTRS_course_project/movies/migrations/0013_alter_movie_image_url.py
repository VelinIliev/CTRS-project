# Generated by Django 4.2.2 on 2023-07-15 08:11

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_alter_movie_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image_url',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Image'),
        ),
    ]
