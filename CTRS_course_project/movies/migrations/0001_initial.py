# Generated by Django 4.2.2 on 2023-06-20 07:04

import CTRS_course_project.movies.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('year', models.PositiveIntegerField(validators=[CTRS_course_project.movies.validators.validate_year])),
                ('image_url', models.URLField(verbose_name='Image URL')),
                ('runtime', models.IntegerField()),
                ('plot', models.TextField()),
                ('directors', models.CharField()),
                ('writers', models.CharField()),
                ('actors', models.CharField()),
                ('genres', models.CharField()),
                ('country', models.CharField()),
                ('languages', models.CharField()),
                ('contentRating', models.CharField()),
                ('imbd_link', models.URLField(verbose_name='Link to IMDB')),
            ],
        ),
    ]